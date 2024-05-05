class BudgetTracker:
    def __init__(self):
        self.expenses = {}
        self.income = 0

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def add_income(self, amount):
        self.income += amount

    def total_expenses(self):
        return sum(self.expenses.values())

    def remaining_balance(self):
        return self.income - self.total_expenses()

    def display_summary(self):
        print("Income: $", self.income)
        print("Expenses:")
        for category, amount in self.expenses.items():
            print(category + ": $", amount)
        print("Total Expenses: $", self.total_expenses())
        print("Remaining Balance: $", self.remaining_balance())


def main():
    tracker = BudgetTracker()

    # Example usage
    tracker.add_income(3000)
    tracker.add_expense("Food", 500)
    tracker.add_expense("Rent", 1000)
    tracker.add_expense("Transportation", 200)
    tracker.add_expense("Entertainment", 300)

    tracker.display_summary()


if __name__ == "__main__":
    main()
