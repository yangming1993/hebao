#!/usr/bin/env python
#encoding: utf-8
'''
@author:ym

@time:2017/9/20
'''
import hashlib
req = '''characterSet=02
&callbackUrl=http://localhost:87/BackUrl.aspx
&notifyUrl=http://localhost:87/NotifyUrl.aspx
&ipAddress=10.9.26.2
&merchantId=888009941120001
&requestId=201103071740065878
&signType=MD5
&type=DirectPay
&version=2.0.0
&amount=100
&bankAbbr=ICBC&currency=00 
&orderDate=20110307
&orderId=201103071740044998
&merAcDate=20110307
&period=7
&periodUnit=02
&merchantAbbr=
&productDesc=1&productId=2&productName=2
&productNum=&reserved1=31
&reserved2=2
&userToken=15116410263
&showUrl=
&couponsFlag=00
'''
req2 = '''characterSet=00&callbackUrl=http://localhost:87/BackUrl.aspx&notifyUrl=http://localhost:87/NotifyUrl.aspx&ipAddress=10.9.26.2&merchantId=888009941120001&requestId=201103071740065878&signType=MD5&type=DirectPay&version=2.0.0&amount=100&bankAbbr=ICBC&currency=00&orderDate=20110307&orderId=201103071740044998&merAcDate=20110307&period=7&periodUnit=02&merchantAbbr=&productDesc=1&productId=2&productName=2&productNum=&reserved1=31&reserved2=2&userToken=15116410263&showUrl=&couponsFlag=00'''
hmac = '865724d8a24ec445e39d327db0a33bd7'

h1 = hashlib.md5(req2.encode()).hexdigest()
print(h1)