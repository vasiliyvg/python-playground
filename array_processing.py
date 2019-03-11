import random
import array


class IntegerArrayProcessor:

    def __init__(self, min_num, max_num):
        self.min = min_num
        self.max = max_num
        self.arr = []

    def generate_array(self):
        print("Generating an array with values from " + str(self.min) + " to " + str(self.max))
        generated = array.array("i", range(self.min, self.max + 1))
        self.arr = list(generated)
        print("Array is generated: " + str(self.arr))
        return self

    def remove_random_number_from_array(self):
        print("Removed random element from array.")
        by_index = random.randint(self.min, self.max - 1)
        print(by_index)
        self.arr.remove(by_index)
        print(self.arr)
        return self

    # Find the missing number in a given integer array
    def find_missing_number_in_array(self):
        arr = self.arr
        n = len(arr)
        for i in range(n):
            if arr[i + 1] != (arr[i] + 1):
                print("Removed element is found: " + str(arr[i] + 1))
                return arr[i] + 1


array_proc = IntegerArrayProcessor(1, 100)

array_proc\
    .generate_array()\
    .remove_random_number_from_array()\
    .find_missing_number_in_array()
