import random
import tkinter as tk
import time


class NQueensGame:
    def __init__(self, master, n=8):
        self.master = master
        self.n = n
        self.master.title("N-Queens Game")

        self.board = [1, 0, 2, 6, 4, 7, 5, 3]

        self.label = tk.Label(master, text="N-Queens Game")
        self.label.pack()

        self.canvas_size = 60
        self.canvas = tk.Canvas(master, width=n * self.canvas_size, height=n * self.canvas_size)
        self.canvas.pack()

        self.draw_board()

        self.solve_button = tk.Button(master, text="Solve", command=self.solve)
        self.solve_button.pack()

        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.pack()

    def draw_board(self):
        self.canvas.delete("all")
        for i in range(self.n):
            for j in range(self.n):
                color = "white" if (i + j) % 2 == 0 else "black"
                self.canvas.create_rectangle(j * self.canvas_size, i * self.canvas_size, (j + 1) * self.canvas_size,
                                             (i + 1) * self.canvas_size, fill=color)
                if j == self.board[i]:
                    self.canvas.create_text((j + 0.5) * self.canvas_size, (i + 0.5) * self.canvas_size,
                                            text="Q", font=("Helvetica", 12), fill="red")

    def solve(self):
        # Mulai mengukur waktu eksekusi
        start_time = time.time()

        solution = self.hill_climbing()

        end_time = time.time()
        execution_time = end_time - start_time

        if solution:
            self.board = solution
            self.draw_board()

        print(f"Waktu Eksekusi solve(): {execution_time} detik")

    def reset(self):
        #self.board = self.initial_solution()
        self.board = [1, 0, 2, 6, 4, 7, 5, 3]
        self.draw_board()

    def initial_solution(self):
        #return random.sample(range(self.n), self.n)  # Solusi awal dengan konfigurasi acak
        return [1, 0, 2, 6, 4, 7, 5, 3]

    def calculate_attacks(self, queens):
        attacks = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(i - j):
                    attacks += 1
        return attacks

    def hill_climbing(self):
        # Mulai mengukur waktu eksekusi
        start_time = time.time()

        iterations = 100

        for _ in range(iterations):
            current_attacks = self.calculate_attacks(self.board)
            if current_attacks == 0:
                # Selesai mengukur waktu eksekusi
                end_time = time.time()
                execution_time = end_time - start_time
                print(f"Waktu Eksekusi hill_climbing(): {execution_time} detik")

                return self.board  # Solusi ditemukan

            for i in range(self.n):
                for j in range(self.n):
                    if i != j:
                        temp_queens = self.board.copy()
                        temp_queens[i], temp_queens[j] = temp_queens[j], temp_queens[i]
                        new_attacks = self.calculate_attacks(temp_queens)

                        if new_attacks < current_attacks:
                            self.board = temp_queens
                            return temp_queens  # Memilih langkah pertama yang mengurangi jumlah serangan

        # Selesai mengukur waktu eksekusi di luar loop
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Waktu Eksekusi hill_climbing(): {execution_time} detik")

        return None  # Solusi tidak ditemukan dalam batas iterasi


def main():
    root = tk.Tk()
    game = NQueensGame(root, n=8)
    root.mainloop()


if __name__ == "__main__":
    main()
