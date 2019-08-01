reset_db:
	dropdb jobs --if-exists
	createdb jobs
	make migrate

migrate:
	python3 manage.py migrate
	# python3 manage.py loaddata fixtures/*

tests:
	python3 manage.py test --parallel

run:
	python3 manage.py runserver

shell:
	python3 manage.py shell_plus --print-sql

fake_db:
	python3 manage.py seed --offers 20

reset_fake_db:
	make reset_db && make fake_db
