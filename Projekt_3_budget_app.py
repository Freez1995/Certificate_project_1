class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = list()

    def deposit(self, deposit_amount, deposit_description=""):
        # deposit money to ledger ( append to list )
        self.depo = dict()
        self.deposit_amount = deposit_amount
        self.deposit_description = deposit_description
        self.depo["amount"] = self.deposit_amount
        self.depo["description"] = self.deposit_description
        self.ledger.append(self.depo)

    def withdraw(self, withdraw_amount, withdraw_description=""):
        # taking money from ledger - (import as negative numbers)
        self.withd = dict()
        self.withdraw_amount = withdraw_amount * -1
        self.withdraw_description = withdraw_description
        if self.check_funds(withdraw_amount) is True:
            try:
                if self.get_balance() > 0:
                    self.withdrawing = self.get_balance() + self.withdraw_amount
                    self.withd["amount"] = self.withdraw_amount
                    self.withd["description"] = self.withdraw_description
                    self.ledger.append(self.withd)
                    return True
            except:
                if self.get_balance() < 0:
                    return False
        else:
            return False

    def get_balance(self):
        self.balance = 0
        for x in range(len((self.ledger))):
            self.balance += self.ledger[x]["amount"]
        return self.balance

    def transfer(self, transfer_amount, destination):
        self.transfer_amount = transfer_amount  # food.transfer_amount = 50
        self.destination = destination  # food.transfer = clothing
        if self.check_funds(transfer_amount) is True:
            self.withdraw(transfer_amount, "Transfer to " + destination.category)
            destination.deposit(transfer_amount, "Transfer from " + self.category)
            return True
        else:
            return False

    def check_funds(self, amount):
        self.amount = amount
        if self.amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        self.stars = "*"
        self.header_align = self.stars * int(((30 - len(self.__dict__["category"])) / 2))
        self.header = self.header_align + self.__dict__["category"] + self.header_align
        self.line = ""
        self.shift = ""
        for x in range(len(self.ledger)):
            self.line += "{:<23}".format(self.ledger[x]["description"][0:23]) + "{:>7.2f}".format(
                float(self.ledger[x]["amount"])) + "\n"
        return self.header + "\n" + self.line + "Total:" + " " + "{:.2f}".format(self.get_balance())


def create_spend_chart(category):

    iznosi = dict()
    for x in category:
        x.total = 0
        for y in range(len((x.ledger))):
            if x.ledger[y]["amount"] < 0:
                x.total += x.ledger[y]["amount"] * -1
                iznosi[x.__dict__["category"]] = x.total
    total = 0
    num = list()
    name = list()
    for key, value in iznosi.items():       # Getting total value of withdraws
        total += value
    for key, value in iznosi.items():       # divide each value to get percentage
        iznosi[key] = value / total
    for key, value in iznosi.items():       # rounding down (svakako na manjeg)percentage to  10
        if int(str(value).split(".")[1][1]) <= 9:
            num.append(int(str(value).split(".")[1][0]) * 10)
        name.append(key)

    result = "Percentage spent by category\n"
    count = 100

    while count >= 0:
        circles = ""
        for x in num:
            if count > x:
                circles += "   "
            if count <= x:
                circles += "o" + "  "
        if count == 0:
            result += str(count).rjust(3) + "|" + " " + circles + "\n"
            break
        else:
            result += str(count).rjust(3) + "|" + " " + circles + "\n"
        count -= 10

    result += "    " + "---" * len(iznosi) + "-" + "\n"
    sorted_names = sorted(name, key=len)
    name_count = len(sorted_names[-1])
    name_count_start = 0

    while name_count_start <= name_count:
        final_name = ""
        for x in name:
            if len(x) <= name_count_start:
                final_name += "   "
            elif len(x) > name_count_start:
                final_name += x[name_count_start] + "  "
        if name_count_start == name_count-1:
            result += "     " + final_name
            break
        else:
            result += "     " + final_name + "\n"
        name_count_start += 1

    return result


food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(create_spend_chart([business, food, entertainment]))





