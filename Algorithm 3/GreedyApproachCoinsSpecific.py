def coin_change(coins, amount):
    changes = []
    largest = 0

    while amount > 0 and largest < len(coins):
        if amount < coins[largest]:
            largest += 1
        else:
            changes.append(coins[largest])
            amount -= coins[largest]
            largest += 1

    return changes

def main():
    coins_all = list(map(int, input("\nEnter all the coins you have at hand:> ").split()))
    
    coins_all.sort(reverse = True)

    print(f"Coins at hand: {coins_all}")

    total_amount = int(input("\nEnter the amount:> "))

    change_list = coin_change(coins_all, total_amount)

    print("\nCoins to be given:", change_list)
    print("Total number of coins:", len(change_list))
    if total_amount != sum(change_list):
        print("Amount unaccounted for = ", total_amount - sum(change_list))

if __name__ == "__main__":
   main()