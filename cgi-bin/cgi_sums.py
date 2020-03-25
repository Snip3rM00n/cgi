#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
operands = form.getlist("operand")
try:
    total = sum([int(operand) for operand in operands])
    body = f"Total Sum: {total}"
except(ValueError, TypeError):
    body = str("Invalid operand, please use integers only."
               f"\nSupplied Operands: {operands}")
print("Content-type: text/plain")
print()
print(body)
