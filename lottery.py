import random
print('Welcome to lottery show \nPlease choose 4 numbers from 1 to 99 and we will show the winning numbers')
firstnum = int(input('Your first number: '))
secnum = int (input('Your second number: '))
thirdnum = int(input('Your third number: '))
finalnum = int(input('Your final number: '))
playernum = [firstnum, secnum, thirdnum, finalnum]
print('\nAnd now here is our winning numbers:')
while 1:
    winnum1 = random.randrange(1,99)
    winnum2 = random.randrange(1,99)
    winnum3 = random.randrange(1,99)
    winnum4 = random.randrange(1,99) 
    if winnum1 != winnum2 != winnum3 != winnum4:
        print(f'first winning number is: {winnum1}')
        print(f'Second winning number is: {winnum2}')
        print(f'Third winning number is: {winnum3}')
        print(f'Final winning number is: {winnum4}')
        break
winlist = [winnum1, winnum2, winnum3, winnum4]
a = 0
for i in playernum:
    for j in winlist:
        if i == j:
            a+=1
if a == 4:
    print('Congratulation, you win a really big prize but since we are poor so you know, no prize at all')
elif a == 3:
    print('Wow, you win a second prize with 3 numbers, but this is for fun so no prize')
elif a == 2:
    print("You win a prize with 2 match numbers, but we are broke so don't ask for a prize please")
elif a == 1:
    print("Hmmmmm........ well, you know, it can consider as a win with 1 number")
else:
    print("Well, I highly recommend you should buy another lottery ticket, maybe you will win next time")