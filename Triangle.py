import matplotlib.pyplot as plt
import numpy as np


class TriangleException(Exception):
    """Custom exception class for errors related to the Triangle class."""


class Triangle:
    """
    A class to represent a triangle.

    Attributes:
        a (float): The length of the first side of the triangle.
        b (float): The length of the second side of the triangle.
        c (float): The length of the third side of the triangle.

    Methods:
        __init__(a, b, c):
            Initializes a Triangle object with three sides and validates the input.
        show():
            Prints the triangle's sides, including the two cathetuses and the hypotenuse.
        __str__():
            Returns a string representation of the triangle.
        isIsosceles():
            Checks if the triangle is isosceles (has at least two equal sides).
        plot():
            Plots the triangle using matplotlib.
    """

    def __init__(self, a, b, c):
        """
        Initializes a Triangle object with three sides.

        Args:
            a (float): The length of the first side.
            b (float): The length of the second side.
            c (float): The length of the third side.

        Raises:
            TriangleException: If any side is non-positive or if the sides do not form a valid triangle.
        """
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
            raise TriangleException(TypeError("Wrong type of parameters. Expected int or float."))
        if a <= 0 or b <= 0 or c <= 0:
            raise TriangleException("Sides must be positive numbers.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise TriangleException("The given sides do not form a valid triangle.")
        self.a = a
        self.b = b
        self.c = c

    def show(self):
        """
        Prints the triangle's sides, including the two cathetuses and the hypotenuse.

        This method assumes the triangle is a right triangle and identifies the hypotenuse
        as the longest side.
        """
        self.plot()
        print(f"Cathetuses: {self.a}, {self.b}; Hypotenuse: {self.c}")

    def __str__(self):
        """
        Returns a string representation of the triangle.

        Returns:
            str: A string describing the triangle's sides.
        """
        return f"Triangle with sides {self.a}, {self.b}, {self.c}"

    def isIsosceles(self) -> bool:
        """
        Checks if the triangle is isosceles.

        An isosceles triangle has at least two sides of equal length.

        Returns:
            bool: True if the triangle is isosceles, False otherwise.
        """
        return self.a == self.b or self.a == self.c or self.b == self.c

    def plot(self):
        """Plots the triangle with correct side lengths, handling all cases."""
        a, b, c = self.a, self.b, self.c

        # Find the longest side and assign points A (0,0) and B (longest, 0)
        sides = [(a, 'a'), (b, 'b'), (c, 'c')]
        longest_side, side_name = max(sides)  # Find the longest side

        # Assign A (0,0) and B (longest_side, 0)
        A = np.array([0, 0])
        B = np.array([longest_side, 0])

        # Calculate the coordinates of C using the law of cosines
        if side_name == 'a':  # Longest side is 'a' → between B and C
            angle = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
            C = np.array([c * np.cos(angle), c * np.sin(angle)])
        elif side_name == 'b':  # Longest side is 'b' → between A and C
            angle = np.arccos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
            C = np.array([a * np.cos(angle), a * np.sin(angle)])
        else:  # Longest side is 'c' → between A and B (standard case)
            angle = np.arccos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
            C = np.array([a * np.cos(angle), a * np.sin(angle)])

        # Plotting
        plt.figure(figsize=(8, 6))
        plt.plot([A[0], B[0]], [A[1], B[1]], 'r-', label=f'Side {side_name}: {longest_side:.2f}')
        plt.plot([A[0], C[0]], [A[1], C[1]], 'g-', label=f'Side {sides[1][1]}: {sides[1][0]:.2f}')
        plt.plot([B[0], C[0]], [B[1], C[1]], 'b-', label=f'Side {sides[2][1]}: {sides[2][0]:.2f}')

        # Annotate vertices
        plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
        plt.text(B[0], B[1], 'B', fontsize=12, ha='left')
        plt.text(C[0], C[1], 'C', fontsize=12, ha='center')

        plt.axis('equal')
        plt.title(f'Triangle: {a}, {b}, {c} ({"Isosceles" if self.isIsosceles() else "Scalene"})')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        plt.grid(True)
        plt.show()


if __name__ == "__main__":
    # Example usage
    try:
        triangle = Triangle(5, 5, 5)
        print(triangle)
        triangle.show()
        print("Is the triangle isosceles?", triangle.isIsosceles())
        #triangle.plot()
    except TriangleException as e:
        print(f"Error: {e}")