
def welcome():
    print("Hello! Welcome to the Employee Pay system!")
    print("This program will calculate the employees gross income, dedecutions, and net income that would be on a weekly paystub.")
    name = input("What is the employee's name?")

def calculate_gross():
    print("Please note that the value entered for hours worked should be the number of hours worked in one week.")
    hours = float(input("How many hours did the employee work?"))
    rate = float(input("What is the employee's hourly pay rate?"))
    gross = hours * rate
    rounded_gross = str(round(gross, 2))
    print("The employee's calculated gross rate is " + rounded_gross)
    

def calculate_deductions():
    gross_input = float(input("Please input the value that was calculated for the employee's gross income."))
    deductions = gross_input * 0.2
    rounded_deductions = str(round(deductions, 2))
    print("The employee's deductions are " + rounded_deductions)

def calculate_net_salary():
    net_gross = float(input("Please input the employee's gross salary."))
    net_deductions = float(input("Please input the employee's deductions."))
    net = net_gross - net_deductions
    rounded_net = str(round(net, 2))
    print ("The employee's net pay is "+ rounded_net)
    print ("This program was created by Sophie Fehrenbacher.")

welcome()
calculate_gross()
calculate_deductions()
calculate_net_salary()

