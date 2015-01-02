#!/usr/bin/python
#
#  ~~~~~~~~~~
# | PyBoiler |
#  ~~~~~~~~~~
#
# @version: alpha-0.2.0 | python 2.7.x
# -
# @desc: jparser.py parses a given JSON file and
# converts the content into a python list
# -
#
# LICENSE
# -------
#
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2014 Bassem Dghaidi <bd@bassemdy.com>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

import os.path
import sys
import json
import pprint
import codecs

''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	--- parse_json_structure(str)
	Parsed the folder/file structure template
	contained in the input JSON file
	If structure is not valid, break the
	runtime and throw exception
'''
def parse_json_structure(file_loc):
	# Test if the file location param
	# has been passed and is not empty
	# Strings return false if empty
	if file_loc:
		# Test if the file exists
		# or an invalid location was
		# provided
		if os.path.isfile(file_loc):
			# Open the file and read the content
			with codecs.open(file_loc, 'rU', 'utf-8') as file_data:
				try:
					template_structure = json.load(file_data)
					# pprint.pprint(template_structure)
					# Return the parsed template
					return template_structure
				except:
					sys.exit('[ERROR]: Cannot parse the provided JSON file: %s' % file_loc)
				# pprint.pprint(template_structure)
		else:
			sys.exit('[ERROR]: Provided template file does not exist. \n[ERROR]: Please use absolute paths and enter the correct file location and name.')


''' ~~~~~~~~~~
	--- Main
	~~~~~~~~~~
'''
if __name__ == "__main__":
	parse_json_structure('/Users/bassemd/Projects/pyboiler/pyboiler/test_files/simple.json')
	# parse_json_structure('/Users/bassemd/Projects/pyboiler/pyboiler/test_files/simple.jsonp')
	# parse_json_structure('/Users/bassemd/Projects/pyboiler/pyboiler/test_files/perror.json')