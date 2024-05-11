number_men = 0
number_women = 0
survived_men = 0
survived_women = 0

with open("data.csv", 'r') as file:
    for line in file:
        data = line.split(',')
        if data[5] == 'male':
            number_men = number_men + 1
            if data[1] == '1':
                survived_men = survived_men + 1
        if data[5] == 'female':
            number_women = number_women + 1
            if data[1] == '1':
                survived_women = survived_women + 1

print('Доля выживших мужчин:', round(survived_men / number_men * 100, 2),
      'Доля выживших женщин:', round(survived_women / number_women * 100, 2))