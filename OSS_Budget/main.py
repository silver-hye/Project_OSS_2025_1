from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 총 지출 보기")
        print("4. 종료")
        print("5. 지출 목표 설정")
        print("6. 지출 목표 진행 상황 보기")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4":
            print("가계부를 종료합니다.")
            break

        elif choice == "5":
             category = input("목표를 설정할 카테고리: ")
             try:
                 amount = int(input("목표 금액(원): "))
                 budget.set_goal(category, amount)
             except ValueError:
                 print("잘못된 금액입니다.\n")

        elif choice == "6":
             budget.show_progress()

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()
