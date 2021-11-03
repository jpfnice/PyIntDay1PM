

d={"Geneva":{"Date":"12/02/2001", "temperature":23.4},
   "Lausanne":{"Date":"14/02/2001", "temperature":29.2},
   "Nyon":{"Date":"14/02/2001", "temperature":24.3}
   }

import json
with open("file.out", "w") as fic:
    json.dump(d,fic) # dict list string bool int float 