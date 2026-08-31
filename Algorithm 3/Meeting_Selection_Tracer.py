def activity_selection1(start, finish):
    result = []
    i = 0
    result.append(i)
    k = 1

    print(f"\nUpto meeting number {k}:> {result}")
    print(f"i = {i}")
    k += 1

    for j in range(1, len(start)):
        if finish[i] <= start[j]:
            result.append(j)
            i = j
            print(f"Upto meeting number {k}:> {result}")
            print(f"i = {i}")
            k += 1

    return result

def main():
    start = [1, 3, 2, 1, 5, 8, 5]
    finish = [2, 4, 5, 6, 6, 9, 9]

    meetings = activity_selection1(start, finish)
    maximum = len(meetings)

    print()
    print(meetings, maximum) 

if __name__ == "__main__":
   main()