from datetime import datetime
import pandas as pd
import os
from bs4 import BeautifulSoup
import requests

class MyWeb:
    def __init__(self):
        self.header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                          "/86.0.4240.75 Safari/537.36"}

        self.session = requests.session()

    def get_url(self, url: str, res_type: str = "bytes"):
        """
        get special response type from url requests. default: bytes
        :param url: link url
        :param res_type: response type from **bytes, str, json, raw**,. Default bytes.
        :return: bytes, str, dict, object
        """
        if not url:
            print('url is null')
            return None

        res = self.session.get(url, headers=self.header)
        if res_type == "bytes":
            return res.content
        if res_type == "str":
            return res.text
        if res_type == "json":
            return res.json()
        return res

    def get_soup(self,url):
        res = self.session.get(url, headers=self.header)
        return BeautifulSoup(res.text, 'html.parser')

    def get_soup_select(self,soup,tag):
        # soup.prettify()
        return soup.select(tag)

    def get_selenium_tag(self,url):

        from selenium import webdriver
        executable_path = 'E:\Chrome\chromedriver.exe'
        driver = webdriver.Chrome(executable_path)
        driver.get(url)
        pagesource = driver.page_source  # 网页源码
        scroll_500px = 'var q=document.documentElement.scrollTop=500'# 滚动条下拉500个像素
        # top_pos = 'var q=document.documentElement.scrollTop=0'# 浏览器顶部位置
        driver.find_element_by_class_name('player').click()
        driver.find_element_by_class_name('').get_attribute('')
        driver.execute_script(scroll_500px)
        driver.close()  # 关闭单个窗口


class MyDate:
    def __init__(self):
        pass

    def get_today_YMD(self):
        return datetime.datetime.now().strftime('%Y-%m-%d')


class MyFile:
    def __init__(self):
        pass

    def concat_same_dir(self, dst_dir: str, suffix: str, is_append=True, add_file_col=False, **kwargs):
        total = pd.DataFrame()
        for i in os.listdir(dst_dir):
            fullpath = os.path.join(dst_dir, i)

            if suffix and not i.endswith(suffix):
                continue

            one_df = pd.DataFrame()
            if suffix in ("xlsx", "xls"):
                one_df = pd.read_excel(fullpath, engine='openpyxl')
            elif suffix == "json":
                one_df = pd.read_json(fullpath, orient='records')
            elif suffix == "csv":
                one_df = pd.read_csv(fullpath)
            else:
                print(f"not support {suffix} file")

            if add_file_col:
                one_df['belong_file'] = i

            if is_append:
                total = pd.concat([total, one_df], ignore_index=True)
            else:
                total = pd.concat([one_df, total], ignore_index=True)
        return total

    def write_file(self,content, filename):
        if isinstance(content, str):
            content = bytes(content, encoding='utf-8')
        with open(filename, 'wb') as f:
            f.write(content)

    def makedir(self,dir_name):
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    def to_sql(self):
        import pymysql

        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', database='', charset='utf8')
        cursor = conn.cursor()
        sql = 'DROP TABLE IF EXISTS '
        cursor.execute(sql)
        sql = '''
            CREATE TABLE  (

            )ENGINE=innodb DEFAULT CHARSET=utf8;
        '''
        cursor.execute(sql)
        cursor.close()
        conn.close()


