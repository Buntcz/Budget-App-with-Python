class Category:
    def __init__(self,category):
        self.ledger = []
        self.category = category
        self.total = 0
    def deposit(self,amount,description):
        new_deposit = {'amount': amount, 'description':description}
        self.ledger.append(new_deposit)
        self.total += amount
        return True
    def withdraw(self,amount,descrition):
        if self.check_funds(amount):
            self.ledger[0]['amount']=  self.ledger[0]['amount'] - amount
            new_withdraw = {'amount': -amount,'description':descrition}
            self.ledger.append(new_withdraw)
            self.total -= amount
            return True
        else:
            return False
    def get_balance(self):
        return self.ledger[0]['amount']
    
    def transfer(self,amount,place):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {place.category.capitalize()}')
            place.deposit(amount,f'Deposit from {self.category.capitalize()}')
            return True
        else:
            return False
    def check_funds(self,amount):
        if self.ledger[0]['amount'] >= amount:
            return True
        else:
            return False
    def __str__(self):
        name_len = len(self.category)
        stars_side = (30 - name_len) // 2
        str_print = ['*' * stars_side,self.category.capitalize(),'*' * stars_side]
        str_items = []
        for item in self.ledger:
            places = 30
            len_desc = len(item['description'])
            str_amount = len(str(item['amount']))
            spaces = 30 - len_desc - str_amount
            if spaces == 0:
                desc = item['description'][:24]
                amount = str(item['amount'][:8])
                str_items.append([amount,desc])
            else:
                str_items.append([item['description'], " " * spaces,str(item["amount"],)])
        
        total = f"Total: {self.total}"
        final_str = []
        for item in str_items:
            final_str.append("".join(item))
        return "".join(str_print) + "\n" + "\n".join(final_str) + "\n" + total


def create_spend_chart(categories):
    pass

food = Category('food')
food.deposit(1000,'deposit')
clothing = Category('Clothing')
food.transfer(100,clothing)
print(food)
