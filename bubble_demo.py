def bubble_sort(li):
    """
    冒泡排序:
    每次都是相邻两个元素之间进行比较,较大者置后,一次大循环过后会将最大者放到最后,同时参与比较的数字减一
    :param li:
    :return:
    """
    for i in range(len(li)-1):  # 外层循环,控制循环次数
        for j in range(0, len(li)-1-i):  # 内层循环,负责控制元素下标
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
    return li


def bubble_sub(li=[]):
    """
    排序思想:
    第一次循环以第一个数为基准,依次与后面的所有数进行比较,如果后面的数比第一个小,就交换两者的位置,即:将较小数提前,
    一次循环过后,数组中的最小数处于第一个位置
    第二次循环会将数组中第二小的数放在第二个位置
    以此类推
    """
    for i in range(len(li)-1):  # 从第一个到倒数第二个数
        for j in range(i+1, len(li)):  # 从第二个数到最后一个数
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
    return li

if __name__ == '__main__':
    new_li = bubble_sort(li=[9,5,6,3,8,2,7,1,66,43])
    print(new_li)


