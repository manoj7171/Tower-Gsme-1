import random

p2 = input('Hi Welcome to the Game. Enter your friend\'s name : ')

p1_floor = 0
p2_floor = 0
day = 0

while day <= 100 and p1_floor < 100 and p2_floor < 100:
    if (p2_floor % 9 != 0 or p2_floor == 0) and p2_floor < 100: 
        day += 1
        input(f'\nPress enter to run day {day} for you ')
        disk = random.randint(1, 6)

        if (p1_floor + disk) % 5 != 0:
            p1_floor += disk
            print(f'Disk says {disk}. You have to move floor No. {p1_floor}')
            if p1_floor >= 100: break
            print(f'\tYou are in floor No. {p1_floor}. \n\t{p2} is in floor No. {p2_floor}')       
        else:
            print(f'Disk says {disk}. You have to move floor No. {p1_floor+disk}.\n But there are Snakes in floor No.{p1_floor}. You can\'t move')
            print(f'\tYou are in floor No. {p1_floor}. \n\t{p2} is in floor No. {p2_floor}')       

    elif p2_floor < 100:
        day += 1
        input(f'{p2} is in ladies room. you have 2 chances. \n\nPress enter to take your bonus chance in day {day} ')
        disk = random.randint(1, 6)
        p1_floor += disk
        print(f'Disk says {disk}. You have to move floor No. {p1_floor}')
        if p1_floor >= 100: break
        print(f'\tYou are in floor No. {p1_floor}. \n\t{p2} is in floor No. {p2_floor}')       
                
        day += 1
        input(f'\nPress enter to take your next chance on day {day} ')
        disk = random.randint(1, 6)
        if (p1_floor + disk) % 5 != 0:
            p1_floor += disk
            print(f'Disk says {disk}. You have to move floor No. {p1_floor}')
            if p1_floor >= 100: break
            print(f'\tYou are in floor No. {p1_floor}. \n\t{p2} is in floor No. {p2_floor}')       
        else:
            print(f'Disk says {disk}. You have to move floor No. {p1_floor+disk}.\n But there are Snakes in floor No.{p1_floor}. You Can\'t move')
            print(f'\tYou are in floor No. {p1_floor}. \n\t{p2} is in floor No. {p2_floor}')       

    if (p1_floor % 9 != 0 or p1_floor == 0) and p1_floor < 100: 
        day += 1
        input(f'\nPress enter to run day {day} for {p2} ')
        disk = random.randint(1, 6)

        if (p2_floor + disk) % 5 != 0:
            p2_floor += disk
            print(f'Disk says {disk}. {p2} have to move floor No. {p2_floor}')
            if p2_floor >= 100: break
            print(f'\tYou are in floor No. {p1_floor}. \n\t{p2} is in floor No. {p2_floor}')       
        else:
            print(f'Disk says {disk}. {p2} have to move floor No. {p2_floor+disk}.\n But there are Snakes in floor No.{p2_floor}. {p2} can\'t move')
            print(f'\tYou are in floor No. {p1_floor}. \n\t{p2} is in floor No. {p2_floor}')       

    elif p1_floor < 100:
        day += 1
        input(f'You are in ladies room. {p2} have 2 chances. \n\npress enter to move bonus day, day {day} for {p2} ')
        disk = random.randint(1, 6)
        p2_floor += disk
        print(f'Disk says {disk}. {p2} have to move floor No. {p2_floor}')
        if p2_floor >= 100: break
        print(f'\tYou are in floor No. {p1_floor}. \n\t{p2} is in floor No. {p2_floor}')       
        
        day += 1
        input(f'\npress enter to move day {day} for {p2} ')
        disk = random.randint(1, 6)
        if (p2_floor + disk) % 5 != 0:
            p2_floor += disk
            print(f'Disk says {disk}. {p2} have to move floor No. {p2_floor}')
            if p2_floor >= 100: break
            print(f'\tYou are in floor No. {p1_floor}. \n\t{p2} is in floor No. {p2_floor}')       
        else:
            print(f'Disk says {disk}. {p2} have to move floor No. {p2_floor+disk}.\n But there are Snakes in floor No.{p2_floor}. {p2} can\'t move')
            print(f'\tYou are in floor No. {p1_floor}. \n\t{p2} is in floor No. {p2_floor}')       

if p1_floor > 100:
    print(f'You can not move floor No. {p1_floor}. So you move to floor No. 100 and Win Congratulation')  
elif p1_floor == 100:
    print(f'You move to floor No. 100 and Win Congratulation') 
   
if p2_floor > 100:
    print(f'{p2} can not move floor No. {p2_floor}. So {p2} move to floor No. 100 and Win Congratulation') 
elif p2_floor == 100:
    print(f'{p2} move to floor No. 100 and Win') 

