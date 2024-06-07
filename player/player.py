import tkinter as tk

class Player:
    def __init__(self, root, game_start_fn):
        self.root = root

        self.players = []  # 플레이어들의 이름을 저장할 리스트
        self.player_money = []  # 플레이어들의 보유 머니를 저장할 리스트

        self.play_order = 1  # 플레이 순서

        self.game_start = game_start_fn

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

        self.start_button = tk.Button(self.root, text="게임 시작", font=("Helvetica", 14), command=self.__get_player_names)
        self.start_button.place(x=300, y=250)
    
    def __get_player_names(self):
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

        tk.Button(self.name_entry_window, text="확인", command=self.__save_player_names).pack(pady=20)
    
    def __save_player_names(self):
        for entry in self.player_name_entries:
            name = entry.get()
            if name:
                self.players.append({ "name": name, "currentPosition": 1, "currentPositionName": "출발지점", "uninhabitedIslandCount": 0 })
            else:
                self.players.append({ "name": f"플레이어 {len(self.players) + 1}", "currentPosition": 1, "currentPositionName": "출발지점", "uninhabitedIslandCount": 0 })  # 이름을 입력하지 않은 경우 기본 이름 설정

        self.name_entry_window.destroy()
        self.label.place_forget()
        self.radio_frame.place_forget()
        self.start_button.place_forget()

        self.__get_player_money()
    def __get_player_money(self):
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

            dict_player = dict(player)

            tk.Label(frame, text=f"{dict_player['name']}의 초기 머니:", font=("Helvetica", 10)).pack(side="left")
            entry = tk.Entry(frame, font=("Helvetica", 10))
            entry.pack(side="left")
            self.money_entries.append(entry)

        tk.Button(self.money_entry_window, text="확인", command=self.__save_player_money).pack(pady=20)

    def __save_player_money(self):
        for entry in self.money_entries:
            if self.auto_money.get():
                self.player_money.append(2000000)  # 200만원 자동 설정
            else:
                try:
                    money = int(entry.get())
                    self.player_money.append(money)
                except ValueError:
                    self.player_money.append(2000000)  # 입력값이 유효하지 않으면 200만원으로 설정

        self.money_entry_window.destroy()
        self.game_start()