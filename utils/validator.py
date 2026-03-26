def validate_input(data):
    required = ["name", "amount", "source"]

    for field in required:
        if field not in data:
            return False, f"{field} missing"

    if data["amount"] <= 0:
        return False, "Invalid amount"

    return True, "OK"
