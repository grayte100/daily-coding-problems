expenses = [2200, 2350, 2600, 2130, 2190]
#Difference between expense in February and January

diff_expenses = abs(expenses[1] - expenses[0])

#Total expenses in first quarter
total_quarter_expenses = expenses[0] + expenses[1] + expenses[2]

#Adding June expenses of 1980 to the list
expenses.append(1980)

print(expenses)
#remove for April and refund 200

heros = ['spider man','thor','hulk','iron man','captain america']

#Number 2

#1 Find out the length of the list
print("The length of the list is", len(heros))

#2 Add black panther to the end of the list

heros.append('black panther')
print(heros)

#3 Remove black panther then add after hulk

heros.remove('black panther')
heros.insert(3, 'black panther')
print (heros)

#4 Replace thor and hulk with doctor strange in one line
heros[1:3]=['doctor strange']
print(heros)

#5 sort in alphabetical order
print(dir(heros))
print(help(heros.sort))
heros.sort()
print(heros)


#number 3
#print all odd numbers within a pre-specified range

max_odd = int(input("Enter the maximum number"))
all_odd = []
for i in range (max_odd):
    if i%2 != 0:
        all_odd.append(i)
print (all_odd)