.PHONY: server
server: ## start server
		python3 manage.py runserver 8080

.PHONY: create
create: ## create new app
		python3 manage.py startapp $(n)

.PHONY: dm
dm: ## do migration
		python3 manage.py migrate

.PHONY: cm
cm: ## create new migration for spec app
		python3 manage.py makemigrations $(n)
