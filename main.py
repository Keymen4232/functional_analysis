import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
try:
    # Введення функції з клавіатури
    expr_str = input("Введіть вашу функцію f(x): ")
    x = sp.symbols('x')
    f = sp.sympify(expr_str)

    # 1. Знаходимо область визначення
    domain = sp.calculus.util.continuous_domain(f, x, sp.S.Reals)

    # Виводимо область визначення
    if domain == sp.S.Reals:
        print("1. Область визначення: x може приймати всі значення")
    else:
        intervals = []
        for interval in domain.args:
            start = '-∞' if interval.start == -sp.oo else interval.start
            end = '∞' if interval.end == sp.oo else interval.end
            intervals.append(f"({start}, {end})")
        print("1. Область визначення:", ",".join(intervals))

    # 2. Знаходимо область значень
    range_values = sp.solve_univariate_inequality(f > 0, x, relational=False)
    if range_values:
        print("2. Область значень:", range_values)
    else:
        print("2. Функція не має області значень на заданому інтервалі")

    # 3. Знаходимо нулі функції
    zeros = sp.solve(f, x)
    print("3. Нулі функції (розв'язки рівняння f(x) = 0):", zeros)

    # 4. Визначаємо знакосталість функції
    sign_changes_pos = sp.solve_univariate_inequality(f > 0, x, relational=False)
    if sign_changes_pos:
        print("4. Функція додатня на інтервалах:", sign_changes_pos)
    else:
        print("4. Функція не додатня на жодному інтервалі")

    sign_changes_neg = sp.solve_univariate_inequality(f < 0, x, relational=False)
    if sign_changes_neg:
        print("5. Функція від'ємна на інтервалах:", sign_changes_neg)
    else:
        print("5. Функція не від'ємна на жодному інтервалі")

    # 6. Визначаємо напрямок зростання і спадання
    derivative = sp.diff(f, x)
    increasing_intervals = sp.calculus.util.continuous_domain(derivative > 0, x, sp.S.Reals)
    if increasing_intervals == sp.S.Reals:
        print("6. Функція зростає на інтервалах: x може приймати всі значення")
    else:
        intervals = []
        for interval in increasing_intervals.args:
            start = '-∞' if interval.start == -sp.oo else interval.start
            end = '∞' if interval.end == sp.oo else interval.end
            intervals.append(f"({start}, {end})")
        print("6. Функція зростає на інтервалах:", ",".join(intervals))

    decreasing_intervals = sp.calculus.util.continuous_domain(derivative < 0, x, sp.S.Reals)
    if decreasing_intervals == sp.S.Reals:
        print("7. Функція не спадає на жодному інтервалі")
    else:
        intervals = []
        for interval in decreasing_intervals.args:
            start = '-∞' if interval.start == -sp.oo else interval.start
            end = '∞' if interval.end == sp.oo else interval.end
            intervals.append(f"({start}, {end})")
        print("7. Функція спадає на інтервалах:", ",".join(intervals))

    # 8. Знаходимо екстремуми і їх значення
    critical_points = sp.solve(derivative, x)
    extrema = [(point, f.subs(x, point)) for point in critical_points]
    if extrema:
        print("8. Екстремуми і значення в точках екстремуму:", extrema)
    else:
        print("8. Функція не має екстремумів на заданому інтервалі")

    print("Made by ChatGPT")

    # Побудова графіка функції
    x_vals = np.linspace(-10, 10, 400)
    y_vals = np.array([f.subs(x, xx) for xx in x_vals], dtype=float)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label=f"${sp.latex(f)}$", color='b')
    plt.title('Графік функції')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    plt.show()

except sp.SympifyError as e:
    print(f"Помилка введення виразу: {e}")
except Exception as e:
    print(f"Виникла невідома помилка: {e}")
