import json
import requests

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
currency1 = 'INR'
currency2 = 'USD'
amount = '1000'
querystring = {"from": currency1, "to": currency2, "amount": amount}

headers = {
    "X-RapidAPI-Key": "a12e70917bmsh3387789a04d76bbp1cd75cjsn39153899c063",
    "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
converted_amount = data['result']['convertedAmount']
formatted = '{:,.2f}'.format(converted_amount)
print(formatted)
