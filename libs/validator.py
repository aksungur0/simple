def validate_input(data: bytes) -> bool:
    if not data or len(data) < 10:
        print("Invalid input data")
        return False
    return True
