def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)


def calorie_estimator(weight, height, age):

    bmr = 10 * weight + 6.25 * height - 5 * age + 5

    return int(bmr * 1.4)
