import openai
import os

api_key = os.getenv("OPENAI_API_KEY", "your_api_key")
openai.api_key = api_key

recipients = ["John Doe", "Jane Smith", "Michael Brown"]

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
Dear {recipient},

We are going to move forward with possibly shady corporate goals. It is designed to achieve maximalist goals.

You are the first to know and as such it is highly confidential.

Regards,
Gyarbij
"""

for recipient in recipients:
    original_email = email_template.format(recipient=recipient)
    rewritten_email = rewrite_email(original_email)
    print(f"Original email to {recipient}:")
    print(original_email)
    print(f"\nRewritten email to {recipient}:")
    print(rewritten_email)
    print("\n" + "-"*40 + "\n")
