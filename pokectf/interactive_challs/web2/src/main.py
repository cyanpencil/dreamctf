import flask
import pygments, pygments.lexers, pygments.formatters, pygments.lexers, nord_pygments
import requests
import os

app = flask.Flask(__name__)

def get_content(fname):
    if os.path.isfile(fname):
        with open(fname) as f:
            return f.read()
    elif os.path.isdir(fname):
        return "\n".join(f"- {x}" for x in os.listdir(fname))
    else:
        return "Nothing seems to be here?"

@app.route("/")
def serve():
    filename = flask.request.args.get("highlight", __file__)
    content = get_content(filename)
    try:
        lexer = pygments.lexers.get_lexer_for_filename(filename)
    except:
        lexer = pygments.lexers.special.TextLexer()
    nord_pygments.Nord.background_color = "#2e3440"
    return pygments.highlight(content, lexer, pygments.formatters.HtmlFormatter(full=True, style=nord_pygments.Nord))


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)