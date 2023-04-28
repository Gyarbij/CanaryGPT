import openai
import os
import json

# Get your API key from the environment variables.
api_key = os.getenv("OPENAI_API_KEY", "your_api_key")
openai.api_key = api_key

# Get sender from environment variables.
sender = os.getenv("SENDER_NAME", "Gyarbij")

# Get a list from the environment variables. 
# Valid input: `$ export RECIPIENT_LIST='["Foo", "bar"]'`
recipients = json.loads(os.getenv("RECIPIENT_LIST", '["John Doe", "Jane Smith", "Michael Brown"]'))

def rewrite_email(email_text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Rewrite the following email in a different way: {email_text}",
        temperature=0.7,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.strip()

email_template = """
Hi {recipient},

We are going to move forward with questionable corporate objective. 

It is designed to achieve maximalist goals while ignoring CSR.

You are the first to know and as such it is highly confidential.

Regards,
{sender}
"""

for recipient in recipients:
    original_email = email_template.format(recipient=recipient, sender=sender)
    rewritten_email = rewrite_email(original_email)
    print(f"Original email to {recipient}:")
    print(original_email)
    print(f"\nRewritten email to {recipient}:")
    print(rewritten_email)
    print("\n" + "-"*40 + "\n")
