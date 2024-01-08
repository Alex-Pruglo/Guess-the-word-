import random
print("Привет! Я загадал слово."
      "Твоя задача отгадать его по буквам!")
input("Нажмите 'Enter' чтобы продолжить.")
words = ["Пират","Самолет","Ежик","Йогурт","Слоник"]
life = 10
word = random.choice(words)
letters = []
while life >0:
      win = True
      for symv in word:
            if symv in letters:
                  print(symv, end=' ')
            else:
                  print("*", end=' ')
                  win = False
      print()
      if win:
            print("Ты победил!")
            break
      letter = input("Введитe букву: ")
      letters.append(letter)
      if letter not in word:
            life -= 1
            print(f"Осталось жизней: {life}")
if life < 1:
      print("Жизни закончились! Ты проиграл.")
