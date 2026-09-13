#!/usr/bin/env python3
"""Run only the reviewed, checksum-pinned RAPP Workspace operator."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import urllib.request

EXPECTED = {'schema': 'rapp-repository-bootstrap/1', 'operator': {'version': '0.1.0', 'url': 'https://raw.githubusercontent.com/kody-w/rapp-tools/b0e37eb3c67e309f342629e0ec96dea2688a5951/rapp_workspace.py', 'sha256': '47ba1ee059449758ef56ecdcd944d5e0521df4a23e9d30f14caacaccf5e2a4c9', 'bytes': 83980, 'source_commit': 'b0e37eb3c67e309f342629e0ec96dea2688a5951'}, 'authority': {'repository': 'kody-w/rapp-1', 'commit': 'dda32d741c7218f41443a5bd17eebfe0eae82cb7', 'revision': 'rev-15', 'frame_hash': '83ca275f35cca96e43d75c99d338326c1a39b2240eabf57eb7c29ac96cc90818', 'spec_sha256': '348e7d5baa94aaf2ce4c5354f3cb261f389298a04af65e271a686d3b62f7c384', 'spec_bytes': 79692, 'bootstrap_sha256': '1666e44acf532f854d4bf74868c9af9f9b362055692189ac858a7c8b52dcd5bb', 'verifier_sha256': '4a4c19912063d5ce15cec69b1aca0cebf5df122fb1c481f357f1cf21bc0a07ff', 'profile': 'exact-integer-reference'}, 'workspace_source': {'repository': 'kody-w/rapp-workspace', 'commit': '44f6f124c47ed610b32e4d78f596b9b099669657', 'filename': 'workspace.zip', 'sha256': 'e940960cf245da5e3f603148c32d0337d42369578db1430ade1ce562c68e9793', 'bytes': 1389750}, 'local_only': True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["audit", "bootstrap", "verify"])
    parser.add_argument("--allow-network", action="store_true")
    parser.add_argument("--operator-file", type=Path, help="Offline copy; must match the exact pin")
    args, remaining = parser.parse_known_args()
    here = Path(__file__).absolute()
    if here.is_symlink() or here.parent.is_symlink():
        raise ValueError("The bootstrap control path must not be a symlink")
    root = here.parent.parent.resolve()
    if root == Path.home().resolve() or root == Path(root.anchor):
        raise ValueError("Refusing to bootstrap a broad home/filesystem root")
    config = here.parent / "bootstrap.json"
    if config.is_symlink() or json.loads(config.read_bytes()) != EXPECTED:
        raise ValueError("The reviewed bootstrap configuration changed")
    cache = here.parent / "cache"
    if cache.is_symlink():
        raise ValueError("The private cache must not be a symlink")
    pin = EXPECTED["operator"]
    target = cache / ("bootstrap-operator-" + pin["sha256"] + ".py")
    if target.is_symlink():
        raise ValueError("The pinned operator must not be a symlink")
    if target.is_file():
        data = target.read_bytes()
    elif args.operator_file is not None:
        if args.operator_file.is_symlink():
            raise ValueError("The offline operator must be a regular file")
        data = args.operator_file.read_bytes()
    elif args.allow_network:
        request = urllib.request.Request(pin["url"], headers={"User-Agent": "RAPP-Workspace-Bootstrap/1"})
        with urllib.request.urlopen(request, timeout=40) as response:
            if response.status != 200 or not response.geturl().startswith("https://"):
                raise ValueError("Pinned operator download did not return successful HTTPS content")
            data = response.read(pin["bytes"] + 1)
    else:
        raise ValueError("Cold bootstrap needs --allow-network or an exact --operator-file; no download was attempted")
    if len(data) != pin["bytes"] or hashlib.sha256(data).hexdigest() != pin["sha256"]:
        raise ValueError("The operator bytes do not match the reviewed immutable pin")
    cache.mkdir(mode=0o700, exist_ok=True)
    guard = cache / ".gitignore"
    if guard.is_symlink() or (guard.exists() and guard.read_bytes() != b"*\n"):
        raise ValueError("The private cache Git guard conflicts")
    if not guard.exists():
        with guard.open("xb") as handle:
            handle.write(b"*\n")
    if not target.exists():
        fd, name = tempfile.mkstemp(prefix=".operator-", dir=cache)
        temporary = Path(name)
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(data)
                handle.flush()
                os.fsync(handle.fileno())
            os.link(temporary, target)
        finally:
            temporary.unlink(missing_ok=True)
    if target.is_symlink() or target.read_bytes() != data:
        raise ValueError("The operator changed during cache publication")
    command = [sys.executable, "-I", "-B", str(target), args.operation, str(root), *remaining]
    if args.allow_network:
        command.append("--allow-network")
    environment = {key: value for key, value in os.environ.items()
                   if key in {"PATH","HOME","SYSTEMROOT","WINDIR","TMPDIR","TEMP","TMP","LANG","LC_ALL"}}
    return subprocess.call(command, env=environment)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError) as error:
        print(json.dumps({"ok": False, "error": str(error)}), file=sys.stderr)
        sys.exit(1)
