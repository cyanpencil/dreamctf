from . import app
import requests

role_mappings = {
    "Challenge Creators": "829438730192027703",
    "Werediscs": "830191378951569428",
    "FTCekoP": "830191390314201150",
    "anti haxxers": "830191403137105930",
    "Almond Butter Banana Ananas": "830191414754410527",
    "carbonara": "830191426641330228",
    "Show Me Your Dance": "830191438288519179",
    "no aspe dai": "830191451395981363",
    "Cyberdawgs": "830191462867009537"
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