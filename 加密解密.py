import numpy as np
import pypinyin


K = np.array([[1,0,1],[3,2,7],[1,9,2]])
dic = {chr(i+96):i for i in range(1,27)}
dic['0'] = 0
decrypt_dic = {str(v):k for k,v in dic.items()}
a = 'acti fsfdon'
b = ''

def product_array(sentence):
    '''

    :param sentence: 接受一个字符串
    :return: 返回矩阵
    '''
    num = len(sentence) // 3 if len(sentence) % 3 == 0 else len(sentence) // 3 + 1
    sentence = sentence.zfill(num * 3)
    sentence_list = [dic[i] for i in sentence]
    np_sentence_array = np.array(sentence_list).reshape(num, 3)
    return np_sentence_array

def encryption(np_array,K):
    '''

    :param np_array: 接受未加密时的矩阵
    :param K: 规则
    :return: 返回加密后的矩阵
    '''
    info_np_array = np.mat(np_array)
    encryption_array = info_np_array * K
    return encryption_array.flatten()

def dec(D1,D):
    '''
    解方程
    :param D1: 公式D1
    :param D: 公式D
    :return: 解密后的字符串
    '''
    num = np.linalg.det(D1) / np.linalg.det(D)
    num = str(str(num).replace('-','').split('.')[0])
    global b
    b += decrypt_dic[num]

def decrypt(np_array,K):
    '''
    解线性方程
    :param np_array:方程式
    :param K:规则
    :return:解密后的内容
    '''
    D = K.transpose()
    for i in np_array:
        for j in range(len(K)):
            k = np.array(K)
            k[j] = i
            D1 = k.transpose()
            dec(D1, D)
            del k
    return b.replace('0','')

def sent(sen):
    sen = sen.lower()
    sen = sen.replace(' ', '')
    sen = pypinyin.lazy_pinyin(sen)
    sentence = ''
    for i in sen:
        for j in i:
            if j.isalpha():
                sentence += j
    return sentence

def product_decrypt_array(string):
    string = string.replace(' ',',')
    array = string.split(',')
    array = filter(lambda x: x and x.strip(), array)
    array = [(i) for i in array]
    np_encryption_array = np.array([array])
    n = np_encryption_array.shape[-1]
    num = n // 3 if n % 3 == 0 else n // 3
    np_encryption_array = np_encryption_array.reshape(num, 3)
    return np_encryption_array

def main():
    i = int(input('1加密,2解密'))
    # i = 2
    # 提取字母
    if i == 1:
        sen = input('要加密的内容')
        sentence = sent(sen)
        # 创建加密矩阵
        np_array = product_array(sentence)
        # 加密并返回加密后的矩阵
        encryption_array = encryption(np_array,K)
        print(encryption_array)
    else:
        encryption_array = input('要解密的数组')
        # encryption_array = '30,186,62,68,156,142'
        # 将一维数组变成多维数组
        np_encryption_array = product_decrypt_array(encryption_array)
        # 解密
        result = decrypt(np_encryption_array,K)
        print(result)

if __name__ == '__main__':
    main()
