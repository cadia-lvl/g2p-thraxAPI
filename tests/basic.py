# -*- coding: utf-8 -*-
import requests


#source: https://www.ruv.is/frett/2020/10/30/domstolar-nyta-ekki-fjarfundarbunad-sem-skyldi
loc = ['standard', 'north', 'northeast', 'south']
for l in loc:
    r = requests.post("http://0.0.0.0:8080/transcribe/ice/"+l, params={'text':'h l a u p a'})
    print(l,r.text)
