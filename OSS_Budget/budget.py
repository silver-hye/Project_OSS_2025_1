import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.goals = {}

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

    def set_goal(self, category, amount):
        self.goals[category] = amount
        print(f"{category} 카테고리의 목표 지출이 {amount}원으로 설정되었습니다.\n")

    def get_total_by_category(self, category):
        return sum(e.amount for e in self.expenses if e.category == category)

    def show_progress(self):
        if not self.goals:
               print("설정된 지출 목표가 없습니다.\n")
               return

        print("\n[지출 목표 진행 상황]")

        for category, goal in self.goals.items():
            spent = self.get_total_by_category(category)
            percent = min(100, round((spent / goal) * 100)) if goal else 0
            remain = goal - spent
            print(f"{category} 목표: {goal}원 | 현재 지출: {spent}원 → {percent}% 소진 (남은 예산: {remain}원)")
        print()