t=1
while  t==1:
    
    print("\n hello there,","\n we will be playing guess the number!!","\n \n 1. you just need to guess numbers from 1-20 ","\n 2. follow the instructions to get to the number","\n 3. reach the number before 5 chances", "\n 4. enjoy!!","\U0001F609")
    import random                           
    z=0
    
    a=(random.randint(1,20))
    print("\n \n enter any number from 1 to 20")
    b=int(input())
    for u in range (5):
        if b>a:
                print("\nguess lower","\U0001F910")
                
        elif b<a:
                print("\nguess higher","\U0001F910")
               
        else:
                print("\U0001f600","won  the game") 
                z=1
                break
                
        print(5-u,"chances left")
        b=int(input("re enter input  "))
    if z==0:
        print("\U0001F923","You lost the game") 
        print("The number was",a)
    j=input("do you want to replay  Y/N :")
    if j=="Y" or j=="y":
        print("hey would you like to set a custom range of guess from 1 to ?? :")
        p=input(" Y/N :")
        if p=="Y" or p=="y":
            print (" \n sorry, service not available")
        else:
            print("\n Okay, Thanks for not showing interest")
        t=1
    else:
        print("good bye , see you soon","\U0001F609")
        t=0