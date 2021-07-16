#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 10:27:03 2021

@author: sharif
"""

def creditCard(balance, annualInterestRate):
    i = 0
    monthlyPayment = 0
    while balance != 0:
        monthlyPayment += 10
        while i < 12:
            monthUnpaidBalance = balance - monthlyPayment 
            totalUnpaidBalance = monthUnpaidBalance + (monthUnpaidBalance * annualInterestRate/12)
            balance = totalUnpaidBalance 
            i +=1
    return monthlyPayment


