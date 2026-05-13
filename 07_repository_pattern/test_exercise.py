from solution import InMemoryExpenseRepo, Expense


def _expense(**kwargs) -> Expense:
    return Expense(**{"description": "coffee", "amount": 3.50, "category": "Food", **kwargs})


def test_add_and_get():
    repo = InMemoryExpenseRepo()
    e = repo.add(_expense())
    assert repo.get(e.id) == e


def test_get_missing_returns_none():
    repo = InMemoryExpenseRepo()
    assert repo.get("nonexistent") is None


def test_list_all():
    repo = InMemoryExpenseRepo()
    repo.add(_expense(description="lunch"))
    repo.add(_expense(description="bus"))
    assert len(repo.list_all()) == 2


def test_delete_existing():
    repo = InMemoryExpenseRepo()
    e = repo.add(_expense())
    assert repo.delete(e.id) is True
    assert repo.get(e.id) is None


def test_delete_missing_returns_false():
    repo = InMemoryExpenseRepo()
    assert repo.delete("does-not-exist") is False
