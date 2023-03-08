# List: append | insert | pop | del | clear | extend | +
test_list = ['Testing', 10, 30, True, 'Python']

test_list.append('PyCharm')
print(test_list)

test_list.insert(2,'New Item')
print(test_list)

test_list.pop()
print(test_list)

del test_list[1]
print(test_list)

test_list_b = ['Batman', 10, 'Don Draper']

test_list.extend(test_list_b)
print(test_list)