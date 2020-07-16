# Deploying a Model

This repo [train a neural network on MNIST with Keras](https://www.tensorflow.org/datasets/keras_example), [create a Flask app to serve it](https://towardsdatascience.com/deploying-deep-learning-models-using-tensorflow-serving-with-docker-and-flask-3b9a76ffbbda), then [containerise and deploy the app onto Heroku](https://medium.com/@ksashok/containerise-your-python-flask-using-docker-and-deploy-it-onto-heroku-a0b48d025e43).

## Setup the Environment

- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip install --upgrade pip && pip install flask tensorflow`
- `pip freeze > requirements.txt`

## Train the Model

This trains a simple neural network to classify MNIST digits.

- `python3 ./train.py`

The model is saved to `mnist/`.

## Build the Flask App

The Flask app is responsible for two things:

1) Serving the static front-end site.
2) Hosting the endpoint which we pass data to for inference.

The app is found at `app.py` and `templates/` and `static/` hold resources for the front-end.  The site is hosted at `/` and one can POST gray-scale image data to `/infer` to pass the image data to the model for inference.

## Deploy to Heroku

You will need Docker and the Heroku CLI installed and authenticated.

- `heroku container:push web --app <app-name>`
- `heroku container:release web --app <app-name>`

Once deployed, navigate to [`https://<app-name>.herokuapp.com/`](https://deployable-model.herokuapp.com/) (the app may take a minute to load).