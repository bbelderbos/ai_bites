import importlib.util
import sys


def pytest_collect_file(parent, file_path):
    """Let me run tests locally against reference.py when solution.py is absent."""
    if file_path.name == "test_exercise.py":
        sys.modules.pop("solution", None)
        exercise_dir = file_path.parent
        if str(exercise_dir) in sys.path:
            sys.path.remove(str(exercise_dir))
        sys.path.insert(0, str(exercise_dir))

        if not (exercise_dir / "solution.py").exists():
            reference = exercise_dir / "reference.py"
            if reference.exists():
                spec = importlib.util.spec_from_file_location("solution", reference)
                assert spec and spec.loader
                module = importlib.util.module_from_spec(spec)
                sys.modules["solution"] = module
                spec.loader.exec_module(module)
