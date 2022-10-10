# exercise 3 #

List = [76, 92.3, 'hello', True, 4, 76]

List.append("apple")        
List.append(76)              
List.insert(3, "cat")        
List.insert(0, 99)         

print(List.index("hello"))   
print(List.count(76))       
del List[1]            
List.pop(List.index(True)) 

print (List)