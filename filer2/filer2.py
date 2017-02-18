# coding: utf-8
"""
ファイル操作をするFiler クラス
"""

import csv
import pickle


class Filer(object):

    @staticmethod
    def read_csv(path, option="rb"):
        f = open(path, option)
        try:
            dataReader = csv.reader(f)
            arr = [row for row in dataReader]
            return arr
        finally:
            f.close()

    @staticmethod
    def write_csv(arr, path, option="ab"):
        f = open(path, option)
        try:
            dataWriter = csv.writer(f)
            dataWriter.writerows(arr)
        finally:
            f.close()

    @staticmethod
    def read_tsv(path, option="rb"):
        f = open(path, option)
        try:
            dataReader = csv.reader(f, delimiter="\t")
            arr = [row for row in dataReader]
        finally:
            return arr

    @staticmethod
    def write_tsv(arr, path, option="ab"):
        f = open(path, option)
        try:
            dataWriter = csv.writer(f, delimiter="\t")
            dataWriter.writerows(arr)
        finally:
            f.close()

    @staticmethod
    def read_pkl(path, option="r"):
        f = open(path, option)
        try:
            arr = pickle.load(f)
            return arr
        finally:
            f.close()

    @staticmethod
    def write_pkl(arr, path, option="w"):
        f = open(path, option)
        try:
            pickle.dump(arr, f)
        finally:
            f.close()

    @staticmethod
    def read_txt(path, option='r', LF='\n'):
        f = open(path)
        try:
            lines = f.readlines()
            lines = [row.rstrip(LF) for row in lines]
            return lines
        finally:
            f.close()

    @staticmethod
    def write_txt(arr, path, option="ab", LF='\n'):
        f = open(path, option)
        try:
            for sentence in arr:
                f.writelines(sentence+LF)
        finally:
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