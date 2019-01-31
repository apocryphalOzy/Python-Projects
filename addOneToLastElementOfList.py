''' 1. Takes a list of numbers
    2. If the number is less than 0 or it is a double digits number then returns None
    3. If it is an empty list then returns None
    4. Else joins the numbers in the list together to create a larger number, 
        for example, if a list consists of [1,2,3] then the larger number will beceome
        123. Next, add one to that new number, so 123 becomes 124.
    5. Finally turns that new number back to a list so 124 becomes [1,2,4] and returns
        the new list. 
'''

def up_array(arr):

    str_ = ''

    if len(arr) == 0:
        return None

    for num in arr:
        if num < 0 or num > 9:
            return None
        else:
            str_ += str(num)

    total = str(int(str_) + 1)
    arr = []

    for number in total:
        arr.append(int(number))

    return arr