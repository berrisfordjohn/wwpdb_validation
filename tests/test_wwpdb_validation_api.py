import unittest
# from tests.access_test_files import TestFiles
import tempfile
import logging
import os
import shutil

import wwpdb_validation.wwpdb_validation_api as wwpdb_validation_api

logger = logging.getLogger()
FORMAT = "%(filename)s - %(funcName)s - %(message)s"
logging.basicConfig(format=FORMAT)
logger.setLevel(logging.DEBUG)


class TestFiles:

    def __init__(self):
        self.FILE_ROOT = os.path.dirname(os.path.realpath(__file__))
        self.path = os.path.dirname(os.path.join(self.FILE_ROOT, '..', '..'))
        self.test_data = os.path.join(self.path, 'test_data')

        self.xml = None
        self.cif = None
        self.sf = None

    def pdb3zt9(self):
        self.xml = os.path.join(self.test_data, "3zt9_validation.xml")
        self.cif = os.path.join(self.test_data, 'pdb3zt9_refmac1_output.cif')
        self.sf = os.path.join(self.test_data, 'r3zt9sf.ent')

    def pdb1cbs(self):
        self.xml = os.path.join(self.test_data, "1cbs_validation.xml")


class TestValidationReportGeneration(unittest.TestCase):

    def setUp(self):
        self.test_files = TestFiles()

    def test_3zt9(self):
        test_dir = tempfile.mkdtemp()
        logging.debug('test dir: {}'.format(test_dir))
        output_pdf_file = os.path.join(test_dir, 'output.pdf')
        output_xml_file = os.path.join(test_dir, 'output.xml')
        output_log_file = os.path.join(test_dir, 'output.log')
        # output_cif_file = os.path.join(test_dir, 'output.cif')
        output_svg_file = os.path.join(test_dir, 'output.svg')
        output_2fofc_file = os.path.join(test_dir, 'output_2fofc')
        output_fofc_file = os.path.join(test_dir, 'output_fofc')
        self.test_files.pdb3zt9()
        worked = wwpdb_validation_api.run_validation_api(
            model_file_path=self.test_files.cif,
            structure_factors=self.test_files.sf,
            output_pdf_file_name=output_pdf_file,
            output_xml_file_name=output_xml_file,
            output_log_file_name=output_log_file,
            output_svg_file_name=output_svg_file,
            # output_2fofc_file_name=output_2fofc_file,
            # output_fofc_file_name=output_fofc_file,
            api_input_url="https://validate-pdbe.wwpdb.org/"
        )
        self.assertTrue(worked)
        shutil.rmtree(test_dir)


if __name__ == '__main__':
    unittest.main()
