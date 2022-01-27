# What is WHIN
Whin is a free implemebtation of a Whatsapp notification service. 
It is free of charge and comes without any commitment from our end but the 'we'll do our best to keep it running' will.
Use it and share it as you deem appropriate; just bear in mind this is not professionally mantained and runs in home labs.
Do not use this service for confidential information. We've tried to do things right but you never know, do you?
We do not track users or messages information, but a method to check issued tokens against phone numbers.

# What is this repository for
This repository is intended to host mini-guides on how to use whin on different platforms. 
It'd be extrmely helpful if you help us with your own area of expertise/technology.

# Getting your token:
In order to protect your privacy, whin will check you are the one sending the notifications to yourself.
To do so, whin uses a pair of token / phone-number where token is your secret.
To get your token, you just need to send a Whatsapp Text to +34613164997 with the word signup and whin will send you your personal token.
You may use this link for that:  https://wa.me/34613164997?text=signup

Note that the Phone and Token values are linked, this means that the node wont work if the phone number used to get the token is not matching the one you used to get the token. This is to prevent spam.

The token is valid for 30 days. Everytime you send a whatsapp message, Time-To-Live is reset to 30 days. Keep using the service from time to time, and it won't expire. If for whatever reason you do not use the service for 30 days, your token will be removed from the cache. Dont panic, you can get a new token repeating the signup process.

