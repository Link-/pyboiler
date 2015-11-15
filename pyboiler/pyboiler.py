#!/usr/bin/python

import argparse
from distutils.util import strtobool
import json
import os


DEFAULT_FOLDER_STRUCTURE = [
	{'folder': 'source'},
	{'folder': 'sublime'},
	{'folder': 'docs'},
	{'file': 'README.md'}
]


def touch(path):
	"""Create an empty file in a given directory"""
	open(path, 'a').close()


def build_folder_structure(project_path, file_loc, override):
	"""Builds the folder structure in a given directory"""

	if file_loc:
		folder_structure = json.load(file_loc)
	else:
		folder_structure = DEFAULT_FOLDER_STRUCTURE

	if override:
		print('> Overriding content of the directory: %s' % project_path)
		print('> Creating the folder structure now... \n')
	else:
		print('> Creating the folder the directory: %s \n' % project_path)

	for lst in folder_structure:
		for t, n in lst.iteritems():
			try:
				joint_path = os.path.join(project_path, n)

				if t == 'folder':
					if not os.path.exists(joint_path):
						os.makedirs(joint_path)
				elif t == 'file':
					touch(joint_path)

				print('Created: %s' % joint_path)

			except OSError:
				print('> Fatal error - exiting...')


def user_yes_no_query(question):
	"""Prompts the user for a choice"""

	print('%s [y/n]:' % question)

	while True:
		try:
			return strtobool(raw_input().lower())
		except ValueError:
			print("Please respond with 'y' or 'n'.")


def main():
	args_parser = argparse.ArgumentParser()

	args_parser.add_argument(
		'-o', '--project-directory',
		dest='project_path',
		help='Project\'s absolute path where the structure will be created',
		type=str,
		required=True)

	args_parser.add_argument(
		'-i', '--folder-structure',
		dest='folder_structure',
		help='file containing the template folder/file structure to be created',
		type=str,
		required=False)

	received_args = args_parser.parse_args()

	if os.path.exists(received_args.project_path):
		override_bool = user_yes_no_query(
			'[WARNING]: Folder already exists, do you wish to override it?')

		if not override_bool:
			exit('[WARNING]: Cleaning up and exiting...')
		else:
			build_folder_structure(
				received_args.project_path,
				received_args.folder_structure,
				True)
	else:
		build_folder_structure(
			received_args.project_path,
			received_args.folder_structure,
			False)


if __name__ == "__main__":
	main()
