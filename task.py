L = ''
L += input("Enter your Gmail:")
Lenn = len(L)

# Создаем цикл чтобы выводились гласные
Buk = "aeyuoi"
s = 0
for i in L:
    if i in Buk:
        s = s+1

# Создаем цикл который выводит каждый 18-ый
# символ в противоположно регистре

my_list = list(L)
my_list = str(my_list)
my_list = my_list.swapcase()


if my_list:
    print(str(my_list[17])+"18")

print(s)
print(Lenn)
