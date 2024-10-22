# def multiply_by2(li):
#     new_li = []
#     for item in li:
#         new_li.append(item*2)
#     return(new_li)

# print(multiply_by2([1,2,3]))

#==================================map=========================
# map, filter, zip, reduce


my_list = [1,2,3]

def multiply_by2(item):
    return item * 2

print(list(map(multiply_by2, my_list)))
print(my_list)