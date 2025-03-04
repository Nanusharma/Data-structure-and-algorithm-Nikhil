def fxn(weight,height,age,required_Weight):
    count=0
    while weight > required_Weight:
        BMR = 10* weight + 6.25* height - 5*age + 5
        # print(f"The BMR is: {BMR}")
        TDEE = BMR *1.375
        # print(f"The TDEE is: {TDEE}")
        print(f"Calories needed to loose 1 kg per week are: {TDEE-1000}")
        weight-=1
        count+=1
    print(f"Total number of weeks taken to reach weight of {required_Weight}kg: {count} ")




weight = 94
height = 178 
age = 21
required_Weight = 72
fxn(weight,height,age,required_Weight)

# TDEE = BMR * Activity Factor
# Sedentary (little/no exercise)	1.2
# Light (1-3 days/week exercise)	1.375
# Moderate (3-5 days/week exercise)	1.55
# Active (6-7 days/week exercise)	1.725
# Very Active (athlete, physical job)	1.9

