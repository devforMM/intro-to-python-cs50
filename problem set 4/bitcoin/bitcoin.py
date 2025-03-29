import requests
import sys
response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
api=response.json()
bpi=api["bpi"]
usd=bpi["USD"]
rate=usd["rate_float"]
if len(sys.argv)==2:
    nbr=sys.argv[1]
    if  not sys.argv[1].isdigit:
        print("Command-line argument is not a number")
        sys.exit
    else:
        nbr=float(nbr)
        bitcoin=rate*nbr
        print(f"${bitcoin:,.4f}")
elif len(sys.argv)==1:
    print("Missing command-line argument")
elif len(sys.argv)==






