from . import app
import requests

role_mappings = {
    "Challenge Creators": "829438730192027703"
}

def execute_webhook(url, message):
    res = requests.post(url, json={
        "content": message
    })
    if res.status_code >= 300:
        print(f"failed to do webhook to {url}: {res.status_code} {res.text}")

def map_to_role(name):
    if name in role_mappings:
        return f"<@&{role_mappings[name]}>"
    return name

def first_blood_hook(name, challenge):
    execute_webhook(app.config['FIRST_BLOOD_WEBHOOK'], f"{map_to_role(name)} got first blood on {challenge}, congrats!")

def solve_hook(name, challenge):
    execute_webhook(app.config['SOLVE_WEBHOOK'], f"{map_to_role(name)} solved {challenge}, congrats!")