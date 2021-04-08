import flask
import pygments, pygments.lexers, pygments.formatters, nord_pygments
import requests, ipaddress

app = flask.Flask(__name__)

@app.route("/")
def serve():
    with open(__file__) as f:
        content = f.read()
    try:
        lexer = pygments.lexers.get_lexer_for_filename(__file__)
    except:
        lexer = pygments.lexers.special.TextLexer()
    nord_pygments.Nord.background_color = "#2e3440"
    return pygments.highlight(content, lexer, pygments.formatters.HtmlFormatter(full=True, style=nord_pygments.Nord))

@app.route("/hit_it")
def hit_it():
    target = flask.request.args.get("it")
    if not target:
        return "Aww?"
    if any(x in target for x in ["127", "local", "flag"]):
        return "Nah, bruv"
    return requests.get(target).text

@app.route("/flag")
def flag():
    if ipaddress.ip_address(flask.request.remote_addr).is_loopback:
        return open("flag.txt").read()
    else:
        return flask.redirect("https://youtu.be/dQw4w9WgXcQ")

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)