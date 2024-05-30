import tkinter as tk
import random
import time

# 보드 설정 (11x11)
board = [
    ["출발지점", "타이베이", "황금열쇠", "베이징", "마닐라", "제주도", "싱가포르", "황금열쇠", "카이로", "이스탄불", "무인도"],
    ["서울", "", "", "", "", "", "", "", "", "", "아테네"],
    ["사회복지\n기금", "", "", "", "", "", "", "", "", "", "황금열쇠"],
    ["뉴욕", "", "", "", "", "", "", "", "", "", "코펜하겐"],
    ["런던", "", "", "", "", "", "", "", "", "", "스톡홀름"],
    ["황금열쇠", "", "", "", "", "", "", "", "", "", "콩고드\n여객기"],
    ["로마", "", "", "", "", "", "", "", "", "", "취리히"],
    ["파리", "", "", "", "", "", "", "", "", "", "황금열쇠"],
    ["콜롬비아호", "", "", "", "", "", "", "", "", "", "베를린"],
    ["도쿄", "", "", "", "", "", "", "", "", "", "몬트리올"],
    ["우주여행", "마드리드", "퀸 엘리자\n베스호", "리스본", "하와이", "부산", "시드니", "상파울로", "황금열쇠", "부에노스\n아이레스", "사회복지\n기금"]
]

# 색상 설정
colors = {
    "top": "lightblue",
    "right": "lightgreen",
    "bottom": "lightcoral",
    "left": "lightgoldenrodyellow",
    "corner": "gray",
    "default": "black"
}

class BuruMarbleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("부루마블 보드 게임")

        self.canvas = tk.Canvas(root, width=880, height=880)
        self.canvas.pack()

        self.cell_width = 80
        self.cell_height = 80

        self.players = []  # 플레이어들의 이름을 저장할 리스트
        self.player_money = []  # 플레이어들의 보유 머니를 저장할 리스트

        self.play_order = 1  # 플레이 순서
        self.dice_result = 0  # 주사위 결과
        self.show_result = False  # 주사위 결과 출력 여부

        self.create_player_selection()

    def create_player_selection(self):
        self.label = tk.Label(self.root, text="플레이어 인원을 선택하세요 (2~4명):", font=("Helvetica", 16))
        self.label.place(x=200, y=50)

        self.player_count = tk.IntVar()
        self.player_count.set(2)  # 기본값 2명 설정

        self.radio_frame = tk.Frame(self.root)
        self.radio_frame.place(x=220, y=100)

        self.radio2 = tk.Radiobutton(self.radio_frame, text="2명", variable=self.player_count, value=2, font=("Helvetica", 14))
        self.radio3 = tk.Radiobutton(self.radio_frame, text="3명", variable=self.player_count, value=3, font=("Helvetica", 14))
        self.radio4 = tk.Radiobutton(self.radio_frame, text="4명", variable=self.player_count, value=4, font=("Helvetica", 14))

        self.radio2.pack(anchor="w")
        self.radio3.pack(anchor="w")
        self.radio4.pack(anchor="w")

        self.start_button = tk.Button(self.root, text="게임 시작", font=("Helvetica", 14), command=self.get_player_names)
        self.start_button.place(x=300, y=250)

    def get_player_names(self):
        num_players = self.player_count.get()
        self.player_name_entries = []

        # 이름 입력창을 추가하는 커스텀 다이얼로그 생성
        self.name_entry_window = tk.Toplevel(self.root)
        self.name_entry_window.title("플레이어 이름 입력")
        self.name_entry_window.geometry("300x200")
        self.name_entry_window.transient(self.root)
        self.name_entry_window.grab_set()

        tk.Label(self.name_entry_window, text="플레이어 이름을 입력하세요:", font=("Helvetica", 12)).pack(pady=10)

        for i in range(num_players):
            tk.Label(self.name_entry_window, text=f"플레이어 {i + 1}:", font=("Helvetica", 10)).pack()
            entry = tk.Entry(self.name_entry_window, font=("Helvetica", 10))
            entry.pack(pady=5)
            self.player_name_entries.append(entry)

        tk.Button(self.name_entry_window, text="확인", command=self.save_player_names).pack(pady=20)

    def save_player_names(self):
        for entry in self.player_name_entries:
            name = entry.get()
            if name:
                self.players.append(name)
            else:
                self.players.append(f"플레이어 {len(self.players) + 1}")  # 이름을 입력하지 않은 경우 기본 이름 설정

        self.name_entry_window.destroy()
        self.label.place_forget()
        self.radio_frame.place_forget()
        self.start_button.place_forget()

        self.get_player_money()

    def get_player_money(self):
        self.money_entry_window = tk.Toplevel(self.root)
        self.money_entry_window.title("초기 머니 설정")
        self.money_entry_window.geometry("400x300")
        self.money_entry_window.transient(self.root)
        self.money_entry_window.grab_set()

        self.money_entries = []
        self.auto_money = tk.BooleanVar()
        self.auto_money.set(True)  # 기본값은 자동 설정

        tk.Label(self.money_entry_window, text="초기 머니 설정", font=("Helvetica", 14)).pack(pady=10)

        auto_money_check = tk.Checkbutton(self.money_entry_window, text="자동 설정 (200만원)", variable=self.auto_money, font=("Helvetica", 12))
        auto_money_check.pack(pady=5)

        for i, player in enumerate(self.players):
            frame = tk.Frame(self.money_entry_window)
            frame.pack(pady=5)

            tk.Label(frame, text=f"{player}의 초기 머니:", font=("Helvetica", 10)).pack(side="left")
            entry = tk.Entry(frame, font=("Helvetica", 10))
            entry.pack(side="left")
            self.money_entries.append(entry)

        tk.Button(self.money_entry_window, text="확인", command=self.save_player_money).pack(pady=20)

    def save_player_money(self):
        for entry in self.money_entries:
            if self.auto_money.get():
                self.player_money.append(2000000)  # 200만원 자동 설정
            else:
                try:
                    money = int(entry.get())
                    self.player_money.append(돈)
                except ValueError:
                    self.player_money.append(2000000)  # 입력값이 유효하지 않으면 200만원으로 설정

        self.money_entry_window.destroy()
        self.create_board()

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
                
                text = board[i][j]
                if text:
                    self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=text, font=("Helvetica", 12))

        # 플레이어 이름 및 보유 머니 출력
        for idx, (player_name, money) in enumerate(zip(self.players, self.player_money)):
            self.canvas.create_text(50, 50 + 20 * idx, text=f"{idx + 1}. {player_name} - {money}원", font=("Helvetica", 12), anchor="w")

        # 스페이스바 이벤트 바인딩
        self.canvas.create_text(440, 700, text=f"플레이어 {self.play_order}번 차례, 스페이스 바를 눌러 주사위를 굴리세요", font=("Helvetica", 16), tags="dice_roll_info")    
        
        self.root.bind('<space>', self.roll_dice)
        
    def roll_dice(self, event):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        self.result = dice1 + dice2
        print(self.result)
        result_text = f"주사위 결과: {dice1}, {dice2} (합: {self.result}) / 스페이스 바를 눌러 차례를 넘기세요"

        self.canvas.delete("dice_roll_info")
        self.canvas.create_text(440, 700, text=result_text, font=("Helvetica", 16), tags="dice_result")
        self.result = 0

        self.play_order += 1
        if (self.play_order > len(self.players)):
            self.play_order = 1

        self.canvas.after(1500, self.reset_dice)

    def reset_dice(self):
        self.canvas.delete("dice_result")
        self.canvas.create_text(440, 700, text=f"플레이어 {self.play_order}번 차례, 스페이스 바를 눌러 주사위를 굴리세요", font=("Helvetica", 16), tags="dice_roll_info")\

# 게임 실행
root = tk.Tk()
app = BuruMarbleGame(root)
root.mainloop()