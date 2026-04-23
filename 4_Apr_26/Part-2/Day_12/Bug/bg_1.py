# def speed(distance, time):
#     return distance / time
    
# print(speed(5, 300))

def speed(distance, time):
    return distance / time
    
print(speed(300, 5))

# note: the order of the arguments matters. 
# In the first case, we were trying to divide 5 by 300, 
# which gives us a very small number (0.016666666666666666). 
# In the second case, we are dividing 300 by 5, 
# which gives us a much larger number (60).