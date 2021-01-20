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

Now that you have a functional API stack, you need data in your database:

1. Run `make migrate REV='6b6df338dfc3'` to initialize tables in your database that match the example data
2. Run `make clean` to ensure the database is shut down
3. Run `make example-data` to populate your database with basic card and deck data
4. Run `make clean` once more to ensure the database is shut down
3. Run `make migrate` to run any subsequent migrations

At this point, you can execute `make run` to start a local development server, and view your
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

### Installing Python dependencies

The Ashes.live API uses [Poetry](https://python-poetry.org/) for dependency management. To
install a new dependency from outside of the container:

```sh
$ make shell
root@123:/code$ poetry add DEPENDENCY
```

(If you are developing within Visual Studio Code, you can open the built-in terminal and skip
the `make shell` command.)

Then commit changes in your updated `poetry.lock` and `pyproject.toml`. Please see the
[Poetry docs](https://python-poetry.org/docs/) for other available commands.

You may wish to shut down your container, run `make build`, and relaunch it to ensure that
newly added dependencies are available. If you pull down code and stuff starts failing in
weird ways, you probably need to run `make build` and `make migrate`.

**Please note:** `make shell` will log you into the Docker container as the root user!
This is unfortunately necessary to allow Poetry to function properly (I haven't found a
good way yet to install initial dependencies as a non-root account and have them work,
which means the shell has to be root in order to properly calculate the dependency graph).

### Update core tools

The underlying Dockerfile uses the following tools, pinned to specific release versions:

* [Dockerize](https://github.com/jwilder/dockerize)
* [Tini](https://github.com/krallin/tini)
* [Poetry](https://python-poetry.org/)

In order to update these tools, you must update their pinned version in `Dockerfile`
and (for Poetry) in `pyproject.toml` then rebuild your API container using `make build`.

## Deployment

Ashes.live is currently setup for deployment to [Render.com](https://render.com). To deploy
a copy of the site:

1. Create a managed Postgres database
2. Create a new Docker service pointing to your Ashes.live GitHub repo with the following settings:
    * **Docker Command:** `/bin/bash -c cd /code && /gunicorn.sh`
	* **Health Check Path:** `/health-check`
	* **Environment Variables:** at minimum, you must set the following environment variables (you
	  can set others, if you like; the available keys are in `.env.example`):
	    - **ENV:** `production`
		- **POSTGRES_DB**
		- **POSTGRES_HOST**
		- **POSTGRES_PASSWORD**
		- **POSTGRES_USER**
		- **SECRET_KEY**
3. Once your Docker service has deployed, you can use the Shell tab to run Alembic migrations, or
   otherwise populate your database with initial data.

That's it!

### Environment variables

Please note that the `.env` file is *not* populated in your production images. The `.env` file
works locally because Docker Compose automatically loads its contents as environment variables, but
when running in production mode Pydantic is not capable of reading an `.env` file with the current
setup (which is why you must define your environment variables one-by-one in the Render control
panel).
