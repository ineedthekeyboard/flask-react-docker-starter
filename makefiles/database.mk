### DATABASE
# ¯¯¯¯¯¯¯¯


database.connect: ## Connect to database
	docker-compose exec database1 psql -U database1_role -d database1
database.migrate: ## Create alembic migration file
	docker-compose run --rm server python src/manage.py db migrate

database.upgrade: ## Upgrade to latest migration
	docker-compose run --rm server python src/manage.py db upgrade

database.downgrade: ## Downgrade latest migration
	docker-compose run --rm server python src/manage.py db downgrade
