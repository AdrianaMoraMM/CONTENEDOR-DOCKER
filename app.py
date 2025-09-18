from flask import Flask, render_template_string

app = Flask(__name__)

# Cargar tu HTML directamente desde el archivo
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

@app.route("/")
def index():
    return render_template_string(html_content)

if __name__ == "__main__":
    # Escuchar en todas las interfaces para que Docker pueda acceder
    app.run(host="0.0.0.0", port=80)