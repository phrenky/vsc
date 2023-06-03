import numpy as np

def Kram(coefficients, constants): #coefficients -- матрица коэффициентов СЛАУ #constants -- столбец свободных членов
    
    num_equations = len(coefficients)
    num_variables = len(coefficients[0])

    # определитель матрицы коэффициентов
    det_coefficients = np.linalg.det(coefficients)

    if det_coefficients == 0:
        raise ValueError("Определитель матрицы коэффициентов равен нулю. Система имеет бесконечное множество решений или не имеет решений.")

    solution = []
    for i in range(num_variables):
        # врем. матрица для вычисления определителя с замененным i-ым столбцом на столбец свободных членов
        temp_matrix = coefficients.copy()
        temp_matrix[:, i] = constants

        # вычисляем определитель врем. матрицы
        det_temp = np.linalg.det(temp_matrix)

        # значение переменной с помощью отношения определителя врем. матрицы к определителю матрицы коэффициентов
        variable_value = det_temp / det_coefficients

        solution.append(variable_value)

    return solution


# Пример использования
coefficients = np.array([[2, 3, 1], [3, -1, 2], [1, 4, -1]])
constants = np.array([1, 1, 2])

solution = Kram(coefficients, constants)
print(float("Решение СЛАУ:", solution))