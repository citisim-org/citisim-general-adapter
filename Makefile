install:
	docker-compose build --no-cache
	docker-compose run --rm server pip install -r requirements-dev.txt --user --upgrade

start:
	docker-compose up server

stop:
	docker-compose stop

daemon:
	docker-compose up -d server

tests:
	docker-compose run --rm testserver

lint:
	docker-compose run --rm server bash -c "python -m flake8 ./src ./test"
