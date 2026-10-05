# choice = input("Enter A, B, or C: ")

# if choice == "A":
#     print("Apple")

# if choice == "B":
#     print("Banana")

# if choice == "C":
#     print("Coconut")

# choice = input("Enter A, B, or C: ")

# if choice == "A":
#     print("Apple")
# elif choice == "B":
#     print("Banana")
# elif choice == "C":
#     print("Coconut")
# else:
#     print("Invalid choice")

# credits = int(input("Enter your college credits: "))

# if credits < 30:
#     print("Freshman")
# elif credits < 60:
#     print("Sophomore")
# elif credits < 90:
#     print("Junior")
# # else:
# #     print("Senior")

# total = 0

# number = int(input("Enter a positive integer (0 to stop): "))

# while number != 0:

#     if number <= 100:
#         total = total + number

#     number = int(input("Enter a positive integer (0 to stop): "))

# print(f"Total = {total}")

# positive = 0
# negative = 0

# number = int(input("Enter a number (0 to stop): "))

# while number != 0:

#     if number > 0:
#         positive = positive + 1
#     elif number < 0:
#         negative = negative + 1

#     number = int(input("Enter a number (0 to stop): "))

# print(f"Positive values = {positive}")
# print(f"Negative values = {negative}")

# number = 1

# while number <= 100:

#     count = 1

#     while count <= 10:
#         print(number, end=" ")
#         number = number + 1
#         count = count + 1

#     print()

number = 1

while number <= 100:

    print(number, end=" ")

    if number % 10 == 0:
        print()

    number = number + 1