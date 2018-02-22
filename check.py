import warnings
import json
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
	song = djv.recognize(FileRecognizer, "wav/hello/test.wav")
	print "From file we recognized: %s\n" % song
	# if match => get existing room
	# else => give new room
	# Fingerprints audio and adds to database, with room id
	djv.fingerprint_directory("wav/hello", [".wav"])
	# Delete file and directory


