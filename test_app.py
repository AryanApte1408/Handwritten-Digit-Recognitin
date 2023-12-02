# import json
# import pytest
# from app import app  # Replace with the actual name of your Flask app file

# @pytest.fixture
# def client():
#     app.config['TESTING'] = True
#     with app.test_client() as client:
#         yield client

# def test_infer_endpoint(client):
#     input_data = {
#         'input': [[0] * 112] * 112  # Replace with your actual input data
#     }

#     response = client.post('/infer', json=input_data)

#     assert response.status_code == 200
#     data = json.loads(response.data.decode('utf-8'))
#     assert 'result' in data
#     assert isinstance(data['result'], int)



from app import normalise

def check_predict():
    assert normalise(0,1,2) == 3

def negative_numbers():
    assert normalise(-3,-4,-5) == -12

def float():
    assert normalise(6.0,7.0,8.0) == 21.0
