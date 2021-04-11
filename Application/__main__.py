print("Importing Libraries")

import numpy as np
# import tensorflow as tf
from json import loads

print("Running")

appliancesData = open("Data/Appliances_5.json", 'r')
dataTable = [loads(line) for line in appliancesData]

for line in dataTable:
    print(line)
