from random import choice


class BillSplitter:

    def __init__(self):
        self.friends_num = None
        self.friends_list = {}
        self.total_bill = 0

    def main(self):
        self.get_fiends_num()
        self.get_friends_list()
        self.get_total_bill()
        if self.check_lucky_game():
            self.calculate_bill(self.friends_num - 1)
            self.start_lucky_game()
        else:
            self.calculate_bill(self.friends_num)
        print(self.friends_list)

    def get_fiends_num(self):
        print('Enter the number of friends joining (including you):')
        while not self.friends_num:
            try:
                self.friends_num = int(input())
            except ValueError:
                print('Wrong value. Please, enter the number: ')
        if self.friends_num <= 0:
            print('No one is joining for the party')
            exit()

    def get_friends_list(self):
        print('Enter the name of every friend (including you), each on a new line:')
        self.friends_list = {input(): 0 for _ in range(self.friends_num)}

    def get_total_bill(self):
        while not self.total_bill:
            try:
                self.total_bill = float(input('Enter the total bill value:\n'))
                if self.friends_num <= 0:
                    raise ValueError
            except ValueError:
                print('Wrong value. Please, enter number > 0')

    def check_lucky_game(self):
        lucky_answer = None
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        while not lucky_answer:
            try:
                lucky_answer = input().lower()
                if (lucky_answer != 'yes') and (lucky_answer != 'no'):
                    lucky_answer = None
                    raise ValueError
            except ValueError:
                print('Wrong value. Please, enter "Yes" or "No": ')
            else:
                if lucky_answer == 'yes':
                    return True
                elif lucky_answer == 'no':
                    print('\nNo one is going to be lucky\n')
                    return False

    def calculate_bill(self, num):
        friend_bill = round(self.total_bill / num, 2)
        self.friends_list = {x: friend_bill for x in self.friends_list.keys()}

    def start_lucky_game(self):
        lucky_friend = choice(list(self.friends_list.keys()))
        print(f'{lucky_friend} is the lucky one!\n')
        self.friends_list[lucky_friend] = 0


my_bill = BillSplitter()
my_bill.main()
