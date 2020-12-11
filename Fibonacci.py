## FIBONACCI SERIES

# O(2^n) time | O(n) space
def get_num_fibonacci(pos):
    if pos == 2:
        return 1
    elif pos == 1:
        return 0
    else:
        return get_num_fibonacci(pos-1) + get_num_fibonacci(pos-2)

# O(n) time | O(1) space
def get_fibonacci(pos):
    last_values = [0, 1]
    counter = 3
    while counter <= pos:
        curr = last_values[0] + last_values[1]
        last_values[0] = last_values[1]
        last_values[1] = curr
        counter +=1
    if pos >= 1:
        return last_values[1]
    last_values[0] 
  


print(get_num_fibonacci(10))
print(get_fibonacci(10))

