# coding: utf-8

import sympy as sp

x = sp.Symbol('x', real=True)
y = sp.Symbol('y', real=True)
z = sp.Symbol('z', real=True)

eq1 = sp.Eq(10.5 * sp.sin(x) + 10.5 * z * sp.sin(x - y), 0.6661)
eq2 = sp.Eq(10 * z * sp.sin(y) + 10.5 * z * sp.sin(y - z), 2.8653)
eq3 = sp.Eq(-10 * z * sp.cos(y) - 10.5 * z * sp.cos(y - z) - 20 * z * z, 1.2244)
result = sp.solve([eq1, eq2, eq3])

print(result)
