import warnings
import json
import sys
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf.SAMPLE") as f:
    config = json.load(f)

if __name__ == '__main__':

	# create a Dejavu instance
	djv = Dejavu(config)

	# Recognize audio from file
	client = sys.argv[1]
	filename = sys.argv[2]
	path = "wav/" + client + "/" + filename + ".wav"
	song = djv.recognize(FileRecognizer, path)
	if not song:
			# if match => get existing room
			print 'We need to make a new room number.'
	else:
		# else => give new room
		print "From file we recognized: %s\n" % song

	# Fingerprints audio and adds to database, with room id
	# djv.fingerprint_directory("wav/hello", [".wav"])
	# Delete file and directory
