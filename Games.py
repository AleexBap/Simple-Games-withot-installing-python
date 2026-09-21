import random
import tkinter as tk
from tkinter import messagebox


# =====================================================================
#  GAME 1 — Rock, Paper, Scissors
# =====================================================================
def jogo_rps(parent):
    CHOICES = ["rock", "paper", "scissors"]

    def decide_winner(player, computer):
        if player == computer:
            return "tie"
        elif (
            (player == "rock" and computer == "scissors") or
            (player == "paper" and computer == "rock") or
            (player == "scissors" and computer == "paper")
        ):
            return "win"
        return "lose"

    root = tk.Toplevel(parent)
    root.title("Rock • Paper • Scissors")
    root.geometry("600x500")
    root.configure(bg="#1e1e2e")
    root.resizable(False, False)

    scores = {"wins": 0, "losses": 0, "ties": 0}

    tk.Label(root, text="Rock • Paper • Scissors",
             font=("Segoe UI", 20, "bold"),
             bg="#1e1e2e", fg="#f5c2e7").pack(pady=15)

    result_label = tk.Label(root, text="Make your move!",
                            font=("Segoe UI", 14),
                            bg="#1e1e2e", fg="#cdd6f4",
                            wraplength=380, justify="center")
    result_label.pack(pady=10)

    choices_label = tk.Label(root, text="You: —   |   Computer: —",
                             font=("Segoe UI", 12, "italic"),
                             bg="#1e1e2e", fg="#a6adc8")
    choices_label.pack(pady=5)

    score_label = tk.Label(root, text="Wins: 0   Losses: 0   Ties: 0",
                           font=("Segoe UI", 11),
                           bg="#1e1e2e", fg="#94e2d5")
    score_label.pack(pady=10)

    def play(player_choice):
        computer_choice = random.choice(CHOICES)
        outcome = decide_winner(player_choice, computer_choice)
        choices_label.config(
            text=f"You: {player_choice.capitalize()}   |   Computer: {computer_choice.capitalize()}"
        )
        if outcome == "tie":
            scores["ties"] += 1
            result_label.config(text=f"It's a tie! Both chose {player_choice}.", fg="#f9e2af")
        elif outcome == "win":
            scores["wins"] += 1
            result_label.config(text=f"You win! {player_choice} beats {computer_choice}.", fg="#a6e3a1")
        else:
            scores["losses"] += 1
            result_label.config(text=f"Computer wins! {computer_choice} beats {player_choice}.", fg="#f38ba8")
        score_label.config(
            text=f"Wins: {scores['wins']}   Losses: {scores['losses']}   Ties: {scores['ties']}"
        )

    button_frame = tk.Frame(root, bg="#1e1e2e")
    button_frame.pack(pady=20)

    button_style = {
        "font": ("Segoe UI", 13, "bold"),
        "width": 11, "height": 2,
        "bd": 0, "fg": "#1e1e2e",
        "activebackground": "#f5c2e7",
        "cursor": "hand2"
    }

    tk.Button(button_frame, text="◉ Rock", bg="#89b4fa",
              command=lambda: play("rock"), **button_style).grid(row=0, column=0, padx=6)
    tk.Button(button_frame, text="📄 Paper", bg="#a6e3a1",
              command=lambda: play("paper"), **button_style).grid(row=0, column=1, padx=6)
    tk.Button(button_frame, text="✂️ Scissors", bg="#f9e2af",
              command=lambda: play("scissors"), **button_style).grid(row=0, column=2, padx=6)

    def reset_game():
        scores["wins"] = scores["losses"] = scores["ties"] = 0
        score_label.config(text="Wins: 0   Losses: 0   Ties: 0")
        result_label.config(text="Make your move!", fg="#cdd6f4")
        choices_label.config(text="You: —   |   Computer: —")

    tk.Button(root, text="Reset Scores", command=reset_game,
              font=("Segoe UI", 11), bg="#cba6f7", fg="#1e1e2e",
              bd=0, padx=15, pady=6, cursor="hand2").pack(pady=10)


# =====================================================================
#  GAME 2 — Dice Roll with Scoring
# =====================================================================
def jogo_dice(parent):
    def roll_dice(sides=6):
        return random.randint(1, sides)

    game_state = {"rounds": 0, "target": 0, "total": 0,
                  "round_number": 0, "history": [], "playing": False}

    root = tk.Toplevel(parent)
    root.title("🎲 Dice Roller Game")
    root.geometry("460x700")
    root.configure(bg="#1e1e2e")
    root.resizable(False, False)

    tk.Label(root, text="🎲 Dice Roller",
             font=("Segoe UI", 22, "bold"),
             bg="#1e1e2e", fg="#f5c2e7").pack(pady=15)

    setup_frame = tk.Frame(root, bg="#1e1e2e")
    setup_frame.pack(pady=10)

    tk.Label(setup_frame, text="Rounds:", font=("Segoe UI", 12),
             bg="#1e1e2e", fg="#cdd6f4").grid(row=0, column=0, padx=8, pady=5, sticky="e")
    rounds_entry = tk.Entry(setup_frame, font=("Segoe UI", 12), width=8,
                            bg="#313244", fg="#cdd6f4", insertbackground="#cdd6f4", bd=0)
    rounds_entry.grid(row=0, column=1, padx=8, pady=5)
    rounds_entry.insert(0, "5")

    tk.Label(setup_frame, text="Target Score:", font=("Segoe UI", 12),
             bg="#1e1e2e", fg="#cdd6f4").grid(row=1, column=0, padx=8, pady=5, sticky="e")
    target_entry = tk.Entry(setup_frame, font=("Segoe UI", 12), width=8,
                            bg="#313244", fg="#cdd6f4", insertbackground="#cdd6f4", bd=0)
    target_entry.grid(row=1, column=1, padx=8, pady=5)
    target_entry.insert(0, "20")

    dice_face = tk.Label(root, text="🎲", font=("Segoe UI", 60),
                         bg="#1e1e2e", fg="#f9e2af")
    dice_face.pack(pady=15)

    stats_frame = tk.Frame(root, bg="#181825", bd=0)
    stats_frame.pack(pady=10, padx=20, fill="x")

    total_label = tk.Label(stats_frame, text="Total: 0",
                           font=("Segoe UI", 14, "bold"),
                           bg="#181825", fg="#89b4fa")
    total_label.pack(side="left", expand=True, pady=10)

    round_label = tk.Label(stats_frame, text="Round: 0 / 0",
                           font=("Segoe UI", 14, "bold"),
                           bg="#181825", fg="#a6e3a1")
    round_label.pack(side="left", expand=True, pady=10)

    target_display = tk.Label(stats_frame, text="Target: 0",
                              font=("Segoe UI", 14, "bold"),
                              bg="#181825", fg="#f38ba8")
    target_display.pack(side="left", expand=True, pady=10)

    tk.Label(root, text="Roll History:", font=("Segoe UI", 12, "italic"),
             bg="#1e1e2e", fg="#a6adc8").pack(pady=(15, 5))

    history_box = tk.Text(root, height=6, width=45, font=("Consolas", 11),
                          bg="#313244", fg="#cdd6f4", bd=0, padx=10, pady=8, wrap="word")
    history_box.pack(pady=5)
    history_box.config(state="disabled")

    status_label = tk.Label(root, text="Set your rounds & target, then roll!",
                            font=("Segoe UI", 12), bg="#1e1e2e", fg="#cba6f7",
                            wraplength=400, justify="center")
    status_label.pack(pady=10)

    button_frame = tk.Frame(root, bg="#1e1e2e")
    button_frame.pack(pady=10)

    def log_history(text):
        history_box.config(state="normal")
        history_box.insert("end", text + "\n")
        history_box.see("end")
        history_box.config(state="disabled")

    def start_game():
        try:
            rounds = int(rounds_entry.get())
            target = int(target_entry.get())
            if rounds <= 0 or target <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter positive integers.", parent=root)
            return

        game_state.update({"rounds": rounds, "target": target, "total": 0,
                           "round_number": 0, "history": [], "playing": True})

        history_box.config(state="normal")
        history_box.delete("1.0", "end")
        history_box.config(state="disabled")
        dice_face.config(text="🎲")
        total_label.config(text="Total: 0")
        round_label.config(text=f"Round: 0 / {rounds}")
        target_display.config(text=f"Target: {target}")
        status_label.config(text="Game started! Click 'Roll Dice' to begin.", fg="#a6e3a1")
        log_history(f"--- New Game (Target: {target}, Rounds: {rounds}) ---")
        roll_button.config(state="normal")
        start_button.config(text="Restart")

    def roll_once():
        if not game_state["playing"]:
            return
        roll = roll_dice()
        game_state["total"] += roll
        game_state["round_number"] += 1
        game_state["history"].append(roll)

        dice_faces = {1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"}
        dice_face.config(text=dice_faces.get(roll, "🎲"))
        total_label.config(text=f"Total: {game_state['total']}")
        round_label.config(text=f"Round: {game_state['round_number']} / {game_state['rounds']}")
        log_history(f"Round {game_state['round_number']}: rolled {roll}, total = {game_state['total']}")

        if game_state["total"] >= game_state["target"]:
            end_game(win=True)
        elif game_state["round_number"] >= game_state["rounds"]:
            end_game(win=False)

    def end_game(win):
        game_state["playing"] = False
        roll_button.config(state="disabled")
        if win:
            status_label.config(
                text=f"🎉 You reached {game_state['total']} in {game_state['round_number']} rounds!",
                fg="#a6e3a1")
            log_history(f"🎉 SUCCESS! Reached {game_state['total']} in {game_state['round_number']} rounds.")
        else:
            status_label.config(
                text=f"💥 Out of rounds! Final score: {game_state['total']} (target was {game_state['target']})",
                fg="#f38ba8")
            log_history(f"💥 FAILED! Final score: {game_state['total']} (target: {game_state['target']})")

    button_style = {
        "font": ("Segoe UI", 13, "bold"),
        "bd": 0, "fg": "#1e1e2e",
        "activebackground": "#f5c2e7",
        "cursor": "hand2",
        "width": 12, "pady": 10,
    }

    start_button = tk.Button(button_frame, text="Start / Restart", bg="#89b4fa",
                             command=start_game, **button_style)
    start_button.grid(row=0, column=0, padx=8)

    roll_button = tk.Button(button_frame, text="🎲 Roll Dice", bg="#a6e3a1",
                            command=roll_once, state="disabled", **button_style)
    roll_button.grid(row=0, column=1, padx=8)


# =====================================================================
#  GAME 3 — Hangman
# =====================================================================
def jogo_hangman(parent):
    WORDS = ["window", "platypus", "building", "mirror", "california",
             "civilization", "invitation", "puzzle", "extremely"]
    MAX_ATTEMPTS = 8

    game_state = {"word": "", "guessed": set(), "attempts": MAX_ATTEMPTS, "playing": False}

    root = tk.Toplevel(parent)
    root.title("🎯 Hangman Game")
    root.geometry("500x750")
    root.configure(bg="#1e1e2e")
    root.resizable(False, False)

    tk.Label(root, text="🎯 Guess the Word",
             font=("Segoe UI", 22, "bold"),
             bg="#1e1e2e", fg="#f5c2e7").pack(pady=15)

    word_display = tk.Label(root, text="_ _ _ _ _",
                            font=("Consolas", 28, "bold"),
                            bg="#1e1e2e", fg="#89b4fa")
    word_display.pack(pady=15)

    stats_frame = tk.Frame(root, bg="#181825")
    stats_frame.pack(pady=8, padx=20, fill="x")

    attempts_label = tk.Label(stats_frame, text=f"Attempts: {MAX_ATTEMPTS}",
                              font=("Segoe UI", 14, "bold"),
                              bg="#181825", fg="#f9e2af")
    attempts_label.pack(side="left", expand=True, pady=12)

    letters_label = tk.Label(stats_frame, text="Used letters: —",
                             font=("Segoe UI", 12),
                             bg="#181825", fg="#a6e3a1")
    letters_label.pack(side="left", expand=True, pady=12)

    canvas = tk.Canvas(root, width=200, height=200,
                       bg="#1e1e2e", highlightthickness=0)
    canvas.pack(pady=10)

    def draw_hangman(wrong):
        canvas.delete("all")
        canvas.create_line(30, 180, 170, 180, fill="#cdd6f4", width=3)
        canvas.create_line(60, 180, 60, 30, fill="#cdd6f4", width=3)
        canvas.create_line(60, 30, 140, 30, fill="#cdd6f4", width=3)
        canvas.create_line(140, 30, 140, 55, fill="#cdd6f4", width=3)
        if wrong >= 1:
            canvas.create_oval(120, 55, 160, 95, outline="#f38ba8", width=3)
        if wrong >= 2:
            canvas.create_line(140, 95, 140, 145, fill="#f38ba8", width=3)
        if wrong >= 3:
            canvas.create_line(140, 110, 115, 130, fill="#f38ba8", width=3)
        if wrong >= 4:
            canvas.create_line(140, 110, 165, 130, fill="#f38ba8", width=3)
        if wrong >= 5:
            canvas.create_line(140, 145, 115, 175, fill="#f38ba8", width=3)
        if wrong >= 6:
            canvas.create_line(140, 145, 165, 175, fill="#f38ba8", width=3)
        if wrong >= 7:
            canvas.create_line(128, 68, 136, 76, fill="#f38ba8", width=2)
            canvas.create_line(136, 68, 128, 76, fill="#f38ba8", width=2)
        if wrong >= 8:
            canvas.create_line(144, 68, 152, 76, fill="#f38ba8", width=2)
            canvas.create_line(152, 68, 144, 76, fill="#f38ba8", width=2)

    status_label = tk.Label(root, text="Click 'New Game' to start!",
                            font=("Segoe UI", 12), bg="#1e1e2e", fg="#cba6f7",
                            wraplength=440, justify="center")
    status_label.pack(pady=10)

    keyboard_frame = tk.Frame(root, bg="#1e1e2e")
    keyboard_frame.pack(pady=10)

    letter_buttons = {}

    def make_letter_button(letter):
        btn = tk.Button(keyboard_frame, text=letter.upper(),
                        font=("Segoe UI", 11, "bold"),
                        width=3, height=1, bd=0,
                        bg="#313244", fg="#cdd6f4",
                        activebackground="#f5c2e7", cursor="hand2",
                        command=lambda l=letter: guess_letter(l))
        letter_buttons[letter] = btn

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i, letter in enumerate(alphabet):
        make_letter_button(letter)
        letter_buttons[letter].grid(row=i // 9, column=i % 9, padx=2, pady=2)

    def update_display():
        display = " ".join(c.upper() if c in game_state["guessed"] else "_"
                           for c in game_state["word"])
        word_display.config(text=display)

    def update_letter_styles():
        for letter, btn in letter_buttons.items():
            if letter in game_state["guessed"]:
                if letter in game_state["word"]:
                    btn.config(bg="#a6e3a1", fg="#1e1e2e", state="disabled")
                else:
                    btn.config(bg="#f38ba8", fg="#1e1e2e", state="disabled")
            else:
                btn.config(bg="#313244", fg="#cdd6f4", state="normal")

    def guess_letter(letter):
        if not game_state["playing"] or letter in game_state["guessed"]:
            return
        game_state["guessed"].add(letter)
        if letter not in game_state["word"]:
            game_state["attempts"] -= 1
            attempts_label.config(text=f"Attempts: {game_state['attempts']}")
        update_display()
        update_letter_styles()
        used = ", ".join(sorted(l.upper() for l in game_state["guessed"]))
        letters_label.config(text=f"Letters: {used}")

        if all(c in game_state["guessed"] for c in game_state["word"]):
            game_state["playing"] = False
            status_label.config(text=f"🎉 You won! The word was \"{game_state['word'].upper()}\".",
                                fg="#a6e3a1")
            for btn in letter_buttons.values():
                btn.config(state="disabled")
            return
        if game_state["attempts"] <= 0:
            game_state["playing"] = False
            wrong = MAX_ATTEMPTS - game_state["attempts"]
            draw_hangman(wrong)
            status_label.config(
                text=f"💥 Out of attempts! The word was \"{game_state['word'].upper()}\".",
                fg="#f38ba8")
            for btn in letter_buttons.values():
                btn.config(state="disabled")
            return
        wrong = MAX_ATTEMPTS - game_state["attempts"]
        draw_hangman(wrong)

    def new_game():
        game_state["word"] = random.choice(WORDS)
        game_state["guessed"] = set()
        game_state["attempts"] = MAX_ATTEMPTS
        game_state["playing"] = True
        attempts_label.config(text=f"Attempts: {MAX_ATTEMPTS}")
        letters_label.config(text="Letters: —")
        status_label.config(text="Pick a letter!", fg="#cba6f7")
        canvas.delete("all")
        draw_hangman(0)
        for btn in letter_buttons.values():
            btn.config(state="normal", bg="#313244", fg="#cdd6f4")
        update_display()

    tk.Button(root, text="🔄 New Game",
              font=("Segoe UI", 13, "bold"),
              bg="#89b4fa", fg="#1e1e2e",
              bd=0, padx=20, pady=10,
              cursor="hand2", activebackground="#f5c2e7",
              command=new_game).pack(pady=15)

    draw_hangman(0)


# =====================================================================
#  GAME 4 — Guess the Number
# =====================================================================
def jogo_guess(parent):
    game_state = {"number": 0, "attempts": 0, "min_range": 1,
                  "max_range": 50, "playing": False}

    root = tk.Toplevel(parent)
    root.title("🔢 Guess the Number")
    root.geometry("560x760")
    root.configure(bg="#1e1e2e")
    root.resizable(False, False)

    tk.Label(root, text="🔢 Guess the Number",
             font=("Segoe UI", 22, "bold"),
             bg="#1e1e2e", fg="#f5c2e7").pack(pady=15)

    tk.Label(root, text="I'm thinking of a number between 1 and 50!",
             font=("Segoe UI", 13),
             bg="#1e1e2e", fg="#cdd6f4").pack(pady=5)

    feedback_label = tk.Label(root, text="❓",
                              font=("Segoe UI", 70, "bold"),
                              bg="#1e1e2e", fg="#f9e2af")
    feedback_label.pack(pady=10)

    feedback_text = tk.Label(root, text="Click 'New Game' to start!",
                             font=("Segoe UI", 14),
                             bg="#1e1e2e", fg="#cba6f7",
                             wraplength=400, justify="center")
    feedback_text.pack(pady=5)

    stats_frame = tk.Frame(root, bg="#181825")
    stats_frame.pack(pady=15, padx=20, fill="x")

    attempts_label = tk.Label(stats_frame, text="Attempts: 0",
                              font=("Segoe UI", 14, "bold"),
                              bg="#181825", fg="#89b4fa")
    attempts_label.pack(side="left", expand=True, pady=12)

    range_label = tk.Label(stats_frame, text="Range: 1 – 50",
                           font=("Segoe UI", 14, "bold"),
                           bg="#181825", fg="#a6e3a1")
    range_label.pack(side="left", expand=True, pady=12)

    entry_frame = tk.Frame(root, bg="#1e1e2e")
    entry_frame.pack(pady=15)

    guess_entry = tk.Entry(entry_frame, font=("Segoe UI", 20, "bold"),
                           width=6, justify="center",
                           bg="#313244", fg="#cdd6f4",
                           insertbackground="#cdd6f4", bd=0)
    guess_entry.pack(side="left", padx=8, ipady=8)
    guess_entry.bind("<Return>", lambda e: submit_guess())

    submit_btn = tk.Button(entry_frame, text="Submit",
                           font=("Segoe UI", 13, "bold"),
                           bg="#89b4fa", fg="#1e1e2e",
                           bd=0, padx=15, pady=8,
                           cursor="hand2", activebackground="#f5c2e7",
                           command=lambda: submit_guess())
    submit_btn.pack(side="left", padx=8)

    tk.Label(root, text="History:", font=("Segoe UI", 11, "italic"),
             bg="#1e1e2e", fg="#a6adc8").pack(pady=(10, 3))

    history_box = tk.Text(root, height=6, width=45, font=("Consolas", 11),
                          bg="#313244", fg="#cdd6f4", bd=0,
                          padx=10, pady=8, wrap="word")
    history_box.pack(pady=5)
    history_box.config(state="disabled")

    def log_history(text):
        history_box.config(state="normal")
        history_box.insert("end", text + "\n")
        history_box.see("end")
        history_box.config(state="disabled")

    def clear_history():
        history_box.config(state="normal")
        history_box.delete("1.0", "end")
        history_box.config(state="disabled")

    def new_game():
        game_state["number"] = random.randint(1, 50)
        game_state["attempts"] = 0
        game_state["playing"] = True
        feedback_label.config(text="❓", fg="#f9e2af")
        feedback_text.config(text="Make your guess!", fg="#cba6f7")
        attempts_label.config(text="Attempts: 0")
        range_label.config(text="Range: 1 – 50")
        clear_history()
        log_history("--- New Game (1 to 50) ---")
        guess_entry.delete(0, "end")
        guess_entry.config(state="normal")
        submit_btn.config(state="normal")
        guess_entry.focus()

    def submit_guess():
        if not game_state["playing"]:
            return
        raw = guess_entry.get().strip()
        try:
            guess = int(raw)
        except ValueError:
            feedback_label.config(text="⚠️", fg="#f38ba8")
            feedback_text.config(text="Please enter a whole number.", fg="#f38ba8")
            guess_entry.delete(0, "end")
            return
        if guess < game_state["min_range"] or guess > game_state["max_range"]:
            feedback_label.config(text="⚠️", fg="#f38ba8")
            feedback_text.config(
                text=f"The number is between {game_state['min_range']} and {game_state['max_range']}.",
                fg="#f38ba8")
            guess_entry.delete(0, "end")
            return
        game_state["attempts"] += 1
        attempts_label.config(text=f"Attempts: {game_state['attempts']}")
        number = game_state["number"]
        if guess < number:
            feedback_label.config(text="⬆️", fg="#89b4fa")
            feedback_text.config(text=f"{guess} is too LOW!", fg="#89b4fa")
            log_history(f"#{game_state['attempts']}: {guess} → ⬆️ too low")
        elif guess > number:
            feedback_label.config(text="⬇️", fg="#f9e2af")
            feedback_text.config(text=f"{guess} is too HIGH!", fg="#f9e2af")
            log_history(f"#{game_state['attempts']}: {guess} → ⬇️ too high")
        else:
            feedback_label.config(text="🎉", fg="#a6e3a1")
            feedback_text.config(
                text=f"Correct! You got it in {game_state['attempts']} attempts!",
                fg="#a6e3a1")
            log_history(f"#{game_state['attempts']}: {guess} → 🎉 CORRECT!")
            game_state["playing"] = False
            submit_btn.config(state="disabled")
            guess_entry.config(state="disabled")
        guess_entry.delete(0, "end")
        guess_entry.focus()

    tk.Button(root, text="🔄 New Game",
              font=("Segoe UI", 13, "bold"),
              bg="#a6e3a1", fg="#1e1e2e",
              bd=0, padx=20, pady=10,
              cursor="hand2", activebackground="#f5c2e7",
              command=new_game).pack(pady=15)

    guess_entry.config(state="disabled")
    submit_btn.config(state="disabled")


# =====================================================================
#  GAME 5 — Coin Flip
# =====================================================================
def jogo_coin(parent):
    game_state = {"score": 0, "wins": 0, "losses": 0,
                  "playing": True, "flipping": False}

    root = tk.Toplevel(parent)
    root.title("👑 Heads or 🦅 Tails")
    root.geometry("580x800")
    root.configure(bg="#1e1e2e")
    root.resizable(False, False)

    tk.Label(root, text="👑 Heads or 🦅 Tails",
             font=("Segoe UI", 22, "bold"),
             bg="#1e1e2e", fg="#f5c2e7").pack(pady=15)

    tk.Label(root, text="Place your bet and flip the coin!",
             font=("Segoe UI", 13),
             bg="#1e1e2e", fg="#cdd6f4").pack(pady=5)

    canvas = tk.Canvas(root, width=180, height=180,
                       bg="#1e1e2e", highlightthickness=0)
    canvas.pack(pady=15)

    def draw_coin(face=None):
        canvas.delete("all")
        canvas.create_oval(20, 20, 160, 160, fill="#f9e2af",
                           outline="#fab387", width=4)
        canvas.create_oval(35, 35, 145, 145, outline="#fab387", width=2)
        if face == "heads":
            canvas.create_text(90, 90, text="👑", font=("Segoe UI", 55))
            canvas.create_text(90, 140, text="HEADS",
                               font=("Segoe UI", 11, "bold"), fill="#7f6000")
        elif face == "tails":
            canvas.create_text(90, 90, text="🦅", font=("Segoe UI", 55))
            canvas.create_text(90, 140, text="TAILS",
                               font=("Segoe UI", 11, "bold"), fill="#7f6000")
        else:
            canvas.create_text(90, 90, text="❓",
                               font=("Segoe UI", 55, "bold"), fill="#7f6000")

    draw_coin()

    result_label = tk.Label(root, text="Choose HEADS or TAILS!",
                            font=("Segoe UI", 14, "bold"),
                            bg="#1e1e2e", fg="#cba6f7",
                            wraplength=420, justify="center")
    result_label.pack(pady=10)

    stats_frame = tk.Frame(root, bg="#181825")
    stats_frame.pack(pady=10, padx=20, fill="x")

    score_label = tk.Label(stats_frame, text="Score: 0",
                           font=("Segoe UI", 14, "bold"),
                           bg="#181825", fg="#89b4fa")
    score_label.pack(side="left", expand=True, pady=12)

    wins_label = tk.Label(stats_frame, text="✅ 0",
                          font=("Segoe UI", 14, "bold"),
                          bg="#181825", fg="#a6e3a1")
    wins_label.pack(side="left", expand=True, pady=12)

    losses_label = tk.Label(stats_frame, text="❌ 0",
                            font=("Segoe UI", 14, "bold"),
                            bg="#181825", fg="#f38ba8")
    losses_label.pack(side="left", expand=True, pady=12)

    bet_frame = tk.Frame(root, bg="#1e1e2e")
    bet_frame.pack(pady=15)

    bet_style = {
        "font": ("Segoe UI", 14, "bold"),
        "bd": 0, "fg": "#1e1e2e",
        "activebackground": "#f5c2e7",
        "cursor": "hand2",
        "width": 10, "pady": 14,
    }

    heads_btn = tk.Button(bet_frame, text="👑 HEADS", bg="#f9e2af",
                          command=lambda: play("heads"), **bet_style)
    heads_btn.grid(row=0, column=0, padx=8)

    tails_btn = tk.Button(bet_frame, text="🦅 TAILS", bg="#cba6f7",
                          command=lambda: play("tails"), **bet_style)
    tails_btn.grid(row=0, column=1, padx=8)

    tk.Label(root, text="History:", font=("Segoe UI", 11, "italic"),
             bg="#1e1e2e", fg="#a6adc8").pack(pady=(10, 3))

    history_box = tk.Text(root, height=6, width=48, font=("Consolas", 10),
                          bg="#313244", fg="#cdd6f4", bd=0,
                          padx=10, pady=8, wrap="word")
    history_box.pack(pady=5)
    history_box.config(state="disabled")

    control_frame = tk.Frame(root, bg="#1e1e2e")
    control_frame.pack(pady=12)

    def log_history(text):
        history_box.config(state="normal")
        history_box.insert("end", text + "\n")
        history_box.see("end")
        history_box.config(state="disabled")

    def clear_history():
        history_box.config(state="normal")
        history_box.delete("1.0", "end")
        history_box.config(state="disabled")

    def update_stats():
        score_label.config(text=f"Score: {game_state['score']}")
        wins_label.config(text=f"✅ {game_state['wins']}")
        losses_label.config(text=f"❌ {game_state['losses']}")

    def animate_coin(callback, steps=8):
        game_state["flipping"] = True
        faces = [None, "heads", "tails", None, "heads", "tails", None, "heads"]

        def step(i):
            if i >= steps:
                callback()
                return
            draw_coin(faces[i % len(faces)])
            root.after(80, lambda: step(i + 1))

        step(0)

    def play(call):
        if game_state["flipping"]:
            return
        heads_btn.config(state="disabled")
        tails_btn.config(state="disabled")
        result_label.config(text="The coin is spinning...", fg="#f9e2af")

        def finish():
            result = random.choice(["heads", "tails"])
            draw_coin(result)
            call_en = "HEADS" if call == "heads" else "TAILS"
            result_en = "HEADS" if result == "heads" else "TAILS"
            if call == result:
                game_state["score"] += 1
                game_state["wins"] += 1
                result_label.config(text=f"It's {result_en}! You won! 🎉", fg="#a6e3a1")
                log_history(f"You bet {call_en} → got {result_en} → ✅ +1")
            else:
                game_state["score"] -= 1
                game_state["losses"] += 1
                result_label.config(text=f"It's {result_en}! You lost. 😢", fg="#f38ba8")
                log_history(f"You bet {call_en} → got {result_en} → ❌ -1")
            update_stats()
            game_state["flipping"] = False
            heads_btn.config(state="normal")
            tails_btn.config(state="normal")

        animate_coin(finish)

    def reset_game():
        game_state["score"] = 0
        game_state["wins"] = 0
        game_state["losses"] = 0
        game_state["playing"] = True
        game_state["flipping"] = False
        update_stats()
        draw_coin()
        result_label.config(text="Choose HEADS or TAILS!", fg="#cba6f7")
        clear_history()
        heads_btn.config(state="normal")
        tails_btn.config(state="normal")

    def quit_game():
        if messagebox.askyesno("Quit", f"Final score: {game_state['score']}\nAre you sure you want to quit?", parent=root):
            root.destroy()

    tk.Button(control_frame, text="🔄 Reset",
              font=("Segoe UI", 12, "bold"),
              bg="#89b4fa", fg="#1e1e2e",
              bd=0, padx=18, pady=8,
              cursor="hand2", activebackground="#f5c2e7",
              command=reset_game).grid(row=0, column=0, padx=6)

    tk.Button(control_frame, text="🚪 Quit",
              font=("Segoe UI", 12, "bold"),
              bg="#f38ba8", fg="#1e1e2e",
              bd=0, padx=18, pady=8,
              cursor="hand2", activebackground="#f5c2e7",
              command=quit_game).grid(row=0, column=1, padx=6)

    update_stats()


# =====================================================================
#  GAME 6 — Blackjack
# =====================================================================
def jogo_blackjack(parent):
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♠", "♥", "♦", "♣"]

    game_state = {"deck": [], "player": [], "dealer": [], "playing": False,
                  "dealer_revealed": False, "wins": 0, "losses": 0, "pushes": 0}

    def make_deck():
        deck = [(r, s) for r in RANKS for s in SUITS]
        random.shuffle(deck)
        return deck

    def card_value(card):
        rank = card[0]
        if rank in ("J", "Q", "K"):
            return 10
        if rank == "A":
            return 11
        return int(rank)

    def hand_value(hand):
        total = sum(card_value(c) for c in hand)
        aces = sum(1 for c in hand if c[0] == "A")
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    root = tk.Toplevel(parent)
    root.title("🃏 Blackjack")
    root.geometry("750x750")
    root.configure(bg="#0b3d2e")
    root.resizable(False, False)

    tk.Label(root, text="🃏 BLACKJACK",
             font=("Segoe UI", 22, "bold"),
             bg="#0b3d2e", fg="#f9e2af").pack(pady=10)

    score_frame = tk.Frame(root, bg="#082a1f")
    score_frame.pack(pady=5, padx=20, fill="x")

    wins_label = tk.Label(score_frame, text="✅ 0", font=("Segoe UI", 13, "bold"),
                          bg="#082a1f", fg="#a6e3a1")
    wins_label.pack(side="left", expand=True, pady=8)

    losses_label = tk.Label(score_frame, text="❌ 0", font=("Segoe UI", 13, "bold"),
                            bg="#082a1f", fg="#f38ba8")
    losses_label.pack(side="left", expand=True, pady=8)

    pushes_label = tk.Label(score_frame, text="🤝 0", font=("Segoe UI", 13, "bold"),
                            bg="#082a1f", fg="#f9e2af")
    pushes_label.pack(side="left", expand=True, pady=8)

    tk.Label(root, text="DEALER", font=("Segoe UI", 12, "bold"),
             bg="#0b3d2e", fg="#cdd6f4").pack(pady=(15, 5))
    dealer_frame = tk.Frame(root, bg="#0b3d2e", height=150)
    dealer_frame.pack()
    dealer_total_label = tk.Label(root, text="Total: ?",
                                  font=("Segoe UI", 13, "bold"),
                                  bg="#0b3d2e", fg="#f9e2af")
    dealer_total_label.pack(pady=5)

    tk.Label(root, text="YOU", font=("Segoe UI", 12, "bold"),
             bg="#0b3d2e", fg="#cdd6f4").pack(pady=(15, 5))
    player_frame = tk.Frame(root, bg="#0b3d2e", height=150)
    player_frame.pack()
    player_total_label = tk.Label(root, text="Total: 0",
                                  font=("Segoe UI", 13, "bold"),
                                  bg="#0b3d2e", fg="#a6e3a1")
    player_total_label.pack(pady=5)

    message_label = tk.Label(root, text="Click 'New Hand' to start!",
                             font=("Segoe UI", 14, "bold"),
                             bg="#0b3d2e", fg="#f5c2e7",
                             wraplength=580, justify="center")
    message_label.pack(pady=15)

    button_frame = tk.Frame(root, bg="#0b3d2e")
    button_frame.pack(pady=10)

    btn_style = {"font": ("Segoe UI", 13, "bold"), "bd": 0, "fg": "#0b3d2e",
                 "activebackground": "#f5c2e7", "cursor": "hand2",
                 "width": 11, "pady": 12}

    def draw_card(parent_widget, card, hidden=False):
        c = tk.Canvas(parent_widget, width=100, height=145, bg="white",
                      highlightthickness=2, highlightbackground="#333")
        c.pack(side="left", padx=6)
        if hidden:
            c.create_rectangle(2, 2, 98, 143, fill="#2b5fa8", outline="")
            c.create_text(50, 72, text="🂠", font=("Segoe UI", 46), fill="white")
            return c
        rank, suit = card
        color = "#c0392b" if suit in ("♥", "♦") else "#1a1a1a"
        c.create_text(10, 10, text=rank, font=("Segoe UI", 14, "bold"),
                      fill=color, anchor="nw")
        c.create_text(10, 32, text=suit, font=("Segoe UI", 14), fill=color, anchor="nw")
        c.create_text(50, 78, text=suit, font=("Segoe UI", 40), fill=color, anchor="center")
        c.create_text(90, 135, text=rank, font=("Segoe UI", 14, "bold"),
                      fill=color, anchor="se")
        c.create_text(90, 113, text=suit, font=("Segoe UI", 14), fill=color, anchor="se")
        return c

    def render_table():
        for w in dealer_frame.winfo_children():
            w.destroy()
        for w in player_frame.winfo_children():
            w.destroy()
        for i, card in enumerate(game_state["dealer"]):
            hide = (i == 0 and not game_state["dealer_revealed"])
            draw_card(dealer_frame, card, hidden=hide)
        for card in game_state["player"]:
            draw_card(player_frame, card)
        if game_state["dealer_revealed"]:
            dealer_total_label.config(text=f"Total: {hand_value(game_state['dealer'])}")
        else:
            if len(game_state["dealer"]) >= 2:
                visible = hand_value(game_state["dealer"][1:])
                dealer_total_label.config(text=f"Total: {visible} + ?")
            else:
                dealer_total_label.config(text="Total: ?")
        player_total_label.config(text=f"Total: {hand_value(game_state['player'])}")

    def update_scoreboard():
        wins_label.config(text=f"✅ {game_state['wins']}")
        losses_label.config(text=f"❌ {game_state['losses']}")
        pushes_label.config(text=f"🤝 {game_state['pushes']}")

    def set_buttons(state):
        hit_btn.config(state=state)
        stand_btn.config(state=state)

    def new_hand():
        game_state["deck"] = make_deck()
        game_state["player"] = [game_state["deck"].pop(), game_state["deck"].pop()]
        game_state["dealer"] = [game_state["deck"].pop(), game_state["deck"].pop()]
        game_state["playing"] = True
        game_state["dealer_revealed"] = False
        message_label.config(text="Your turn! Hit or Stand?", fg="#f5c2e7")
        render_table()
        set_buttons("normal")
        if hand_value(game_state["player"]) == 21:
            message_label.config(text="🎉 BLACKJACK! Let's see the dealer...", fg="#f9e2af")
            set_buttons("disabled")
            root.after(800, dealer_play)

    def player_hit():
        if not game_state["playing"]:
            return
        game_state["player"].append(game_state["deck"].pop())
        render_table()
        if hand_value(game_state["player"]) > 21:
            message_label.config(
                text=f"💥 Bust! You had {hand_value(game_state['player'])}. Dealer wins.",
                fg="#f38ba8")
            game_state["playing"] = False
            game_state["losses"] += 1
            update_scoreboard()
            set_buttons("disabled")
        elif hand_value(game_state["player"]) == 21:
            message_label.config(text="21! Let's see the dealer...", fg="#f9e2af")
            set_buttons("disabled")
            root.after(600, dealer_play)

    def player_stand():
        if not game_state["playing"]:
            return
        set_buttons("disabled")
        dealer_play()

    def dealer_play():
        game_state["playing"] = False
        game_state["dealer_revealed"] = True
        render_table()

        def draw_next():
            if hand_value(game_state["dealer"]) < 17:
                game_state["dealer"].append(game_state["deck"].pop())
                render_table()
                root.after(700, draw_next)
            else:
                resolve_winner()

        root.after(500, draw_next)

    def resolve_winner():
        p = hand_value(game_state["player"])
        d = hand_value(game_state["dealer"])
        if d > 21:
            message_label.config(text=f"🎉 Dealer bust! You win! ({p} vs {d})", fg="#a6e3a1")
            game_state["wins"] += 1
        elif p > d:
            message_label.config(text=f"🎉 You win! ({p} vs {d})", fg="#a6e3a1")
            game_state["wins"] += 1
        elif p < d:
            message_label.config(text=f"😢 Dealer wins. ({p} vs {d})", fg="#f38ba8")
            game_state["losses"] += 1
        else:
            message_label.config(text=f"🤝 Push! ({p} vs {d})", fg="#f9e2af")
            game_state["pushes"] += 1
        update_scoreboard()

    hit_btn = tk.Button(button_frame, text="🃏 Hit", bg="#a6e3a1",
                        command=player_hit, **btn_style)
    hit_btn.grid(row=0, column=0, padx=6)

    stand_btn = tk.Button(button_frame, text="✋ Stand", bg="#f9e2af",
                          command=player_stand, **btn_style)
    stand_btn.grid(row=0, column=1, padx=6)

    tk.Button(button_frame, text="🔄 New Hand", bg="#89b4fa",
              command=new_hand, **btn_style).grid(row=0, column=2, padx=6)

    update_scoreboard()
    set_buttons("disabled")


# =====================================================================
#  GAME 7 — Battleship
# =====================================================================
def jogo_battleship(parent):
    SIZE = 10
    LETTERS = "ABCDEFGHIJ"
    COLUMNS = [str(i) for i in range(1, 11)]
    FLEET = [(4, 1), (3, 2), (2, 3), (1, 4)]
    TOTAL_SHIP_CELLS = sum(length * count for length, count in FLEET)

    game_state = {"ship": set(), "hits": 0, "misses": 0, "shots": 0,
                  "playing": False, "wins": 0, "losses": 0, "buttons": {}}

    def can_place(ship_cells, occupied):
        for (r, c) in ship_cells:
            if not (0 <= r < SIZE and 0 <= c < SIZE):
                return False
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if (r + dr, c + dc) in occupied:
                        return False
        return True

    def place_fleet():
        occupied = set()
        for length, count in FLEET:
            for _ in range(count):
                placed = False
                attempts = 0
                while not placed and attempts < 3000:
                    attempts += 1
                    orientation = random.choice(["h", "v"])
                    if orientation == "h":
                        row = random.randint(0, SIZE - 1)
                        col = random.randint(0, SIZE - length)
                        cells = [(row, col + i) for i in range(length)]
                    else:
                        row = random.randint(0, SIZE - length)
                        col = random.randint(0, SIZE - 1)
                        cells = [(row + i, col) for i in range(length)]
                    if can_place(cells, occupied):
                        for cell in cells:
                            occupied.add(cell)
                        placed = True
                if not placed:
                    return place_fleet()
        return occupied

    root = tk.Toplevel(parent)
    root.title("🚢 Battleship")
    root.geometry("820x920")
    root.configure(bg="#0a192f")
    root.resizable(False, False)

    tk.Label(root, text="🚢 BATTLESHIP", font=("Segoe UI", 20, "bold"),
             bg="#0a192f", fg="#64ffda").pack(pady=8)

    tk.Label(root, text=f"Sink the whole fleet on a {SIZE}×{SIZE} sea",
             font=("Segoe UI", 12), bg="#0a192f", fg="#ccd6f6").pack(pady=2)

    fleet_text = "Fleet:   " + "   ".join(f"{count}×{length}" for length, count in FLEET)
    tk.Label(root, text=fleet_text, font=("Segoe UI", 11, "italic"),
             bg="#0a192f", fg="#8892b0").pack(pady=2)

    score_frame = tk.Frame(root, bg="#112240")
    score_frame.pack(pady=8, padx=20, fill="x")

    wins_label = tk.Label(score_frame, text="✅ 0", font=("Segoe UI", 13, "bold"),
                          bg="#112240", fg="#64ffda")
    wins_label.pack(side="left", expand=True, pady=8)

    losses_label = tk.Label(score_frame, text="❌ 0", font=("Segoe UI", 13, "bold"),
                            bg="#112240", fg="#ff6b6b")
    losses_label.pack(side="left", expand=True, pady=8)

    shots_label = tk.Label(score_frame, text="🎯 0", font=("Segoe UI", 13, "bold"),
                           bg="#112240", fg="#ffd93d")
    shots_label.pack(side="left", expand=True, pady=8)

    board_frame = tk.Frame(root, bg="#0a192f")
    board_frame.pack(pady=12)

    for c in range(SIZE):
        tk.Label(board_frame, text=COLUMNS[c], font=("Segoe UI", 11, "bold"),
                 bg="#0a192f", fg="#8892b0", width=3).grid(row=0, column=c + 1, pady=4)

    for r in range(SIZE):
        tk.Label(board_frame, text=LETTERS[r], font=("Segoe UI", 11, "bold"),
                 bg="#0a192f", fg="#8892b0", width=3).grid(row=r + 1, column=0)
        for c in range(SIZE):
            btn = tk.Button(board_frame, text="🌊",
                            font=("Segoe UI", 12),
                            width=2, height=1, bd=0,
                            bg="#1e3a5f", fg="white",
                            activebackground="#64ffda", cursor="hand2",
                            command=lambda rr=r, cc=c: shoot(rr, cc))
            btn.grid(row=r + 1, column=c + 1, padx=2, pady=2, ipadx=5, ipady=5)
            game_state["buttons"][(r, c)] = btn

    status_label = tk.Label(root, text="Click 'New Game' to start!",
                            font=("Segoe UI", 13, "bold"),
                            bg="#0a192f", fg="#64ffda",
                            wraplength=760, justify="center")
    status_label.pack(pady=10)

    progress_label = tk.Label(root, text=f"Hits: 0 / {TOTAL_SHIP_CELLS}",
                              font=("Segoe UI", 12),
                              bg="#0a192f", fg="#ccd6f6")
    progress_label.pack(pady=2)

    button_frame = tk.Frame(root, bg="#0a192f")
    button_frame.pack(pady=12)

    btn_style = {"font": ("Segoe UI", 12, "bold"), "bd": 0, "fg": "#0a192f",
                 "activebackground": "#ffffff", "cursor": "hand2",
                 "padx": 18, "pady": 10}

    def update_scoreboard():
        wins_label.config(text=f"✅ {game_state['wins']}")
        losses_label.config(text=f"❌ {game_state['losses']}")
        shots_label.config(text=f"🎯 {game_state['shots']}")
        progress_label.config(text=f"Hits: {game_state['hits']} / {TOTAL_SHIP_CELLS}")

    def disable_board():
        for btn in game_state["buttons"].values():
            btn.config(state="disabled")

    def enable_board():
        for btn in game_state["buttons"].values():
            btn.config(state="normal", text="🌊", bg="#1e3a5f", fg="white")

    def new_game():
        game_state["ship"] = place_fleet()
        game_state["hits"] = 0
        game_state["misses"] = 0
        game_state["shots"] = 0
        game_state["playing"] = True
        enable_board()
        update_scoreboard()
        status_label.config(text="Take your first shot! 🎯", fg="#64ffda")

    def shoot(r, c):
        if not game_state["playing"]:
            return
        btn = game_state["buttons"][(r, c)]
        if btn["state"] == "disabled":
            return
        game_state["shots"] += 1
        if (r, c) in game_state["ship"]:
            btn.config(text="💥", bg="#ff6b6b", fg="white", state="disabled")
            game_state["hits"] += 1
            status_label.config(
                text=f"💥 HIT at {LETTERS[r]}{COLUMNS[c]}! ({game_state['hits']}/{TOTAL_SHIP_CELLS})",
                fg="#64ffda")
            if game_state["hits"] >= TOTAL_SHIP_CELLS:
                game_state["playing"] = False
                game_state["wins"] += 1
                status_label.config(
                    text=f"🎉 You sank the whole fleet in {game_state['shots']} shots!",
                    fg="#64ffda")
                disable_board()
        else:
            btn.config(text="⚪", bg="#0a192f", fg="#8892b0", state="disabled")
            game_state["misses"] += 1
            status_label.config(text=f"💧 Water at {LETTERS[r]}{COLUMNS[c]}! Try again.",
                                fg="#8892b0")
        update_scoreboard()

    def reveal_ship():
        if game_state["playing"]:
            if not messagebox.askyesno("Reveal", "Revealing the fleet counts as a loss. Continue?", parent=root):
                return
            game_state["playing"] = False
            game_state["losses"] += 1
            update_scoreboard()
        for (r, c) in game_state["ship"]:
            btn = game_state["buttons"][(r, c)]
            if btn["state"] != "disabled":
                btn.config(text="🚢", bg="#ffd93d", fg="#0a192f", state="disabled")
            else:
                btn.config(text="💥", bg="#ff6b6b", fg="white")
        disable_board()
        status_label.config(text="👁️ Fleet revealed!", fg="#ffd93d")

    def quit_game():
        if messagebox.askyesno("Quit",
                               f"Shots: {game_state['shots']}\nHits: {game_state['hits']}\nAre you sure you want to quit?",
                               parent=root):
            root.destroy()

    tk.Button(button_frame, text="🔄 New Game", bg="#64ffda",
              command=new_game, **btn_style).grid(row=0, column=0, padx=6)
    tk.Button(button_frame, text="👁️ Reveal", bg="#ffd93d",
              command=reveal_ship, **btn_style).grid(row=0, column=1, padx=6)
    tk.Button(button_frame, text="🚪 Quit", bg="#ff6b6b",
              command=quit_game, **btn_style).grid(row=0, column=2, padx=6)

    update_scoreboard()
    disable_board()


# =====================================================================
#  GAME 8 — Memory Match
# =====================================================================
def jogo_memory(parent):
    SYMBOLS = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊",
               "🐻", "🐼", "🐨", "🐯", "🦁", "🐮",
               "🐸", "🐵", "🐔", "🐧", "🍎", "🍌"]
    ROWS = 6
    COLS = 6
    LETTERS = "ABCDEF"
    COLUMNS = [str(i) for i in range(1, 7)]

    game_state = {"grid": [], "revealed": set(), "matched": set(),
                  "attempts": 0, "first_pick": None, "lock": False,
                  "playing": False, "wins": 0, "losses": 0, "buttons": {}}

    def make_grid():
        cards = SYMBOLS * 2
        random.shuffle(cards)
        return [cards[i * COLS:(i + 1) * COLS] for i in range(ROWS)]

    root = tk.Toplevel(parent)
    root.title("🧠 Memory Game")
    root.geometry("760x900")
    root.configure(bg="#1a1a2e")
    root.resizable(False, False)

    tk.Label(root, text="🧠 MEMORY GAME", font=("Segoe UI", 22, "bold"),
             bg="#1a1a2e", fg="#e94560").pack(pady=12)

    tk.Label(root, text=f"Find all {len(SYMBOLS)} pairs!",
             font=("Segoe UI", 12),
             bg="#1a1a2e", fg="#cdd6f4").pack(pady=4)

    score_frame = tk.Frame(root, bg="#16213e")
    score_frame.pack(pady=10, padx=20, fill="x")

    wins_label = tk.Label(score_frame, text="✅ 0", font=("Segoe UI", 13, "bold"),
                          bg="#16213e", fg="#a6e3a1")
    wins_label.pack(side="left", expand=True, pady=8)

    losses_label = tk.Label(score_frame, text="❌ 0", font=("Segoe UI", 13, "bold"),
                            bg="#16213e", fg="#f38ba8")
    losses_label.pack(side="left", expand=True, pady=8)

    attempts_label = tk.Label(score_frame, text="🎯 0", font=("Segoe UI", 13, "bold"),
                              bg="#16213e", fg="#f9e2af")
    attempts_label.pack(side="left", expand=True, pady=8)

    pairs_label = tk.Label(score_frame, text=f"🃏 0 / {len(SYMBOLS)}",
                           font=("Segoe UI", 13, "bold"),
                           bg="#16213e", fg="#89b4fa")
    pairs_label.pack(side="left", expand=True, pady=8)

    board_frame = tk.Frame(root, bg="#1a1a2e")
    board_frame.pack(pady=15)

    for c in range(COLS):
        tk.Label(board_frame, text=COLUMNS[c], font=("Segoe UI", 11, "bold"),
                 bg="#1a1a2e", fg="#8892b0", width=4).grid(row=0, column=c + 1, pady=3)

    for r in range(ROWS):
        tk.Label(board_frame, text=LETTERS[r], font=("Segoe UI", 11, "bold"),
                 bg="#1a1a2e", fg="#8892b0", width=3).grid(row=r + 1, column=0)
        for c in range(COLS):
            btn = tk.Button(board_frame, text="?",
                            font=("Segoe UI Emoji", 20),
                            width=3, height=1, bd=0,
                            bg="#0f3460", fg="#e94560",
                            activebackground="#e94560", cursor="hand2",
                            command=lambda rr=r, cc=c: click_card(rr, cc))
            btn.grid(row=r + 1, column=c + 1, padx=4, pady=4, ipadx=4, ipady=4)
            game_state["buttons"][(r, c)] = btn

    status_label = tk.Label(root, text="Click 'New Game' to start!",
                            font=("Segoe UI", 13, "bold"),
                            bg="#1a1a2e", fg="#e94560",
                            wraplength=700, justify="center")
    status_label.pack(pady=12)

    button_frame = tk.Frame(root, bg="#1a1a2e")
    button_frame.pack(pady=10)

    btn_style = {"font": ("Segoe UI", 12, "bold"), "bd": 0, "fg": "#1a1a2e",
                 "activebackground": "#e94560", "cursor": "hand2",
                 "padx": 16, "pady": 10}

    def update_scoreboard():
        wins_label.config(text=f"✅ {game_state['wins']}")
        losses_label.config(text=f"❌ {game_state['losses']}")
        attempts_label.config(text=f"🎯 {game_state['attempts']}")
        pairs_done = len(game_state["matched"]) // 2
        pairs_label.config(text=f"🃏 {pairs_done} / {len(SYMBOLS)}")

    def reset_board():
        for btn in game_state["buttons"].values():
            btn.config(text="?", bg="#0f3460", fg="#e94560",
                       font=("Segoe UI Emoji", 20), state="normal")

    def disable_board():
        for btn in game_state["buttons"].values():
            btn.config(state="disabled")

    def new_game():
        game_state["grid"] = make_grid()
        game_state["revealed"] = set()
        game_state["matched"] = set()
        game_state["attempts"] = 0
        game_state["first_pick"] = None
        game_state["lock"] = False
        game_state["playing"] = True
        reset_board()
        update_scoreboard()
        status_label.config(text="Pick the first card!", fg="#e94560")

    def click_card(r, c):
        if not game_state["playing"] or game_state["lock"]:
            return
        if (r, c) in game_state["revealed"] or (r, c) in game_state["matched"]:
            return
        btn = game_state["buttons"][(r, c)]
        card_value = game_state["grid"][r][c]
        btn.config(text=card_value, bg="#f9e2af", fg="#1a1a2e",
                   font=("Segoe UI Emoji", 22))
        game_state["revealed"].add((r, c))

        if game_state["first_pick"] is None:
            game_state["first_pick"] = (r, c)
            status_label.config(text="Pick the second card!", fg="#f9e2af")
            return

        r1, c1 = game_state["first_pick"]
        r2, c2 = r, c
        game_state["attempts"] += 1
        game_state["lock"] = True
        v1 = game_state["grid"][r1][c1]
        v2 = game_state["grid"][r2][c2]

        if v1 == v2:
            game_state["matched"].add((r1, c1))
            game_state["matched"].add((r2, c2))
            game_state["buttons"][(r1, c1)].config(bg="#a6e3a1", state="disabled")
            game_state["buttons"][(r2, c2)].config(bg="#a6e3a1", state="disabled")
            status_label.config(text=f"✅ Pair found! ({v1})", fg="#a6e3a1")
            game_state["first_pick"] = None
            game_state["lock"] = False
            update_scoreboard()
            if len(game_state["matched"]) == ROWS * COLS:
                game_state["playing"] = False
                game_state["wins"] += 1
                status_label.config(
                    text=f"🎉 Congratulations! You completed it in {game_state['attempts']} attempts!",
                    fg="#a6e3a1")
                disable_board()
                update_scoreboard()
        else:
            status_label.config(text=f"❌ Not a pair ({v1} ≠ {v2})...", fg="#f38ba8")

            def hide_cards():
                for (rr, cc) in [(r1, c1), (r2, c2)]:
                    b = game_state["buttons"][(rr, cc)]
                    b.config(text="?", bg="#0f3460", fg="#e94560",
                             font=("Segoe UI Emoji", 20))
                    game_state["revealed"].discard((rr, cc))
                game_state["first_pick"] = None
                game_state["lock"] = False
                status_label.config(text="Try again!", fg="#e94560")

            root.after(900, hide_cards)
            update_scoreboard()

    def quit_game():
        if messagebox.askyesno("Quit",
                               f"Attempts: {game_state['attempts']}\nPairs: {len(game_state['matched'])//2}/{len(SYMBOLS)}\nAre you sure you want to quit?",
                               parent=root):
            root.destroy()

    tk.Button(button_frame, text="🔄 New Game", bg="#e94560",
              command=new_game, **btn_style).grid(row=0, column=0, padx=6)
    tk.Button(button_frame, text="🚪 Quit", bg="#89b4fa",
              command=quit_game, **btn_style).grid(row=0, column=1, padx=6)

    update_scoreboard()
    disable_board()


# =====================================================================
#  MENU
# =====================================================================
GAMES = [
    ("◉ Rock, 📄 Paper, ✂️ Scissors", jogo_rps),
    ("🎲 Dice Roll",                  jogo_dice),
    ("🎯 Hangman",                    jogo_hangman),
    ("🔢 Guess the Number",           jogo_guess),
    ("👑 Coin Flip 🦅",               jogo_coin),
    ("🃏 Blackjack",                  jogo_blackjack),
    ("🚢 Battleship",                 jogo_battleship),
    ("🧠 Memory Match",               jogo_memory),
]


def abrir_jogo(funcao):
    funcao(menu_root)


menu_root = tk.Tk()
menu_root.title("🎮 My Games")
menu_root.geometry("800x800")
menu_root.configure(bg="#1e1e2e")
menu_root.resizable(False, False)

tk.Label(menu_root, text="🎮 MY GAMES",
         font=("Segoe UI", 22, "bold"),
         bg="#1e1e2e", fg="#f5c2e7").pack(pady=20)

tk.Label(menu_root, text="Pick a game to play",
         font=("Segoe UI", 12),
         bg="#1e1e2e", fg="#cdd6f4").pack(pady=(0, 15))

frame = tk.Frame(menu_root, bg="#1e1e2e")
frame.pack(pady=10)

for i, (name, funcao) in enumerate(GAMES):
    btn = tk.Button(
        frame, text=name,
        font=("Segoe UI", 13, "bold"),
        bg="#89b4fa", fg="#1e1e2e",
        bd=0, width=26, pady=12,
        cursor="hand2", activebackground="#f5c2e7",
        command=lambda f=funcao: abrir_jogo(f)
    )
    btn.grid(row=i, column=0, pady=6)

tk.Button(
    menu_root, text="🚪 Quit",
    font=("Segoe UI", 12, "bold"),
    bg="#f38ba8", fg="#1e1e2e",
    bd=0, padx=20, pady=8,
    cursor="hand2", activebackground="#f5c2e7",
    command=menu_root.destroy
).pack(pady=20)

menu_root.mainloop()