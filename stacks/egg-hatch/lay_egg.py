"""Lay a wake egg: your packed Brainstem plus the guide any AI needs, in one rapp/1 organism egg.

    python3 lay_egg.py <your.brainstem.py> <github-login> <name> [out.egg]

<your.brainstem.py> is a packed Brainstem from rapp-brainfreeze (`brainfreeze pack`, or `freeze` then `pack`).
The egg holds it, its soul, a minted rappid and skill.md (how an AI wakes it, talks through it, sends it home).
It is verified with the rapp/1 reference before it is written. No sign-in or key goes in: brainfreeze never
packs them.
"""
import base64
import io
import sys
import tarfile
import time
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import rapp1  # noqa: E402


def soul_of(packed):
    """The soul inside a packed Brainstem (its PAYLOAD zip holds snapshot.tar.gz)."""
    text = packed.decode("utf-8")
    start = text.index("PAYLOAD = (") + len("PAYLOAD = (")
    lines = text[start:text.index("\n)\n", start)].split("\n")
    blob = base64.b64decode("".join(l.strip().strip('"') for l in lines if l.strip()))
    snap = zipfile.ZipFile(io.BytesIO(blob)).read("snapshot.tar.gz")
    with tarfile.open(fileobj=io.BytesIO(snap)) as t:
        return t.extractfile("rapp_brainstem/soul.md").read()


def lay(packed_path, owner, slug, out=None):
    packed = Path(packed_path).read_bytes()
    if b"def host(args)" not in packed:
        raise SystemExit("that file can't wake inside an AI yet: pack it with a brainfreeze that has `host`")
    rid = rapp1.mint_rappid(owner.lower(), slug)
    files = {"rappid.json": rapp1.canonical({"schema": "rapp/1", "rappid": rid}).encode(),
             "soul.md": soul_of(packed), "brainstem.py": packed, "skill.md": (HERE / "skill.md").read_bytes()}
    blob = rapp1.pack_egg("organism", rid, time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime()), files=files,
                          payload={"memory_included": True, "settings_needed": [], "start_here": "skill.md",
                                   "made_with": "RAR stacks/egg-hatch"})
    ok, step, why = rapp1.verify_egg(blob)
    if not ok:
        raise SystemExit(f"laid an egg that fails its own check at {step}: {why}")
    out = Path(out or f"{owner.lower()}--{slug}.egg")
    out.write_bytes(blob)
    return out, rid


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    out, rid = lay(*sys.argv[1:5])
    print(f"laid {out} ({out.stat().st_size} bytes), {rid}; open it with hatch_app.py or hand it to any AI")
