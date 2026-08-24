PI = 22/7

def area_circle(r):
    area = PI * r * r
    return area

def circumference_circle(r):
    circum = 2 * PI * r
    return circum

def main():
    radius = float(input("Enter the radius of the circle: "))

    area_circ = area_circle(radius)
    circumference = circumference_circle(radius)

    print(f"The area of the circle is: {area_circ:.2f}, and circumeference is : {circumference:.2f}")

if __name__=="__main__":
    main()