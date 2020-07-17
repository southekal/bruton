TEST_PATH=./tests
.DEFAULT_GOAL := help
.PHONY: help

help:
	@echo "options available:"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
			 | sed -n 's/^\(.*\): \(.*\)##\(.*\)/\1\3/p' \
			 | column -t  -s ' '

clean-pyc: ## [remove .pyc files]
	find . -name "*.pyc" -exec rm -f {} \;

test: ## [run unit tests]
	python -m unittest discover $(TEST_PATH)

run: ## [run flask app]
	python3 app.py

git-deploy: ## [deploy master branch to git]
	git push -u origin master

heroku-deploy: ## [deploy master branch to heroku]
	git push heroku master
