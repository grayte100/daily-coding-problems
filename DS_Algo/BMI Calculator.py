#BMI Calculator

#name1 = "YK"
#height_m1 = 2
#weight_kg1 = 90

#name2 = "YK's sister"
#height_m2 = 1.8
#weight_kg2 = 70

#name3 = "YK's brother"
#height_m3 = 2.5
#weight_kg3 = 160

name = ["YK", "YK's brother", "YK's sister"]
height_m = [2.0, 1.8, 2.5]
weight_kg = [90, 70, 160]
def bmi_calculator(name, weight, height):
    i = 0
    while i < (len(name)):
        bmi = weight_kg[i]/((height_m[i])**2)
        print("bmi:", bmi)
        i += 1
        
    if bmi < 25:
        return name + "is not overweight"
    else:
        return name + "is overweight"
       
    
result1 = bmi_calculator(name[0], weight_kg[0], height_m[0])
result2 = bmi_calculator(name[1], weight_kg[1], height_m[1])
result3 = bmi_calculator(name[2], weight_kg[2], height_m[2])
    
print(result1)
print(result2)
print(result3)