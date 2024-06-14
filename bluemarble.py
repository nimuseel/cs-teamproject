import tkinter as tk
from tkinter import messagebox, Toplevel, Listbox, END
import random
from utils import Utils
from player.player import Player
from city.city import City

# 보드 설정 (11x11)
board = [
    [{'name': '출발지점', 'index': 1, 'price': 0, 'toll': 0},
     {'name': '타이베이', 'index': 2, 'price': 300000, 'toll': 300000},
     {'name': '황금열쇠', 'index': 3, 'price': 0, 'toll': 0},
     {'name': '베이징', 'index': 4, 'price': 350000, 'toll': 350000},
     {'name': '마닐라', 'index': 5, 'price': 250000, 'toll': 250000},
     {'name': '제주도', 'index': 6, 'price': 200000, 'toll': 200000},
     {'name': '싱가포르', 'index': 7, 'price': 400000, 'toll': 40000},
     {'name': '황금열쇠', 'index': 8, 'price': 0, 'toll': 0},
     {'name': '카이로', 'index': 9, 'price': 300000, 'toll': 300000},
     {'name': '이스탄불', 'index': 10, 'price': 350000, 'toll': 350000},
     {'name': '무인도', 'index': 11, 'price': 0, 'toll': 0}],
    [{'name': '서울', 'index': 40, 'price': 1000000, 'toll': 100000},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '아테네', 'index': 12, 'price': 300000, 'toll': 300000}],
    [{'name': '사회복지기금', 'index': 39, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '황금열쇠', 'index': 13, 'price': 0, 'toll': 0}],
    [{'name': '뉴욕', 'index': 38, 'price': 800000, 'toll': 80000},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '코펜하겐', 'index': 14, 'price': 300000, 'toll': 200000}],
    [{'name': '런던', 'index': 37, 'price': 700000, 'toll': 200000},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '스톡홀름', 'index': 15, 'price': 500000, 'toll': 200000}],
    [{'name': '황금열쇠', 'index': 36, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '여객기', 'index': 16, 'price': 600000, 'toll': 200000}],
    [{'name': '로마', 'index': 35, 'price': 550000, 'toll': 100000},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '취리히', 'index': 17, 'price': 350000, 'toll': 150000}],
    [{'name': '파리', 'index': 34, 'price': 750000, 'toll': 350000},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '황금열쇠', 'index': 18, 'price': 0, 'toll': 0}],
    [{'name': '콜롬비아호', 'index': 33, 'price': 650000, 'toll': 65000},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '베를린', 'index': 19, 'price': 600000, 'toll': 60000}],
    [{'name': '도쿄', 'index': 32, 'price': 700000, 'toll': 70000},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '', 'index': 0, 'price': 0, 'toll': 0},
     {'name': '몬트리올', 'index': 20, 'price': 400000, 'toll': 40000}],
    [{'name': '우주여행', 'index': 31, 'price': 0, 'toll': 0},
     {'name': '마드리드', 'index': 30, 'price': 450000, 'toll': 45000},
     {'name': '퀸 엘리자호', 'index': 29, 'price': 500000, 'toll': 50000},
     {'name': '리스본', 'index': 28, 'price': 350000, 'toll': 35000},
     {'name': '하와이', 'index': 27, 'price': 300000, 'toll': 30000},
     {'name': '부산', 'index': 26, 'price': 250000, 'toll': 25000},
     {'name': '시드니', 'index': 25, 'price': 400000, 'toll': 40000},
     {'name': '상파울로', 'index': 24, 'price': 450000, 'toll': 45000},
     {'name': '황금열쇠', 'index': 23, 'price': 0, 'toll': 0},
     {'name': '부에노스', 'index': 22, 'price': 350000, 'toll': 35000},
     {'name': '사회복지기금', 'index': 21, 'price': 0, 'toll': 0}]
]

# 색상 설정
colors = {
    "top": "lightblue",
    "right": "lightgreen",
    "bottom": "lightcoral",
    "left": "lightgoldenrodyellow",
    "corner": "gray",
    "default": "white"
}

class BuruMarbleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("부루마블 보드 게임")

        self.canvas = tk.Canvas(root, width=880, height=880)
        self.canvas.pack()

        self.cell_width = 80
        self.cell_height = 80

        player = Player(root, self.start_game)

        self.players = player.players
        self.community_chest_fund = 0

        self.play_order = 1  # 플레이 순서
        self.dice_result = 0  # 주사위 결과
        self.show_result = False  # 주사위 결과 출력 여부

        self.city = []  # 도시 정보를 저장할 리스트
        self.turn_count = 0
        self.max_turn = player.max_turn

        self.is_double = False
        self.space_travel_player = None  # 우주여행을 실행한 플레이어를 추적하기 위한 변수

        player.create_player_selection()

    def start_game(self, players, max_turn):
        self.players = players
        self.max_turn = max_turn
        self.create_board()
        self.show_city_info_popup()

    def create_board(self):
        for i in range(11):
            for j in range(11):
                x1 = j * self.cell_width
                y1 = i * self.cell_height
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_height

                if (i == 0 and j == 0) or (i == 0 and j == 10) or (i == 10 and j == 0) or (i == 10 and j == 10):
                    color = colors["corner"]
                    outline_color = "black"
                elif i == 0:
                    color = colors["top"]
                    outline_color = "black"
                elif j == 10:
                    color = colors["right"]
                    outline_color = "black"
                elif i == 10:
                    color = colors["bottom"]
                    outline_color = "black"
                elif j == 0:
                    color = colors["left"]
                    outline_color = "black"
                else:
                    color = colors["default"]
                    outline_color = color

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=outline_color)
                
                text = board[i][j].get("name")
                if text:
                    self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, font=("Helvetica", 12), fill="black")

        # 플레이어 이름 및 보유 머니 출력
        self.show_player_info()
        self.show_turn_info()

        # 스페이스바 이벤트 바인딩
        self.canvas.create_text(440, 700, text=f"{self.players[self.play_order -1]['name']} 님의 차례, 스페이스 바를 눌러 주사위를 굴리세요", font=("Helvetica", 16), tags="dice_roll_info", fill="black")
        
        self.root.bind('<space>', self.roll_dice)

    def show_city_info_popup(self):
        self.city_info_popup = Toplevel(self.root)
        self.city_info_popup.title("도시 정보")
        self.city_info_popup.geometry("300x1100")

        self.city_info_text = tk.Text(self.city_info_popup, wrap="word", width=35, height=70)
        self.city_info_text.pack(pady=10)

        self.update_city_info_popup()

    def update_city_info_popup(self):
        self.city_info_text.config(state="normal")
        self.city_info_text.delete("1.0", END)

        flat_board = Utils.flatted_board(board)
        for item in flat_board:
            if item["name"] not in ["출발지점", "황금열쇠", "무인도", "사회복지기금", "우주여행"]:
                city = self.get_city(item["name"])
                owner = city.get_owner()
                owner_name = owner["name"] if owner else "없음"
                city_info = f"도시: {item['name']}\n구매 가격: {item['price']}원\n통행료: {item['toll']}원\n소유주: {owner_name}\n\n"
                self.city_info_text.insert(END, city_info)

        self.city_info_text.config(state="disabled")
        
    def roll_dice(self, event):

        self.turn_count += 1 # 턴수 증가
        self.show_turn_info()
        if self.space_travel_player == self.players[self.play_order - 1]:
            self.show_city_selection(self.players[self.play_order - 1])
        else:
            self.__roll_dice_logic(event)

        if self.turn_count == self.max_turn:
            self.end_game2()

    def __roll_dice_logic(self, event):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        self.result = dice1 + dice2
        self.is_double = dice1 == dice2
        
        current_player = self.players[self.play_order - 1]
        
        result_text = f"주사위 결과: {dice1}, {dice2} (합: {self.result})"
        double_text = f"더블! 주사위를 한 번 더 굴리세요"
        render_text = result_text + double_text if self.is_double else result_text

        if current_player.get("currentPositionName") == "무인도":
            self.canvas.delete("uninhabited_island_info")

            if current_player["uninhabitedIslandCount"] == 3:
                self.canvas.create_text(440, 700, text=render_text, font=("Helvetica", 16), tags="dice_result", fill="black")
                current_player["uninhabitedIslandCount"] = 0
                self.update_player_info()
                self.__update_play_order()
            else:
                if self.is_double:
                    self.canvas.create_text(440, 700, text=f"탈출했습니다! {render_text}", font=("Helvetica", 16), tags="dice_result", fill="black")
                    current_player["uninhabitedIslandCount"] = 0
                    self.update_player_info()
                    self.__update_play_order()
                else:
                    current_player["uninhabitedIslandCount"] += 1
                    self.canvas.create_text(440, 700, text=f'{result_text}. 탈출 실패! 카운트: {current_player["uninhabitedIslandCount"]}', font=("Helvetica", 16), tags="dice_result", fill="black")
                    self.__update_play_order()
            self.canvas.after(1000, self.reset_dice)
        else:
            self.update_player_info()
            self.canvas.delete("dice_roll_info")
            self.canvas.create_text(440, 700, text=render_text, font=("Helvetica", 16), tags="dice_result", fill="black")
            if not self.is_double:
                self.__update_play_order()
            self.canvas.after(1000, self.reset_dice)

    def random_gimick(self):
        current_player = self.players[self.play_order - 1]
        current_money = current_player['money']
        gimick_type = random.choice(["move", "gain", "lose"])

        if gimick_type == "move":
            teleport = random.choice([1, 11, 21, 31])  # 출발지, 무인도, 우주여행, 사회복지기금
            current_player["currentPosition"] = teleport
            flat_board = Utils.flatted_board(board)
            current_player["currentPositionName"] = next(item["name"] for item in flat_board if item["index"] == teleport)
            result_text = f"{current_player['name']}님이\n {current_player['currentPositionName']}으로 이동합니다."
            if current_player["currentPositionName"] == "우주여행":
                self.space_travel_player = current_player

        elif gimick_type == "gain":
            gain_money = int(0.2 * current_money)
            current_player['money'] += gain_money
            result_text = f"{current_player['name']}님이\n {gain_money}원(현재 금액의 20%)을 받습니다."

        elif gimick_type == "lose":
            lose_money = int(0.2 * current_money)
            current_player['money'] -= lose_money
            result_text = f"{current_player['name']}님이\n {lose_money}원(현재 금액의 20%)을 잃습니다."

        messagebox.showinfo("황금열쇠 이벤트 발생!", result_text)

    def gain_community_chest_fund(self):
        amount = self.community_chest_fund
        self.players[self.play_order - 1]['money'] += amount
        self.community_chest_fund = 0 # 사회복지기금 초기화
        result_text = f"{self.players[self.play_order - 1]['name']}님이 사회복지기금 {amount}원을 받습니다."
        messagebox.showinfo("사회복지기금 회수", result_text)

    def lose_community_chest_fund(self):
        amount = int(0.2 * self.players[self.play_order - 1]['money']) # 시작 금액의 20%
        self.players[self.play_order - 1]['money'] -= amount
        self.community_chest_fund += amount
        result_text = f"{self.players[self.play_order - 1]['name']}님이 사회복지기금에 {amount}원을 기부합니다."
        messagebox.showinfo("사회복지기금 기부", result_text)

    def reset_dice(self):
        self.result = 0
        self.canvas.delete("dice_result")
        current_player = self.players[self.play_order - 1]
        escape_info_text = f"{self.players[self.play_order -1]['name']} 님의 차례, 무인도에 갇혀 더블이 나오거나, 세 번 주사위를 굴리면 탈출할 수 있습니다."
        lets_escape_text = f"{self.players[self.play_order -1]['name']} 님의 차례, 스페이스 바를 눌러 무인도를 탈출하세요."
        uninhabited_island_info_render_text = lets_escape_text if current_player["uninhabitedIslandCount"] == 3 else escape_info_text
        if current_player.get("currentPositionName") == "무인도":
            self.canvas.create_text(440, 700, text=uninhabited_island_info_render_text, font=("Helvetica", 16), tags="uninhabited_island_info", fill="black")
        else:
            self.canvas.create_text(440, 700, text=f"{self.players[self.play_order -1]['name']} 님의 차례, 스페이스 바를 눌러 주사위를 굴리세요", font=("Helvetica", 16), tags="dice_roll_info", fill="black")

    def show_player_info(self):
        self.canvas.delete("player_info")
        for idx, player in enumerate(self.players):
            player_name = player["name"]
            current_player_position_name = player["currentPositionName"]
            cities_owned = ', '.join(city.get_name() for city in player["cities"]) if player["cities"] else "없음"
            self.canvas.create_text(100, 120 + 70 * idx, text=f"{idx + 1}. {player_name} - {player['money']}원 \n 보유 도시: {cities_owned} \n 현재 위치: {current_player_position_name}", font=("Helvetica", 14), anchor="w", fill="black", tags="player_info")

    def show_turn_info(self):
        self.canvas.delete("turn_info")
        self.canvas.create_text(600, 600, text=f"현재 턴수 : {self.turn_count}\n최대 턴수 : {self.max_turn}\n\n사회복지기금 : {self.community_chest_fund}원", font=("Helvetica", 12), tags="turn_info", fill="black")

    def update_player_info(self):
        flat_board = Utils.flatted_board(board)
        current_player = self.players[self.play_order - 1]
        next_position_index = current_player.get("currentPosition") + self.result
        is_around_game = next_position_index > 40

        if is_around_game:
            next_position_index -= 40
            current_player['money'] += self.__get_start_point_money()

        filtered_board_item = next(item for item in flat_board if item.get("index") == next_position_index)
        current_player["currentPosition"] = filtered_board_item.get("index")
        current_player["currentPositionName"] = filtered_board_item.get("name")

        if current_player["currentPositionName"] == "무인도":
            self.is_double = False

        self.canvas.delete("player_info")
        self.show_player_info()

        if current_player["currentPositionName"] == "황금열쇠":
            self.random_gimick()
        elif current_player["currentPositionName"] == "사회복지기금":
            if current_player["currentPosition"] == 21:  # 사회복지기금 회수
                self.gain_community_chest_fund()
            elif current_player["currentPosition"] == 39:  # 사회복지기금 기부
                self.lose_community_chest_fund()
        elif current_player["currentPositionName"] == "우주여행":
            self.ask_for_space_travel(current_player)
        elif current_player["currentPositionName"] not in ["출발지점", "무인도", "황금열쇠", "사회복지기금"]:
            city = self.get_city(current_player["currentPositionName"])
            if city.get_owner() is None and city.is_buyable():
                self.ask_to_buy_city(current_player, city)
            else:
                if city.get_owner() != current_player:
                    self.pay_toll_with_city_sell(current_player, city.get_owner(), city, city.get_toll())
                    self.show_player_info()

    def ask_for_space_travel(self, player):
        space_travel_cost = 400000
        if player['money'] < space_travel_cost:
            messagebox.showinfo("우주여행 불가", f"소유한 돈이 부족하여 우주여행을 할 수 없습니다. (필요 금액: {space_travel_cost}원)")
            return

        response = messagebox.askyesno("우주여행", "우주여행을 하시겠습니까?")
        if response:
            columbia_owner = self.get_city("콜롬비아호").get_owner()
            if columbia_owner and columbia_owner != player:
                player['money'] -= space_travel_cost
                columbia_owner['money'] += space_travel_cost
            elif columbia_owner != player:
                player['money'] -= space_travel_cost

            self.space_travel_player = player  # 우주여행을 실행한 플레이어를 추적
            messagebox.showinfo("우주여행", "다음 턴에 원하는 도시로 이동할 수 있습니다.")
        self.show_player_info()

    def get_city(self, city_name):
        for player in self.players:
            for city in player["cities"]:
                if city.get_name() == city_name:
                    return city
        flat_board = Utils.flatted_board(board)
        for item in flat_board:
            if item["name"] == city_name:
                return City(city_name, item["index"], item["price"], item["toll"])
        return City(city_name, -1, 0, 0)

    def __get_start_point_money(self):
        return 200000

    def __update_play_order(self):
        self.play_order += 1
        if self.play_order > len(self.players):
            self.play_order = 1

    def ask_to_buy_city(self, player, city):
        if city.get_owner() is None and city.is_buyable():
            if player['money'] >= city.get_price():
                response = messagebox.askyesno("도시 구매", f"{player['name']}님, {city.get_name()} 도시를 {city.get_price()}원에 구매하시겠습니까?")
                if response:
                    city.buy_city(player)
                    messagebox.showinfo("구매 완료", f"{player['name']}님이 {city.get_name()} 도시를 구매하였습니다.")
                    self.update_city_info_popup() 
                    self.show_player_info()
                else:
                    messagebox.showinfo("구매 취소", f"{player['name']}님이 {city.get_name()} 도시 구매를 취소하였습니다.")
            else:
                messagebox.showinfo("구매 불가", f"소유한 돈이 부족하여 {player['name']}님은 {city.get_name()} 도시를 구매할 수 없습니다.")
        else:
            messagebox.showinfo("구매 불가", f"{city.get_name()} 도시는 이미 다른 플레이어가 소유하고 있거나 구매할 수 없습니다.")

    def show_city_selection(self, player):
        def on_select_city():
            selected_city_name = city_listbox.get(city_listbox.curselection())
            selected_city = self.get_city(selected_city_name)
            player["currentPosition"] = selected_city.get_index()
            player["currentPositionName"] = selected_city_name
            self.space_travel_player = None
            self.root.bind('<space>', self.roll_dice)
            city_selection_window.destroy()
            self.show_player_info()
            self.perform_city_action(player)

        self.root.unbind('<space>')

        city_selection_window = Toplevel(self.root)
        city_selection_window.title("도시 선택")
        city_selection_window.geometry("300x350")
        
        tk.Label(city_selection_window, text=f"{player['name']}님, 이동할 도시를 선택하세요.", font=("Helvetica", 12)).pack(pady=10)
        
        city_listbox = Listbox(city_selection_window, width=40, height=15)
        city_listbox.pack(pady=10)

        flat_board = Utils.flatted_board(board)
        for item in flat_board:
            if item["name"] not in ["우주여행"]:
                city_listbox.insert(END, item["name"])

        select_button = tk.Button(city_selection_window, text="선택", command=on_select_city)
        select_button.pack(pady=10)

        self.root.wait_window(city_selection_window)

    def perform_city_action(self, player):
        city_name = player["currentPositionName"]
        if city_name in ["출발지점", "무인도", "황금열쇠", "사회복지기금"]:
            self.execute_special_action(city_name)
        else:
            city = self.get_city(city_name)
            if city.get_owner() is None and city.is_buyable():
                self.ask_to_buy_city(player, city)
            else:
                if city.get_owner() != player:
                    self.pay_toll_with_city_sell(player, city.get_owner(), city, city.get_toll())
            self.show_player_info()

    def execute_special_action(self, action_name):
        current_player = self.players[self.play_order - 1]
        if action_name == "황금열쇠":
            self.random_gimick()
        elif action_name == "사회복지기금":
            if current_player["currentPosition"] == 21:
                self.gain_community_chest_fund()
            elif current_player["currentPosition"] == 39:
                self.lose_community_chest_fund()
        self.show_player_info()

    def show_city_sell_popup(self, player, required_amount):
        def on_submit():
            selected_city_full_name = city_listbox.get(city_listbox.curselection())
            selected_city_name = selected_city_full_name.split(' - ')[0]
            selected_city = self.get_city(selected_city_name)
            if selected_city.sell_city(player):
                self.update_city_info_popup()
            self.root.bind('<space>', self.roll_dice)
            popup.destroy()

        self.root.unbind('<space>')

        popup = Toplevel(self.root)
        popup.title("도시 판매")
        tk.Label(popup, text=f"{player['name']}님, 통행료가 부족하여 도시를 판매해야 합니다.").pack()
        tk.Label(popup, text=f"필요한 금액: {required_amount}원").pack()
        
        city_listbox = Listbox(popup, width = 40, height = 15)
        for city in player['cities']:
            city_listbox.insert(END, f"{city.get_name()} - {city.get_price()}원")
        city_listbox.pack()
        
        tk.Button(popup, text="Sell City", command=on_submit).pack()

        self.root.wait_window(popup)

    def pay_toll_with_city_sell(self, player, owner, city, toll_amount):
        self.bankrupt_flag = False
        total_paid = player['money']
        player['money'] = 0

        while total_paid < toll_amount and player['cities']:
            required_amount = toll_amount - total_paid
            self.show_city_sell_popup(player, required_amount)
            total_paid += player['money']
            player['money'] = 0  # 도시 판매 후 금액 초기화

        if total_paid >= toll_amount:
            remaining_money = total_paid - toll_amount
            player['money'] = remaining_money
            owner['money'] += toll_amount
            messagebox.showinfo("통행료 지불 완료", f"{player['name']}님이 {owner['name']}님에게 {city.get_name()} 도시의 통행료 {toll_amount}원을 지불했습니다. 남은 금액: {remaining_money}원")
        else:
            owner['money'] += total_paid
            if not player['cities'] and total_paid < toll_amount:
                messagebox.showinfo("파산", f"{player['name']}님이 {owner['name']}님에게 {city.get_name()} 도시의 통행료 {total_paid}원을 지불하고 파산했습니다.")
                player['money'] = 0
                self.bankrupt_flag = True  # 파산 플래그 설정
            else:
                messagebox.showinfo("통행료 지불 완료", f"{player['name']}님이 {owner['name']}님에게 {city.get_name()} 도시의 통행료 {total_paid}원을 지불했습니다. 남은 금액: {player['money']}원")

    def end_game(self): # 한 명 제외 파산했을 때 게임 승리
        winner = self.players[0]
        messagebox.showinfo("게임 종료", f"{winner['name']}님이 승리했습니다!")
        self.root.quit()  # 게임 종료

    def end_game2(self): # 최대 턴 수에 도달하여 가장 많은 돈을 가진 사람이 승리
        max_total_value = 0
        winner = None
        
        for player in self.players:
            total_city_value = sum(city.get_price() for city in player['cities'])
            total_value = player['money'] + total_city_value
            
            if total_value > max_total_value:
                max_total_value = total_value
                winner = player
        
        messagebox.showinfo("게임 종료", f"{winner['name']}님이 승리했습니다! 총 자산: {max_total_value}원(도시가치 포함)")
        self.root.quit()  # 게임 종료

# 게임 실행
root = tk.Tk()
app = BuruMarbleGame(root)
root.mainloop()