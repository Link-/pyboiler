#!/usr/bin/python
# 
#  ~~~~~~~~~~
# | PyBoiler |
#  ~~~~~~~~~~
# 
# @version: alpha-0.1.4 | python 2.7.x
# -
# @desc: PyBoiler is a simple python script
# that creates the basic folder/file structure
# for simple python projects.
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

import os, sys
from os.path import join, exists
from distutils.util import strtobool
import argparse

# Modify the folder stucture as you like
FOLDER_STRUCTURE = [{'folder': 'source'}, 
					# {'file': 'source/file1.txt'},
					{'folder': 'sublime'}, 
					# {'file': 'sublime/file2.txt'}, 
					{'folder': 'docs'}, 
					# {'file': 'docs/file3.txt'}, 
					# {'file': 'docs/file4.txt'},
					{'file': 'README.md'}]

''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	--- touch(str)
	Create an empty file in a given directory
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
def touch(path):
	open(path, 'a').close()


''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	--- build_folder_structure(str, boolean)
	Builds the folder structure in
	a given directory
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
def build_folder_structure(project_path, override):
	if override:
		sys.stdout.write('Overriding content of the directory: %s \n' % project_path)
		sys.stdout.write('Creating the folder structure now... \n\n')
	else:
		sys.stdout.write('Creating the folder the directory: %s \n\n' % project_path)

	# Create the source dir
	for lst in FOLDER_STRUCTURE:
		for t, n in lst.iteritems():
			try:
				# Define full path
				joint_path = join(project_path, n)

				if t == 'folder':
					# Make Directory
					if not exists(joint_path):
						os.makedirs(joint_path)
				elif t == 'file':
					# Create file
					touch(joint_path)

				sys.stdout.write('Created: %s \n' % joint_path)

			except OSError:
				sys.stdout.write('ERROR: fatal error - exiting...\n');


''' ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	--- user_yes_no_query(str)
	Prompts the user for a choice
	return Boolean
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
def user_yes_no_query(question):
	sys.stdout.write('%s [y/n]:\n' % question)

	# Keep waiting for the proper answer
	while True:
		try:
			return strtobool(raw_input().lower())

		except ValueError:
			sys.stdout.write('Please respond with \'y\' or \'n\'.\n')


''' ~~~~~~~~~~
	--- main()
	~~~~~~~~~~
'''
def main():
	# First we parse the CLI arguments passed to the script
	args_parser = argparse.ArgumentParser()

	args_parser.add_argument('-o', '--project-directory',
						dest = 'project_path',
						help = 'Project\'s absolute path where the structure will be created', 
						type=str, required=True)

	received_args = args_parser.parse_args()

	# We verify the received argument's validity
	# first we check if the folder exists and 
	# prompt for override choice
	if os.path.exists(received_args.project_path):
		# Warn that the folder exists and ask if override
		override_bool = user_yes_no_query('WARN: Folder already exists, do you wish to override it?')

		if override_bool == False:
			# Exit if no override is wanted
			sys.exit('Cleaning up and exiting...')
		else: 
			# Continue the code execution
			build_folder_structure(received_args.project_path, True)
	else:
		# Continue as normal
		build_folder_structure(received_args.project_path, False)


''' ~~~~~~~~~~
	--- Main
	~~~~~~~~~~
'''
if __name__ == "__main__":
	main()