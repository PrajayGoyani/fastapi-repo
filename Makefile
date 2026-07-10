.PHONY: dev start stop stop-dev

dev:
	docker compose --profile dev up -d

start:
	docker compose --profile prod up -d

stop:
	docker compose --profile prod down

stop-dev:
	docker compose --profile dev down 
