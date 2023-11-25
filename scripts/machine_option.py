def machine_option(region, large_body):
    if region == "Craniospinal":
        return ["TB"]
    elif region == "Breast":
        if large_body:
            return ["TB", "U"]
        else:
            return ["TB", "VB", "U"]
    elif region == "BreastSpecial":
        return ["TB"]
    elif region == "Head_Neck":
        if large_body:
            return ["TB"]
        else:
            return ["TB", "VB"]
    elif region == "Abdomen":
        if large_body:
            return ["TB"]
        else:
            return ["TB", "VB"]
    elif region == "Pelvis":
        if large_body:
            return ["TB"]
        else:
            return ["TB", "VB"]
    elif region == "Crane":
        if large_body:
            return ["TB"]
        else:
            return ["TB", "VB"]
    elif region == "Lung":
        if large_body:
            return ["TB"]
        else:
            return ["TB", "VB"]
    elif region == "LungSpecial":
        if large_body:
            return ["TB"]
        else:
            return ["TB", "VB"]
    elif region == "WholeBrain":
        if large_body:
            return ["U"]
        else:
            return ["VB", "U"]