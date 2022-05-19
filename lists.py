games=["Football","Cricket","Basketball"]
numbers=[1,2,3,4,5,6]
print(games)
print(games[2])
print(games[-2])
# printing after some index
print(games[1:])
# printing from one index to another
print(games[0:2])
games[2]="Volleyball"
print(games[2])
# list functions
luckey_numbers=[4,8,15,16,22,16,16,23,45]
days=["Sunday","Monday","Tuesday","Wednesday"]
print(days)
#extend function
#days.extend(luckey_numbers)
days.append(58)
# adding in the middle of list
days.insert(4,"Thursday")
# days.remove(15)

# deleting list data
# days.clear()
# popping data in list
days.pop()
print(days.index("Sunday"))

print(luckey_numbers.count(16))
luckey_numbers.sort()
days.sort()
print(luckey_numbers)
print(days)
luckey_numbers.reverse()
print(luckey_numbers)
days2=days.copy()
print(days2)
