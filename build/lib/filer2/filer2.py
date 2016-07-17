# coding: utf-8
"""
ファイル操作をするFiler クラス
"""

import csv
import pickle


class Filer(object):

    @staticmethod
    def readcsv(path, option="rb"):
        f = open(path, option)
        dataReader = csv.reader(f)
        arr = [row for row in dataReader]
        return arr

    @staticmethod
    def writecsv(arr, path, option="ab"):
        f = open(path, option)
        dataWriter = csv.writer(f)
        dataWriter.writerows(arr)
        f.close()

    @staticmethod
    def readtsv(path, option="rb"):
        f = open(path, option)
        dataReader = csv.reader(f, delimiter="\t")
        arr = [row for row in dataReader]
        return arr

    @staticmethod
    def writetsv(arr, path, option="ab"):
        f = open(path, option)
        dataWriter = csv.writer(f, delimiter="\t")
        dataWriter.writerows(arr)
        f.close()

    @staticmethod
    def readdump(path, option="r"):
        f = open(path, option)
        arr = pickle.load(f)
        f.close()
        return arr

    @staticmethod
    def writedump(arr, path, option="w"):
        f = open(path, option)
        pickle.dump(arr, f)
        f.close()

    @staticmethod
    def readtxt(path, option='r', LF='\n'):
        f = open(path)
        lines = f.readlines()
        f.close()
        lines = [row.rstrip(LF) for row in lines]
        return lines

    @staticmethod
    def writetxt(arr, path, option="ab", LF='\n'):
        f = open(path, option)
        for sentence in arr:
            f.writelines(sentence+LF)
        f.close()

    @staticmethod
    def conv_encoding(data):
        lookup = ('utf_8', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213',
                  'shift_jis', 'shift_jis_2004', 'shift_jisx0213',
                  'iso2022jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_3',
                  'iso2022_jp_ext', 'latin_1', 'ascii')
        encode = None
        for encoding in lookup:
            try:
                data = data.decode(encoding)
                encode = encoding
                break
            except:
                pass
        if isinstance(data, unicode):
            return data, encode
        else:
            raise LookupError