habits = []

def add_habit():
    name = input("Enter habit: ")
    habits.append({"name": name, "done": False})
    print("Habit added!\n")

def show_habits():
    if not habits:
        print("No habits yet\n")
        return

    print("\nYour Habits:")
    for i, h in enumerate(habits):
        if h["done"]:
            print(i+1, h["name"], "✅")
        else:
            print(i+1, h["name"], "❌")
    print()

def mark_done():
    show_habits()
    num = int(input("Enter number: ")) - 1
    if 0 <= num < len(habits):
        habits[num]["done"] = True
        print("Done!\n")

def show_stats():
    total = len(habits)
    done = 0

    for h in habits:
        if h["done"]:
            done += 1

    if total == 0:
        print("No data\n")
        return

    percent = (done / total) * 100
    print("Progress:", percent, "%")

    # AI thinking (simple)
    if percent == 100:
        print("🔥 Perfect!")
    elif percent >= 50:
        print("👍 Good")
    else:
        print("⚠️ Improve")

def menu():
    while True:
        print("1 Add Habit")
        print("2 Show Habits")
        print("3 Mark Done")
        print("4 Show Stats")
        print("5 Exit")

        choice = input("Enter: ")

        if choice == "1":
            add_habit()
        elif choice == "2":
            show_habits()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            show_stats()
        elif choice == "5":
            break
        else:
            print("Wrong choice\n")

menu()
