# aaa = open('allData.csv')

# for a in aaa:
#     a = a.rstrip()
#     a_line = 0
#     for line in a:
#         a_line = a_line+1
#     if a.__contains__('AAA'):
#         print(a)
# print(f"There are {a_line} AAA batery orders here.")

fname = input('Enter the file name: ')
orders = open(fname)
count = 0 
for order in orders:
    order = order.rstrip()
    if order.__contains__('AAA'):
        count = count +1
        print(order)
print(f"There are {count} AAA batery orders in the {fname} file. ")    