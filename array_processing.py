import random
import array


class IntegerArrayProcessor:

    def __init__(self, min_num, max_num):
        self.min = min_num
        self.max = max_num
        self.arr = []
        self.updated_arr = []

    def generate_array(self):
        print("Generating an array with values from " + str(self.min) + " to " + str(self.max))
        generated = random.sample(range(self.min, self.max + 1), self.max)
        self.arr = list(generated)
        print(str(self.arr))
        return self

    def remove_random_number_from_array(self):
        by_index = random.randint(self.min, self.max - 1)
        self.updated_arr = self.arr.copy()
        print("Removed value " + str(self.updated_arr.pop(by_index)) + ", located by index " + str(by_index))
        print(self.updated_arr)
        return self

    def find_missing_number_in_array(self):
        arr = self.arr
        updated_arr = self.updated_arr
        for i in range(len(arr)):
            if arr[i] != updated_arr[i]:
                print("Removed element is found: " + str(arr[i]))
                return arr[i]

    def duplicate_random_number_in_array(self):
        rand_num = random.randint(self.min, self.max)
        by_index = random.randint(self.min, self.max - 1)
        self.updated_arr = self.arr.copy()
        self.updated_arr.insert(by_index, rand_num)
        print("Duplicated value " + str(rand_num) + ", located by index " + str(by_index))
        print(self.updated_arr)
        return self

# todo finish
    def find_duplicated_numbers_in_array(self):
        updated_arr = self.updated_arr
        seen = {}
        dupes = []
        for x in updated_arr:
            if x not in seen:
                seen[x] = 1
            else:
                if seen[x] == 1:
                    dupes.append(x)
                seen[x] += 1
        print(dupes)
        return dupes


array_proc = IntegerArrayProcessor(1, 100)
array_proc.generate_array()

# Find the missing number in a given integer array
# array_proc\
#     .remove_random_number_from_array()\
#     .find_missing_number_in_array()

# Find the duplicate number on a given integer array
array_proc\
    .duplicate_random_number_in_array()\
    .find_duplicated_numbers_in_array()

