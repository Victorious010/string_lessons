L = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch.    
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.      
Namespaces are one honking great idea -- let's do more of those!"""
email = "ilya.trusov.8208@gmail.com"
input_text = "{}{}".format(L, email)
print(len(input_text))

# Создаем цикл чтобы выводились гласные
Buk = "aeyuoi"
s = 0
for i in input_text:
    if i in Buk:
        s = s + 1
print(s)
# Создаем цикл который выводит каждый 18-ый
# символ в противоположно регистре


input_text = input_text.swapcase()

for count, sign in enumerate(input_text):
    if count % 18 == 0:
        print(".{}:{}".format(count, sign))
