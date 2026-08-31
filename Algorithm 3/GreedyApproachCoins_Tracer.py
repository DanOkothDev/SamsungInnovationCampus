def coin_change(coins, amount):
    changes = []
    largest = 0

    print("\nStarting point...")
    print("----------------------------")
    print("Coins so far: ", changes)

    print("\nLooping starts...")
    print("----------------------------")

    while amount > 0:
        if amount < coins[largest]:
            print(f"\nIndex {largest}\nAmount remaining: {amount}")
            print(f"Coin being considered: {coins[largest]}\nVerdict: Can't be used")
            print("Coins so far: ", changes)
            largest += 1
        else:
            print(f"\nIndex {largest}\nAmount remaining: {amount}")
            print(f"Coin being considered: {coins[largest]}\nVerdict: Added to the change")

            changes.append(coins[largest])
            amount -= coins[largest]

            print("Coins so far: ", changes)

    return changes

def main():
    coins_all = [500, 100, 50, 10]

    total_amount = int(input("\nEnter the amount:> "))

    change_list = coin_change(coins_all, total_amount)

    print("\n--------------------------------------------------------")
    print("\nCoins to be given:", change_list)
    print("Total number of coins:", len(change_list))

if __name__ == "__main__":
   main()