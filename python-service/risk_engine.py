def calculate_risk(data):
    score = 0

    if data.get("source") == "cash" and data.get("amount", 0) > 50000:
        score += 40

    if data.get("source") == "crypto":
        score += 50

    if data.get("international"):
        score += 30

    if score < 30:
        level = "LOW"
    elif score <= 70:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return score, level
