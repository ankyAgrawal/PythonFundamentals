#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May 20 12:13:16 2018

@author: Ankit

Model for aircraft flight
"""

class Flight: 
    
    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid Airline code '{}'".format(number))
        if not (number[2:].isdigit() and int(number[2:])<=9999):
            raise ValueError("Invalid route number '{}'".format(number))
            
        self._number=number
        self._aircraft = aircraft
        
        rows,seat_letters = self._aircraft.seating_plan()
        self._seating = [None]+[{letter:None for letter in seat_letters} for _ in rows]
        
        
    def number(self):
        return self._number
    
    def airline(self):
        return self._number[:2]
    
    def aircraftmodel(self):
        return self._aircraft.model()
    
    def _parse_seat(self,seat):
        
        rows,seat_letters = self._aircraft.seating_plan()
        
        letter = seat[-1]
        
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))
            
        row_text=seat[:-1]
        
        try:
           row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))
            
        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))
        
        return row,letter
    
    def allocate_seat(self,seat,passenger):
        """
        Usage :Allocation of seats to passenger
        
        Raise : ValueError
        """
        row,letter = self._parse_seat(seat)
        
        if self._seating[row][letter] is not None:
            raise ValueError("seat {} is already occupied".format(seat))
            
        self._seating[row][letter]=passenger
        
    def relocate_passenger(self,from_seat,to_seat):
        from_row,from_letter = self._parse_seat(from_seat)
        
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No Passenger to relocate in seat {}".format(from_seat))
        
        to_row,to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(" seat {} already occupied".format(to_seat))
            
        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None
        
    def num_seats_available(self):
        empty_seats=0
        for seat in self._seating[1:]:
            for value in seat.values():
                if value is None:
                    empty_seats+=1
        return empty_seats
            


class Aircraft:
    def __init__(self,registration):
        self._registration=registration;
        
    def registration(self):
        return self._registration
    
    def num_seats(self):
        row,row_seats = self.seating_plan()
        return len(row)*len(row_seats)    

    
class Airbus319(Aircraft):
    
    def model(self):
        return "Airbus A319"
    
    def seating_plan(self):
        return range(1,22), "ABCDE"

class Boing799(Aircraft):
    
    def model(self):
        return "Boing 799"
    
    def seating_plan(self):
        return range(1,56), "ABCDEFGHIJKL"
    
def make_flights():
    f1 = Flight("AA319",Airbus319("Airbus319"))
    f2 = Flight("BB799",Boing799("Boing799"))
    f1.allocate_seat("4A","Ankit")
    f1.allocate_seat("4B","Sakshi")
    
    f2.allocate_seat("10A","Ankit")
    f2.allocate_seat("10B","Sakshi")
    
    return f1,f2