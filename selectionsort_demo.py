"""选择排序"""

# [1,5,3,4,2]


def selectionsort(li=[]):
    for i in range(len(li)):
        min_index = i  # 定义一个变量指向最小数,记录其下标,这里是初始化操作
        for j in range(i, len(li)):
            if li[j] < li[min_index]:
                min_index = j  # 如果后面的数字比这个变量指向的数字还要小,就改变变量的指向,所以该变量始终指向最小数字
        li[i], li[min_index] = li[min_index], li[i]  # 每个大循环结束之后,都将最小数提前
    return li


if __name__ == '__main__':
    result = selectionsort(li=[1,5,3,4,2])
    print(result)

