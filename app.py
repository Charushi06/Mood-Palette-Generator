from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Predefined palettes by mood
MOOD_PALETTES = {
    "calm": ["#A8DADC", "#457B9D", "#F1FAEE", "#E63946", "#1D3557"],
    "energetic": ["#FF6B6B", "#FFD93D", "#6BCB77", "#4D96FF", "#FF922B"],
    "romantic": ["#FFC4E1", "#FF758F", "#FFD6D6", "#F67280", "#C06C84"],
    "mysterious": ["#2E2E2E", "#1B1B1B", "#3D3D3D", "#4E4E50", "#6F2232"],
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_palette", methods=["POST"])
def get_palette():
    data = request.get_json()
    mood = data.get("mood")
    palette = MOOD_PALETTES.get(mood.lower(), [])
    return jsonify(palette=palette)

if __name__ == "__main__":
    app.run(debug=True)
