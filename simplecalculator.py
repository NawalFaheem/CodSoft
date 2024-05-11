                       #SIMPLE CALCULATOR

# function for addition
  def add(num1,num2):
  return num1+num2
# function for subtraction
def sub(num1,num2):
  return num1-num2
# function for multiplication
def mul(num1,num2):
  return num1*num2
# function for division
def div(num1,num2):
  return num1/num2
print("Select the operator:\n"
       "1-Addition \n"
       "2-Subtraction \n"
       "3-Multiplication \n"
       "4-Division \n")
select=int(input("Select Operations \n"))
num1=int(input("Enter first number:\n"))
num2=int(input("Enter second number\n"))
if select==1:
  print(num1,"+",num2,"=",add(num1,num2))
elif select==2:
  print(num1,"-",num2,"=",sub(num1,num2))
elif select==3:
  print(num1,"*",num2,"=",mul(num1,num2))
elif select==4:
  print(num1,"/",num2,"=",div(num1,num2))
else:
  print("Invalid Input");
print("=== Code Execution Successful ===")

















))
