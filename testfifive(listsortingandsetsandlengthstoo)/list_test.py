def remove_duplicates(name): #function with one arg
    making_set = set(name)#obtaining length of the set
    making_list = list(name)#obtaining length of the list
    diff = len(making_list)-len(making_set)
                    #subtracting the lengths of the list and set
                    #the length of the list is always higher than that of a set ....if
                    #they are equal then the word is an isogram: name whose letters dont repeat
    if diff == 0 :
        making_list = list(making_set)
        making_list.sort()
        answer = "".join(making_list),diff
        return tuple(answer)
    else:
        making_list = list(making_set)
        making_list.sort()
        answer = "".join(making_list),diff
        return tuple(answer)
