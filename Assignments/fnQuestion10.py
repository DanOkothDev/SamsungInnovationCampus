def temp():

    degree = []
    fahrenheit = []

    for i in range(0, 301, 20):
        D = (i - 32) * 5/9
        degree.append(D)
        fahrenheit.append(i)

    return fahrenheit,degree

def main():
    fahren, degree = temp()
    print("Fahrenheit      Celsius")
    
    for f, d in zip(fahren, degree):
        print(f"  {f}          {d:.2f}")
    

if __name__ == "__main__":
    main()