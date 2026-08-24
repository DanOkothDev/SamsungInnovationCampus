def calc_vol(a, b, c):
    vol = a * b * c
    return vol

def main():
    length = float(input("Enter the length of the cube: "))
    height = float(input("Enter the height of the cube: "))
    breadth = float(input("Enter the breadth of the cube: "))

    volume_of_cube = calc_vol(length, height, breadth)

    print(f"Length: {length}, height: {height}, breadth: {breadth}. Volume is: {volume_of_cube}")

main()