import os
from PIL import Image
from PIL.ExifTags import TAGS
import tkinter as tk
from tkinter import filedialog
# from lan import TAGS_CN

s = {}


def init():
    s = {}


def bianli(path):
    files = os.listdir(path)  # 得到文件夹下的所有文件名称

    for file in files:  # 遍历文件夹
        file_path = (path + '/' + file)
        if not os.path.isdir(file_path):  # 判断是否是文件夹，不是文件夹才打开

            try:
                img = Image.open(file_path)
                try:
                    exif = img._getexif()
                    if exif.get(37386, 0):
                        focal_length = int(
                            exif[37386][0] / exif[37386][1])  # 焦距
                        if s.get(focal_length, 0):
                            s[focal_length] = s[focal_length] + 1
                        else:
                            s[focal_length] = 1
                except:
                    # print('The image has no exif')
                    pass
            except IOError:
                # print('file not an image file')
                pass

        else:
            bianli(file_path)


if __name__ == '__main__':

    # root = "."

    root = tk.Tk()
    root.withdraw()

    search_path = filedialog.askdirectory()
    if search_path == '':
        print("no folder!")
        os.system('pause')
        os._exit(0)

    init()
    bianli(search_path)
    # print(s)
    if s:
        list = sorted(s.items(), key=lambda s: s[1], reverse=True)  # 排序成列表
        slen = len(s)
        for i in range(slen):
            print("%-3d" % (i + 1), '焦距：' + "%-3s" %
                  str(list[i][0]) + 'mm', '', str(list[i][1]) + '张')
    else:
        print("请将此文件放在需要统计的文件目录！\n")
    print("\n")
    os.system('pause')


# 打印exif字典标签
# print(TAGS)
