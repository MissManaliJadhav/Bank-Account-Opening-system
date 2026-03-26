BLACKLIST = ["Fraud Person", "Scammer XYZ"]

def aml_check(name):
    if name in BLACKLIST:
        return False
    return True
