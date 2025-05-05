def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    bmi = weight / (height * height)
    
    print("BMI = " + str(bmi))
    
    if bmi < 18.5:
        print("Under Weight")
        return -1
    elif 18.5 <= bmi <= 25.0:
        print("Normal Weight")
        return 0
    else:
        print("Over Weight")
        return 1

result = calculate_bmi(weight=80, height=1.85)
print("Returned Value:", result)
