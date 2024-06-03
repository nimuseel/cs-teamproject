class City:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.owner = None

    def Set_owner(self, owner):
        self.owner = owner

    def Get_owner(self):
        return self.owner

    def Get_name(self):
        return self.name

    def Get_price(self):
        return self.price

    def Buy_city(self, player):
        if self.owner is None:
            self.owner = player
            return True
        else:
            return False

    def Sell_city(self):
        if self.owner is not None:
            self.owner = None
            return True
        else:
            return False
