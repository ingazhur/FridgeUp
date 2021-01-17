var accountSid = 'AC9b616397831e57f06ee0f6eec20eb791'; // Your Account SID from www.twilio.com/console
var authToken = '525ff2ca841b0f1a4c1b8ca88d34d394';   // Your Auth Token from www.twilio.com/console

var twilio = require('twilio');
var client = new twilio(accountSid, authToken);

client.messages.create({
    body: 'Hello from Node',
    to: '+18479753586',  // Text this number
    from: '+12187369065' // From a valid Twilio number
})
.then((message) => console.log(message.sid));
