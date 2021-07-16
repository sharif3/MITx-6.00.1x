#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 19:17:03 2021

@author: sharif
"""

def creditCard(balance, annualInterestRate):
    monthlyPayment = 10
    nuBalance = balance 
    while nuBalance > 0: 
        monthlyPayment += 10
        nuBalance = balance
        i = 0
        while i < 12: 
            monthUnpaidBalance = nuBalance - monthlyPayment 
            totalUnpaidBalance = monthUnpaidBalance + (monthUnpaidBalance * annualInterestRate/12)
            nuBalance = totalUnpaidBalance 
            i +=1
    return monthlyPayment

