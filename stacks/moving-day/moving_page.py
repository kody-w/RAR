"""Page: /api/moving/ — the move files on this computer, and a download link for the newest one (this computer only)."""
import os

name = "moving"
MOVES = os.environ.get("MOVING_DAY_DIR") or os.path.expanduser("~/.brainstem/moving-day")


def _files():
    if not os.path.isdir(MOVES):
        return []
    fs = [f for f in os.listdir(MOVES) if f.endswith(".snapshot.tar.gz")]
    return sorted(fs, key=lambda f: os.path.getmtime(os.path.join(MOVES, f)), reverse=True)


def handle(method, path, body):
    fs = _files()
    if path == "latest" and fs:
        import flask
        return flask.send_file(os.path.join(MOVES, fs[0]), as_attachment=True, download_name=fs[0]), 200
    return {"move_files": [{"name": f, "mb": round(os.path.getsize(os.path.join(MOVES, f)) / 1e6, 1)} for f in fs],
            "download_newest": "/api/moving/latest" if fs else None,
            "how": "Say 'pack my Brainstem for moving' to make one; on the new computer say 'unpack my move file'."}, 200
