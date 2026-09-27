"""
Quadratic Equation Solver
Solves ax^2 + bx + c = 0 for real or complex roots.
"""

import cmath


def solve_quadratic(a, b, c):
    """Return the two roots of ax^2 + bx + c = 0 (real or complex)."""
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be 0 (not a quadratic equation).")

    discriminant = b ** 2 - 4 * a * c
    sqrt_disc = cmath.sqrt(discriminant)

    root1 = (-b + sqrt_disc) / (2 * a)
    root2 = (-b - sqrt_disc) / (2 * a)

    return root1, root2, discriminant


def format_root(root):
    """Format a complex number nicely, dropping the imaginary part if it's 0."""
    if root.imag == 0:
        return f"{root.real:.4g}"
    return f"{root.real:.4g} {'+' if root.imag >= 0 else '-'} {abs(root.imag):.4g}i"


def main():
    print("=== Quadratic Equation Solver ===")
    print("Solves ax^2 + bx + c = 0\n")

    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    root1, root2, discriminant = solve_quadratic(a, b, c)

    print(f"\nEquation: {a}x^2 + {b}x + {c} = 0")
    print(f"Discriminant: {discriminant.real:.4g}")

    if discriminant.real > 0:
        print("Result: Two distinct real roots")
    elif discriminant.real == 0:
        print("Result: One repeated real root")
    else:
        print("Result: Two complex roots")

    print(f"\nRoot 1: {format_root(root1)}")
    print(f"Root 2: {format_root(root2)}")


if __name__ == "__main__":
    main()