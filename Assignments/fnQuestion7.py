from fnQuestion1 import area_circle

def area_rectangle(a, b):
    area = a * b
    return area

def area_triangle(a, b):
    area = 0.5 * a * b
    return area

def main():
    print("\nChoose a figure to calculate the area")
    print("1. Triangle")
    print("2. Circle")
    print("3. Rectangle\n")

    choice = int(input("Enter your choice(1-3): "))
    if choice == 1:
        base, height = map(float, input("Enter the base and height of the triangle: ").split())
        
        areaTriangle = area_triangle(base,height)
        print(f"Triangle: Base -> {base}, Height -> {height}, Area: {areaTriangle}\n")
    elif choice == 2:
        radius = float(input("Enter the radius of the circle: "))

        areaCircle = area_circle(radius)
        print(f"Circle: Radius -> {radius}, Area: {areaCircle}\n")
    elif choice == 3:
        length = float(input("Enter the length of the reactangle: "))
        width = float(input("Enter the width of the rectangle: "))

        areaRectangle = area_rectangle(length, width)
        print(f"Rectangle, Length -> {length}, Width -> {width}, Area: {areaRectangle}\n")

    else:
        print("Invalid input!!!!\n\n")

if __name__ == "__main__":
    main()