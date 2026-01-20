def average(mylist):
    result = sum(mylist) / len(mylist)
    return result


average_Value = average([10, 20, 30, 40, 50])
print(f"the average value is: {average_Value}")