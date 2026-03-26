def calculate_risk(data):
    score = 0

    amount = data.get("amount", 0)
    source = data.get("source", "").lower()
    international = data.get("international", False)

    # RULE 1
    if source == "cash" and amount > 50000:
        score += 40

    # RULE 2
    if source == "crypto":
        score += 50

    # RULE 3
    if international:
        score += 30

    # LEVEL
    if score < 30:
        level = "LOW"
    elif score <= 70:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return score, level
