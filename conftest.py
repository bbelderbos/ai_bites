import sys


def pytest_collect_file(parent, file_path):
    if file_path.name == "test_exercise.py":
        sys.modules.pop("solution", None)
        exercise_dir = str(file_path.parent)
        if exercise_dir in sys.path:
            sys.path.remove(exercise_dir)
        sys.path.insert(0, exercise_dir)
