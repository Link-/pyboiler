#!/usr/bin/python
# @version: alpha-0.3.0 | python 2.7.x
# -
# @desc: PyBoiler is a simple python script
# that creates the basic folder/file structure
# for simple python projects.
# -

import argparse
from distutils.util import strtobool
import codecs
import json
import os


DEFAULT_FOLDER_STRUCTURE = [
	{'folder': 'source'},
	{'folder': 'sublime'},
	{'folder': 'docs'},
	{'file': 'README.md'}
]


def make_file(path):
	"""Create an empty file in a given directory"""
	open(path, 'a').close()


def make_folder(path):
	"""Create an empty directory"""
	if not os.path.exists(path):
		os.makedirs(path)


def build_structure(target, source, override):
	"""Builds the folder structure in a given directory"""
	if source:
		try:
			if os.path.isfile(source):
				"""Handle UTF-8 Files"""
				with codecs.open(source, 'rU', 'utf-8') as file_data:
					structure = json.load(file_data)
		except:
			exit('> Fatal error - cannot parse the provided JSON files: %s' % source)
	else:
		"""Use the default structure if the above fails"""
		structure = DEFAULT_FOLDER_STRUCTURE

	print('> {} folder structure: {}\n'.format(
		'Overriding' if override else 'Creating',
		target))

	for entry in structure:
		for _type, name in entry.iteritems():
			try:
				joined = os.path.join(target, name)
				if _type == 'folder':
					make_folder(joined)
				elif _type == 'file':
					make_file(joined)
				print('Created: %s' % joined)
			except OSError:
				exit('> Fatal error - exiting...')


def user_yes_no_query(question):
	"""Prompts the user for a choice"""

	print('%s [y/n]:' % question)

	while True:
		try:
			return strtobool(raw_input().lower())
		except ValueError:
			print("Please respond with 'y' or 'n'.")


def build_parser():
	"""Builds the argument parser"""
	parser = argparse.ArgumentParser()

	parser.add_argument(
		'-o', '--output-directory',
		dest='target',
		help='Target output path where the structure will be created',
		type=str,
		required=True)

	parser.add_argument(
		'-s', '--source-file',
		dest='source',
		help='Source JSON file containing structure to be created',
		type=str,
		required=False)

	return parser


def main():
	args = build_parser().parse_args()

	exists = os.path.exists(args.target)
	should_override = lambda: user_yes_no_query(
			'> Folder already exists, do you wish to override it?')

	if exists:
		if should_override():
			build_structure(args.target, args.source, override=True)
	else:
		build_structure(args.target, args.source, override=False)


if __name__ == "__main__":
	main()
