num_set = []

def check_num():
    while True:
        try:
            num = input("Enter a number or type 'done': ")
            lower_num = num.lower()
            if lower_num == "done":
                return
            isinstance(num, int)
            num = int(num)
            num_set.append(num)
        except:
            print("Invalid input")
       
def check_size():
    if not num_set:
        return  
    else:
        print("Maximum is", max(num_set))
        print("Minimum is", min(num_set))
                               
check_num()
check_size()