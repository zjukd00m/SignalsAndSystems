import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Validator for the 'Degree' input
def only_numbers(char: str):
    """
    Validate if the character sequence has only digits

    Args:
        char (str): the input sequence

    Returns:
        bool: Whether or not the character sequence has only digits
    """
    return char.isdigit()


def polynomial(x, N: int):
    y = np.zeros_like(x)

    for n in range(N + 1):
        y += x**n

    return y


class App(tk.Tk):
    def __init__(self, title: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(title)
        self.resizable(False, False)

        # App title (TOP CENTER)
        self.label_title = tk.Label(
            self, text="Polynomial Functions", font=("Arial", 18)
        )
        self.label_title.grid(row=0, column=0, columnspan=2)

        # Equation that's being plotted
        self.label_plotted_equation = tk.Label(
            self, text=r"$x^2 + x + 1$", font=("Arial", 15)
        )
        self.label_plotted_equation.grid(row=1, column=0, columnspan=2)

        # === Matplotlib setup
        self.graph = plt.figure()
        self.subplot = self.graph.add_subplot(111)

        self.setup_canvas()
        # self.subplot.spines["left"].set_position("center")
        # self.subplot.spines["bottom"].set_position("center")

        self.time_vector = np.arange(-10, 10, 0.01)

        # Canvas where the equations will be plotted
        self.canvas = FigureCanvasTkAgg(self.graph, self)
        self.canvas.get_tk_widget().grid(row=2, column=0, columnspan=2)

        # Graph the y=x equation
        self.subplot.plot(polynomial(x=self.time_vector, N=1))

        # Layout (horizontal)
        self.calculate_btn = tk.Button(
            self,
            text="Calculate",
            font=("Arial", 18),
            command=self.handle_calculate_btn,
        )
        self.calculate_btn.grid(row=3, column=0)

        self.label_polynomial_degree = tk.Label(self, text="Degree")
        self.label_polynomial_degree.grid(row=3, column=1)

        self.entry_polynomial_degree = tk.Entry(
            self, validate="key", validatecommand=(self.register(only_numbers), "%S")
        )
        self.entry_polynomial_degree.grid(row=4, column=1)

        # self.label_polynomial_degree = tk.Label(self, text="Coefficients")
        # self.label_polynomial_degree.grid(row=5, column=1)

    def handle_calculate_btn(self):
        polynomial_degree = self.entry_polynomial_degree.get()

        if not polynomial_degree or int(polynomial_degree) < 0:
            print("This is not valid :c")
            return None

        # Clear the canvas to avoid overlapping of more than one vector
        self.subplot.clear()

        self.subplot.plot(polynomial(x=self.time_vector, N=int(polynomial_degree)))

        self.setup_canvas()

        # Paint the new graph using the new values of the y-axis
        self.graph_it()

    def graph_it(self):
        self.graph.canvas.draw()

    def setup_canvas(self):
        self.subplot.set_xlabel("Time")
        self.subplot.set_ylabel("Y(t)")
        self.subplot.grid()


if __name__ == "__main__":
    app = App("Polynomial Functions")

    app.mainloop()
