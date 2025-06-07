import datetime
from expense import Expense
import json

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
         data = [e.__dict__ for e in self.expenses]  
         json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
              self.expenses = json.load(f)
        except FileNotFoundError:
              print("불러올 파일이 없습니다.")


