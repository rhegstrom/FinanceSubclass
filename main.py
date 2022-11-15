# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 07:43:51 2022

@author: Roger Hegstrom(rhegstrom@avc.edu)

I hope this is enough to demonstrate my understanding of inheritance
using the class finance which inherits the class loan. Which then uses variables
stored in the loan class as well as in the finance class to calculate Value401K()

"""

from loanClass import loan

class finance(loan):
    currentD = 0.00
    
    def __init__(self, name):
        super().__init__(name)
    
    def set401KCurrentD(self, amt):
        self.currentD = amt
        print(f'Setting 401K currentD to ${amt}')
        
    def Value401K(self):
        return self.currentD + self._Pmt * ((1+self._ratePct/1200)**self._months - 1)/(self._ratePct/1200)
    
               



if __name__ == "__main__":
    f = finance('401K Retirement Account')
    f.setPmt(20)               # monthly contribution
    f.setRate(2)               # 2% interest rate
    f.set401KCurrentD(12500)   # Initial contribution
    f.setMonths(60)            # How many months paid
    
    print(f'\n\nMy 401K value is: ${f.Value401K():.2f}')
    pass
