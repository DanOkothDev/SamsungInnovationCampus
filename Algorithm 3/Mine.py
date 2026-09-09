def bubblesort(n):
    if len(n) == 0:
        return n

    for i in range(len(n)):
        for j in range(1, len(n)):
            if n[j - 1] > n[j]:
                n[j - 1], n[j] = n[j], n[j - 1]

    return n


def main():
    n = [2, 3, 9, 5, 7, 4, 8, 4, 6]

    print(bubblesort(n))
    



if __name__ == "__main__":
    main()