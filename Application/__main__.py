print("Importing Libraries")

import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from json import loads

maxRating = 5
batchSize = 512
highestRating = 5.0

print("Running")

appliancesData = open("Data/Office_Products_5.json", 'r')  # Opens data file.
dataTable = [loads(line) for line in appliancesData]  # Converts each line of data into a dictionary.

# Makes list of tuples with the reviews tied to their ratings.
reviews = list()
ratings = list()
for review in dataTable:
    reviews.append(review["reviewText"])
    ratings.append(float(review["overall"])/highestRating)

# Split lists.
length = len(reviews)
trainReviews, validationReviews, testReviews = np.split(reviews, [round(length * 0.3), round(length * 0.5)])
trainRatings, validationRatings, testRatings = np.split(ratings, [round(length * 0.3), round(length * 0.5)])

# Convert lists into tensors.
trainData = tf.data.Dataset.from_tensor_slices((trainReviews, trainRatings))
validationData = tf.data.Dataset.from_tensor_slices((validationReviews, validationRatings))
testData = tf.data.Dataset.from_tensor_slices((testReviews, testRatings))

# Makes first layer. Used to convert text into numbers.
embedding = "https://tfhub.dev/google/nnlm-en-dim50/2"
hubLayer = hub.KerasLayer(embedding, input_shape=[], dtype=tf.string, trainable=True)

# Creates model with 2 layers.
model = tf.keras.Sequential()
model.add(hubLayer)
model.add(tf.keras.layers.Dense(16, activation='relu'))
model.add(tf.keras.layers.Dense(1))

model.summary() # Shows summary of the model.

# Compiles model using logit, an optimizer and a chosen metric.
model.compile(optimizer='adam', loss=tf.keras.losses.BinaryCrossentropy(from_logits=True), metrics=['accuracy'])

# Fits the model to the data.
history = model.fit(trainData.shuffle(round(length*0.3)).batch(batchSize),
                    epochs=10,
                    validation_data=validationData.batch(batchSize),
                    verbose=1)

# Evaluates the model's accuracy and loss.
results = model.evaluate(testData.batch(batchSize), verbose=2)

# Shows results of evaluation.
print("Results:")
for name, value in zip(model.metrics_names, results):
    print("%s: %.3f" % (name, value))
