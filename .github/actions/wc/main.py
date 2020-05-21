import json
import os

str = json.loads(os.environ['COUNTED_STRING'])

print(len(str))
