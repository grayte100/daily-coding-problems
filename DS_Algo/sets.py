given_list2 = [1,3,4,1,3]
new_set2 = set()
for x in given_list2:
    new_set2.add(x)
new_list = [x for x in new_set2]
print (sum(new_list))


n = int(input("Enter "))
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
avg_marks = round((sum(scores)/3.00),2)
print(avg_marks)