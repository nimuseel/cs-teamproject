import tkinter as tk
import random
from utils import Utils
from player.player import Player

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
        self.player_money = player.player_money

        self.play_order = 1  # 플레이 순서
        self.dice_result = 0  # 주사위 결과
        self.show_result = False  # 주사위 결과 출력 여부

        self.city = []  # 도시 정보를 저장할 리스트

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
        
    def roll_dice(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        self.result = dice1 + dice2
        is_double = dice1 == dice2
        
        result_text = f"주사위 결과: {dice1}, {dice2} (합: {self.result})"
        double_text = f"더블! 주사위를 한 번 더 굴리세요"
        render_text = result_text + double_text if is_double else result_text

        self.update_player_info()

        self.canvas.delete("dice_roll_info")
        self.canvas.create_text(440, 700, text=render_text, font=("Helvetica", 16), tags="dice_result", fill="black")
        self.result = 0

        if is_double == False:
            self.play_order += 1
            if (self.play_order > len(self.players)):
                self.play_order = 1

        self.canvas.after(1500, self.reset_dice)

    def reset_dice(self):
        self.canvas.delete("dice_result")
        self.canvas.create_text(440, 700, text=f"플레이어 {self.play_order}번 차례, 스페이스 바를 눌러 주사위를 굴리세요", font=("Helvetica", 16), tags="dice_roll_info", fill="black")

    def show_player_info(self):
        for idx, (player, money) in enumerate(zip(self.players, self.player_money)):
            player_name = dict(player)["name"]
            current_player_position_name = dict(player)["currentPositionName"]
            self.canvas.create_text(60, 70 + 50 * idx, text=f"{idx + 1}. {player_name} - {money}원 \n 보유 도시: 없음 \n 현재 위치: {current_player_position_name}", font=("Helvetica", 14), anchor="w", fill="black", tags="player_info")

    def update_player_info(self):
        flatten_board = Utils.flatted_board(board)
        
        current_player = self.players[self.play_order - 1]
        next_position_index = current_player.get("currentPosition") + self.result
        
        filtered_board_item = list(filter(lambda x: x.get("index") == next_position_index, flatten_board))[0]
        
        current_player["currentPosition"] = filtered_board_item.get("index")
        current_player["currentPositionName"] = filtered_board_item.get("name")

        self.canvas.delete("player_info")
        self.show_player_info()
        
# 게임 실행
root = tk.Tk()
app = BuruMarbleGame(root)
root.mainloop()