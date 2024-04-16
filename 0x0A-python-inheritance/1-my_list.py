#/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        """
        Method Prints sorted list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

