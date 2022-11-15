# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 16:38:26 2021
@author: 16617
Interest rate problem
given 2 o 3, solve for the last one
"""

class loan:
    def __init__(self, name):
        self._name= name
        
    def who(self):
        print(self._name)
        
    def setPV(self, PV):
        self._PV = PV
        print('present value = ', self._PV)
        
    def setRate(self, ratePct):
        #set interest, apr
        self._ratePct = ratePct
        print('APR = ', self._ratePct,'%')
        
    def setMonths(self, months):
        self._months = months
        print(self._months, 'months')
        
    def computePmt(self):
        # formula: pmt = PV*(r*(1+r)**n)/((1+r)**months -1)
        r = self._ratePct/100/12
        self._Pmt = self._PV*(r*(1+r)**self._months)/((1+r)**self._months-1)
        print('payment = $', round(self._Pmt,2))
        return self._Pmt
    
    def setPmt(self, pmt):
        self._Pmt = pmt

if __name__ == "__main__":
    loan1 = loan('Dr J')
    loan1.who()

    loan1.setPV(27150)  #mini cooper
    loan1.setRate(1.9)
    loan1.setMonths(42)
    payment = loan1.computePmt()

