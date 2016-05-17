# coding: utf-8
# 참고문헌: http://docs.sympy.org/dev/modules/integrals/integrals.html#sympy.integrals.transforms.laplace_transform
#   http://www.mathalino.com/reviewer/advance-engineering-mathematics/table-laplace-transforms-elementary-functions

import sympy as sp
from sympy.integrals.transforms import inverse_laplace_transform
from sympy.integrals.transforms import laplace_transform

t, s, p = sp.symbols('t s p')
w = sp.Symbol('w', real=True)
a = sp.Symbol('a', real=True)
y = a * sp.sin(w * t)
print("y = %s" % y)

Y = laplace_transform(y, t, s)[0]
print("Y = %s" % Y)

yi = inverse_laplace_transform(a * w/(s**2 + w**2), s, t)
print("yi = %s" % str(yi))
