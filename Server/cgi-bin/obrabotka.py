#!/usr/bin/env python3

import cgi

our_form = cgi.FieldStorage ()

in_name = our_form.getfirst("in_name","Отсутсвуют данные")
in_password = our_form.getfirst("in_password","Отсутсвуют данные")

print("Content-type: text/html")
print()
print(in_name)
print(in_password)
