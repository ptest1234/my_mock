# 测试用例demo文件
import requests

class TestPytestDemo:
	def test_get_demo(self):
		base_url = "https://my-json-server.typicode.com/ptest1234/my_mock"
		#发起请求
		request = requests.get(f"{base_url}/get")
		print(request.text)
		#断言
		assert request.status_code == 200
		assert request.json()['name'] == '请求成功'


	def test_post_demo(self):
		base_url = "https://my-json-server.typicode.com/ptest1234/my_mock"
		requests_data = {
			"title": "test",
			"body": "bar",
			"userId": 2
		}
		# 发起请求
		response = requests.post(f"{base_url}/posts", requests_data)
		# 断言
		assert response.status_code == 201
		print(response.json())
		assert response.json()['userId'] == '20'
		assert response.json()['id'] == 3
		# attach(data=self.driver.get_screenshot_as_png())截图