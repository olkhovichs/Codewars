def find_outlier(integers):
    even = [x for x in integers if x % 2 == 0]
    if len(even) == 1:
        return even[0]
    else:
        odd = [x for x in integers if x % 2 != 0]
        return odd[0]
    
     
    