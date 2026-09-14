import json
from pathlib import Path
from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)

# Resolves to src/data/roblox_games.json
DATA_FILE = Path(__file__).resolve().parent / "data" / "roblox_games.json"


def load_games():
    """Load the games list from the JSON file."""
    if not DATA_FILE.exists():
        return []
    with open(str(DATA_FILE), "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


import os 
def save_games(games): 
    """Save the updated list of games back to the JSON file.""" 
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True) 
    temp_file = DATA_FILE.with_name(DATA_FILE.name + ".tmp") 
    with open(str(temp_file), "w", encoding="utf-8") as file: 
        json.dump(games, file, indent=2, ensure_ascii=False) 
    os.replace(str(temp_file), str(DATA_FILE))

@app.route("/")
def games():
    games_list = load_games()
    return render_template("games.html", games=games_list)


@app.route("/games/<int:game_id>")
def game_details(game_id):
    games_list = load_games()
    # Find game by its 'id' field rather than list index
    game = next((g for g in games_list if g.get("id") == game_id), None)

    if game is None:
        abort(404)

    return render_template("game_details.html", game=game)


@app.route("/addgame")
def addgame():
    return render_template("addgame.html")


@app.route("/add", methods=["POST"])
def add():
    games_list = load_games()

    # Determine the next unique ID
    new_id = max([g.get("id", 0) for g in games_list], default=0) + 1

    new_game = {
        "id": new_id,
        "title": request.form.get("title", "").strip(),
        "genre": request.form.get("genre", "").strip(),
        "subgenre": request.form.get("sub-genre", "").strip(),
        "description": request.form.get("description", "").strip(),
        "roblox_url": request.form.get("game-link", "").strip(),
        "rating": request.form.get("rating", "").strip(),
        "image": request.form.get("image", "").strip(),
        "comment": request.form.get("comment", "").strip(),
        "visits": request.form.get("visits", "").strip(),
        "likes": request.form.get("likes", "").strip(),
    }

    games_list.append(new_game)
    save_games(games_list)

    return redirect(url_for("games"))


if __name__ == "__main__":
    app.run(debug=True)