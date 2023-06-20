#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : relax
# @time   : 06/19/23 17:13:20
# @File   : paths.py
import os
import json

def getDirectoryTree(folder):
    """
    遍历本地目录返回字典树
    :param folder:文件目录
    :return:目录的字典
    """
    dirtree = {'children': []}
    if os.path.isfile(folder):
        return {'text': os.path.basename(folder), 'url': os.path.abspath(folder)}
    else:
        dirtree['text'] = os.path.basename(folder)
        for item in os.listdir(folder):
            dirtree['state'] = 'closed'
            dirtree['children'].append(getDirectoryTree(os.path.join(folder, item)))
        return dirtree


def getDirectoryTreeWithJson(folder):
    """
    把字典树转换为字符串并返回
    :param folder: 文件夹
    :return:字符串
    """
    return json.dumps(getDirectoryTree(folder))


if __name__ == '__main__':
    fpaths = []
    jjj = getDirectoryTreeWithJson("../rb3d")
    with open("sss.json", 'w') as w:
        w.write(jjj)
    print(jjj)
