# Makefile
.PHONY: help test html pdf clean
.DEFAULT_GOAL := help

help: ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

test: ## Run tests with pytest
	uv run pytest

html: ## Build HTML documentation
	uv run make -C docs html

pdf: ## Build PDF documentation
	uv run make -C docs latexpdf

clean: ## Clean documentation builds
	uv run make -C docs clean

