# mas = [5,4,3,2,1]
# n = len(mas)
# count = 0
# print(f"Original array {mas} and count of changing {count}")
#
# for run in range(n-1):
#     for i in range(n-1):
#         print(f"Сейчас сравниваем {mas[i]} с {mas[i+1]}")
#         if mas[i] > mas[i+1]:
#             count += 1
#             mas[i], mas[i+1] = mas[i+1], mas[i]
#
# print(f"Bubble sorted array {mas} and count of changing {count}")

mas = [5,4,3,2,1]
n = len(mas)
count = 0
print(f"Original array {mas} and count of changing {count}")

for run in range(n-1):
    for i in range(n-1-run):
        print(f"Сейчас сравниваем {mas[i]} с {mas[i+1]}")
        if mas[i] > mas[i+1]:
            count += 1
            mas[i], mas[i+1] = mas[i+1], mas[i]

print(f"Bubble sorted array {mas} and count of changing {count}")