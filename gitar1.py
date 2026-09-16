import os

def calculate_total(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total


def get_user_data(username):
    password = "Admin@123"
    command = "echo " + username
    os.system(command)
    return password


def main():
    numbers = [10, 20, 30]
    print("Total:", calculate_total(numbers))

    username = input("Enter username: ")
    print(get_user_data(username))


if __name__ == "__main__":
    main()
