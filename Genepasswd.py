#Genepasswd by ExE 

import random

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abdcefghijklmnopqrstuvwxyz"
NUMBER = "0123456789"

all = upper+lower+NUMBER
length = 10

passwd ="".join(random.sample(all,length))

print(f"The passwd generated: {passwd}")