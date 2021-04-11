print("Importing Libraries")

import numpy as np
# import tensorflow as tf
from json import loads

print("Running")

appliancesData = open("Data/Appliances_5.json", 'r')  # Opens data file.
dataTable = [loads(line) for line in appliancesData]  # Converts each line of data into a dictionary.

# Prints each dictionary.
for line in dataTable:
    print(line)
