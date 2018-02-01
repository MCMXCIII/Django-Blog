import requests
import urllib.request, json
with urllib.request.urlopen("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD") as url:
    data = json.loads(url.read().decode())
    #for printing the data i need.
    #print(data)
    print(coin, " is : ", [data][0]['USD'])
    #print(str( "Hello " + [data][0]['USD']))
