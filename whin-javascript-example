const https = require('https')

const data = JSON.stringify({
  phone: 'your_phone_goes_here',
  token: "your_token_goes_here",
  text: "Hello from WHIN!"
})

const options = {
  hostname: 'whin.inutil.info',
  port: 443,
  path: '/whin',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': data.length
  }
}

const req = https.request(options, res => {
  console.log(`statusCode: ${res.statusCode}`)

  res.on('data', d => {
    process.stdout.write(d)
  })
})

req.on('error', error => {
  console.error(error)
})

req.write(data)
req.end()
