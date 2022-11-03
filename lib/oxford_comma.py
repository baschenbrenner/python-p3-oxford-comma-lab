import ipdb

def oxford_comma(items):
    counter = 1
    new_list=[]
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return items[0] + " and " + items[1]
    for item in items:
        
        if (counter == len(items)):
            new_list.append("and " + item)
        else:
            new_list.append(item+",")
            counter +=1
    
    

    return " ".join(new_list)
