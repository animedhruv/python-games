t=1
while  t==1:
    
    print("\n hello there,","\n we will be playing guess the number!!","\n \n 1. you just need to guess numbers from 1-20 ","\n 2. follow the instructions to get to the number","\n 3. reach the number in 5 chances", "\n 4. enjoy!!","\U0001F609")
    import random                           
    z=0
    
    a=(random.randint(1,20))
    print("\n \n enter any number from 1 to 20")
    b=int(input())
    for u in range (5):
        if b>a:
                 print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nyour guess",b," is wrong ,guess a lower number","\U0001F910",)
                
        elif b<a:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nyour guess",b," is wrong ,guess a higher number","\U0001F910",)
               
        else:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n"+" \U0001f600","won  the game in",u+1,"chances") 
                z=1
                break
                
       
        if u<4: 
            print(4-u,"chances left\n")
            b=int(input("re enter input  "))
    if z==0:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\nU0001F923 You lost the game") 
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
