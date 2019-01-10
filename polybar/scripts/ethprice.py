#!/usr/bin/env python
import requests as r
try:
    d = r.get('https://koinex.in/api/ticker')
    price = d.json()['prices']['inr']['ETH']
    print(str(price))
except Exception as e:
    print(0)
