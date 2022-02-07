for i in range(100):
    points1=0
    points2=0
    import random
    a=random.randrange(0,9)
    b=random.randrange(0,9)
    def letter(x,y):
        return chr(random.randint(ord(x), ord(y)))
    c=letter('a','h')
    d=letter('a','h')
    rook=(a,c)
    print("Rooks dimensions are:")
    print(rook)
    bishop=(b,d)
    print("Bishop dimensions are:")
    print(bishop)
    while(rook!=bishop):
        print("Player1 is moving the rook")
        print("Player2 is moving the bishop")

        print("How do you want to move your rook?")
        answer=input("H for horizontal,V for vertically\n")
        if (answer=="H"):
            import random
            a2=random.randrange(0,9)
            rook=(a2,c)
            if (rook==bishop):
                print("You win player1!")
                points1+=1
            else:
                print("Your new position is:")
                print(rook)
        else:
             c2=chr(random.randint(ord('a'), ord('h')))
             rook=(a,c2)
             if (rook==bishop):
                print("You win player1!")
                points1+=1
             else:
                print("Your new position is:")
                print(rook)
        print("How do you want to move your bishop?\n")
        print("Top-right,Top-left,Bottom-left,Bottom-right")
        answer2=input("TR for top-right,TL for top-left,BL for bottom-left,BR for bottom-right")
        if (answer2=="TR"):
            d2=chr(random.randint(ord('a'), ord('h')))
            import random
            b2=random.randrange(0,9)
            bishop=(b2,d2)
            if(bishop==rook):
                    print("You win player2!")
                    points2+=1
            else:
                    print("Your new dimensions are:")
                    print(bishop)
        elif(answer2=="TL"):
            d2=chr(random.randint(ord('a'), ord('h')))
            import random
            b2=random.randrange(0,9)
            bishop=(b2,d2)
            if(bishop==rook):
                    print("You win player2!")
                    points2+=1
            else:
                    print("Your new dimensions are:")
                    print(bishop)
        elif (answer2=="BL"):
            d2=chr(random.randint(ord('a'), ord('h')))
            import random
            b2=random.randrange(0,9)
            bishop=(b2,d2)
            if(bishop==rook):
                    print("You win player2!")
                    points2+=1
            else:
                    print("Your new dimensions are:")
                    print(bishop)
        elif (answer2=="BR"):
            d2=chr(random.randint(ord('a'), ord('h')))
            import random
            b2=random.randrange(0,9)
            bishop=(b2,d2)
            if(bishop==rook):
                    print("You win player2!")
                    points2+=1
            else:
                    print("Your new dimensions are:")
                    print(bishop)
    print(points1)
    print(points2)



# 7x7
for i in range(100):
    points1=0
    points2=0
    import random
    a=random.randrange(0,8)
    b=random.randrange(0,8)
    def letter(x,y):
        return chr(random.randint(ord(x), ord(y)))
    c=letter('a','g')
    d=letter('a','g')
    rook=(a,c)
    print("Rooks dimensions are:")
    print(rook)
    bishop=(b,d)
    print("Bishop dimensions are:")
    print(bishop)
    while(rook!=bishop):
        print("Player1 is moving the rook")
        print("Player2 is moving the bishop")

        print("How do you want to move your rook?")
        answer=input("H for horizontal,V for vertically\n")
        if (answer=="H"):
            import random
            a2=random.randrange(0,8)
            rook=(a2,c)
            if (rook==bishop):
                print("You win player1!")
                points1+=1
            else:
                print("Your new position is:")
                print(rook)
        else:
             c2=chr(random.randint(ord('a'), ord('h')))
             rook=(a,c2)
             if (rook==bishop):
                print("You win player1!")
                points1+=1
             else:
                print("Your new position is:")
                print(rook)
        print("How do you want to move your bishop?\n")
        print("Top-right,Top-left,Bottom-left,Bottom-right")
        answer2=input("TR for top-right,TL for top-left,BL for bottom-left,BR for bottom-right")
        if (answer2=="TR"):
            d2=chr(random.randint(ord('a'), ord('g')))
            import random
            b2=random.randrange(0,8)
            bishop=(b2,d2)
            if(bishop==rook):
                    print("You win player2!")
                    points2+=1
            else:
                    print("Your new dimensions are:")
                    print(bishop)
        elif(answer2=="TL"):
            d2=chr(random.randint(ord('a'), ord('g')))
            import random
            b2=random.randrange(0,8)
            bishop=(b2,d2)
            if(bishop==rook):
                    print("You win player2!")
                    points2+=1
            else:
                    print("Your new dimensions are:")
                    print(bishop)
        elif (answer2=="BL"):
            d2=chr(random.randint(ord('a'), ord('g')))
            import random
            b2=random.randrange(0,8)
            bishop=(b2,d2)
            if(bishop==rook):
                    print("You win player2!")
                    points2+=1
            else:
                    print("Your new dimensions are:")
                    print(bishop)
        elif (answer2=="BR"):
            d2=chr(random.randint(ord('a'), ord('g')))
            import random
            b2=random.randrange(0,8)
            bishop=(b2,d2)
            if(bishop==rook):
                    print("You win player2!")
                    points2+=1
            else:
                    print("Your new dimensions are:")
                    print(bishop)
    print(points1)
    print(points2)

    # 7x8
    for i in range(100):
        points1=0
        points2=0
        import random
        a=random.randrange(0,8)
        b=random.randrange(0,8)
        def letter(x,y):
            return chr(random.randint(ord(x), ord(y)))
        c=letter('a','h')
        d=letter('a','h')
        rook=(a,c)
        print("Rooks dimensions are:")
        print(rook)
        bishop=(b,d)
        print("Bishop dimensions are:")
        print(bishop)
        while(rook!=bishop):
            print("Player1 is moving the rook")
            print("Player2 is moving the bishop")

            print("How do you want to move your rook?")
            answer=input("H for horizontal,V for vertically\n")
            if (answer=="H"):
                import random
                a2=random.randrange(0,8)
                rook=(a2,c)
                if (rook==bishop):
                    print("You win player1!")
                    points1+=1
                else:
                    print("Your new position is:")
                    print(rook)
            else:
                 c2=chr(random.randint(ord('a'), ord('h')))
                 rook=(a,c2)
                 if (rook==bishop):
                    print("You win player1!")
                    points1+=1
                 else:
                    print("Your new position is:")
                    print(rook)
            print("How do you want to move your bishop?\n")
            print("Top-right,Top-left,Bottom-left,Bottom-right")
            answer2=input("TR for top-right,TL for top-left,BL for bottom-left,BR for bottom-right")
            if (answer2=="TR"):
                d2=chr(random.randint(ord('a'), ord('h')))
                import random
                b2=random.randrange(0,8)
                bishop=(b2,d2)
                if(bishop==rook):
                        print("You win player2!")
                        points2+=1
                else:
                        print("Your new dimensions are:")
                        print(bishop)
            elif(answer2=="TL"):
                d2=chr(random.randint(ord('a'), ord('h')))
                import random
                b2=random.randrange(0,8)
                bishop=(b2,d2)
                if(bishop==rook):
                        print("You win player2!")
                        points2+=1
                else:
                        print("Your new dimensions are:")
                        print(bishop)
            elif (answer2=="BL"):
                d2=chr(random.randint(ord('a'), ord('h')))
                import random
                b2=random.randrange(0,8)
                bishop=(b2,d2)
                if(bishop==rook):
                        print("You win player2!")
                        points2+=1
                else:
                        print("Your new dimensions are:")
                        print(bishop)
            elif (answer2=="BR"):
                d2=chr(random.randint(ord('a'), ord('h')))
                import random
                b2=random.randrange(0,8)
                bishop=(b2,d2)
                if(bishop==rook):
                        print("You win player2!")
                        points2+=1
                else:
                        print("Your new dimensions are:")
                        print(bishop)
        print(points1)
        print(points2)
