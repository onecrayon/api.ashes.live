# Ashes.live API

This is the backend API for Ashes.live, a fan-developed deckbuilder and community site for the card game Ashes Reborn.

## Dependencies

You must install the following to run CardPlay.live locally:

* [Docker](https://docs.docker.com/engine/installation/)
* [Docker Compose](https://docs.docker.com/compose/install/) (included in Docker
  Desktop on Windows and Mac)
* Make

That's it! For local development, all other code is executed in Docker via Make using
the standard [3 Musketeers](https://3musketeers.io/) pattern.

### Running on Windows

**Please note:** in order to run Docker Desktop on Windows you will need Windows Pro.

One easy way to install `make` on Windows:

1. Install the [Chocolatey](https://chocolatey.org/install) package manager
2. Run `choco install make` in an elevated command prompt

## Running locally

After installing the dependencies above:

1. Create a copy of `.env.example` named `.env` in your root directory
2. Update `POSTGRES_PASSWORD` and other settings in `.env` for local development
3. Run `make` from the root project directory

This will build your main Docker container and show you the available commands you can
execute with `make`.

Your two typical commands will be `make run` (which will launch a local, auto-refreshing
development server) and `make shell` (which will open a shell connection within Docker).

After running `make run`, you can access your site at <http:localhost:8000>.

### Installing Python dependencies

Ashes.live uses [Poetry](https://python-poetry.org/) for dependency management. To
install a new dependency:

```sh
$ make shell
root@123:/code$ poetry add DEPENDENCY
```

Then commit changes in your updated `poetry.lock` and `pyproject.toml`. Please see the
[Poetry docs](https://python-poetry.org/docs/) for other available commands.

**Please note:** `make shell` will log you into the Docker container as the root user!
This is unfortunately necessary to allow Poetry to function properly (I haven't found a
good way yet to install initial dependencies as a non-root account and have them work,
which means the shell has to be root in order to properly calculate the dependency graph).

### Developing within the Docker container

You can use [Visual Studio Code](https://code.visualstudio.com/) to develop directly within
the Docker container, allowing you direct access to the Python environment (which means
linting, access to Python tools, and working code analysis for free). To do so:

1. Install [Visual Studio Code](https://code.visualstudio.com/), if you haven't already
2. Install the [Remote Development extension pack](https://aka.ms/vscode-remote/download/extension)
3. Outside VSCode in your favored command line, execute `make run` to launch the API container
4. Use the Remote Explorer in the left sidebar of VSC to attach to the running API container
   (likely named `asheslive_api_1`). You can find explicit instructions for this in the
   [Visual Studio Code documentation](https://code.visualstudio.com/docs/remote/containers#_attaching-to-running-containers)
5. If this is your first time attaching, open the Command Palette and type "attached" then
   select "Remote-Containers: Open Attached Configuration File...", replace the contents
   of the file with the following, and save:

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
		"ms-python.python"
	]
}
```

You will need to start the API prior to launching VSCode to automatically attach to it.
(I am looking into ways to improve this workflow, but short-term this is the easiest
to get working consistently without requiring rebuiding the API with every poetry change.)

**Please note:** you *must* run your make commands in an external shell! The VSCode Terminal
will provide you access to the equivalent of `make shell`, but running the standard make
commands there will result in Docker-in-Docker, which is not desirable in this instance.

### Update core tools

The underlying Dockerfile uses the following tools, pinned to specific release versions:

* [Dockerize](https://github.com/jwilder/dockerize)
* [Tini](https://github.com/krallin/tini)
* [Poetry](https://python-poetry.org/)

In order to update these tools, you must update their pinned version in `docker/Dockerfile`
and (for Poetry) in `pyproject.toml` then rebuild your API container using `make build`.

## Code logic

The primary entrypoint for the application is `api/main.py`. This file defines
the FastAPI app and attaches all site routers.

Route view functions are defined in `views`, organized by base URL segment.

### API documentation

Ashes.live uses FastAPI's automatically-generated OpenAPI documentation. You can find the
site's docs at <http://localhost:8000/docs> once you have the site running locally.

### Testing strategy

TBD
