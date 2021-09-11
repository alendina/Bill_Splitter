import random


class BillSplitter:
    def __init__(self):
        self.friends = {}
        self.friends_qty = None
        self.total_bill = None

    def invite_friends(self):
        print("Enter the number of friends joining (including you):")
        self.friends_qty = int(input())
        if self.friends_qty <= 0:
            print("No one is joining for the party")
            exit()
        else:
            print("Enter the name of every friend (including you), each on a new line:")
            while len(self.friends) < self.friends_qty:
                friend = input()
                self.friends[friend] = 0
            # print(self.friends)

    def split_bill(self, total_bill):
        split_equally = round(total_bill / self.friends_qty, 2)
        for friend in self.friends:
            self.friends[friend] = split_equally
        print(self.friends)

    def lucky_one(self):
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        lucky_answer = input()
        if lucky_answer == "Yes":
            lucky = random.choice(list(self.friends.keys()))
            print("{} is the lucky one!".format(lucky))
            split_bill = round(self.total_bill / (self.friends_qty - 1), 2)
            for friend in self.friends:
                if friend == lucky:
                    self.friends[friend] = 0
                else:
                    self.friends[friend] = split_bill
            print(self.friends)
        else:
            print("No one is going to be lucky")
            self.split_bill(self.total_bill)

    def main(self):
        self.invite_friends()
        try:
            print("Enter the total bill value:")
            self.total_bill = int(input())
        except (TypeError, ValueError):
            print("Bill should be an integer value greater than 0!")
        else:
            self.lucky_one()


my_bill = BillSplitter()
my_bill.main()