from twilio.rest import Client

accountSID = 'AC4912f24a49a900478bcd80eeac5350de'
authToken = '6bd393fc1e457c30580f5178275dcc17'
twilioNumber = '+13608690197'

client = Client(accountSID,authToken)
message = client.messages.create(
    from_ = twilioNumber,
    to = '+886909756966',
    body = '嗨~鯊魚'
)
