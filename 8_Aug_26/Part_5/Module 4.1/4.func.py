def simple_calculator(a,b):
    # print(f"Addition: {a+b}")
    # print(f"Subtraction: {a-b}")
    # print(f"Multiplication: {a*b}")
    # print(f"Division: {a/b}")
    return a+b, a-b, a*b, a/b


result = simple_calculator(10, 10)
add_result, sub_result, mul_result, div_result = result


print(add_result)
print(sub_result)
print(mul_result)
print(div_result)