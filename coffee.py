#Your code goes here
#might have to try make num 2 a global 
num = int(input("Please enter change for product: "))

x = 75 
num = int(input("Please enter change for product: "))
def change(num):
    if num == 50:
        print("Change accepted, amount due is: ", x - num)
    if num == 25:
        print("Change accepted, amount due is: ", x - num)
    if num == 10:
        print("Change accepted, amount due is: ", x - num)
    if num == 5:
        print("Change accepted, amount due is: ", x - num)
   
def change(num2):
     
     if num2 == 50:
        print("Change accepted, amount due is: ", x - num - num2)
     if num2 == 25:
        print("Change accepted, amount due is: ", x - num - num2)
     if num2 == 10:
        print("Change accepted, amount due is: ", x - num - num2)
     if num2 == 5:
        print("Change accepted, amount due is: ", x - num - num2)

def main():
    num = int(input("Please enter change for product: "))
    change(num)
    change(num2)
    

main()