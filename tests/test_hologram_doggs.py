import hashlib
import json
import pathlib
import re


ROOT = pathlib.Path(__file__).resolve().parent.parent
CATALOG = ROOT / "doggs" / "holograms"
RAPPID = re.compile(
    r"^rappid:@[a-z0-9]+(?:-[a-z0-9]+)*/"
    r"[a-z0-9]+(?:-[a-z0-9]+)*:[0-9a-f]{64}$"
)
HEX64 = re.compile(r"^[0-9a-f]{64}$")


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_hologram_dogg_index_and_record_hashes():
    channels = load(ROOT / "doggs" / "index.json")
    assert channels == {
        "schema": "rar-dogg-channels/1.0",
        "channels": [{
            "id": "holograms",
            "name": "Hologram DOGGs",
            "index_url": (
                "https://raw.githubusercontent.com/kody-w/RAR/main/"
                "doggs/holograms/index.json"
            ),
            "record_schema": "rar-hologram-dogg/1.0",
            "consumer": "kody-w/rapp-zoo",
        }],
    }
    index = load(CATALOG / "index.json")
    assert index["schema"] == "rar-hologram-dogg-index/1.0"
    assert index["renderer"] == {
        "repository": "kody-w/rapp-zoo",
        "minimum_version": "1.2.0",
        "engine": "three-r128",
    }
    assert [entry["id"] for entry in index["entries"]] == [
        "holo-avatar",
        "holo-briefing",
        "holo-nexus",
    ]
    for entry in index["entries"]:
        assert RAPPID.fullmatch(entry["rappid"])
        assert HEX64.fullmatch(entry["record_sha256"])
        record_path = CATALOG / f"{entry['id']}.json"
        record_bytes = record_path.read_bytes()
        assert hashlib.sha256(record_bytes).hexdigest() == entry["record_sha256"]
        assert entry["record_url"].endswith(f"/doggs/holograms/{entry['id']}.json")


def test_hologram_doggs_are_closed_data_not_executable_code():
    allowed = {
        "schema",
        "id",
        "rappid",
        "name",
        "kind",
        "version",
        "engine",
        "minimum_zoo_version",
        "description",
        "source_file",
        "default_seed",
        "accent",
        "data_binding",
        "scene",
        "summon",
    }
    for record_path in CATALOG.glob("holo-*.json"):
        record = load(record_path)
        assert set(record) == allowed
        assert record["schema"] == "rar-hologram-dogg/1.0"
        assert record["kind"] in {"character", "data-projection"}
        assert record["engine"] == "three-r128"
        assert RAPPID.fullmatch(record["rappid"])
        assert HEX64.fullmatch(record["default_seed"])
        assert record["summon"] == {
            "adapter": "rapp-zoo",
            "endpoint": "/api/holograms/summon",
        }
        encoded = json.dumps(record).lower()
        for forbidden in (
            "<script",
            "javascript:",
            "shader",
            "http://",
            "https://",
            "eval(",
        ):
            assert forbidden not in encoded
