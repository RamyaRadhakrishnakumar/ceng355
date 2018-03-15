import sys
from firebase import firebase
firebase = firebase.FirebaseApplication('https://qr-merchant.firebaseio.com')
#result = firebase.post('707070','-L7HG_GC6224t03pw3il', {'Account Balance': '3'})
#AccountBalance = firebase.get('/707070','/Account Balance')
AccountBalance = firebase.get('https://qr-merchant.firebaseio.com','/Account Balance')
                                        
#result = firebase.put('/707070','/Account Balance', 17)
#result = firebase.put('https://qr-merchant.firebaseio.com','/Account Balance', 17)

print (AccountBalance)

try:
    while True:
        code = 0;
        code = input("Scan: ")
        finalbalance = float(code) + float(AccountBalance)
        print(finalbalance)
        print("Thank you for paying " + "$" + code)
        #firebase.post('/707070','/-L7HOdwdQJlojKFOCYO7/Account Balance', 'finalbalance')
       # fire = firebase.FirebaseApplication('https://qrmoney-1aec0.firebaseio.com/707070/-L7HOdwdQJlojKFOCYO7/Account Balance')
        #firebase.put('/707070','/Account Balance', float(finalbalance))
        firebase.put('https://qr-merchant.firebaseio.com','/Account Balance', float(finalbalance))

except KeyboardInterrupt:
    print ("\nExit")
# firebase.post('/707070','/-L7HHUkldi2mTXgYokCA','Account Balance', finalbalance)
