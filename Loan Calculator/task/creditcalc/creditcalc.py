import math
import argparse


def calculate_periods(principal, payment, interest):
    i = interest / (12 * 100)
    p, a = principal, payment
    periods = math.log(a / (a - i * p), 1 + i)
    return math.ceil(periods)


def calculate_annuity_payment(principal, periods, interest):
    i = interest / (12 * 100)
    p, n = principal, periods
    annuity_payment = p * (i * pow(1 + i, n)) / (pow(1 + i, n) - 1)
    return math.ceil(annuity_payment)


def calculate_principal(payment, periods, interest):
    i = interest / (12 * 100)
    a, n = payment, periods
    principal = a / ((i * pow(1 + i, n)) / (pow(1 + i, n) - 1))
    return principal


def calculate_differentiated_payments(principal, periods, interest, month):
    i = interest / (12 * 100)
    p, n, m = principal, periods, month
    differentiated_payments = (p / n) + i * (p - (p * (m - 1) / n))
    return math.ceil(differentiated_payments)


def main():
    parser = argparse.ArgumentParser(description='Loan Calculator Stage 3/4')
    parser.add_argument('--type', type=str, help='Type of payment')
    parser.add_argument('--principal', type=float, help='Loan principal')
    parser.add_argument('--payment', type=float, help='Monthly payment amount')
    parser.add_argument('--periods', type=int, help='Number of payments (Months)')
    parser.add_argument('--interest', type=float, help='Loan interest rate (Annual)')

    args = parser.parse_args()
    total_payment = 0.0
    principal = -0.0

    if args.principal and args.principal < 0:
        print('Incorrect parameters')
        return
    if args.periods and args.periods < 0:
        print('Incorrect parameters')
        return
    if args.interest and args.interest < 0:
        print('Incorrect parameters')
        return
    if args.payment and args.payment < 0:
        print('Incorrect parameters')
        return
    if not args.interest or not args.type:
        print('Incorrect parameters')
        return
    if args.type == 'diff' and args.payment:
        print('Incorrect parameters')
        return
    elif args.type == 'diff':
        for i in range(args.periods):
            current_payment = calculate_differentiated_payments(args.principal, args.periods, args.interest, i + 1)
            total_payment += current_payment
            print(f"Month {i}: payment is {current_payment}")
    elif args.type == 'annuity':
        if args.principal and args.payment and not args.periods:
            periods = calculate_periods(args.principal, args.payment, args.interest)
            years, months = divmod(periods, 12)
            if years > 1 and months > 1:
                print(f"It will take {years} years and {months} months to repay this loan!")
            elif years > 1 and months == 1:
                print(f"It will take {years} years and {months} month to repay this loan!")
            elif years > 1 and months == 0:
                print(f"It will take {years} years!")
            elif years == 1 and months > 1:
                print(f"It will take {years} year and {months} months to repay this loan!")
            elif years == 1 and months == 1:
                print(f"It will take {years} year and {months} month to repay this loan!")
            elif years == 1 and months == 0:
                print(f"It will take {years} year to repay this loan!")
            elif years == 0 and months > 1:
                print(f"It will take {months} months to repay this loan!")
            elif years == 0 and months == 1:
                print(f"It will take {months} month to repay this loan!")
            total_payment = args.payment * periods
        elif args.principal and args.periods and not args.payment:
            payment = calculate_annuity_payment(args.principal, args.periods, args.interest)
            print(f"Your monthly payment = {payment}!")
            total_payment = payment * args.periods
        elif args.payment and args.periods and not args.principal:
            principal = calculate_principal(args.payment, args.periods, args.interest)
            print(f"Your loan principal = {principal}!")
            total_payment = args.payment * args.periods
        else:
            print("Incorrect parameters")

    if args.type == 'diff':
        print("\n")
    if not args.principal:
        print("Overpayment = {}".format(math.ceil(total_payment - principal)))
    else:
        print("Overpayment = {}".format(math.ceil(total_payment - args.principal)))


if __name__ == "__main__":
    main()
