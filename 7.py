with open('tales.txt', 'r') as document:
    answer = {}
    for line in document:
        line = line.split()
        if not line:  # empty line?
            continue
        answer[line[0]] = line[1:]
print(answer)
print("Dictionary's keys are:")
l=list(answer.keys())
print(l)
print("Select a key: \n")
k=int(input())
print("Maximum value:")
print(max(l[k]))
print("Minimum value:")
print(min(l[k]))
most_common = max(l, key = l[k].count)
print("Most frequent value:")
print(most_common)
