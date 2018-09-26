from itertools import groupby


def compression(sen):
    '''
    压缩
    :param sen: 要压缩的句子
    :return: 压缩后的句子
    '''
    a,num,c = sen[0],0,''
    sen += '.'
    for i in sen:
        if i == a:
            num += 1
        else:
            c = c + a + str(num) if num != 1 else c + a
            a = i
            num = 1
    return c


def decompression(sen,start=0,end=1,c='',n='1'):
    '''
    解压
    :param sen: 要解压的句子
    :return: 解压后的句子
    '''
    if end > len(sen):
        c = c + c[-1] * (int(n) - 1)
        return c
    if sen[start:end].isalpha():
        c = c + sen[start:end]
        start = end
        end  = end + 1
        return decompression(sen,start,end,c)
    elif sen[start:end].isdigit():
        n = sen[start:end]
        end = end + 1
        return decompression(sen, start, end,c,n)
    else:
        start = end - 1
        c = c + c[-1]*(int(n)-1)
        return decompression(sen, start, end,c)


# def decompression(sen):
#     '''
#     解压
#     :param sen: 要解压的句子
#     :return: 解压后的句子
#     '''
#     c = ''
#     lis = [''.join(list(k)) for g,k in groupby(sen,key=lambda x:x.isalpha())]
#     for i in lis[::2]:
#         index = lis.index(i) +1
#         num = int(lis[index]) -1
#         c = c + i + i[-1]*num
#     return c
print(decompression('a10vv3'))
