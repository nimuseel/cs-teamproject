class City:
    def __init__(self, name):
        self.name = name
        self.price = 100000  # 도시 가격을 10만원으로 고정
        self.owner = None

    def set_owner(self, owner):
        self.owner = owner

    def get_owner(self):
        return self.owner

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

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
            player.money += self.price
            player.cities.remove(self)
            return True
        else:
            return False