# 功能列表
db.json自定义mock服务 

pytest测试github工作流持续集成

运行配置
# 运行步骤：
版本：python3.12
安装需要包：pip3 install -r requirements.txt
# pytest 分布式执行 
pytest -n 2 -v
# 根据标签执行测试
pytest -m Smoke
# 生成allure报告服务
allure serve temp
# 切换环境运行测试
pytest --env=dev 