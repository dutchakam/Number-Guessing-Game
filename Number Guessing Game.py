# @Time    : 2021/01/25
# @Author  : alexanderdutchak@gmail.com
# @Software: IDLE

import random

score=10
ndx_cnt=0

n=[18,16,14,12,10,9,8,7,6]
x=(random.randint(0,100))
print("Guess a number from 0 to 100")
print("Hint: The number is less than", (x+(random.randint(10,20))), "and greater than", (x-(random.randint(10,20))))
while True:
    y=input("Choose your number:")
    try:
        val=int(y)
    except ValueError:
        print("That is not an integer! D:<")
        continue
    if val not in range(0,100):
        print("Your guess must be a number from 0 to 100.")
        continue
    if val==x:
        print("Good guess!")
        break
    else:
        score-=1
        if score>=1:
            print("Score=",score)
            print("Try Again")
            print("Hint: The number is less than", (x+(random.randint(1,n[ndx_cnt]))), "and greater than", (x-(random.randint(1,n[ndx_cnt]))))
            ndx_cnt+=1
        else:
            print("Score=",score)
            print("YOU LOSE!")
            break
            

        
