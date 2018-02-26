import sys
import json

def convert_file(file_name):
	print("Reading " + file_name)
	data = json.load(open(file_name)) # TODO check file exists
	print(len(data))

if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Please pass json file as argument.")
		sys.exit()

	convert_file(sys.argv[1])