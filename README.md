# AI Bites

Warmup exercises for the [Agentic AI Cohort](https://pythonagenticai.com).

10 bite-sized exercises that teach the foundations of building real AI apps — from your first Claude API call up to a working ReAct agent loop. Each bite is self-contained, test-driven, and completable in 20–30 minutes.

## Prerequisites

- Python **3.12+**
- [`uv`](https://github.com/astral-sh/uv)
- An Anthropic API key

## Setup

```bash
git clone https://github.com/bbelderbos/ai_bites.git
cd ai_bites
make setup
export ANTHROPIC_API_KEY=sk-ant-...   # or put it in your shell rc / .envrc
```

Tests **mock the API** — you don't need a real key just to make the tests pass. You only need it when you want to run your code against the actual model.

## How to do a bite

Each bite folder (e.g. `01_first_api_call/`) contains:

| File | What it is |
|------|-----------|
| `exercise.md` | What you're building and why |
| `template.py` | Your starting point — has TODOs |
| `reference.py` | Reference solution — peek **only when stuck** |
| `test_exercise.py` | Tests you need to make pass |

Workflow:

```bash
# 1. Read the task
open 01_first_api_call/exercise.md

# 2. Copy the template to solution.py (this is what tests import)
cp 01_first_api_call/template.py 01_first_api_call/solution.py

# 3. Fill in the TODOs, then run the tests
make test BITE=01

# 4. When it's green, see how the reference did it
diff 01_first_api_call/solution.py 01_first_api_call/reference.py
```

> `solution.py` is gitignored — your code stays local.

## Make targets

```bash
make setup              # uv sync
make test               # run all bites (solutions you've completed)
make test BITE=05       # run a single bite
make progress           # ASCII progress bar across all 10 bites
make help               # list all targets
```

## The 10 bites

| # | Topic | Concept | Level |
|---|-------|---------|-------|
| 01 | First API Call | `client.messages.create`, response parsing | Easy |
| 02 | Structured Outputs | Pydantic + JSON from LLM | Easy |
| 03 | System Prompt Design | Role, constraints, output format | Easy |
| 04 | Multi-turn Chat | Conversation history | Easy |
| 05 | Tool Use | Function calling, agentic loop | Medium |
| 06 | Provider Protocol | `Protocol`, swappable providers | Medium |
| 07 | Repository Pattern | Data layer abstraction, CRUD | Medium |
| 08 | Service Layer | Orchestration, dependency injection | Medium |
| 09 | Human-in-the-Loop | Confidence threshold, user confirmation | Medium |
| 10 | Agent Loop | ReAct pattern, multi-tool agents | Medium |

## Next step

Done with the bites? The full curriculum picks up where these leave off — production-grade AI apps with architecture, testing, security, and human-in-the-loop design:

→ [pythonagenticai.com](https://pythonagenticai.com)
