# Ashes.live API

This is the backend API for Ashes.live, a fan-developed deckbuilder and community site for the card
game Ashes Reborn.

## Dependencies

You must install the following to run the Ashes.live API locally:

* [Docker](https://docs.docker.com/engine/installation/)
* [Docker Compose](https://docs.docker.com/compose/install/) (included in Docker
  Desktop on Windows and Mac)
* Make

That's it! For local development, all other code is executed in Docker via Make using
the standard [3 Musketeers](https://3musketeers.io/) pattern.

### Running on Windows

**Please note:** in order to run Docker Desktop on Windows you will need a recent copy of
Windows 10 with [WSL 2 enabled](https://docs.microsoft.com/en-us/windows/wsl/install-win10).

Because WSL 2 runs faster when files are living under the Linux filesystem, you will probably
want to clone this repo into your Linux file system, install `make` under your Linux distro
(if necessary) and then execute your make commands from the WSL command line (accessible via
`wsl` in PowerShell, or by opening the Linux terminal directly).

This means that on Windows you are typically:

* **Windows:** Installing and running Docker Desktop
* **Windows:** Using VisualStudio Code or PyCharm to edit the files store in WSL file system
  (see below)
* **Linux/WSL:** Running `make` commands in a WSL command line instead of standard Windows cmd or Powershell
* **Linux/WSL:** Performing git actions in WSL (no need to install git in Windows for this project)

However, if for whatever reason you do want to install `make` on Windows, this is an easy way:

1. Install the [Chocolatey](https://chocolatey.org/install) package manager
2. Run `choco install make` in an elevated command prompt

## First run

After installing the dependencies above:

1. Create a copy of `.env.example` named `.env` in your root directory
2. *At minimum* update `POSTGRES_PASSWORD` and `SECRET_KEY` in `.env` (you can update other
   values if you wish; they aren't required to run locally, though)
3. Run `make` from the root project directory

This will build your main Docker container and display the available commands you can
execute with `make`.

Now that you have a functional API stack, you can run `make data` to create some example
testing data in your database (note: this may fail if you have never run `make run` or
`make db` prior to `make data` because the Postgres database must be initialized first).

**Please note:** if you do *not* use the example data, you will need to install the extension
`pgcrypto` before running any migrations (via the SQL `create extension pgcrypto;`).

At this point, you can execute `make up` to start a local development server, and view your
site's API documentation at <http:localhost:8000>.

From within the API docs, you can query the API directly and inspect its output. If you need
to authenticate, use the email `hello@ashes.live` as the username with the password `changeme`
to log in as IsaacBot#30000. **You must not make your API public without changing this password.**

If you are running a local development server to work on the front-end application, you're done!

If you wish to contribute to the API, read on!

### Developing within the Docker container

You can use [Visual Studio Code](https://code.visualstudio.com/) to develop directly within
the Docker container, allowing you direct access to the Python environment (which means
linting, access to Python tools, working code analysis for free, and bash shell access
without needing to run a make command). To do so:

1. Install [Visual Studio Code](https://code.visualstudio.com/), if you haven't already
2. Install the [Remote Development extension pack](https://aka.ms/vscode-remote/download/extension)
3. **Outside VSCode** in your favored command line, execute `make run` to launch the API container
4. **Inside VSCode** use the Remote Explorer in the left sidebar of VSC to attach to the running
   API container (likely named `asheslive:dev`). You can find explicit instructions for this in the
   [Visual Studio Code documentation](https://code.visualstudio.com/docs/remote/containers#_attaching-to-running-containers)
5. If this is your first time attaching, open the Command Palette and type "container" then
   select "Remote-Containers: Open Container Configuration", replace the contents
   of the file with the following, save, and then close the window and re-attach to the container:

```json
{
	"workspaceFolder": "/code",
	"settings": {
		"terminal.integrated.shell.linux": "/bin/bash",
		"python.pythonPath": "/usr/local/bin/python3.8",
		"python.linting.pylintEnabled": true,
		"python.linting.enabled": true,
		"editor.formatOnSave": true,
		"python.formatting.provider": "black",
		"editor.wordWrapColumn": 88
	},
	"remoteUser": "root",
	"extensions": [
		"EditorConfig.EditorConfig",
		"ms-python.python"
	]
}
```

You will need to start the API prior to launching VSCode to automatically attach to it.
(I am looking into ways to improve this workflow, but short-term this is the easiest
to get working consistently without requiring rebuiding the API with every poetry change.)

**Please note:** you *must* run your make commands in an external shell! The VSCode Terminal
in your attached container window will provide you access to the equivalent of `make shell`,
but running the standard make commands there will result in Docker-in-Docker, which is not
desirable in this instance.

### Configuring PyCharm

You can use [PyCharm](https://www.jetbrains.com/pycharm/) to develop directly within
the Docker container, allowing you access to the Python environment (which means
linting, access to Python tools, etc.). To do so:

1. [Install PyCharm](https://www.jetbrains.com/pycharm/download/), if you haven't already
2. In your favorite Terminal, run `make run` to ensure the local stack is running
3. Open PyCharm's Settings (on Windows) or Preferences (on macOS)
4. Under Project -> Python Interpreter, click the gear icon by the Python Interpreter dropdown and choose "Add..."
5. Select "Docker Compose" as the type in the left sidebar 
6. Select `api` under the "Service" dropdown
7. Apply your changes and close the settings

#### Debugging in PyCharm

You will now have auto-completion, automatic imports, and code navigation capabilities in PyCharm.
To enable local debugging:

1. In the upper right of the main window, click "Add Configuration..."
2. Click the "+" button and choose "Python" as the template
3. Name your configuration whatever you like (e.g. `Local`)
4. Select "Script path", switch it to "Module name", then enter `uvicorn` as the "Module name"
5. Enter `api.main:app --reload --host 0.0.0.0 --port 8000` as the "Parameters"
6. Choose the Python Interpreter you set up in the previous steps
7. Apply your changes
8. In your favorite Terminal, exit the running local stack (if it is still running)
9. You can now launch a local stack (or debug a local stack) with the buttons in the upper right corner of the main
   window (the stack should auto-reload as you save files)
   
#### Automatic code formatting in PyCharm

This project is configured to use `isort` and `black` for import and code formatting, respectively.
You can trigger formatting across the full project using `make format`, or you can also set up automatic
formatting on a per-file basis within PyCharm:

1. Open PyCharm's Settings (on Windows) or Preferences (on macOS)
2. Under Tools -> File Watchers, click the "+" button and choose the "custom" template
3. Name your File Watcher whatever you like (e.g. "isort & black")
4. Configure the following settings:
    * File type: `Python`
    * Scope: `Project Files`
    * Program: `make` (macOS/Linux) or `wsl` (Windows)
    * Arguments: `format FILEPATH=$FilePathRelativeToProjectRoot$` (macOS/Linux) or
      `make format FILENAME="$UnixSeparators($FilePathRelativeToProjectRoot$)$"` (Windows)
    * Output paths to refresh: `$FilePath$`
    * Working Directory and Environment Variables -> Working directory: `$ProjectFileDir$`
    * Uncheck Advanced Options -> Auto-save edited files to trigger the watcher
    * Uncheck Advanced Options -> Trigger the watcher on external changes

If automatic formatting is behaving too slowly for your tastes, you can optionally install isort and black in
your local environment and configure them that way:

* https://github.com/pycqa/isort/wiki/isort-Plugins
* https://black.readthedocs.io/en/stable/editor_integration.html

## Development

The Ashes.live API uses the [FastAPI](https://fastapi.tiangolo.com/) framework to handle view
logic, and [SQLAlchemy](https://www.sqlalchemy.org/) for models and database interaction.
[Pydantic](https://pydantic-docs.helpmanual.io/) is used for modeling and validating endpoint
input and output. [Pytest](https://docs.pytest.org/en/latest/) is used for testing.

### Code logic

The primary entrypoint for the application is `api/main.py`. This file defines
the FastAPI app and attaches all site routers. Site modules are organized as follows:

* `api/views`: Route view functions, typically organized by base URL segment. Start here to
  trace a code path for a given endpoint.
* `api/models`: Data models used to persist to and represent info from the database
* `api/schemas`: Pydantic models used to validate and model endpoint input/output
* `api/tests`: Integration tests (with some unit tests where integration testing is not feasible)
* `api/services`: Functions for performing "business logic"; e.g. creating and modifying models,
  shared queries that span model relationships, etc.
* `api/utils`: Utility functions for doing a single small thing (placed here because multiple
  endpoints leverage the function, or to make testing easier)

Services and utility functions are quite similar. Generally speaking, if it's working with simple
data, it's a utility. If it's manipulating models, it's probably a service.

You will likely leverage the following files, as well:

* `api/db.py`: Convenience access to SQLAlchemy objects and methods
* `api/depends.py`: View dependencies (e.g. to allow endpoints access to the logged-in user)
* `api/environment.py`: Exports the `settings` object for access to environment settings

### Testing strategy

I am shooting to maintain 100% code coverage. When you submit a PR, I will expect you to
include tests that fully cover your code. You can view line-by-line coverage information
by executing `make test` and then loading `htmlcov/index.html` into your favorite browser.

Note that full code coverage simply means the tests must exercise all possible logic paths
in your code. However, If you check the `api/tests` folder you will find that most existing
tests are *integration* tests; they setup a scenario, query a single endpoint, and check that
the status code is correct (typically no other information is verified). Tests do not need
to exhaustively cover every eventuality; they simply need to ensure that all code paths are
functional and appear to be working as expected.

Testing performs queries against an actual database, and every individual test starts with
an empty slate (there is no pre-existing data, and data does not persist between tests).

In some instances, you may need to write unit tests instead (for instance, user badge generation
logic does this). This will typically come up when you need to verify error handling within
a service or utility function for failure states that are not possible to trigger externally.

### Migrations

Migrations are handled by Alembic. To create a new migration:

* Add or edit models or properties in `api/models`. If you add a new model class, make sure to
  hoist the class to the root module in `api/models/__init__.py` or else it will not be
  detected by Alembic!
* Execute `make migrate-new ARGS='Short description here'`
* This will create a new file in `migrations/versions`; verify the contents and remove the
  "autogenerated" comments.
* You can now run `make migrate` to update your local database!

You can find documentation for Alembic here: https://alembic.sqlalchemy.org/en/latest/

Make sure that your model classes all inherit from `api.db.AlchemyBase`! This is what allows
SQLAlchemy and Alembic to map the class to a table definition.

### Installing Python dependencies

The Ashes.live API uses [Poetry](https://python-poetry.org/) for dependency management. To
install a new dependency from outside of the container execute the following:

```sh
make poetry-add ARGS='name_of_package'
```

For more advanced interaction with poetry, use `make shell`.

(If you are developing within Visual Studio Code, you can open the built-in terminal and skip
the `make shell` command.)

Then commit changes in your updated `poetry.lock` and `pyproject.toml`. Please see the
[Poetry docs](https://python-poetry.org/docs/) for other available commands.

You must shut down your container, run `make build`, and relaunch it to ensure that
newly added dependencies are available. If you pull down code and stuff starts failing in
weird ways, you probably need to run `make build` and `make migrate`.

**Please note:** `make shell` will log you into the Docker container as the root user!
This is unfortunately necessary to allow Poetry to function properly (I haven't found a
good way yet to install initial dependencies as a non-root account and have them work,
which means the shell has to be root in order to properly calculate the dependency graph).

### Update core tools

The underlying Dockerfile uses Poetry, pinned to a specific release version. In order to
update poetry, you must update its pinned version in `Dockerfile` then rebuild your API
container using `make build`.

### AI-generated code

You may notice that there is a `CLAUDE.md` file for providing Claude Code with guidance for
how to interact with the codebase. I am experimenting with offsetting some of the repetitive
tasks that are keeping me from actually developing this site onto AI, but please note that
I am not interested in new features completely coded by AI. If you submit a PR with
AI-generated code from a careful prompt and a deep understanding of the project, that is fine,
but please don't try to substitute an LLM for understanding and thinking about the code yourself.

## Deployment

Ashes.live is currently setup for deployment to [Opalstack](https://opalstack.com).
(Docs for replicating an install TBD.)
