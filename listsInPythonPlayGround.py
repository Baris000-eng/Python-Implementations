teams= ["Fenerbahçe","Galatasaray","Beşiktaş","Fenerbahçe","Trabzonspor"]
team_points=[77,60,81,72]
print(teams.count("Fenerbahçe"))#Counts how many times "Fenerbahçe" appears in the list called "teams".
print(teams)#Prints the whole list
teams.sort()#For sorting a list in alphabetical order/ascending order.
print(teams)
print(team_points.reverse())#To reverse a list
another_teams=teams.copy()#To copy the contents of one list to another list
print(another_teams)
print(teams[0])#1st element
print(teams[1])#2nd element
print(teams[2])#3rd element
print(teams[3])#4th element
print(teams[-1])#Last element
print(teams[-4])#First element
print(teams[-3])#2nd element
print(teams[-2])#3rd element
print(teams[1:])#Prints the elements starting at 2nd element 
print(teams[:3])#Prints the elements to the end of the last element(not including last one)
print(teams[1:3])#Prints starting at 2nd element ending at last one(not including last one)
print(team_points)
teams.extend(team_points)#The usage of the extend function to add two lists and obtain one list in which two lists are merged.
print(teams)
teams.remove(teams[0])#The usage of remove function(The purpose of remove() function is to remove an element from the list)
print(teams)
print(teams.index("Galatasaray"))#Obtaining the index of the element called "Galatasaray"
teams.clear()#Deletes all elements in the list
print(teams)

