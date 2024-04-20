import requests
import json


with open('./config/config.json', 'r') as file:
    config_data = json.load(file)

with open('./config/request.json', 'r') as file:
    request_data = json.load(file)

with open('./config/response_data.json', 'r',) as file:
    response_data = json.load(file)


def test_get_demo():
    base_url = config_data['host']
    get_api = config_data['getAPI']
    get_api_response_data = response_data['getAPI']
    # 发送请求
    response = requests.get(base_url+get_api)

    # 检查响应状态码
    assert response.status_code == 200

    # 检查响应数据
    assert response.json() == get_api_response_data

def test_post_demo():
    base_url = config_data['host']
    post_api = config_data['postAPI']
    data = request_data['postApi']
    post_api_response_data = response_data['postAPI']
    # 发送请求
    response = requests.post(base_url + post_api, data=data)

    # 检查响应状态码
    assert response.status_code == 201

    # 检查响应数据
    assert response.json() == post_api_response_data