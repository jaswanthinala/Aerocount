from twilio.rest import Client

# Twilio credentials (Replace these with your actual credentials)
account_sid = ""
auth_token = ""
twilio_number = ""  # Your Twilio phone number
to_number = ""     # Receiver's phone number (must be in E.164 format)

try:
    # Create a Twilio client
    client = Client(account_sid, auth_token)

    # Send SMS
    message = client.messages.create(
        body=" ",
        from_=twilio_number,
        to=to_number
    )

    print(f"✅ ALooo! Message SID: {message.sid}")

except Exception as e:
    print(f"❌ Error sending message: {str(e)}")

