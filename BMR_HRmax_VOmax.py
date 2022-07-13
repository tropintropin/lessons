"""Simple sport calculator

Program help you to calculate your maximal heart rate,
maximal VO2 volume and your basal metabolic rate (BMR).

Allowed input for gender is cirillic letters 'М', 'м' and
latin letters 'M', 'm' for male and 'Ж', 'ж', 'F', 'f', 'W', 'w'
for female.

Other inputs support only integers.

Author: Valery Tropin
tropin.tropin@gmail.com
2022...

"""

def hr_max(ask_age):
    out_hr_max = 205.8 - (0.685 * float(ask_age))
    return out_hr_max
              
def vo2_max(out_hr_max, ask_hr_rest):
    out_vo2_max = 15 * (float(out_hr_max) / float(ask_hr_rest))
    return out_vo2_max
              
def bmr(ask_weight, ask_height, ask_age, ask_gender):
    if ask_gender.lower() in ['м', 'm']:
        my_gender = 'мужской'
        out_bmr_male = 10 * float(ask_weight) + 6.25 * float(ask_height) - 5.0 * float(ask_age) + 5
        out_bmr = out_bmr_male
        return out_bmr, my_gender
    elif ask_gender.lower() in ['ж', 'f', 'w']:
        my_gender = 'женский'
        out_bmr_woman = 10 * float(ask_weight) + 6.25 * float(ask_height) - 5.0 * float(ask_age) - 161
        out_bmr = out_bmr_woman
        return out_bmr, my_gender

while True:
    ask_gender = input("Какого вы пола?\nПожалуйста, указывайте ваш биологический пол!\nВведите «М», если вы мужчина или «Ж», если женщина.\n")
    if ask_gender.lower() not in ['м', 'ж', 'm', 'f', 'w']:
        continue
    else:
        break

while True:
    ask_age = input("Сколько вам лет? ")
    if ask_age.isnumeric() != True:
        continue
    else:
        break

while True:
    ask_height = input("Какого вы роста (в см)? ")
    if ask_height.isnumeric() != True:
        continue
    else:
        break

while True:
    ask_weight = input("Сколько вы весите (в кг)? ")
    if ask_weight.isnumeric() != True:
        continue
    else:
        break

while True:
    ask_hr_rest = input("Каков ваш пульс в состоянии покоя (в ударах в минуту)? ")
    if ask_hr_rest.isnumeric() != True:
        continue
    else:
        break

my_hr_max = hr_max(ask_age)
my_vo2_max = vo2_max(hr_max(ask_age), ask_hr_rest)
my_bmr, my_gender = bmr(ask_weight, ask_height, ask_age, ask_gender)

print(f"Ваш пол: {my_gender}")
print(f"Ваш максимальный пульс: {my_hr_max:.0f} уд. в минуту.")
print(f"Максимальный объём потребляемого кислорода составит:\n{my_vo2_max:.2f} мл на кг массы тела в минуту")
print(f"Суточный калораж (BMR) = {my_bmr:.2f} ккал.\n(BMR рассчитан по формуле The Mifflin St Jeor)")