# PyBoiler
PyBoiler is a simple python 2.7 script to create a project template in a given directory.

### Version

    alpha-0.2.0

### Installation

	pip install pyboiler --pre
	
	# '--pre' is added to install pre-major-release versions

### Usage
PyBoiler is extremely simple to use. 

##### Create a JSON file to match the folder structure you desire:

    $: nano structure.json 
    
    # Paste the below into your file and modify as you desire
	[{'folder': 'source'}, 
     {'file': 'source/file1.txt'}, # Nested file
     {'folder': 'sublime'}, 
     {'file': 'sublime/file2.txt'}, 
     {'folder': 'docs'}, 
     {'file': 'docs/file3.txt'}, 
     {'file': 'docs/file4.txt'},
     {'file': 'README.md'}]

##### How to execute

	usage: pyboiler.py [-h] -o PROJECT_PATH

	required arguments:
  		-o PROJECT_PATH, --project-directory PROJECT_PATH 
  				Project's absolute path where the structure will be created  		
                        	
    optional arguments:
      	-h, --help 	
      			Show this help message and exit
      			
        -i FOLDER_STRUCTURE, --folder-structure FOLDER_STRUCTURE
                JSON file containing the template folder/file
                structure to be created

Note: If the argument `-i` is not specified the script will use the default template (hardcoded) 

### Change Log
#### alpha-0.2.0
* Folder and File structure template can be imported from a JSON file
* Added jparser.py to parse and validate the JSON file

### Tests
This script has been tests on Mac OS X 10.9.4 only. There is no guarantee it will perform as expected on other Operating Systems.

### LICENSE

	DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE

			Version 2, December 2004

	Copyright (C) 2014 Bassem Dghaidi <bd@bassemdy.com>

	Everyone is permitted to copy and distribute verbatim or modified
	copies of this license document, and changing it is allowed as long
	as the name is changed.

		DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
		TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

	0. You just DO WHAT THE FUCK YOU WANT TO.