import psutil
import time
import os
#funk till övervakning 
def monitor_system(interval=2):
    """Övervakar CPU, RAM och disk under intervaller av 2 sekunder."""
    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    try:
        while True:
            clear_console()
            cpu_percent = psutil.cpu_percent(interval=1)
            print(f"CPU-usage: {cpu_percent}%")

            memory = psutil.virtual_memory()
            print(f"Memory-usage: {memory.percent}% "
                  f"(Använt: {memory.used / (1024**3):.2f} GB av {memory.total / (1024**3):.2f} GB)")

            
            time.sleep(interval)

    except KeyboardInterrupt:
        print("\nÖvervakning avbruten.")


#menu 
def first_menu():
    while True:
        print("=== WELCOME ===")
        print("1. MONITORING")
        print("2. LIST MONITORING")
        print("3. LARM")
        print("4. SHOW LARM")
        print("5. START MONITORING")
        print("6. EXIT")
        print("================")

        choice = input("SELECT WHAT YOU WANT TO DO: ").strip()
        if choice == '1':
            print("YOUR MONITORING (placeholder)\n")
        elif choice == '2':
            print("LIST OF MONITORING (placeholder)\n")
        elif choice == '3':
            larm_menu()
        elif choice == '4':
            print("SHOW LARM (placeholder)\n")
        elif choice == '5':
            print("STARTING MONITORING...\n")
            monitor_system()  #
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Ogiltigt val, försök igen.\n")


def larm_menu():
    while True:
        print("== WELCOME TO LARM ==")
        print("1. CPU USAGE")
        print("2. MEMORY USAGE")
        print("3. DISK USAGE")
        print("4. GO BACK")

        choice = input("SELECT WHAT YOU WANT TO DO: ").strip()
        if choice == '1':
            print("CPU USAGE (placeholder)\n")
        elif choice == '2':
            print("MEMORY USAGE (placeholder)\n")
        elif choice == '3':
            print("DISK USAGE (placeholder)\n")
        elif choice == '4':
            return
        else:
            print("Ogiltigt val, försök igen.\n")


#för att programmet ska kunna köras
if __name__ == "__main__":
    first_menu()
