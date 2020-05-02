def bot(bot_name, bot_year):
    print('My name is : ' + bot_name)
    print('I was created : ' + bot_year)


def remind_name():
    print('Please, remind me your name.')
    name = input('>> ')
    print('What a great name you have ' + name)
    return name


def Bmi():
    weight = float(input(f"Please {name} enter your weight in kg! "))
    height = float(input(f"Please {name} enter your height in cm! "))
    BMI = float((weight / (height * height)) * 10000)  # BMI equation
    BMI_ = float("{0:.2f}".format(BMI))
    print(BMI_)
    if BMI_ < 18.5:
        print("You are severly underweight")
    elif 18.5 < BMI_ < 24.9:
        print("You are Normal ")
        print("Perfect")
    elif 25 < BMI_ < 29.9:
        print("Overweight")
    elif 30 < BMI_ < 34.9:
        print("Obese")
    elif BMI_ > 35:
        print("Extremly obese")
        print("So dangerous you have to lose weight")


def end():
    print("good by have a great day...")


bot("Sam", "2020")
name = remind_name()
Bmi()
end()
