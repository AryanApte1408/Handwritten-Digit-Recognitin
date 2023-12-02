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

# # Call infer function and store the result
# predicted_class_result = infer()

# # Now you can use predicted_class_result outside the function
# class_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# def func(x):
#     if x == 1:
#         if predicted_class_result in class_list:
#            return True
           




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




def infer(data):
    image = data.reshape((112, 112))[::4, ::4].reshape((1, 28, 28))
    result = model(image).numpy()
    predicted_class = int(np.argmax(result))
    print(f"Predicted Class: {predicted_class}")
    return predicted_class

# Route to handle the POST request
@app.route('/infer', methods=['POST'])
def infer_route():
    data = np.array(request.json['input'])
    predicted_class_result = infer(data)
    class_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = func(1, predicted_class_result, class_list)
    return json.dumps({'result': result})

def func(x, predicted_class_result, class_list):
    if x == 1:
        return predicted_class_result in class_list

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

def normalise(m,x,c):
    return m + x + c
