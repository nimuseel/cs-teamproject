class City:
    def __init__(self, name):
        self.name = name
        self.price = 100000  # 도시 가격을 10만원으로 고정
        self.toll = 50000  # 통행료를 5만원으로 설정
        self.owner = None

    def set_owner(self, owner):
        self.owner = owner

    def get_owner(self):
        return self.owner

    def get_name(self):
        return self.name

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
                # 플레이어가 통행료를 지불할 돈이 없는 경우
                player['money'] = 0  # 남은 돈을 모두 지불
                self.owner['money'] += player['money']
                return True
        return False

    def is_buyable(self):
        return self.name not in ["출발지점", "무인도"]