import os
import sys
import requests


def KG_View(entity):
    url = 'https://api.ownthink.com/kg/knowledge?entity=%s' % entity  # 知识图谱API

    sess = requests.get(url)  # 请求
    text = sess.text  # 获取返回的数据

    response = eval(text)  # 转为字典类型
    knowledge = response['data']

    nodes = []
    for avp in knowledge['avp']:
        if avp[1] == knowledge['entity']:
            continue
        node = {'source': knowledge['entity'], 'target': avp[1], 'type': "resolved", 'rela': avp[0]}
        nodes.append(node)

    for node in nodes:
        node = str(node)
        node = node.replace("'type'", 'type').replace("'source'", 'source').replace("'target'", 'target')
        print(node + ',')


if __name__ == '__main__':
    KG_View('图灵')