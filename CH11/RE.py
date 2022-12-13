import re

fname = open('regex_sum_1705070.txt')
data = fname.read()

for line in data:
    lst = re.findall('[0-9]+', data)
    
i_lst = [int(i) for i in lst]

print(sum(i_lst))