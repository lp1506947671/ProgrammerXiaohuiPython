def bucket_sort(array):
    if not array:
        return []
    # 1. 获取最大值和最小值
    max_value = array[0]
    min_value = array[0]
    for i in array:
        if i > max_value:
            max_value = i
        if i < min_value:
            min_value = i

    # 2.初始化桶
    bucket_list = [[] for i in array]
    # 3.遍历原始数组,将每个元素放入桶中
    for i in array:
        num = int((i - min_value) * (len(bucket_list) - 1) / (max_value - min_value))
        bucket_list[num].append(i)
    # 4.对每个桶内部进行排序
    for i in bucket_list:
        i.sort()

    # 5.输出全部元素
    result = [j for i in bucket_list for j in i]
    return result


my_array = list([4.12, 6.421, 0.0023, 3.0, 2.123, 8.122, 4.12, 10.09])
print(bucket_sort(my_array))
