def calculate(a: int, b: int, op: str) -> float | int:
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다.")
        return a / b
    raise ValueError("지원하지 않는 연산자입니다. +, -, *, / 만 가능합니다.")


def main() -> None:
    try:
        a = int(input("첫 번째 정수를 입력하세요: ").strip())
        op = input("연산자를 입력하세요 (+, -, *, /): ").strip()
        b = int(input("두 번째 정수를 입력하세요: ").strip())
        result = calculate(a, b, op)
        print(f"결과: {result}")
    except ValueError as error:
        print(f"입력 오류: {error}")
    except ZeroDivisionError as error:
        print(f"계산 오류: {error}")


if __name__ == "__main__":
    main()
