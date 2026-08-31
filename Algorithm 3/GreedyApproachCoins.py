def coin_change(coins, amount):
    changes = []
    largest = 0

    while amount > 0:
        if amount < coins[largest]:
            largest += 1
        else:
            changes.append(coins[largest])
            amount -= coins[largest]

    return changes

def main():
    coins_all = [500, 100, 50, 10]

    total_amount = int(input("\nEnter the amount:> "))

    change_list = coin_change(coins_all, total_amount)

    print("\nCoins to be given:", change_list)
    print("Total number of coins:", len(change_list))

if __name__ == "__main__":
   main()