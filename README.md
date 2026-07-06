# Roblox Games Rater

A tiny Flask web app for learning Python, HTML, CSS, Git, and GitHub.

## What Is Inside

- `app.py` starts the web server.
- `templates/games.html` is the page HTML.
- `static/styles.css` controls the page style.
- `TEACHING_SCRIPT.md` is a lesson script for learning Git and GitHub.

## Run It

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Flask:

```bash
pip install -r requirements.txt
```

Start the app:

```bash
python app.py
```

Open the local address shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## The Three Git Ideas

- `git status` asks: what changed?
- `git add .` puts changes in the backpack.
- `git commit -m "message"` makes a checkpoint.
- `git push` uploads checkpoints to GitHub.
- `git pull` downloads new checkpoints from GitHub.
