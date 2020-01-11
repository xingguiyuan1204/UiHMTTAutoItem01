from time import sleep

from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()

app_login_data = read_yaml("mp_login.yaml")[0]

class TestAppLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        driver = GetDriver.get_app_driver()
        # 获取 统一入口类
        self.applogin = PageIn(driver).page_get_PageAppLogin()

    # 结束
    def teardown_class(self):
        sleep(5)
        # 关闭driver
        GetDriver.quit_app_driver()

    # 登录测试方法
    def test01_app_login(self,username=app_login_data[0],pwd=app_login_data[1]):
        # 调用app登录方法
        self.applogin.page_app_login(username,pwd)
        # 断言是否登录成功
        try:
            assert self.applogin.page_if_element_exists()
            # 截图
        except Exception as e:
            # 截图
            self.applogin.base_get_img()
            # 日志
            log.error(e)
            # 抛异常
            raise


