
# Online Python - IDE, Editor, Compiler, Interpreter
n = int(input("Enter the initial number:"))
names = []
scores = []

for m in range(n):
    name = input("Enter the name of the student")
    score = int(input("Enter the score of the student"))
    names.append(name)
    scores.append(score)
records = []
for k in range(len(names)):
    records.append([names[name],scores[score]])
    
print(names)
print(scores)