import tkinter as tk
from tkinter import messagebox
import random
from utils import Utils
from player.player import Player
from city.a import City

# 보드 설정 (11x11)
board = [
    [{'name': '출발지점', 'index': 1}, {'name': '타이베이', 'index': 2}, {'name': '황금열쇠', 'index': 3}, {'name': '베이징', 'index': 4}, {'name': '마닐라', 'index': 5}, {'name': '제주도', 'index': 6}, {'name': '싱가포르', 'index': 7}, {'name': '황금열쇠', 'index': 8}, {'name': '카이로', 'index': 9}, {'name': '이스탄불', 'index': 10}, {'name': '무인도', 'index': 11}],
    [{'name': '서울', 'index': 40}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '아테네', 'index': 12}],
    [{'name': '사회복지\n기금', 'index': 39}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '황금열쇠', 'index': 13}],
    [{'name': '뉴욕', 'index': 38}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '코펜하겐', 'index': 14}],
    [{'name': '런던', 'index': 37}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '스톡홀름', 'index': 15}],
    [{'name': '황금열쇠', 'index': 36}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '콩고드\n여객기', 'index': 16}],
    [{'name': '로마', 'index': 35}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '취리히', 'index': 17}],
    [{'name': '파리', 'index': 34}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '황금열쇠', 'index': 18}],
    [{'name': '콜롬비아호', 'index': 33}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '베를린', 'index': 19}],
    [{'name': '도쿄', 'index': 32}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '', 'index': 0}, {'name': '몬트리올', 'index': 20}],
    [{'name': '우주여행', 'index': 31}, {'name': '마드리드', 'index': 30}, {'name': '퀸 엘리자\n베스호', 'index': 29}, {'name': '리스본', 'index': 28}, {'name': '하와이', 'index': 27}, {'name': '부산', 'index': 26}, {'name': '시드니', 'index': 25}, {'name': '상파울로', 'index': 24}, {'name': '황금열쇠', 'index': 23}, {'name': '부에노스\n아이레스', 'index': 22}, {'name': '사회복지\n기금', 'index': 21}]
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

        player = Player(root, self.create_board)

        self.players = player.players
        self.community_chest_fund = 0

        self.play_order = 1  # 플레이 순서
        self.dice_result = 0  # 주사위 결과
        self.show_result = False  # 주사위 결과 출력 여부

        self.city = []  # 도시 정보를 저장할 리스트
        self.turn_count = 0
        self.max_turns = 20

        self.is_double = False

        player.create_player_selection()

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

        # 스페이스바 이벤트 바인딩
        self.canvas.create_text(440, 700, text=f"플레이어 {self.play_order}번 차례, 스페이스 바를 눌러 주사위를 굴리세요", font=("Helvetica", 16), tags="dice_roll_info", fill="black")    
        
        self.root.bind('<space>', self.roll_dice)
        
    def roll_dice(self, event):
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

    def check_winner(self):
        active_players = [player['money'] for player in self.players if player['money'] > 0]
        if len(active_players) == 1 or self.turn_count >= self.max_turns:
            max_money = max(player['money'] for player in self.players)
            winner_index = next(i for i, player in enumerate(self.players) if player['money'] == max_money)
            winner_name = self.players[winner_index]["name"]
            self.canvas.create_text(440, 440, text=f"게임 종료! 승자: {winner_name}", font=("Helvetica", 24), fill="red")
            self.root.unbind('<space>')

    def random_gimick(self):
        current_player = self.players[self.play_order - 1]
        current_money = current_player['money']
        gimick_type = random.choice(["move", "gain", "lose"])

        if gimick_type == "move":
            teleport = random.choice([1, 11, 21, 31])  # 출발지, 무인도, 우주여행, 사회복지기금
            current_player["currentPosition"] = teleport
            flat_board = Utils.flatted_board(board)
            current_player["currentPositionName"] = next(item["name"] for item in flat_board if item["index"] == teleport)
            result_text = f"{current_player['name']}님이 {current_player['currentPositionName']}으로 이동합니다."

        elif gimick_type == "gain":
            gain_money = int(0.2 * current_money)
            current_player['money'] += gain_money
            result_text = f"{current_player['name']}님이 {gain_money}원을 받습니다."

        elif gimick_type == "lose":
            lose_money = int(0.2 * current_money)
            current_player['money'] -= lose_money
            result_text = f"{current_player['name']}님이 {lose_money}원을 잃습니다."

        self.canvas.delete("gimick_result")
        self.canvas.create_text(440, 740, text=result_text, font=("Helvetica", 16), tags="gimick_result", fill="black")

    def gain_community_chest_fund(self):
        self.players[self.play_order - 1]['money'] += self.community_chest_fund
        self.community_chest_fund = 0  # 사회복지기금 초기화

    def lose_community_chest_fund(self):
        amount = int(0.2 * self.players[self.play_order - 1]['money'])
        self.players[self.play_order - 1]['money'] -= amount
        self.community_chest_fund += amount

    def reset_dice(self):
        self.result = 0
        self.canvas.delete("dice_result")
        current_player = self.players[self.play_order - 1]
        escape_info_text = f"플레이어 {self.play_order}번 차례, 무인도에 갇혀 더블이 나오거나, 세 번 주사위를 굴리면 탈출할 수 있습니다."
        lets_escape_text = f"플레이어 {self.play_order}번 차례, 스페이스 바를 눌러 무인도를 탈출하세요."
        uninhabited_island_info_render_text = lets_escape_text if current_player["uninhabitedIslandCount"] == 3 else escape_info_text
        if current_player.get("currentPositionName") == "무인도":
            self.canvas.create_text(440, 700, text=uninhabited_island_info_render_text, font=("Helvetica", 16), tags="uninhabited_island_info", fill="black")
        else:
            self.canvas.create_text(440, 700, text=f"플레이어 {self.play_order}번 차례, 스페이스 바를 눌러 주사위를 굴리세요", font=("Helvetica", 16), tags="dice_roll_info", fill="black")

    def show_player_info(self):
        self.canvas.delete("player_info")
        for idx, player in enumerate(self.players):
            player_name = player["name"]
            current_player_position_name = player["currentPositionName"]
            cities_owned = ', '.join(city.get_name() for city in player["cities"]) if player["cities"] else "없음"
            self.canvas.create_text(100, 120 + 70 * idx, text=f"{idx + 1}. {player_name} - {player['money']}원 \n 보유 도시: {cities_owned} \n 현재 위치: {current_player_position_name}", font=("Helvetica", 14), anchor="w", fill="black", tags="player_info")

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
        elif current_player["currentPositionName"] == "사회복지\n기금":
            if current_player["currentPosition"] == 21:  # 사회복지기금 회수
                self.gain_community_chest_fund()
            elif current_player["currentPosition"] == 39:  # 사회복지기금 기부
                self.lose_community_chest_fund()
        else:
            city = City(current_player["currentPositionName"])
            if city.get_owner() is None:
                self.ask_to_buy_city(current_player, city)

    def __get_start_point_money(self):
        return 200000

    def __update_play_order(self):
        self.play_order += 1
        if self.play_order > len(self.players):
            self.play_order = 1

    def ask_to_buy_city(self, player, city):
        response = messagebox.askyesno("도시 구매", f"{city.get_name()} 도시를 {city.get_price()}원에 구매하시겠습니까?")
        if response:
            city.buy_city(player)
            messagebox.showinfo("구매 완료", f"{city.get_name()} 도시를 구매하였습니다.")
            self.show_player_info()  # 플레이어 정보 업데이트
        else:
            messagebox.showinfo("구매 취소", "도시 구매를 취소하였습니다.")
# 게임 실행
root = tk.Tk()
app = BuruMarbleGame(root)
root.mainloop()