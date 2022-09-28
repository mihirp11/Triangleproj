def main():
    a = float(input('Enter the length of the first side: '))
    b = float(input('Enter the length of the second side: '))
    c = float(input('Enter the length of the third side: '))
    s = (a + b + c)/2.0
    area_squared = s * (s - a) * (s - b) * (s - c)
    if area_squared >= 0:
        print('IS A TRIANGLE : AREA SQUARED = ', area_squared)
    else:
        print('IS NOT A TRIANGLE AREA SQUARED = ', area_squared)
main()