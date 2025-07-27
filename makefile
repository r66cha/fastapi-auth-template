run:
	uv run main.py
	
urun:
	uv run uvicorn_main.py

# --

secret:
	python src/core/dependencies/secret_generator.py

superuser:
	python src/api/create_superuser.py

# --

alembic-revision:
	alembic revision --autogenerate -m "$(m)"

alembic-upgrade:
	alembic upgrade head

# --

docker_build:
	docker compose up --build -d

# --

install-uv:
	curl -LsSf https://astral.sh/uv/install.sh | sh

install-req:
	uv pip install -r requirements.txt

freeze:
	uv pip freeze > requirements.txt

