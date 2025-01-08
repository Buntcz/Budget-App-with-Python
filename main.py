class Category:
    def __init__(self,category):
        self.ledger = []
        self.category = category
        self.total = 0
    def deposit(self,amount,description=""):
        new_deposit = {'amount': amount, 'description':description}
        self.ledger.append(new_deposit)
        self.total += amount
        return True
    def withdraw(self,amount,descrition=""):
        if self.check_funds(amount):
            new_withdraw = {'amount': -amount,'description':descrition}

            self.ledger.append(new_withdraw)
            self.total -= amount
            return True
        else:
            return False
    def get_balance(self):
        return self.total
    
    def transfer(self,amount,place):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {place.category.capitalize()}')
            place.deposit(amount,f'Transfer from {self.category.capitalize()}')
            return True
        else:
            return False
    def check_funds(self,amount):
        if float(self.ledger[0]['amount']) >= amount:
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
            amount = float(item["amount"])
            str_amount = f"{amount:.2f}"
            spaces = places - len_desc - len(str_amount)
            if spaces <= 0:
                desc = item['description']
                amount = float(item['amount'])
                str_amount = f"{amount:.2f}"
                spacing = 7 - len(str_amount)
                str_items.append([desc[:23]," "*spacing,str_amount])
            else:
                amount = float(item["amount"])
                str_amount = f"{amount:.2f}"
                str_items.append([item['description'], " " * spaces,str_amount])
        
        total = f"Total: {self.total}"
        final_str = []
        for item in str_items:
            final_str.append("".join(item))
        return "".join(str_print) + "\n" + "\n".join(final_str) + "\n" + total


class Category:
    def __init__(self,category):
        self.ledger = []
        self.category = category
        self.total = 0
    def deposit(self,amount,description=""):
        new_deposit = {'amount': amount, 'description':description}
        self.ledger.append(new_deposit)
        self.total += amount
        return True
    def withdraw(self,amount,descrition=""):
        if self.check_funds(amount):
            new_withdraw = {'amount': -amount,'description':descrition}

            self.ledger.append(new_withdraw)
            self.total -= amount
            return True
        else:
            return False
    def get_balance(self):
        return self.total
    
    def transfer(self,amount,place):
        if self.check_funds(amount):
            self.withdraw(amount,f'Transfer to {place.category.capitalize()}')
            place.deposit(amount,f'Transfer from {self.category.capitalize()}')
            return True
        else:
            return False
    def check_funds(self,amount):
        if float(self.ledger[0]['amount']) >= amount:
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
            amount = float(item["amount"])
            str_amount = f"{amount:.2f}"
            spaces = places - len_desc - len(str_amount)
            if spaces <= 0:
                desc = item['description']
                amount = float(item['amount'])
                str_amount = f"{amount:.2f}"
                spacing = 7 - len(str_amount)
                str_items.append([desc[:23]," "*spacing,str_amount])
            else:
                amount = float(item["amount"])
                str_amount = f"{amount:.2f}"
                str_items.append([item['description'], " " * spaces,str_amount])
        
        total = f"Total: {self.total}"
        final_str = []
        for item in str_items:
            final_str.append("".join(item))
        return "".join(str_print) + "\n" + "\n".join(final_str) + "\n" + total


def create_spend_chart(categories):
    total_spent = 0
    total_spent = round(total_spent,2)
    final_list = []
    dashes = "---"
    c_names = []
    dashes_list = ["\n","    -"]
    spent_by_category = []
    for i in range(100,-10,-10):
        if i == 100:
            final_list.append(f"{i}| ")
        elif i == 0:
            final_list.append(f"  {i}| ")
        else:
            final_list.append(f" {i}| ")
        
    for category in categories:
        total_spent_category = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total_spent_category += round(abs(item["amount"]),2)
                total_spent += round(abs(item["amount"]),2)
        spent_by_category.append(round(total_spent_category,2))
        dashes_list.append(dashes)
        c_names.append(category.category)
    percent_table = []
    for i in range(len(categories)):
        percent_spent = (100 * round((spent_by_category[i] / total_spent),2))
        percent_table.append(percent_spent)
    for i in range(len(categories)):
        for j in range(100,-10,-10):
            if j >= percent_table[i]:
                final_list[j // 10] = f"{final_list[j//10]}o  "
    max_length = max(len(name) for name in c_names)
    rows = ["     "]
    for i in range(max_length):
        row = "     "
        for name in c_names:
            row +=(name[i] if i < len(name) else " ") + "  "
        rows.append(row)
    head_string = "Percentage spent by category\n"
    
    return head_string + "\n".join(final_list)  + "".join(dashes_list) + "\n".join(rows)
    
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(25.20,'new shirt')
auto = Category('Auto')
food.transfer(100,auto)
auto.withdraw(40.12,"Fixes")
categories = [food,clothing,auto]
print(create_spend_chart(categories))