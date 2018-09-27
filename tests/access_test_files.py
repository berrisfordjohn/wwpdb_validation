import os

class TestFiles:

    def __init__(self):
        self.FILE_ROOT = os.path.dirname(os.path.realpath(__file__))
        self.path = os.path.dirname(os.path.join(self.FILE_ROOT, '..', '..'))
        self.test_data = os.path.join(self.path, 'test_data')

        self.cif = None
        self.structure_factor = None

    def pdb3zt9(self):
        self.cif = os.path.join(self.test_data, "pdb3zt9_refmac1.cif")
        self.structure_factor = os.path.join(self.test_data, 'r3zt9sf.ent')

    def pdb4hg7(self):
        self.cif = os.path.join(self.test_data, "deposition_refmac1.cif")

    def pdb6fqf(self):
        self.cif = os.path.join(self.test_data, "pdb6fqf_refmac1.cif")
        self.structure_factor = os.path.join(self.test_data, 'r6fqfsf.ent')

    def pdb6db6(self):
        self.cif = os.path.join(self.test_data, 'pdb6db6_refmac1.cif')
        self.structure_factor = os.path.join(self.test_data, 'r6bd6sf.ent')

    def pdb5l1z(self):
        self.cif = os.path.join(self.test_data, "5l1z_refmac1.cif")
        self.structure_factor = os.path.join(self.test_data, 'r5l1zsf.ent')
