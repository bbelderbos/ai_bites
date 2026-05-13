.PHONY: help setup test progress clean
.DEFAULT_GOAL := help

BITE ?=

help:  ## Show this help
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z_-]+:.*##/ {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup:  ## Install dependencies (uv sync)
	uv sync

test:  ## Run tests. Use BITE=05 to run a single bite, omit to run all
ifeq ($(strip $(BITE)),)
	uv run pytest -q
else
	@dir=$$(ls -d $(BITE)_*/ 2>/dev/null | head -1); \
	if [ -z "$$dir" ]; then echo "No bite matching '$(BITE)_*'"; exit 1; fi; \
	uv run pytest -q $$dir
endif

progress:  ## Show ASCII progress bar across all 10 bites
	@uv run python scripts/progress.py

clean:  ## Remove pycaches and progress state
	find . -type d -name __pycache__ -not -path "./.venv/*" -exec rm -rf {} + 2>/dev/null || true
	rm -f .ai_bites_progress.json
