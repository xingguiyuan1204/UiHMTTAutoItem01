
import page
from base.app_base import AppBase


class PageAppLogin(AppBase):

    def page_input_username(self,username):
        self.base_input(page.app_username,username)

    def page_input_pwd(self,pwd):
        self.base_input(page.app_pwd,pwd)

    def page_click_app_login_bth(self):
        self.base_click(page.app_login_btn)

    # 判断我是否存在
    def page_if_element_exists(self):
        try:
            el = self.base_find(page.app_me, timeout=3)
            print("找到我的菜单了！,它的位置位于：{}".format(el.location))
            return True  # 找到
        except:
            print("没到我的菜单！")
            return False  # 没找到

    # 登录业务
    def page_app_login(self,username,pwd):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_app_login_bth()

    # 登录成功业务
    def page_app_login_ok(self, username="13812345678", pwd="246810"):
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_app_login_bth()
