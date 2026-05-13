import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / ".ai_bites_progress.json"

GREEN = "\033[92m"
DIM = "\033[90m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
RESET = "\033[0m"


def find_bites() -> list[Path]:
    return sorted(p for p in ROOT.iterdir() if p.is_dir() and p.name[:2].isdigit())


def has_student_solution(bite: Path) -> bool:
    return (bite / "solution.py").exists()


def run_tests(bite: Path) -> bool:
    result = subprocess.run(
        ["uv", "run", "pytest", "-q", "--no-header", str(bite / "test_exercise.py")],
        cwd=ROOT,
        capture_output=True,
    )
    return result.returncode == 0


def load_state() -> dict:
    if STATE.exists():
        return json.loads(STATE.read_text())
    return {"completed": [], "history": []}


def save_state(state: dict) -> None:
    STATE.write_text(json.dumps(state, indent=2))


def main() -> int:
    bites = find_bites()
    state = load_state()
    completed = set(state["completed"])
    newly_done = []

    print(f"\n{BOLD}AI Bites — Progress{RESET}\n")

    for bite in bites:
        name = bite.name
        if not has_student_solution(bite):
            mark = f"{DIM}·{RESET}"
            status = f"{DIM}not started{RESET}"
        elif run_tests(bite):
            mark = f"{GREEN}✓{RESET}"
            status = f"{GREEN}passing{RESET}"
            if name not in completed:
                newly_done.append(name)
                completed.add(name)
        else:
            mark = f"{YELLOW}✗{RESET}"
            status = f"{YELLOW}in progress{RESET}"
        print(f"  {mark}  {name:<25} {status}")

    bar = "".join(
        f"{GREEN}█{RESET}" if b.name in completed else f"{DIM}░{RESET}" for b in bites
    )
    pct = round(100 * len(completed) / len(bites))
    print(f"\n  [{bar}]  {len(completed)}/{len(bites)}  ({pct}%)\n")

    if newly_done:
        print(f"  {GREEN}🎉 New this run: {', '.join(newly_done)}{RESET}\n")
        state["history"].append(
            {"at": datetime.now(timezone.utc).isoformat(), "completed": newly_done}
        )

    state["completed"] = sorted(completed)
    save_state(state)

    if len(completed) == len(bites):
        print(
            f"  {BOLD}{GREEN}All bites complete. Ready for the cohort → https://pythonagenticai.com{RESET}\n"
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
