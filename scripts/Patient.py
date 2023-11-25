class Patient:
    def __init__(self, weight, region, disability, fraction_num):
        self.weight = weight
        self.region = region
        self.disability = disability
        self.fraction_num = fraction_num
        self.large_body = weight_check(self.weight)

def weight_check(weight):
    heavy = 100
    large_body = False
    if weight > heavy:
        large_body = True
    return large_body

Regions = ["Craniospinal", "Breast", "BreastSpecial", "Head_Neck", "Abdomen", "Pelvis",
           "Crane", "Lung", "LungSpecial", "WholeBrain"]