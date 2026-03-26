BLACKLIST = ["Fraud Person", "Scammer XYZ"]

def aml_check(name):
    return name not in BLACKLIST
