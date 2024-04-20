import pytest
import os

if __name__ == '__main__':
    pytest.main(['--env=dev'])
    # os.system('allure generate temp -o report --clean')
