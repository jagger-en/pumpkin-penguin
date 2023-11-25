class Machine:
    def __init__(self, machine_type, index):
        self.type = machine_type
        self.index = index

machine_type = ["TB", "VB", "U"]


TB1 = Machine("TB",1)
TB2 = Machine("TB",2)
VB1 = Machine("VB",1)
VB2 = Machine("VB",2)
U = Machine("U",1)