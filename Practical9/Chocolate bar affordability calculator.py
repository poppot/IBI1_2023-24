def calculator(total_money,price):                                           #A calculator to calculate the data already input and print the result
    bar=str(total_money//price)
    rest_money=str(total_money%price)
    print("you can buy "+bar+" bars, you rest "+rest_money+" dollar")
total_money=int(input(":"))                                                                  #receive the data
price=int(input(':'))
calculator(total_money,price)                                                                
