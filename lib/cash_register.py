#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
      # Constructor method to initialize the instance variables
      self.discount = discount  # Represents the discount percentage
      self.total = 0  # Represents the total price
      self.last_transaction = 0  # Represents the price of the last transaction
      self.items = []  # Represents a list of items added to the cash register

  def add_item(self, title, price, quantity=1):
      # Method to add an item to the cash register
      self.last_transaction = price * quantity  # Calculate the price of the current transaction
      self.total += self.last_transaction  # Add the price of the current transaction to the total
      for _ in range(quantity):
          self.items.append(title)  # Append the item title to the list of items

  def apply_discount(self):
      # Method to apply a discount to the total price
      if self.discount > 0:  # Check if a discount is applicable
          discount_as_percent = (100 - float(self.discount)) / 100  # Calculate the discount as a percentage
          self.total = int(self.total * discount_as_percent)  # Apply the discount to the total
          print(f"After the discount, the total comes to ${self.total}.")
      else:
          print("There is no discount to apply.")  # Print a message when no discount is applicable

  def void_last_transaction(self):
      # Method to void the last transaction
      self.total -= self.last_transaction  # Subtract the price of the last transaction from the total
