"""Session 8 capstone: interactive task list with lists and loops."""

# Filename: src/L1/S8/03_task_manager.py

import sys

HELP_TEXT = """03_task_manager.py

Purpose
    Build a simple task list: add items, list them, mark one done (remove).

Usage
    python src/L1/S8/03_task_manager.py
"""


def show_tasks(tasks: list[str]) -> None:
    if not tasks:
        print("  (no tasks yet)")
        return
    for index, task in enumerate(tasks, start=1):
        print(f"  {index}. {task}")


def main(argv: list[str]) -> int:
    if any(arg in {"-h", "--help"} for arg in argv[1:]):
        print(HELP_TEXT)
        return 0

    print("=== Session 8: Task manager ===")
    print("Commands: add, list, done <number>, quit\n")

    tasks: list[str] = []

    while True:
        command = input("task> ").strip().lower()

        if command == "quit":
            print("Goodbye!")
            break

        if command == "list":
            print("Tasks:")
            show_tasks(tasks)
            continue

        if command == "add":
            label = input("  task name: ").strip()
            if label:
                tasks.append(label)
                print(f"  added {label!r}")
            continue

        if command.startswith("done "):
            try:
                number = int(command.split(maxsplit=1)[1])
            except (IndexError, ValueError):
                print("  usage: done <number>")
                continue
            if 1 <= number <= len(tasks):
                finished = tasks.pop(number - 1)
                print(f"  completed {finished!r}")
            else:
                print("  invalid task number")
            continue

        print("  unknown command — try add, list, done <n>, quit")
    return 0


raise SystemExit(main(sys.argv))
