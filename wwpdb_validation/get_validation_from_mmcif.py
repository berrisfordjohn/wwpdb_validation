from wwpdb_validation.cif_handling import mmcifHandling
import logging
import argparse

logger = logging.getLogger()
FORMAT = "%(filename)s - %(funcName)s - %(message)s"
logging.basicConfig(format=FORMAT)

class ExtractValidationFromMmcif():

    def __init__(self, mmcif_file):
        self.mmcif_file = mmcif_file
        self.mm = mmcifHandling(fileName=self.mmcif_file)
        self.validate_data = dict()
        self.category = None

    def parse_mmcif(self):
        parsed = self.mm.parse_mmcif()
        return parsed

    def get_validation_data(self):
        parsed = self.parse_mmcif()
        if parsed:
            self.get_distant_solvent()
        return self.validate_data

    def get_mmcif_cat(self):
        return '_{}.'.format(self.category)

    def get_distant_solvent(self):
        self.category = 'pdbx_distant_solvent_atoms'
        category_data = self.mm.getCategory(category=self.category)
        if category_data:
            cat_validation_data = category_data.get(self.get_mmcif_cat())
            model_nums = cat_validation_data.get('PDB_model_num')
            auth_atom_ids = cat_validation_data.get('auth_atom_id')
            auth_chain_ids = cat_validation_data.get('auth_asym_id')
            auth_seq_nums = cat_validation_data.get('auth_seq_id')
            macromolecule_distances = cat_validation_data.get('neighbor_macromolecule_distance')
            ligand_distances = cat_validation_data.get('neighbor_ligand_distance')

            output_dict = {'model_nums': model_nums, 'atoms': auth_atom_ids, 'chains': auth_chain_ids,
                           'seqnum': auth_seq_nums, 'mm_dict': macromolecule_distances, 'lig_dist': ligand_distances}

            self.validate_data[self.category] = output_dict

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_mmcif', help='input mmcif file', type=str, required=True)
    parser.add_argument('-d', '--debug', help='debugging', action='store_const', dest='loglevel', const=logging.DEBUG,
                        default=logging.INFO)

    args = parser.parse_args()
    logger.setLevel(args.loglevel)

    validation_data = ExtractValidationFromMmcif(mmcif_file=args.input_mmcif).get_validation_data()
    print(validation_data)