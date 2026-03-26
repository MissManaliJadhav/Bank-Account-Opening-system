def extract_text(documents):
    extracted = {}

    for doc in documents:
        if doc["type"] == "PAN":
            extracted["pan"] = "ABCDE1234F"
        elif doc["type"] == "AADHAR":
            extracted["aadhar"] = "123412341234"

    return extracted
