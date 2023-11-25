import tkinter as tk


class NQueensGame:
    def __init__(self, master, n=4):
        self.master = master
        self.n = n
        self.master.title("N-Queens Game")

        # Set a fixed initial state
        self.board = [1, 2, 3, 0]

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
                self.canvas.create_rectangle(j * self.canvas_size, i * self.canvas_size, (j + 1) * self.canvas_size, (i + 1) * self.canvas_size, fill=color)
                if j == self.board[i]:
                    self.canvas.create_text((j + 0.5) * self.canvas_size, (i + 0.5) * self.canvas_size,
                                            text="Q", font=("Helvetica", 12), fill="red")

    def solve(self):
        solution = self.hill_climbing()
        if solution:
            self.board = solution
            self.draw_board()

    def reset(self):
        self.board = [1,2,3,0]  # Reset to the fixed initial state
        self.draw_board()

    def initial_solution(self):
        return [1, 2,3,0]  # Set a fixed initial state

    def calculate_attacks(self, queens):
        attacks = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if queens[i] == queens[j] or abs(queens[i] - queens[j]) == abs(i - j):
                    attacks += 1
        return attacks

    def hill_climbing(self):
        iterations = 1000

        for _ in range(iterations):
            current_attacks = self.calculate_attacks(self.board)
            if current_attacks == 0:
                return self.board  # Solution found

            for i in range(self.n):
                for j in range(self.n):
                    if i != j:
                        temp_queens = self.board.copy()
                        temp_queens[i], temp_queens[j] = temp_queens[j], temp_queens[i]
                        new_attacks = self.calculate_attacks(temp_queens)

                        if new_attacks < current_attacks:
                            self.board = temp_queens
                            return temp_queens  # Choose the first step that reduces the number of attacks

        return None  # Solution not found within the iteration limit

def main():
    root = tk.Tk()
    game = NQueensGame(root, n=4)
    root.mainloop()

if __name__ == "__main__":
    main()
