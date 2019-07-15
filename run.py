# coding=utf-8
"""
程序运行入口
"""

import sys
import re

try:
    from everyday_wechat import __version__
    print('EverydayWechat 程序版本号：{}'.format(__version__))
except Exception as exception:
    print(str(exception))
    print('请将脚本放在项目根目录中运行')
    print('请检查项目根目录中的 everyday_wechat 文件夹是否存在')
    exit(1)



def run():
    """ 主程序入口"""

    # 判断当前环境是否为 python 3
    if sys.version_info[0] == 2:
        print('此项目不支持 Python 版本！')
        return

    # 检查依赖库是否都已经安装上
    try:
        import itchat
        import apscheduler
        import requests
        # import requests_html
        from bs4 import BeautifulSoup
        if itchat.__version__ != '1.3.10':
            print('请将 itchat 的版本升级至 1.3.10！')
            return

    except (ModuleNotFoundError) as error:
        # No module named 'teim'
        no_modules = re.findall(r"named '(.*?)'$", str(error))
        if no_modules:
            print('当前环境缺少 {} 库'.format(no_modules[0]))
        else:
            print('当前环境库不完整')
        return

    try:
        from everyday_wechat.utils import config
        from everyday_wechat.utils.db_helper import is_open_db
        from everyday_wechat import main
        db_text = '已开启数据库功能' if is_open_db else '数据库未开启或启动失败'
        print(db_text)
    except Exception as exception:
        print(str(exception))
        return

    main.run()



if __name__ == '__main__':
    run()
