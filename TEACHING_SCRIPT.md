# Teaching Script: GitHub For An 11-Year-Old

Goal for today: make a GitHub home for the project and learn the daily workflow.

Use this like a conversation. Let the student type as much as possible.

## 1. Explain The Story

Say:

"Our project lives on this computer. Git is like a time machine for the project. GitHub is like a safe online backpack where we can store the project and share it."

The important words:

- Repository: the project folder.
- Commit: a checkpoint in the project.
- Push: upload our checkpoints to GitHub.
- Pull: download new checkpoints from GitHub.
- Clone: make a copy from GitHub onto a computer.

Ask:

"If we break the code, why is a checkpoint useful?"

Expected answer:

"Because we can look back and fix it."

## 2. Show The Project

Open the folder:

```bash
cd roblox-games-rater
```

Show the files:

```bash
ls
```

Say:

"This project has Python, HTML, and CSS. Git watches all of these files."

Run the app:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Stop the server with `Ctrl+C`.

## 3. First Git Commands

Ask Git what it sees:

```bash
git status
```

Say:

"Status is like asking Git: what is different right now?"

Make a tiny change in `templates/games.html`. For example, change the game title.

Ask Git again:

```bash
git status
```

See exactly what changed:

```bash
git diff
```

Say:

"Diff shows the before and after."

## 4. Make A Checkpoint

Put the change in the backpack:

```bash
git add .
```

Make the checkpoint:

```bash
git commit -m "Change game title"
```

Say:

"A good commit message says what changed in a short sentence."

Look at the checkpoints:

```bash
git log --oneline
```

## 5. Upload To GitHub

Upload:

```bash
git push
```

Say:

"Push means GitHub now has the checkpoint too."

Open the GitHub repo page in the browser. Refresh it and show the commit.

## 6. Practice The Daily Loop

Say:

"Every coding session can use the same loop."

The loop:

```bash
git pull
# make a small change
git status
git diff
git add .
git commit -m "Describe the change"
git push
```

Have the student say what each command means:

- Pull: get the newest project.
- Status: see what changed.
- Diff: see the exact edit.
- Add: choose files for the checkpoint.
- Commit: make the checkpoint.
- Push: upload it.

## 7. A Small Challenge

Student task:

1. Add one more game card in `templates/games.html`.
2. Change one color in `static/styles.css`.
3. Run the app and check it in the browser.
4. Commit with:

```bash
git add .
git commit -m "Add another game card"
git push
```

## 8. Rules For Working Together

Say:

"Before you start coding, pull. After you finish a small good change, commit and push."

Rules:

- Pull before starting.
- Make one small change at a time.
- Run the app before pushing.
- Use clear commit messages.
- If Git says something scary, stop and ask before guessing.

## 9. What To Do On Another Computer

Clone the repo:

```bash
git clone REPLACE_WITH_GITHUB_URL
cd roblox-games-rater
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then use the daily loop from section 6.
