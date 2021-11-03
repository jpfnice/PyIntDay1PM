

import json
with open("file.out", "r") as fic:
    d=json.load(fic)
    
print(d, type(d))