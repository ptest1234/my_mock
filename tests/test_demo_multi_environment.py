import allure
import requests


@allure.feature("多环境测试")
class TestDemoMultiEnvironment:

    @allure.story("Test example get endpoint")
    @allure.title("Verify the get API")
    @allure.description("verify the get API response status code and data")
    @allure.severity("blocker")
    def test_get_demo_env(self, env_config, env_request_data, env_response_data):
        # 获取对于环境的数据
        base_url = env_config['host']
        get_api = env_config['getAPI']
        get_api_response_data = env_response_data['getAPI']
        # 发送请求
        response = requests.get(base_url + get_api)
        # 检查响应状态码
        assert response.status_code == 200
        # 检查响应数据
        assert response.json() == get_api_response_data

    @allure.story("Test example POST API")
    @allure.title("Verify the POST API")
    @allure.description("verify the POST API response status code and data")
    @allure.severity("Critical")
    def test_post_demo_env(self, env_config, env_request_data, env_response_data):

        base_url = env_config['host']
        post_api = env_config['postAPI']
        data = env_request_data['postApi']
        post_api_response_data = env_response_data['postAPI']
        # 发送请求
        response = requests.post(base_url + post_api, data=data)
        # 检查响应状态码
        assert response.status_code == 201
        # 检查响应数据
        print("response data is" + str(response.json()))
        assert response.json() == post_api_response_data
