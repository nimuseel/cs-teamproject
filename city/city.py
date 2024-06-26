class City:
    def __init__(self, name, index, price, toll):
        self.name = name
        self.index = index
        self.price = price
        self.toll = toll
        self.owner = None

    def set_owner(self, owner):
        self.owner = owner

    def get_owner(self):
        return self.owner

    def get_name(self):
        return self.name

    def get_index(self):
        return self.index

    def get_price(self):
        return self.price

    def get_toll(self):
        return self.toll

    def buy_city(self, player):
        if self.owner is None and player['money'] >= self.price:
            self.owner = player
            player['money'] -= self.price
            player['cities'].append(self)
            return True
        else:
            return False

    def sell_city(self, player):
        if self.owner == player:
            self.owner = None
            player['money'] += self.price
            player['cities'].remove(self)
            return True
        else:
            return False

    def pay_toll(self, player):
        if self.owner is not None and self.owner != player:
            if player['money'] >= self.toll:
                player['money'] -= self.toll
                self.owner['money'] += self.toll
                return True
            else:
                player['money'] = 0
                self.owner['money'] += player['money']
                return True
        return False

    def is_buyable(self):
        return self.name not in ["출발지점", "무인도"]
