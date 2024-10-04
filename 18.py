single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
for i in single_digits:
    print(i)
    squares = [i*i for i in single_digits]
print (squares)