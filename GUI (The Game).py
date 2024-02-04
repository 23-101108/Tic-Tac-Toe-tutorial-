import tkinter as tk
from tkinter import messagebox
import random
from PIL import ImageTk, Image
import pygame

def start_game():
    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.iconbitmap('icon.ico')

    def on_start_game():
        pygame.mixer.music.load('click.wav')
        pygame.mixer.music.play()
        player_name=entry_player.get()
        friend_name=entry_friend.get()

        if player_name=='':
            player_name='Player One'
        if friend_name=='':
            friend_name='Player Two'

        if var.get() == 1:
            messagebox.showinfo("Tic Tac Toe", "Starting Football Game")
            root.destroy()
            play_game(player_name,friend_name)
        else:
            messagebox.showinfo("Tic Tac Toe", "Starting Standard Game")
            root.destroy()
            footbal_game(player_name,friend_name)

    label_player = tk.Label(root, text="Enter Your Name:")
    entry_player = tk.Entry(root)
    label_friend = tk.Label(root, text="Enter Friend's Name:")
    entry_friend = tk.Entry(root)
    label_edition = tk.Label(root, text="Choose Edition:")
    var = tk.IntVar()
    radio_standard = tk.Radiobutton(root, text="Football", variable=var, value=0)
    radio_football = tk.Radiobutton(root, text="Standard", variable=var, value=1)
    button_start = tk.Button(root, text="Start Game", command=on_start_game)
    button_Quit = tk.Button(root, text="Quit Game",command=root.destroy)

    label_player.grid(row=0, column=0, padx=10, pady=5)
    entry_player.grid(row=0, column=1, padx=10, pady=5)
    label_friend.grid(row=1, column=0, padx=10, pady=5)
    entry_friend.grid(row=1, column=1, padx=10, pady=5)
    label_edition.grid(row=2, column=0, padx=10, pady=5)
    radio_standard.grid(row=2, column=1, padx=10, pady=5)
    radio_football.grid(row=2, column=2, padx=10, pady=5)
    button_start.grid(row=3, column=1, pady=10)
    button_Quit.grid(row=3, column=2, pady=10)

    root.mainloop()


def play_game(player_name,friend_name):
    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.iconbitmap('icon.ico')
    root.attributes("-fullscreen", True)

    board = [[3 * row + col + 1 for col in range(3)] for row in range(3)]

    player = [player_name, friend_name]
    Symboll = ['X', 'O']

    current_player = 0

    def on_click(row, col):
        nonlocal current_player

        pygame.mixer.music.load('click.wav')
        pygame.mixer.music.play()

        if board[row][col] == 0:
            return

        board[row][col] = Symboll[current_player]
        button = buttons[row][col]
        button.config(text=Symboll[current_player], state=tk.DISABLED)

        if check_winner():
            pygame.mixer.music.load('win_sound.wav')
            pygame.mixer.music.play()
            messagebox.showinfo("Tic Tac Toe", f"Congratulations!"
                                               f" {player[current_player]} is the Winner!")
            root.destroy()
            start_game()

        elif check_tie():
            pygame.mixer.music.load('Lose sound effects.wav')
            pygame.mixer.music.play()
            messagebox.showinfo("Tic Tac Toe", "The Game is Tie!")
            root.destroy()
            start_game()

        else:
            current_player = (current_player + 1) % 2

    def check_winner():
        for i in range(3):
            if all(board[i][j] == Symboll[current_player] for j in range(3)) or all(
                    board[j][i] == Symboll[current_player] for j in range(3)):
                return True
        if all(board[i][i] == Symboll[current_player] for i in range(3)) or all(
                board[i][2 - i] == Symboll[current_player] for i in range(3)):
            return True
        return False

    def check_tie():
        return all(isinstance(cell, str) for row in board for cell in row)

    buttons = [[0, 0, 0] for _ in range(3)]

    def resume_game():
        pygame.mixer.music.load('click.wav')
        pygame.mixer.music.play()
        print('resume game')

    def restart_game():
        pygame.mixer.music.load('click.wav')
        pygame.mixer.music.play()
        root.destroy()
        play_game()

    def quit_game():
        pygame.mixer.music.load('click.wav')
        pygame.mixer.music.play()
        root.destroy()
        start_game()

    menu = tk.Menu(root)

    root.config(menu=menu)
    file_menu = tk.Menu(menu, tearoff=0)
    file_menu.add_command(label="Resume", command=resume_game,font=('normal',10))
    file_menu.add_command(label="Restart", command=restart_game,font=('normal',10))
    file_menu.add_command(label="Quit", command=quit_game,font=('normal',10))

    menu_button = tk.Button(root, text="Menu", font=('normal', 20), command=lambda: file_menu.post(200, 400))
    menu_button.grid(row=4,column=1)


    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text="", font=('normal', 20), height=2, width=5,
                                      command=lambda row=i, col=j: on_click(row, col))
            buttons[i][j].grid(row=i, column=j)


    root.mainloop()


def footbal_game(player_name,friend_name):
    global menu_visible

    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.iconbitmap('icon.ico')
    root.attributes("-fullscreen", True)


    football_clubs = ["ACM.png","Arsenal.png","Atletico.png","barca.png",
                      "Bayern.png","Chelsea.png","MAN city.png","Man United.png",
                      "Liverpool.png","KING.png","juve.png","inter.png","Dortmond.png",
                      "PSG.png","Rome.png","spurs.png"
                      ]

    football_Data = ['south_america.png', 'north_america.png',
                     'asia.png', 'manager.png', 'world_cup.png',
                     'champions_league.png', 'copa_america.png',
                     'afcon.png', 'euro.png', 'salah.png', 'africa.png',
                     'icon.png', 'cr7.png', 'messi.png', 'belgium.png',
                     'arab.png', 'saudi_league.png', 'la_liga.png',
                     'premier_league.png', 'seria_a.png'
                     ]

    random_club_1 = random.choice(football_clubs)
    football_clubs.remove(random_club_1)
    random_club_2 = random.choice(football_clubs)
    football_clubs.remove(random_club_2)
    random_club_3 = random.choice(football_clubs)
    football_clubs.remove(random_club_3)

    club_image_1 = ImageTk.PhotoImage(Image.open(random_club_1))
    club_image_2 = ImageTk.PhotoImage(Image.open(random_club_2))
    club_image_3 = ImageTk.PhotoImage(Image.open(random_club_3))

    random_data_1 = random.choice(football_Data)
    football_Data.remove(random_data_1)
    random_data_2 = random.choice(football_Data)
    football_Data.remove(random_data_2)
    random_data_3 = random.choice(football_Data)
    football_Data.remove(random_data_3)

    data_image_1 = ImageTk.PhotoImage(Image.open(random_data_1))
    data_image_2 = ImageTk.PhotoImage(Image.open(random_data_2))
    data_image_3 = ImageTk.PhotoImage(Image.open(random_data_3))

    player = [player_name, friend_name]
    Symboll = ['X', 'o']

    current_player = 0

    board = [[3 * row + col + 1 for col in range(3)] for row in range(3)]

    def on_click(row, col):
        nonlocal current_player
        pygame.mixer.music.load('click.wav')
        pygame.mixer.music.play()
        if board[row][col] == 0:
            return
        board[row][col] = Symboll[current_player]
        button = buttons[row][col]
        button.config(text=Symboll[current_player], state=tk.DISABLED)
        if check_winner_football():
            pygame.mixer.music.load('win_sound.wav')
            pygame.mixer.music.play()
            messagebox.showinfo("Tic Tac Toe", f"Congratulations! {player[current_player]} is the Winner!")
            root.destroy()
            start_game()
        elif check_tie_football():
            pygame.mixer.music.load('Lose sound effects.wav')
            pygame.mixer.music.play()
            messagebox.showinfo("Tic Tac Toe", "The Game is Tie!")
            root.destroy()
            start_game()
        else:
            current_player = (current_player + 1) % 2

    def check_winner_football():
        for i in range(3):
            if all(board[i][j] == Symboll[current_player] for j in range(3)) or all(
                    board[j][i] == Symboll[current_player] for j in range(3)):
                return True
        if all(board[i][i] == Symboll[current_player] for i in range(3)) or all(
                board[i][2 - i] == Symboll[current_player] for i in range(3)):
            return True
        return False

    def check_tie_football():
        return all(isinstance(cell, str) for row in board for cell in row)

    buttons = [[0, 0, 0] for _ in range(3)]

    def resume_game():
        pygame.mixer.music.load('click.wav')
        pygame.mixer.music.play()
        print('resume game')

    def restart_game():
        pygame.mixer.music.load('click.wav')
        pygame.mixer.music.play()
        root.destroy()
        footbal_game()

    def quit_game():
        pygame.mixer.music.load('click.wav')
        pygame.mixer.music.play()
        root.destroy()
        start_game()

    menu = tk.Menu(root)
    root.config(menu=menu)
    file_menu = tk.Menu(menu, tearoff=0)
    file_menu.add_command(label="Resume", command=resume_game,font=('normal',10))
    file_menu.add_command(label="Restart", command=restart_game,font=('normal',10))
    file_menu.add_command(label="Quit", command=quit_game,font=('normal',10))

    menu_button = tk.Button(root, text="Menu", font=('normal', 20), command=lambda: file_menu.post(400, 400))
    menu_button.grid(row=4,column=4)


    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text="", font=('normal', 20), height=2, width=5,
                                      command=lambda row=i, col=j: on_click(row, col))
            buttons[i][j].grid(row=i, column=j)

    label_club_1 = tk.Label(root, image=club_image_1)
    label_club_1.grid(row=4, column=0)

    label_club_2 = tk.Label(root, image=club_image_2)
    label_club_2.grid(row=4, column=1)

    label_club_3 = tk.Label(root, image=club_image_3)
    label_club_3.grid(row=4, column=2)

    label_data_1 = tk.Label(root, image=data_image_1)
    label_data_1.grid(row=0, column=4)

    label_data_2 = tk.Label(root, image=data_image_2)
    label_data_2.grid(row=1, column=4)

    label_data_3 = tk.Label(root, image=data_image_3)
    label_data_3.grid(row=2, column=4,padx=5)


    root.mainloop()


pygame.init()
pygame.mixer.init()
start_game()
