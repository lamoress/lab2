import math
import sympy
def extended_gcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        x, u = u - q * x, x
        y, v = v - q * y, y
    return a, u, v  # Возвращает НОД и коэффициенты y_p = u и y_q = v

# Параметры
p = 730367822456513
q = 414259691036167
c = 10
N = p * q

# Шаг 1: Вычислить m_p и m_q
m_p = pow(c, (p+1)//4, p)
m_q = pow(c, (q+1)//4, q)

# Шаг 2: Найти y_p и y_q с помощью РАЕ
gcd, y_p, y_q = extended_gcd(p, q)  # gcdex возвращает gcd и коэффициенты

# Проверим, что y_p * p + y_q * q действительно равно 1
assert gcd == 1 and (y_p * p + y_q * q) % N == 1

# Шаг 3: Вычислить корни
r1 = (y_p * p * m_q + y_q * q * m_p) % N
r2 = (y_p * p * m_q - y_q * q * m_p) % N
r3 = N - r1
r4 = N - r2



p = 730367822456513
q = 414259691036167
c = 16822699634989797327123095165092932420211999031886


print("Hello")
print("Hello")
print("Hello")
print("Jacobi symbol (c/p):", jacobi_p)
print("Jacobi symbol (c/q):", jacobi_q)

# Вывод результатов
print("Четыре возможных корня: ", r1, r2, r3, r4)
print("m_p:", m_p)
print("m_q:", m_q)
print("y_p:", y_p)
print("y_q:", y_q)
print("N", c)
