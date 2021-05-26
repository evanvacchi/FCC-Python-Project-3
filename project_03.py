class Category:

    def __init__(self, name): #the below are instance variables for the other methods
        self.name = name
        self.ledger = list()
        self.balance = 0
        self.withdraw_amount = 0
        #print(name, 'constructed')

    def deposit(self, amount, description = ''):
        self.balance = self.balance + amount
        #print('amount', self.amount)
        self.description = description
        #print('description', description)
        d = {'amount': amount, 'description': self.description}
        self.ledger.append(d)
        # print(self.ledger)

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount) != True:
            return False
        self.description = description
        withdraw_amount = amount * -1
        d = {'amount': withdraw_amount, 'description': self.description}
        self.ledger.append(d)
        self.balance = self.balance + withdraw_amount
        self.withdraw_amount = withdraw_amount + self.withdraw_amount
        return True

    def get_balance(self):
        return(self.balance)

    def transfer(self, amount, category):
        if self.check_funds(amount) == False:
            return(False)
        else:
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            #print(True)
            return(True)

    def check_funds(self, amount):
        #returns False if amount is greater than total(balance), else true
        if amount > self.balance:
            #print(False)
            return(False)
        else:
            return(True)

    def __str__(self):
        string = self.name
        new_string = string.center(30, '*')
        newlst = list()
        total = 0
        for item in self.ledger:
            #print(item['description'] + str(item['amount'])) # this fixed the dictionary problem from before
            amt = item['amount']
            total = amt + total
            amt = str(amt)
            if '.' not in amt:
                amt = str(amt) + '.00'
            else:
                amt = str(format(float(amt), '.2f'))
            des = item['description']
            if len(des) > 23:
                des = des[0:23]
            newlst.append(des + amt.rjust(30-len(des)))
            #print(newlst)
        total = str(format(float(total), '.2f')) #two decimal places
        # if len(total) - total.index('.') == 1:
        #     total = total + '000'
        if len(newlst) == 1:
            return (new_string + '\n' + newlst[0] + '\n' + 'Total: ' + total)
        if len(newlst) == 2:
            return (new_string + '\n' + newlst[0] + '\n' + newlst[1] + '\n' + 'Total: ' + total)
        if len(newlst) == 3:
            return (new_string + '\n' + newlst[0] + '\n' + newlst[1] + '\n' + newlst[2] + '\n' + 'Total: ' + total)
        if len(newlst) == 4:
            return (new_string + '\n' + newlst[0] + '\n' + newlst[1] + '\n' + newlst[2] + '\n' + newlst[3] + '\n' + 'Total: ' + total)

def create_spend_chart(categories):
    ans = []
    title = 'Percentage spent by category'
    ans.append(title)
    #print(title)
    y_axis = ['100|', ' 90|', ' 80|', ' 70|', ' 60|', ' 50|', ' 40|', ' 30|', ' 20|', ' 10|', '  0|']
    percentagelist = []
    numlist = []
    bars = []
    # for i in categories[0].masterledger:
    #     totalwithdraws = abs(i) + totalwithdraws # total spent over all categories
    totalwithdraws = 0
    for i in categories:
        totalwithdraws = i.withdraw_amount + totalwithdraws
    #print('total withdraws', totalwithdraws)
    for i in categories:
        totalpercategory = int((abs(i.withdraw_amount) / abs(totalwithdraws))* 100)
        #print(totalpercategory)
        if totalpercategory < 10:
            totalpercategory = 0
        totalpercategory = str(totalpercategory)
        try:
            if totalpercategory[1] != '0':
                totalpercategory = int(totalpercategory[0] + '0')
        except:
            pass
        percentagelist.append(totalpercategory)
        #print(totalpercategory)
    #print(percentagelist)
    for i in percentagelist:
        num = round(int(i) / 10)
        numlist.append(num) # number of circles for bar chart for each category
    #print(numlist)
    #print(numlist)

    strlen = 3

    for i in range(100, -10, -10): # making the graph y-axis & bars
        if len(str(i)) < strlen:
            diff = strlen - len(str(i))
            line = diff * ' ' + str(i) + '| '
        else:
            line = str(i) + '| '
        #print(line)
        for item in percentagelist:
            percent = int(item)
            if i <= percent:
                line = line + 'o' + '  '
            else:
                line = line + ' '*3
        #print(line)
        ans.append(line)


    # bars.append(y_axis) # work from lines here to line 161 (after graph append) new graph print out
    # lenbars = 11
    # for h in numlist:
    #     h = 'o' + 'o' * h #added additional 'o' for zero percentage?
    #     bars.append(h)
    #     # if len(h) > lenbars:
    #     #     lenbars = len(h) # sets maximum length of the bar / doesn't matter with y axis anymore
    # #print(bars)
    # for n, i in enumerate(bars):
    #     if len(i) < lenbars:
    #         filler = lenbars - len(i)
    #         i = ' ' * filler + i # sets all bars equal length so I can do the zip function
    #         bars[n] = i
    #     #print(i)
    #     #print(numlist)
    # #print(bars)
    #
    # # for i in y_axis:
    # #     print(i, end ='')
    # #     for j in numlist:
    # #         if str(j) in i:
    # #             print('o')
    #
    # for b, x, y, z in zip(*bars):
    #     graph = b + x.rjust(2) + y.rjust(3) + z.rjust(3) + '  '
    #     ans.append(graph)
    #     print(b, x, y.rjust(2), z.rjust(2))
    #     print(graph)

    if len(percentagelist) == 1:
        dash = '    ----'
        ans.append(dash)
        #print(dash)
    if len(percentagelist) == 2:
        dash = '    -------'
        ans.append(dash)
        #print(dash)
    if len(percentagelist) == 3:
        dash = '    ----------'
        ans.append(dash)
        #print(dash)
    else:
        dash = '    -------------'
        ans.append(dash)
        #print(dash)

    maxlength = 0
    verticalprint = []
    for i in categories:
        words = i.name
        verticalprint.append(words)
        if len(words) > maxlength:
            maxlength = len(words)
    for n, j in enumerate(verticalprint): #finding and replacing list items to make them the same length
        if len(j) < maxlength:
            addspace = maxlength - len(j)
            j = j + ' ' * addspace
            #print(j, len(j))
            verticalprint[n] = j
    #print(verticalprint)

    for x, y, z in zip(*verticalprint): #vertically prints list on x - axis
        x_axis = x.rjust(6) + y.rjust(3) + z.rjust(3) + '  '
        ans.append(x_axis)
        #print(x.rjust(6), y.rjust(2), z.rjust(2))
        #print(x_axis)

    finalsolution = ''
    for i in ans:
        finalsolution = finalsolution + '\n' + i
    #print(finalsolution.lstrip())
    finalsolution = finalsolution.lstrip()
    print(finalsolution)
    return(finalsolution)


gaming = Category('Business')
gaming.deposit(900, 'deposit')
gaming.withdraw(10.99, 'withdraw for travel')

concerts = Category('Food')
concerts.deposit(900, 'deposit')
concerts.withdraw(105.55, 'withdraw')
concerts.withdraw(20, 'hotdogs')

# gaming.transfer(24, concerts)

heroin = Category('Entertainment')
heroin.deposit(900, 'deposit')
heroin.withdraw(33.40, 'withdraw')

testlst = [gaming, concerts, heroin]
create_spend_chart(testlst)
# print(gaming.ledger)
print(gaming)
print(concerts)
print(heroin)
