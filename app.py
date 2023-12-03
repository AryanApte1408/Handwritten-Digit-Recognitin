# from flask import Flask, request, render_template
# import tensorflow as tf
# import numpy as np
# import json
# import os
# #om
# app = Flask(__name__)
# port = int(os.environ.get("PORT", 5000))

# (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
# model = tf.keras.models.load_model('mnist')

# @app.route('/')
# def root():
#     return render_template("paint.html")

# @app.route('/infer', methods=['POST'])
# # def infer():
# #     data = np.array(request.json['input'])
# #     image = data.reshape((112, 112))[::4, ::4].reshape((1, 28, 28))
# #     result = model(image).numpy()
    
# #     predicted_class = int(np.argmax(result))
# #     print(f"Predicted Class: {predicted_class}")

# #     return predicted_class


# # class_list = [0,1,2,3,4,5,6,7,8,9]
# # def func(x):
# #     if x == 1:
# #         if predicted_class in class_list:

# def normalise(x):
#     return x* 1/255

# def predict(y):
#     normalise(y)
    
# def infer():
#     data = np.array(request.json['input'])
#     image = data.reshape((112, 112))[::4, ::4].reshape((1, 28, 28))
#     result = model(image).numpy()
#     predicted_class = int(np.argmax(result))
#     print(f"Predicted Class: {predicted_class}")

#     return predicted_class

           

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=port)


# # calculator.py
# def add(a, b):
#     return a + b

from flask import Flask, request, render_template
import tensorflow as tf
import numpy as np
import json
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
model = tf.keras.models.load_model('mnist')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/paint')
def paint():
    return render_template("paint.html")

@app.route('/infer', methods=['POST'])
def infer():
    data = np.array(request.json['input'])
    image = data.reshape((112, 112))[::4,::4].reshape((1, 28, 28))
    result = model(image).numpy()
    return json.dumps({ 'result': int(np.argmax(result)) })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

