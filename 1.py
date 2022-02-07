rows, cols = (3,3)
arr = [[0 for i in range(cols)] for j in range(rows)]
arr[0][0]= 0
arr[0][1]= 0
arr[0][2]= 0
arr[1][0]= 0
arr[1][1]= 0
arr[1][2]= 0
arr[2][0]= 0
arr[2][1]= 0
arr[2][2]= 0
for row in arr:
    print(row)
f1=False
f2=False
f3=False
steps=0
small=9
medium=9
big=9
total=27
for i in range(100):
    a=0
    b=0
    print("The size of the ring will be selected randomly!")
    print("1 for small,2 for medium,3 for big")
    import random
    s=(random.randrange(1,4))
    if(s==1):
        print("selected size: small")
        steps+=1
        print("The blocks will be selected randomly!")
        import random
        x=random.randrange(0,3)
        y=random.randrange(0,3)
        if(arr[x][y]==0): # Block is empty!
            arr[x][y]=1 # 1 for small
            f1=True
            small-=1
            total-=1
            steps+=1
        else: # block is not empty
            if(arr[x][y]==1):
                small-=1
                steps+=1
                total-=1
            else:
                print("Can't put different sizes in the same block!")
                import random
                a=(random.randrange(2,4))
                if(a==2):
                    print("selected size: medium")
                    steps+=1
                    print("The blocks will be selected randomly!")
                    medium-=1
                    f2=True
                    total-=1
                    steps+=1
                else:
                    print("selected size: big")
                    steps+=1
                    print("The blocks will be selected randomly!")
                    import random
                    x=random.randrange(0,3)
                    y=random.randrange(0,3)
                    arr[x][y]=3 # 3 for big
                    small-=1
                    f3=True
                    total-=1
                    steps+=1
    elif(s==2):
        print("selected size: medium")
        steps+=1
        print("The blocks will be selected randomly!")
        import random
        x=random.randrange(0,3)
        y=random.randrange(0,3)
        if(arr[x][y]==0): # Block is empty!
            arr[x][y]=2 # 2 for medium
            medium-=1
            f2=True
            total-=1
            steps+=1
            print(arr[x][y])
            print(x,y)
        else: #Block is not empty
            print("Can't put different sizes in the same block!")
            import random
            a=random.randrange(1,4,2)
            if(a==1):
                print("selected size: small")
                steps+=1
                print("The blocks will be selected randomly!")
                import random
                x=random.randrange(0,3)
                y=random.randrange(0,3)
                arr[x][y]=1 # 1 for small
                f1=True
                small-=1
                total-=1
                steps+=1
            else:
                print("selected size: big")
                steps+=1
                print("The blocks will be selected randomly!")
                import random
                x=random.randrange(0,3)
                y=random.randrange(0,3)
                arr[x][y]=3 # 3 for big
                small-=1
                f3=True
                total-=1
                steps+=1
    elif(s==3):
        print("selected size: big")
        steps+=1
        print("The blocks will be selected randomly!")
        import random
        x=random.randrange(0,3)
        y=random.randrange(0,3)
        if(arr[x][y]==0): # Block is empty!
            arr[x][y]=3 # 3 for big
            small-=1
            f3=True
            total-=1
            steps+=1
        else: #Block is not empty
            print("Can't put different sizes in the same block!")
            import random
            a=random.randrange(1,3)
        if(a==1):
            print("selected size: small")
            steps+=1
            print("The blocks will be selected randomly!")
            import random
            x=random.randrange(0,3)
            y=random.randrange(0,3)
            arr[x][y]=1 # 1 for small
            f1=True
            small-=1
            total-=1
            steps+=1
        else:
            print("selected size: medium")
            steps+=1
            print("The blocks will be selected randomly!")
            import random
            x=random.randrange(0,3)
            y=random.randrange(0,3)
            arr[x][y]=2 # 2 for medium
            medium-=1
            f2=True
            total-=1
            steps+=1
        j=0
        if(arr[0][j]==1 or arr[1][j+1]==1 or arr[2][j+2]==1):
            break
            print("break")
            print(steps)
            print(total)
        elif(arr[j][0]==1 or arr[j+1][1]==1 or arr[j+2][2]==1):
            break
            print("break")
            print(steps)
            print(total)
        elif(arr[0][0]==arr[1][1]==arr[2][2]):
            print("break")
            print(steps)
            print(total)
        elif(arr[0][2]==arr[1][1]==arr[2][0]):
            break
            print("break")
            print(steps)
            print(total)
        elif(arr[0][j]==2 or arr[1][j+1]==2 or arr[2][j+2]==2):
            break
            print("break")
            print(steps)
            print(total)
        elif(arr[j][0]==2 or arr[j+1][1]==2 or arr[j+2][2]==2):
            break
            print("break")
            print(steps)
            print(total)
        elif(arr[0][j]==3 or arr[1][j+1]==3 or arr[2][j+2]==3):
            break
            print("break")
            print(steps)
            print(total)
        elif(arr[j][0]==3 or arr[j+1][1]==3 or arr[j+2][2]==3):
            break
            print("break")
            print(steps)
            print(total)
