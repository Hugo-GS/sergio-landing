import os
from flask import Flask, render_template, abort, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return "Server Test"

@app.route("/landing/<int:id>")
def get_landing(id: int):
    template_folder = f"landing-{id}"
    template_file = f"landing-{id}.html"
    template_path = f"{template_folder}/{template_file}"
    
    full_path = os.path.join(app.template_folder, template_path)
    
    if not os.path.exists(full_path):
        abort(404)
    
    return render_template(template_path)

@app.route("/static/<path:filepath>")
def serve_static(filepath):
    """Sirve cualquier archivo estático (CSS, JS, imágenes, etc.)"""
    file_path = os.path.join(app.static_folder, filepath)
    
    if not os.path.exists(file_path):
        abort(404)
    
    directory = os.path.dirname(file_path)
    filename = os.path.basename(file_path)
    
    return send_from_directory(directory, filename)

if __name__ == "__main__":
    # Render proporciona el puerto a través de la variable de entorno PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)