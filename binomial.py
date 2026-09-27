"""
binomial.py - Binomial Expression Module
Handles (a + b)^n expansion using Binomial Theorem
Formula: (a + b)^n = Σ [nCk * a^(n-k) * b^k]
"""

import math

def nCr(n, r):
    """Combination: nCr = n! / (r! * (n-r)!)"""
    if r > n:
        return 0
    return math.comb(n, r)  # Python 3.8+ has this built-in

def expand_binomial(a, b, n):
    """
    Expand (a + b)^n
    Returns list of terms like [(coeff, power_of_a, power_of_b)]
    """
    terms = []
    for k in range(n + 1):
        coeff = nCr(n, k)
        power_a = n - k
        power_b = k
        terms.append((coeff, power_a, power_b))
    return terms

def binomial_expression_string(n, var1='a', var2='b'):
    """Returns expansion string like: a^2 + 2ab + b^2"""
    terms = expand_binomial(1, 1, n)
    result = []
    for coeff, pa, pb in terms:
        term = ""
        # Coefficient
        if coeff != 1 or (pa == 0 and pb == 0):
            term += f"{coeff}"
        
        # Variable a
        if pa > 0:
            if pa == 1:
                term += f"{var1}"
            else:
                term += f"{var1}^{pa}"
        
        # Variable b
        if pb > 0:
            if pb == 1:
                term += f"{var2}"
            else:
                term += f"{var2}^{pb}"
        
        result.append(term)
    
    return " + ".join(result)

def evaluate_binomial(a, b, n):
    """Calculate numeric value of (a + b)^n using binomial theorem"""
    total = 0
    for k in range(n + 1):
        coeff = nCr(n, k)
        total += coeff * (a ** (n - k)) * (b ** k)
    return total

def format_expansion(a, b, n):
    """Pretty print expansion"""
    print(f"\n=== Expanding ({a} + {b})^{n} ===")
    print(f"Formula: (a + b)^n = Σ nCk * a^(n-k) * b^k")
    print(f"\nExpansion:")
    for k in range(n + 1):
        coeff = nCr(n, k)
        pa = n - k
        pb = k
        value = coeff * (a ** pa) * (b ** pb)
        print(f"  k={k}: {coeff} * {a}^{pa} * {b}^{pb} = {value}")
    
    print(f"\nTotal = {evaluate_binomial(a, b, n)}")
    print(f"Check: ({a} + {b})^{n} = {(a + b) ** n}")

def main():
    print("=== Binomial Expression Calculator ===")
    
    # Example 1: Simple
    print("\n1. (a + b)^2 =", binomial_expression_string(2))
    print("2. (a + b)^3 =", binomial_expression_string(3))
    print("3. (a + b)^4 =", binomial_expression_string(4))
    print("4. (a + b)^5 =", binomial_expression_string(5))

    # Example 2: With numbers
    a = float(input("\nEnter a: "))
    b = float(input("Enter b: "))
    n = int(input("Enter n (power): "))

    format_expansion(a, b, n)

if __name__ == "__main__":
    main()