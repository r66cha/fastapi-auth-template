run:
	uv run main.py
	
urun:
	uv run uvicorn_main.py

secret:
	python src/core/dependencies/secret_generator.py

alembic revision:
	alembic revision --autogenerate -m "$(m)"

alembic upgrade:
	alembic upgrade head

docker build:
	docker compose up --build -d