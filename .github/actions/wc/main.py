import json
import os

str = json.loads(os.environ['INPUT_COUNTED_STRING'])

print(len(str))
