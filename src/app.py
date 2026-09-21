import json
import os
from pathlib import Path
from flask import Flask, abort, redirect, render_template, request, url_for

app = Flask(__name__)

# Primary data file inside the project workspace
PRIMARY_DATA_FILE = Path(__file__).resolve().parent / "data" / "roblox_games.json"

# Fallback data file in LocalAppData (used when Windows Defender Controlled Folder Access protects Documents)
FALLBACK_DATA_FILE = (
    Path(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")))
    / "roblox-games-rater"
    / "roblox_games.json"
)

# Kept for backward compatibility
DATA_FILE = PRIMARY_DATA_FILE


def get_active_data_file():
    """Determine which file has the latest data."""
    if FALLBACK_DATA_FILE.exists():
        if not PRIMARY_DATA_FILE.exists():
            return FALLBACK_DATA_FILE
        try:
            if FALLBACK_DATA_FILE.stat().st_mtime >= PRIMARY_DATA_FILE.stat().st_mtime:
                return FALLBACK_DATA_FILE
        except OSError:
            return PRIMARY_DATA_FILE
    return PRIMARY_DATA_FILE


def load_games():
    """Load the games list from the active JSON file."""
    active_file = get_active_data_file()
    if not active_file.exists():
        return []
    try:
        with open(str(active_file), "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        secondary = PRIMARY_DATA_FILE if active_file == FALLBACK_DATA_FILE else FALLBACK_DATA_FILE
        if secondary.exists():
            try:
                with open(str(secondary), "r", encoding="utf-8") as file:
                    return json.load(file)
            except (json.JSONDecodeError, OSError):
                return []
        return []


def save_games(games):
    """Save the updated list of games back to the JSON file, with automatic fallback."""
    saved_primary = False

    # Try saving to primary workspace data file first
    try:
        PRIMARY_DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        temp_file = PRIMARY_DATA_FILE.with_name(PRIMARY_DATA_FILE.name + ".tmp")
        with open(str(temp_file), "w", encoding="utf-8") as file:
            json.dump(games, file, indent=2, ensure_ascii=False)
        os.replace(str(temp_file), str(PRIMARY_DATA_FILE))
        saved_primary = True
    except (OSError, IOError, PermissionError):
        # Controlled Folder Access or file lock prevented saving to workspace
        saved_primary = False

    # If saving to primary failed, save to user AppData fallback
    if not saved_primary:
        FALLBACK_DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        temp_file = FALLBACK_DATA_FILE.with_name(FALLBACK_DATA_FILE.name + ".tmp")
        with open(str(temp_file), "w", encoding="utf-8") as file:
            json.dump(games, file, indent=2, ensure_ascii=False)
        os.replace(str(temp_file), str(FALLBACK_DATA_FILE))

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