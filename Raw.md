#Sending whin from any system is extremely simple.
whin uses a backend that is triggered on the endpoint https://whin.inutil.info/whin
All you need to do is to POST the text you want to send, together with your credentials in the right format.

While the rest of the documents will include examples in specific tools  or languages, this is a very simple definition of the structure.

URL: https://whin.inutil.info/whin
Request Type: POST
Payload: JSON with: {type='text, phone='xxxxxxxx', token='xxxxxxxxx'}

And that is it pretty much. 
