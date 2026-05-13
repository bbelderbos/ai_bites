---
level: medium
tags: [repository-pattern, protocols, data-layer, pydantic]
track: agentic_ai
sequence: 7
author: Bob Belderbos & Juanjo Expósito
---

# The Repository Pattern

The repository pattern separates data access from business logic. Services talk to a `Repo` interface — not directly to SQLite, files, or any specific backend.

The payoff:
- Swap in-memory storage for a real database without touching your service
- Test your service without a database at all
- One interface, many implementations

**Why care?** This is how the cohort's expense classifier stays testable while supporting both in-memory (tests) and SQLite (production) backends.

## Task

`Expense` and the `ExpenseRepo` Protocol are already defined. Implement `InMemoryExpenseRepo` with full CRUD:
- `add(expense)` — store and return the expense
- `get(expense_id)` — return the expense or `None`
- `list_all()` — return all stored expenses
- `delete(expense_id)` — remove it, return `True` if found, `False` if not
