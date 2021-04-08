import flask
import pygments, pygments.lexers, pygments.formatters, pygments.lexers, nord_pygments
import sqlite3

app = flask.Flask(__name__)

@app.route("/")
def index():
    with open(__file__) as f:
        content = f.read()
    lexer = pygments.lexers.get_lexer_for_filename(__file__)
    nord_pygments.Nord.background_color = "#2e3440"
    return pygments.highlight(content, lexer, pygments.formatters.HtmlFormatter(full=True, style=nord_pygments.Nord))

@app.route("/db")
def db():
    with sqlite3.connect("flag.db") as flagcon:
        with sqlite3.connect(":memory:") as con:
            try:
                con.executescript(flask.request.args.get("script", ""))
                flag = flagcon.execute("SELECT flag FROM flag").fetchone()[0]
                ref = con.execute("SELECT * FROM whatsthis").fetchone()[0]
                if ref == flag:
                    return f"Since you already seem to know it, here's the flag again... {flag}"
                print(ref, flag)
            except:
                pass
    return "Nope"

if __name__ == "__main__":
    with sqlite3.connect("flag.db") as con:
        con.execute("DROP TABLE IF EXISTS flag");
        con.execute("CREATE TABLE flag (flag VARCHAR(80) PRIMARY KEY)");
        with open("flag.txt") as f:
            con.execute("INSERT INTO flag VALUES (?)", (f.read(),))
    app.run("0.0.0.0", 5000)
