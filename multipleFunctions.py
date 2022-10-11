class multipleFunctions():
    def oddEven():
        num=int(input("Enter the number:"))
        if((num%2)==0):
            print("Even number")
            message="Even number"
        else:
            print("Odd number")
            message="Odd number"
        return message


    def BMI():
        bmi=int(input("Enter the BMI Index:"))
        if(bmi<18.5):
            print("Underweight")
            message="Underweight"
        elif(bmi<=24.9):
            print("Normal")
            message="Normal"
        elif(bmi<=29.9):
            print("Overweight")
            message="Overweight"
        else:
            print("Very Overweight")
            message="Very Overweight"
        return message