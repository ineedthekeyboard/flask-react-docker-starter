### SERVER
# ¯¯¯¯¯¯¯¯¯¯¯

server.startprod:
	docker-compose up -d --build

server.startdev: ## Start server in its docker container
	docker-compose --project-name devserver -f docker-compose.dev.yaml up -d --build

server.bash: ## Connect to server to lauch commands
	docker-compose exec server bash

server.stop: ## Start server in its docker container
	docker-compose stop

server.logs: ## Display server logs
	tail -f /opt/services/webapp/server_unicorn.log

server.upgrade: ## Upgrade pip dependencies
	docker-compose run --rm server bash -c "python vendor/bin/pip-upgrade requirements.txt requirements-dev.txt --skip-virtualenv-check"
