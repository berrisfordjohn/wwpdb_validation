#!/usr/bin/env python
import logging
import pprint
import os
import argparse
from .xml_parsing import parse_xml


logger = logging.getLogger()
FORMAT = "%(filename)s - %(funcName)s - %(message)s"
logging.basicConfig(format=FORMAT)

class validationReport:
    def __init__(self, xml_file):
        """
        :param xml_file: input aimless XML file
        """
        self.xml_file = xml_file
        self.tree = None
        self.root = None
        self.result = dict()


    def parse_xml(self):
        """
            checks input file is XML file, parses it.
            prevents parsing twice by checking if self.tree already exists
        :return: True if a parsed aimless XML file, False if not
        """
        if not self.tree:
            self.root = parse_xml(xml_file=self.xml_file)

        if self.root is not None:
            if self.root.tag == 'AIMLESS_PIPE' or self.root.tag == 'AIMLESS':
                logging.debug('is an aimless xml file')
                return True
        return False
