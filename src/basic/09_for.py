# For
text = 'Python'

for count in text:
    print(count)

test_list = ['Testing', 10, 30, True, 'Python']

for count in test_list:
    print(count)

test_enumerate = enumerate(test_list, start=1)

for count in test_enumerate:
    print(count)