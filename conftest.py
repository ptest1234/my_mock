import os

import pytest
import json


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="dev", help="env：表示命令行参数内容，不填写默认输出default的值内容"
    )

@pytest.fixture(scope="session")
def env_config(request):
    # env = os.getenv("ENV", "dev")
    env = request.config.getoption("--env")
    print(f"env: {env}")
    with open(f"./config/{env}_config.json") as f:
        env_data = json.load(f)
    return env_data


@pytest.fixture(scope="session")
def env_request_data(request):
    env = request.config.getoption("--env")
    with open(f"./config/{env}_request_data.json") as f:
        request_data = json.load(f)
    return request_data


@pytest.fixture(scope="session")
def env_response_data(request):
    env = request.config.getoption("--env")
    with open(f"./config/{env}_response_data.json") as f:
        _response_data = json.load(f)
    return _response_data

