def int_check():
    while True:
        try:
            int_num = int(input())
            return int_num
        except:
            print('You need to enter an INTEGER number!')


def digit_sum(num2chek):
    sum_num = 0
    for i in range(len(num2chek)):
        if num2chek[i].isdigit():
            temp = int(num2chek[i])
            sum_num = sum_num + temp
    return sum_num

def partition(array, n):
    for i in range(0, len(array), n):
        yield array[i:i + n]