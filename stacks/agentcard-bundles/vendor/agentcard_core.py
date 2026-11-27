"""Agent cards: one Brainstem agent (a *_agent.py file) packed so it can be traded.

A card is a JSON object:

    {
      "schema": "rapp-agent-card/1",
      "name": "PipelineVelocityAgent",        # the agent's tool name (^[A-Za-z0-9_-]+$)
      "file": "pipeline_velocity_agent.py",   # where it lands in agents/
      "version": "1.0.0",
      "author": "kody-w",
      "description": "...",
      "parameters": {...},                    # copy of metadata["parameters"], for preview only
      "requires": ["requests"],               # non-stdlib modules the source imports
      "permissions": ["network", "memory"],   # what the source appears to touch (labels, not a sandbox)
      "source": "<the whole Python file>",
      "sha256": "<sha256 of source, utf-8>",
      "files": [{"path": "lib/pypdf-6.0.0-py3-none-any.whl", "sha256": "...", "b64": "..."}],
                                              # optional: what the agent needs, carried INSIDE the card
                                              # (pure-Python wheels and sibling .py files only, never native code)
      "signer": "<base64 Ed25519 public key>",   # optional
      "signature": "<base64 Ed25519 signature>"  # optional, over signing_message(card)
    }

The fields a signature covers are name, version and sha256 (which pins the source), so a
signer vouches for exactly this code. Cards travel as .agentcard files (the JSON) or as
links: rapp://card?d=<base64url(raw-deflate(compact JSON))>, small enough for a QR code
when the agent is small.

This module is plain standard-library Python. It runs on the phone inside the app and on
any computer through tools/agentcard.py.
"""
import base64
import hashlib
import json
import re
import zlib

SCHEMA = "rapp-agent-card/1"
LINK_PREFIX = "rapp://card?d="
NAME_RE = re.compile(r"^[A-Za-z0-9_-]+$")
FILE_RE = re.compile(r"^[A-Za-z0-9_]+_agent\.py$")
MAX_SOURCE_BYTES = 512 * 1024
MAX_FILES_BYTES = 16 * 1024 * 1024
FILE_PATH_RE = re.compile(r"^lib/(?:[A-Za-z0-9_.+-]+-(?:py3|py2\.py3|py3[0-9]+)-none-any\.whl|[A-Za-z0-9_]+\.py)$")
NATIVE_SUFFIXES = (".so", ".dylib", ".pyd", ".dll", ".a", ".o")


class CardError(ValueError):
    pass


def source_sha256(source: str) -> str:
    return hashlib.sha256(source.encode("utf-8")).hexdigest()


def files_sha256(card: dict) -> str:
    """One fingerprint over every carried file (path and hash, sorted by path). Empty when there are none."""
    files = card.get("files") or []
    if not files:
        return ""
    lines = sorted(f"{f['path']} {f['sha256']}" for f in files)
    return hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()


def signing_message(card: dict) -> bytes:
    """The exact bytes a card's signature covers. The Swift app builds the same bytes.
    A card that carries files adds one line, the fingerprint of those files; older cards are unchanged."""
    msg = f"{SCHEMA}\n{card['name']}\n{card['version']}\n{card['sha256']}"
    fs = files_sha256(card)
    return (msg + (f"\n{fs}" if fs else "")).encode("utf-8")


def file_problems(files) -> list:
    """Carried files must be pure Python, fingerprinted, and inside lib/. Wheels are opened and checked for native code."""
    import io, zipfile
    if not isinstance(files, list):
        return ["files must be a list"]
    out, total, seen = [], 0, set()
    for i, f in enumerate(files, 1):
        if not isinstance(f, dict) or not all(isinstance(f.get(k), str) for k in ("path", "sha256", "b64")):
            out.append(f"file {i} needs path, sha256 and b64 as strings"); continue
        path = f["path"]
        if path in seen:
            out.append(f"{path} is listed twice"); continue
        seen.add(path)
        if not FILE_PATH_RE.match(path):
            out.append(f"{path}: only lib/<pure-Python wheel ending -none-any.whl> or lib/<name>.py can ride on a card"); continue
        try:
            data = base64.b64decode(f["b64"], validate=True)
        except ValueError:
            out.append(f"{path}: b64 does not decode"); continue
        total += len(data)
        if hashlib.sha256(data).hexdigest() != f["sha256"]:
            out.append(f"{path} does not match its fingerprint"); continue
        if path.endswith(".whl"):
            try:
                names = zipfile.ZipFile(io.BytesIO(data)).namelist()
            except zipfile.BadZipFile:
                out.append(f"{path} is not a readable wheel"); continue
            bad = [n for n in names if n.lower().endswith(NATIVE_SUFFIXES) or n.startswith("/") or ".." in n.split("/")]
            if bad:
                out.append(f"{path} carries native or unsafe files ({bad[0]}); only pure Python can run on this phone")
    if total > MAX_FILES_BYTES:
        out.append(f"carried files are {total // 1024} KB, more than {MAX_FILES_BYTES // (1024 * 1024)} MB")
    return out


def problems(card) -> list:
    """Everything wrong with a card's shape and fingerprint. Empty list means it is well formed.
    Signatures are checked separately (verify_signature), because a card may be unsigned."""
    if not isinstance(card, dict):
        return ["a card must be a JSON object"]
    out = []
    if card.get("schema") != SCHEMA:
        out.append(f"schema must be {SCHEMA!r}, got {card.get('schema')!r}")
    for key in ("name", "file", "version", "source", "sha256"):
        if not isinstance(card.get(key), str) or not card.get(key):
            out.append(f"{key} is missing or not a string")
    if out:
        return out
    if not NAME_RE.match(card["name"]):
        out.append(f"name {card['name']!r} is not tool-safe (letters, digits, _ and - only)")
    if not FILE_RE.match(card["file"]):
        out.append(f"file {card['file']!r} must be a plain name ending in _agent.py")
    if len(card["source"].encode("utf-8")) > MAX_SOURCE_BYTES:
        out.append(f"source is larger than {MAX_SOURCE_BYTES // 1024} KB")
    actual = source_sha256(card["source"])
    if actual != card["sha256"]:
        out.append(f"sha256 does not match the source (card says {card['sha256'][:12]}…, source is {actual[:12]}…)")
    if ("signature" in card) != ("signer" in card):
        out.append("signature and signer must come together")
    if "files" in card:
        out.extend(file_problems(card["files"]))
    for key in ("requires", "permissions"):
        if key in card and not (isinstance(card[key], list) and all(isinstance(x, str) for x in card[key])):
            out.append(f"{key} must be a list of strings")
    return out


def verify_signature(card: dict):
    """True / False if the card is signed and a verifier is available, None if unsigned or no verifier.
    The phone checks signatures with CryptoKit; on a computer this uses `cryptography` when installed."""
    if "signature" not in card:
        return None
    try:
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
        from cryptography.exceptions import InvalidSignature
    except ImportError:
        return None
    try:
        key = Ed25519PublicKey.from_public_bytes(base64.b64decode(card["signer"]))
        key.verify(base64.b64decode(card["signature"]), signing_message(card))
        return True
    except (InvalidSignature, ValueError):
        return False


def to_json(card: dict) -> str:
    return json.dumps(card, indent=2, ensure_ascii=False) + "\n"


def to_link(card: dict) -> str:
    raw = json.dumps(card, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    comp = zlib.compressobj(9, zlib.DEFLATED, -15)   # raw deflate: what Apple's Compression calls ZLIB
    packed = comp.compress(raw) + comp.flush()
    return LINK_PREFIX + base64.urlsafe_b64encode(packed).decode("ascii").rstrip("=")


def parse(data) -> dict:
    """A card from .agentcard bytes/text or a rapp://card link."""
    if isinstance(data, bytes):
        data = data.decode("utf-8")
    text = data.strip()
    if text.startswith(LINK_PREFIX):
        b64 = text[len(LINK_PREFIX):].split("&", 1)[0]
        b64 += "=" * (-len(b64) % 4)
        try:
            raw = zlib.decompress(base64.urlsafe_b64decode(b64), -15, )
        except (zlib.error, ValueError) as e:
            raise CardError(f"the link does not decode: {e}")
        text = raw.decode("utf-8")
    try:
        card = json.loads(text)
    except json.JSONDecodeError as e:
        raise CardError(f"not a card (bad JSON: {e})")
    if not isinstance(card, dict):
        raise CardError("not a card (JSON is not an object)")
    return card
