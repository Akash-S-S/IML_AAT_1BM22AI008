from fractions import Fraction

X_white = 5
X_black = 4
Y_white = 7
Y_black = 6

total_X = X_white + X_black
P_WX = Fraction(X_white, total_X)
P_BX = Fraction(X_black, total_X)

P_BY_given_WX = Fraction(Y_black, Y_white + Y_black + 1)
P_BY_given_BX = Fraction(Y_black + 1, Y_white + Y_black + 1)

P_BY = P_BY_given_WX * P_WX + P_BY_given_BX * P_BX

print(P_BY)
