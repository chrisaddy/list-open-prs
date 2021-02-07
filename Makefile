build:
	docker build -t list-open-prs .

run:
	docker run --env-file .env list-open-prs

test: # need to install act to run locally
	act pull_request --secret-file .env
