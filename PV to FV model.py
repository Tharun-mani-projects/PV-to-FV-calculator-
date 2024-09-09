#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def calulate_fv(PV,i,m,n,):
    return(PV*(1+i/m)**(m*n))
present_value = float(input("What is the current present value of the amount in $ : "))
compounding_periods = float(input("What is the periodicity? : "))
interest_rate = float(input("What is the stated interest rate? : "))
years = float(input("Number of years til maturity? : "))

FV = calulate_fv(present_value,interest_rate,compounding_periods,years)
print("The present value of the amount is ${}, the future value will be ${}, when the stated interest rate is {}%, and it was invested for {} years."
      .format(present_value,round(FV,2),(interest_rate*100),years))
input()


# In[ ]:




