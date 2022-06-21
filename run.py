#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import json
f = open('D:/dynamic-einvoice/e_inoivce-windows/backage.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

print("urlllllllll",data[0].get("url"))
os.system(data[0].get("url"))
