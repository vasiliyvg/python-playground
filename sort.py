class Sort:

    def __init__(self, arr):
        self.arr = arr

    # Algorithm:
    # https://2.bp.blogspot.com/-uB94SH5WlZ0/U-zFpfRb6EI/AAAAAAAAByE/SyemBWPWRBU/s1600/Bubble%2BSort%2BFlowchart%2Bin%2BJava.jpg
    def bubble(self):
        arr = self.arr
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
        return arr


sort = Sort([9, 7, 3, 6, 2])
print(sort.bubble())







