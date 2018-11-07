import math
a_value = float(input("a value: "))
b_value = float(input("b value: "))
c_value = float(input("c value: "))

def get_quadratic(a, b, c):
	inside_square = (b**2) - (4*a*c)
	if inside_square < 0:
		quadratic_equation_pos = "Imaginary!"
		quadratic_equation_neg = "Imaginary!"
	else:
		square_value = math.sqrt(inside_square)
		quadratic_equation_pos = (-b + square_value)/(2*a)
		quadratic_equation_neg = (-b - square_value)/(2*a)
	return (quadratic_equation_pos, quadratic_equation_neg)

print()	
print(get_quadratic(a_value, b_value, c_value))
print()
print(input("Press enter to execute program."))