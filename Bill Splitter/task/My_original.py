import random

friends_num = int(input('Enter the number of friends joining (including you):\n'))
if friends_num > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    friends_list = {input(): 0 for _ in range(friends_num)}
    total_bill = int(input('Enter the total bill value:\n'))

    lucky_game = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n').lower()
    if lucky_game == 'yes':
        lucky_friend = random.choice(list(friends_list.keys()))
        print(f'{lucky_friend} is the lucky one!\n')
        friend_bill = round(total_bill / (friends_num - 1), 2)
        friends_list = {x: friend_bill for x in friends_list.keys()}
        friends_list[lucky_friend] = 0
        print(friends_list)

    else:
        print('\nNo one is going to be lucky\n')
        friend_bill = round(total_bill / friends_num, 2)
        friends_list = {x: friend_bill for x in friends_list.keys()}
        print(friends_list)
else:
    print('No one is joining for the party')

