import requests

url = 'https://whin.inutil.info/whin'
postdata = {'phone': 'your_whatsapp_number', 'token':'your_token_number', 'text':'Hello from WHIN'}

x = requests.post(url, data = postdata)

print(x.text)
