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
		structure = json.load(source)
	else:
		structure = DEFAULT_FOLDER_STRUCTURE

	print('> {} folder structure: {}\n'.format(
		'Overriding' if override else 'Creating',
		target))

	builder = {
		'file': make_file,
		'folder': make_folder,
	}

	for entry in structure:
		for _type, name in entry.iteritems():
			try:
				joined = os.path.join(target, name)
				builder[_type](joined)  # dispatch based on node type
				print('Created: %s' % joined)
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
