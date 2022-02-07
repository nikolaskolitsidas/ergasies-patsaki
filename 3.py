f=open("tales.txt","r")
tmp=f.read()
y=''.join([i for i in tmp if not i.isdigit()])
x=y.split()
print(x)
pairs=0
words=len(x) #words=139010
a=[]
final=[]
i=1
while i<139010:
    if(len(x[i-1])+len(x[i]))==20:
        pairs+=1
        a.append(x[i-1])
        a.append(x[i])
    else:
        final.append(x[i-1])
        final.append(x[i])
    i+=1
print(pairs)
print(len(a))
print("the maximum length of a remaining string in the list is 7")
rest1=0
rest2=0
rest3=0
rest4=0
rest5=0
rest6=0
rest7=0
for i in range(len(final)):
    if len(final[i])==1:
        rest1+=1
    elif len(final[i])==2:
        rest2+=1
    elif len(final[i])==3:
        rest3+=1
    elif len(final[i])==4:
        rest4+=1
    elif len(final[i])==5:
        rest5+=1
    elif len(final[i])==6:
        rest6+=1
    else:
        rest7+=1
print("Words with one letter are:" + str(rest1))
print("Words with two letters are:" + str(rest2))
print("Words with three letters are:" + str(rest3))
print("Words with four letters are:" + str(rest4))
print("Words with five letters are:" + str(rest5))
print("Words with six letters are:" + str(rest6))
print("Words with seven letters are:" + str(rest7))
