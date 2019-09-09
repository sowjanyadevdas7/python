# Adds List Element as value of List. 
List = ['Mathematics', 'chemistry', 1997, 2000] 
List.append(20544) 
print(List) 

#######
List = ['Mathematics', 'chemistry', 1997, 2000] 
# Insert at index 2 value 10087 
List.insert(2,10087)      
print(List)

#####

List1 = [1, 2, 3] 
List2 = [2, 3, 4, 5] 
  
# Add List2 to List1 
List1.extend(List2)         
print(List1) 
  
#Add List1 to List2 now 
List2.extend(List1)  
print(List2)



####
List = [1, 2, 3, 4, 5, 7] 
print(sum(List))

####
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1] 
print(List.count(1)) 

#####
List = [1, 2, 3, 1, 2, 1, 2, 3, 2, 1, 4] 
print(len(List))

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 

#Reverse flag is set True 
List.sort(reverse=True) 

#List.sort().reverse(), reverses the sorted list 
print(List)

List = [2.3, 4.445, 3, 5.33, 1.054, 2.5] 
print(List.pop(1)) 





