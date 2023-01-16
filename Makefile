# force to use bash
SHELL                 = /bin/bash
WRKDIR               := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
DEV_LAYOUT_ENV_LOCAL := bundles/backend/conf/local.env
BATCH_SIZE           := 5000
SEED_DATA_PATH       := fixtures


.PHONY: build
build: ## Build image
	@ docker build -t frontend-telebot:latest .


.PHONY: run
run: build ## Run app
	@ docker run -d -v /app/dev-layout:/app/dev-layout -v /app/telebot:/opt/app -v /root/.git-credentials:/root/.git-credentials -v /root/.gitconfig:/root/.gitconfig -v /root/.ssh:/root/.ssh frontend-telebot:latest


#
# Absolutely awesome: http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
#
.PHONY: help
help:
	@ grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
