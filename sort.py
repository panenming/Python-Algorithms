'''
冒泡排序 时间复杂度 O(n^2)
'''
def short_bubble_sort(a_list):
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                a_list[i],a_list[i + 1] = a_list[i + 1],a_list[i]
        pass_num = pass_num - 1

'''
选择排序 时间复杂度O(n^2)
'''
def selection_sort(a_list):
    for fill_slot in range(len(a_list) - 1,0,-1):
        pos_of_max = 0
        for location in range(1,fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        a_list[fill_slot],a_list[pos_of_max] = a_list[pos_of_max],a_list[fill_slot]

a_list = [54,26,93,17,77,31,44,55,20]
selection_sort(a_list)
print(a_list)

'''
插入排序 时间复杂度O(n^2)
'''
def insertion_sort(a_list):
    for index in range(1,len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

def insertion_sort_binarysearch(a_list):
    for index in range(1,len(a_list)):
        current_value = a_list[index]
        position = index
        low = 0
        high = index - 1
        while low <= high:
            mid = (low + high) / 2
            if a_list[mid] > current_value:
                high = mid - 1
            else:
                low = mid + 1
        #数据移动（假设前边都是排序好的数组）
        while position > low:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value

a_list = [54,26,93,15,77,31,44,55,20]
insertion_sort(a_list)
print(a_list)
insertion_sort(a_list)
print(a_list)

'''
合并排序 时间复杂度 O(nlogn)
'''
def merge_sort(a_list):
    print("Spliting ",a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = 0;j = 0;k = 0;
        #合并
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1
        #其中一个数组数据结束，另一个还有数据
        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1
        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
    print("merging ",a_list)

a_list = [54,26,93,17,77,31,44,55,20]
merge_sort(a_list)
print(a_list)

'''
快速排序
首先，它每次都是选择第一个元素都为主元，这个回合就是要确定主元的位置；然后，有两个指针，
一个leftmark指向主元的后面一个位置，另一个rightmark指向要排序的数组最后一个元素；
接着，两个指针分别向中间移动，leftmark遇到比主元大的元素停止，rightmark遇到比主元小的元素停止，
如果此时leftmark<rightmark，也就是说中间还有未处理(未确定与主元大小关系)的元素，那么就交换leftmark和rightmark位置上的元素，
然后重复刚才的移动操作，直到rightmark<leftmark；最后，停止移动时候rightmark就是主元要放置的位置，
因为它停在一个比主元小的元素的位置上，之后交换主元和rightmark指向的元素即可。完了之后，递归地对主元左右两边的数组进行排序即可。
'''
def quick_sort(a_list):
    quick_sort_helper(a_list,0,len(a_list) - 1)
def quick_sort_helper(a_list,first,last):
    if first < last:
        split_point = partition(a_list,first,last)
        quick_sort_helper(a_list,first,split_point - 1)
        quick_sort_helper(a_list,split_point + 1,last)
def partition(a_list,first,last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark],a_list[right_mark] = a_list[right_mark],a_list[left_mark]
    a_list[first],a_list[right_mark]= a_list[right_mark],a_list[first]
    return right_mark

a_list = [54,26,93,17,77,31,44,55,20]
quick_sort(a_list)
print(a_list)

'''
希尔排序 时间复杂度[O(n),O(n^2)]
'''
def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list,start_position,sublist_count)
        print("After increments of size ",sublist_count," the list is ",a_list)
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list,start,gap):
    for i in range(start + gap,len(a_list),gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value
a_list = [54,26,93,17,77,31,44,55,20,88]
print("shell sort-----")
shell_sort(a_list)
print(a_list)
'''
堆排序
'''
'''
计数排序
'''
'''
基数排序
'''
'''
桶排序
'''
if __name__ == '__main__':
    a_list = [20,40,30,90,50,80,70,60,110,100]
    short_bubble_sort(a_list)
    print(a_list)