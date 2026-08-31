def find_minimum(row, col, triangle):
    if row == len(triangle):
        print(len(triangle))
        return 0
    else:
        print(len(triangle))
        minimum = min(find_minimum(row + 1, col, triangle), find_minimum(row + 1, col + 1, triangle))
        return triangle[row][col] + minimum

def main():
    triangle = [
                [2],
                [3, 4],
                [6, 5, 7],
                [4, 1, 8, 3]
               ]
    print(triangle)
    minimum = find_minimum(0, 0, triangle)
    print("\nThe minimum cost is",minimum)

if __name__ == "__main__":
   main()