"""Simple terminal UI for calculator operations."""

from calc import add, divide, multiply, subtract


OPERATIONS = {
    "1": ("add", add),
    "2": ("subtract", subtract),
    "3": ("multiply", multiply),
    "4": ("divide", divide),
}


def _read_number(label: str) -> float:
    while True:
        raw = input(f"Enter {label}: ").strip()
        try:
            return float(raw)
        except ValueError:
            print("Invalid number. Try again.")


def main() -> None:
    print("Calculator TUI")
    print("1) add")
    print("2) subtract")
    print("3) multiply")
    print("4) divide")

    choice = input("Choose operation (1-4): ").strip()
    if choice not in OPERATIONS:
        print("Invalid choice.")
        return

    op_name, op_func = OPERATIONS[choice]
    first = _read_number("first number")
    second = _read_number("second number")

    try:
        result = op_func(first, second)
    except ZeroDivisionError as err:
        print(f"Error: {err}")
        return

    print(f"Result ({op_name}): {result}")


if __name__ == "__main__":
    main()
