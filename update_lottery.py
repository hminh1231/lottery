import random

class Lottery:
    def menu(self):
        '''This function help print out menu'''
        print('Welcome to lottery show \nPlease choose 4 numbers from 1 to 99 and we will show the winning numbers')
        
    def user_numbers(self):
        '''This function take user input numbers
        _ Raise error if it out of range or not a number
        _ Print out user chosen numbers'''
        user_nums = []
        print("Enter 4 unique numbers between 1 and 99.")
        while len(user_nums) < 4:
            try:
                num = int(input(f'Enter number {len(user_nums)+1}: '))
                if num < 1 or num > 99:
                    print('Number out of range. Try again.')
                elif num in user_nums:
                    print('Number already entered. Enter a different number.')
                else:
                    user_nums.append(num)
            except ValueError:
                print('Invalid input. Please enter a number.')
        print(f'Your first number is: {user_nums[0]}')
        print(f'Your second number is {user_nums[1]}')
        print(f'Your third number is {user_nums[2]}')
        print(f'Your fourth number is {user_nums[3]}')
        return user_nums
    
    def winning_numbers(self):
        '''This function random 4 winning numbers and print it out'''
        winning_nums = random.sample(range(1, 100), 4)
        print(f'The first winning number is {winning_nums[0]}')
        print(f'The second winning number is {winning_nums[1]}')
        print(f'The third winning number is {winning_nums[2]}')
        print(f'The fourth winning number is {winning_nums[3]}')
        return winning_nums
    
    def compare(self,arr1,arr2):
        '''This function will take result of user numbers and winning numbers and compare it
        _ Print out the result'''
        total = 0
        for i in range(4):
            if arr1[i] == arr2[i]:
                total += 1
        if total == 4:
            print('Congratulation, you win a really big prize but since we are poor so you know, no prize at all')
        elif total == 3:
            print('Wow, you win a second prize with 3 numbers, but this is for fun so no prize')
        elif total == 2:
            print("You win a prize with 2 match numbers, but we are broke so don't ask for a prize please")
        elif total == 1:
            print("Hmmmmm........ well, you know, it can consider as a win with 1 number")
        else:
            print("Well, I highly recommend you should buy another lottery ticket, maybe you will win next time")
            
    def display(self):
        '''Display menu, call other functions and ask if user want to continue playing or not'''
        while True:
            self.menu()
            print('')
            user = self.user_numbers()
            print('')
            winning = self.winning_numbers()
            print('')
            self.compare(user,winning)
            print('')
            continue_playing = input('Do you want to continue (Y/N): ')
            if continue_playing == 'N':
                break
            elif continue_playing != 'Y':
                print('Invalid input, please try again')
                
play = Lottery()
play.display()