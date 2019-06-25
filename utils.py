import subprocess
import click

@click.group()
def server():
    pass

## Start server in its docker container
@server.command()
def startprod():
    click.echo(subprocess.run("docker-compose up -d server nginx", shell=True, check=True))

## Start server in its docker container dev
@server.command()
def startdev():
   click.echo(subprocess.run("docker-compose up devserver", shell=True, check=True))

## Stop server in its docker container dev
@server.command()
def stop():
    click.echo(subprocess.run("docker-compose stop", shell=True, check=True))

## Install server with its dependencies
@server.command()
def install():
    click.echo(subprocess.run("docker-compose run --rm devserver pip install -r requirements-dev.txt --user --upgrade --no-warn-script-location", shell=True, check=True))

## Show Server Logs
@server.command()
def show_server_logs():
    click.echo(subprocess.run("tail -f server_unicorn.log", shell=True, check=True))

## Connect to server to lauch commands
@server.command()
@click.option('--container_name', default='server')
def bash(container_name):
    click.echo(subprocess.run(f'docker-compose exec {container_name} bash', shell=True, check=True))

## Install server with its dependencies
@server.command()
def run_tests():
    subprocess.run("docker-compose run --rm testserver pip install -r requirements-dev.txt --user --upgrade --no-warn-script-location", shell=True, check=True)
    click.echo(subprocess.run("docker-compose run --rm testserver", shell=True, check=True))

cli = click.CommandCollection(sources=[server])
if __name__ == '__main__':
    cli()

# server.upgrade: ## Upgrade pip dependencies
# 	docker-compose run --rm server bash -c "python vendor/bin/pip-upgrade requirements.txt requirements-dev.txt --skip-virtualenv-check"

# .PHONY: coverage
# test.coverage: ## Generate test coverage
# 	docker-compose run --rm testserver bash -c "python -m pytest --cov-report term --cov-report html:coverage --cov-config setup.cfg --cov=src/ test/"

# test.lint: ## Lint python files with flake8
# 	docker-compose run --rm server bash -c "python -m flake8 ./src ./test"

# test.safety: ## Check for dependencies security breach with safety
# 	docker-compose run --rm server bash -c "python vendor/bin/safety check"