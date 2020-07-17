import os

import requests

MAILGUN_DOMAIN = os.environ.get("MAILGUN_DOMAINi", None)
MAILGUN_BASE_URL = f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}"


def send_email(to_emails, subject, html_content):
    try:
        r = requests.post(f"{MAILGUN_BASE_URL}/messages",
                          auth=("api", os.environ.get("MAILGUN_API_KEY")),
                          data={"from": f"bgaster <bgaster@{MAILGUN_DOMAIN}>",
                                "to": to_emails,
                                "subject": subject,
                                "html": html_content
                                }
                          )
        print(f"status: {r.status_code}")
        print(f"data: {r.text}")
        print(f"headers: {r.headers}")

    except Exception as e:
        print(f"ERROR: {e}")


