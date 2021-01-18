sum=0

while(True):
    pappu=input("Enter the name of an product:")
    if(pappu!='q'):
        
        gupta=input(f"Enter the price of an {pappu}:")
        sum=sum+int(gupta)
        print("\n")

        
    else:
        print(f"Your total order bill is {sum}\n")
        print("Thank you from Guddu kirana Store")
        break
