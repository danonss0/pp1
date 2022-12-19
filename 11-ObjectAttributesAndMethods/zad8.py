class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)

    def print_in_col2(array):
        for i in range(len(array)):
            print(array[i], end='')
            if len(array)-i == 1:
                continue
            else:
                print(",", end='')


my_array = [4, 1, 8, 7, 2]
Arrays.print_in_col2(my_array)
