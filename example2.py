# example mro
class O: pass
class G(O): pass
class E(G): pass
class F(G): pass
class D(E): pass
class C(E,F): pass
class B(D,F): pass
class A(C,B): pass
print(A.__mro__)