def verify_kyc(data):
    return bool(data.get("pan") and data.get("aadhar"))
