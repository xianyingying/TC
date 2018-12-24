import json


class readJson(object):
    def load_data(self, fileName):
        try:
            f = open("D:/TC/H5/data/%s" % fileName,
                     encoding='utf-8')  # 设置以utf - 8 解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
            data = json.load(f)
            return data
        except Exception as e:
            print("文件没找到", format(e))
