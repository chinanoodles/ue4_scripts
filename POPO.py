#coding=utf-8
'''
Created on 2015年5月12日

@author: hzwangzhiwei
'''
import os
import json
import logging
import sys
sys.path.append("Q:/HoudiniTool/HexTool/scripts/python/requests")

import requests

POPO_interface = 'http://hs.nie.netease.com:8888/api/post_popo'
logger = logging.getLogger(__name__)

DEBUG = os.environ.get("DEBUG")
POPO_USER = os.environ.get("POPO_USER")

reload(sys)
sys.setdefaultencoding('utf-8')

def send_to_user(popo, msg, font = '宋体', italic = '0', underline = '0', color = '000000', atuids=None):
    try:
        if DEBUG: msg = "%s\r\nsend to: %s" % (msg, popo)
        r = requests.post('http://10.246.13.189:10024/api/post_popo',
                  data = {
                          'uid': POPO_USER if DEBUG else popo,
                          'msg': msg,
                          'font': font,
                          'italic': italic,
                          'underline': underline,
                          'color': color,
                          'atuids': json.dumps(atuids) if atuids != None else None
                })
        r = r.json()
        if r['status'] == 1:
            logger.info("send to: %s, msg: %s", popo, msg)
            return True
        return False
    except Exception as e:
        logger.exception(e)
        return False

def send_to_users(popos, msg, font = '微软雅黑', italic = '0', underline = '0', color = 'EE6AA7'):
    try:
        if DEBUG: msg = "%s\r\nsend to: %s" % (msg, json.dumps(popos))
        r = requests.post(POPO_interface,
                  data = {
                          'uids': json.dumps([POPO_USER]) if DEBUG else json.dumps(popos),
                          'msg': msg,
                          'font': font,
                          'italic': italic,
                          'underline': underline,
                          'color': color
                })
        r = r.json()
        if r['status'] == 1:
            logger.info("send to: %s, msg: %s", popos, msg)
            return True
        return False
    except Exception as e:
        logger.exception(e)
        return False

# popo 发送图片方式如下
# 将图片放到 10.246.14.135 的目录 /home/yqn1481/hex_platform/Flasky/Scripts/app/static/popo_img 可自动获得对应的网址链接（获取其他任意有效的图片地址
# print send_to_user(u'你的popo前缀', '%feedback_duty_week @所有人  \r\n[img]http://10.246.14.135:8080/static/popo_img/demo.png[/img]')

# @所有人 可直接在msg中添加该文本


if __name__ == '__main__':
    # print send_to_user(u'1426385', r'%feedback_duty_week',atuids=[u'liuyuzhe@corp.netease.com'])
    # json.dumps(['123'])
    #print send_to_user( 1391879, '[emts]'+r'_popo_emoticon_sys_0037_\r\n鼓掌\r\n(AA)'+'[/emts]')
    #send_to_user( 1391879, '[emts]'+r'_popo_emoticon_sys_0037_\r\n鼓掌\r\n(AA)'+'[/emts]')
    print(POPO_USER)



