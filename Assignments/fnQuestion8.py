def calc_tax(gross_pay):
    if gross_pay >= 50000:
        tax_amount = gross_pay * 0.35

    elif gross_pay >= 40000:
        tax_amount = gross_pay * 0.30

    elif gross_pay >= 20000:
        tax_amount = gross_pay * 0.25

    elif gross_pay >= 12000:
        tax_amount = gross_pay * 0.15
    else:
        tax_amount = 0

    return tax_amount

def main():
    gross = float(input("Enter your gross pay: "))

    tax = calc_tax(gross)
    net_pay = gross - tax

    print(f"\nYour gross pay is: Ksh {gross:,.2f}, accumulating a tax of: Ksh {tax:,.2f} and your net pay is: Ksh {net_pay:,.2f}\n")



if __name__ == "__main__":
    main()