class Money:
    def __init__(self,rupees,dollars,pounds):
        self.rupees = rupees
        self.dollars = dollars
        self.pounds = pounds

    def __str__(self):
        return f"rupees: {self.rupees} , dollars: {self.dollars} , pounds: {self.pounds}"

    def __add__(self,other):
        trupees = self.rupees + other.rupees
        tdollars = self.dollars + other.dollars
        tpounds = self.pounds + other.pounds
        return Money(trupees,tdollars,tpounds)

jmoney = Money(10,20,30)
mmoney = Money(10,20,30)
tmoney = jmoney + mmoney
print(tmoney)
