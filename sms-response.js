const accountSid = process.env.TWILIO_ACCOUNT_SID; // Your Account SID from www.twilio.com/console
const authToken = process.env.TWILIO_AUTH_TOKEN;   // Your Auth Token from www.twilio.com/console

const client = require('twilio')(accountSid, authToken);

client.messages.create({
    body: 'Hello from Node',
    to: '+18473933309',  // Text this number
    from: '+12187369065' // From a valid Twilio number
})
.then((message) => console.log(message.sid));
