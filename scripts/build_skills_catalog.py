#!/usr/bin/env python3
"""Build the distinct, static RAR Skills catalog without executing skill code.

Canonical skill records live at ``skills/@publisher/slug/manifest.json`` and
point to immutable GitHub revisions. Existing Scout skills are projected into
the same read-only catalog with an explicit relationship to their source
artifact; they never become duplicate agent registry entries.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path, PurePosixPath


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
SCOUT_CATALOG = REPO_ROOT / "scout" / "catalog" / "catalog.json"
OUTPUT = REPO_ROOT / "api" / "v1" / "skills.json"
LIFECYCLE_FILE = REPO_ROOT / "state" / "skill_lifecycle.json"
RECEIPTS_DIR = REPO_ROOT / "state" / "skill-receipts"

SKILL_SCHEMA = "rar-skill/1.0"
CATALOG_SCHEMA = "rar-skills-catalog/1.0"
MANIFEST_HASH_ALGORITHM = "sha256-canonical-json-v1"
FILE_HASH_ALGORITHM = "sha256"
RAW_BASE = "https://raw.githubusercontent.com/kody-w/RAR/main"
PAGES_BASE = "https://kody-w.github.io/RAR"
MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_TOTAL_BYTES = 8 * 1024 * 1024

NAME_RE = re.compile(
    r"^@(?P<publisher>[A-Za-z0-9](?:[A-Za-z0-9-]{0,38}))/"
    r"(?P<slug>[a-z0-9]+(?:-[a-z0-9]+)*)$"
)
REPOSITORY_RE = re.compile(
    r"^(?P<owner>[A-Za-z0-9](?:[A-Za-z0-9-]{0,38}))/"
    r"(?P<repo>[A-Za-z0-9_.-]+)$"
)
SEMVER_RE = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")
DIGEST_RE = re.compile(r"^[0-9a-f]{64}$")
REVISION_RE = re.compile(r"^[0-9a-f]{40}$")
TAG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PATH_RE = re.compile(r"^[A-Za-z0-9._/-]+$")

REQUIRED_FIELDS = {
    "schema",
    "artifact_type",
    "name",
    "version",
    "display_name",
    "description",
    "author",
    "tags",
    "source",
    "install",
    "protocol_conformance",
}
OPTIONAL_FIELDS = {
    "category",
    "compatibility",
    "license",
    "relationships",
}
SEARCH_STOPWORDS = {
    "and",
    "are",
    "for",
    "from",
    "into",
    "its",
    "that",
    "the",
    "this",
    "with",
}


class SkillMetadataError(ValueError):
    """Raised when a skill record cannot be admitted safely."""


def canonical_json(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )


def render_manifest(manifest: dict) -> bytes:
    return (
        json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    ).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def manifest_sha256(manifest: dict) -> str:
    return sha256_bytes(render_manifest(manifest))


def semver_key(value: str) -> tuple[int, int, int] | None:
    match = SEMVER_RE.fullmatch(str(value or ""))
    if not match:
        return None
    return tuple(int(part) for part in match.groups())


def normalize_digest(value: str) -> str:
    return str(value or "").strip().lower().removeprefix("sha256:")


def parse_skill_name(name: str) -> tuple[str, str] | None:
    match = NAME_RE.fullmatch(str(name or ""))
    if not match:
        return None
    return f"@{match.group('publisher')}", match.group("slug")


def safe_relative_path(value: object) -> str | None:
    text = str(value or "")
    if (
        not text
        or not PATH_RE.fullmatch(text)
        or "\\" in text
        or any(ord(char) < 32 for char in text)
    ):
        return None
    path = PurePosixPath(text)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        return None
    return path.as_posix()


def canonical_manifest_path(name: str, *, root: Path | None = None) -> Path:
    parsed = parse_skill_name(name)
    if not parsed:
        raise SkillMetadataError(
            "Skill name must be @publisher/lowercase-kebab-case"
        )
    publisher, slug = parsed
    return (root or SKILLS_DIR) / publisher / slug / "manifest.json"


def _require_text(
    manifest: dict,
    field: str,
    errors: list[str],
    *,
    maximum: int,
) -> None:
    value = manifest.get(field)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{field} must be a non-empty string")
    elif len(value) > maximum:
        errors.append(f"{field} must be at most {maximum} characters")


def validate_manifest(
    manifest: object,
    *,
    expected_name: str | None = None,
    expected_path: Path | None = None,
) -> list[str]:
    if not isinstance(manifest, dict):
        return ["skill artifact must be a JSON object"]

    errors: list[str] = []
    missing = sorted(REQUIRED_FIELDS - set(manifest))
    unknown = sorted(set(manifest) - REQUIRED_FIELDS - OPTIONAL_FIELDS)
    errors.extend(f"Missing required field: {field}" for field in missing)
    errors.extend(f"Unsupported field: {field}" for field in unknown)

    if manifest.get("schema") != SKILL_SCHEMA:
        errors.append(f"schema must be '{SKILL_SCHEMA}'")
    if manifest.get("artifact_type") != "skill":
        errors.append("artifact_type must be 'skill'")

    parsed_name = parse_skill_name(manifest.get("name", ""))
    if not parsed_name:
        errors.append("name must be @publisher/lowercase-kebab-case")
    elif expected_name and manifest["name"].casefold() != expected_name.casefold():
        errors.append("manifest name does not match requested skill identity")

    if semver_key(str(manifest.get("version") or "")) is None:
        errors.append("version must be MAJOR.MINOR.PATCH semver")

    _require_text(manifest, "display_name", errors, maximum=120)
    _require_text(manifest, "description", errors, maximum=500)
    _require_text(manifest, "author", errors, maximum=120)

    tags = manifest.get("tags")
    if not isinstance(tags, list) or not tags:
        errors.append("tags must be a non-empty list")
    elif (
        len(tags) > 20
        or any(not isinstance(tag, str) or not TAG_RE.fullmatch(tag) for tag in tags)
        or len(tags) != len(set(tags))
    ):
        errors.append("tags must be unique lowercase kebab-case strings (max 20)")

    category = manifest.get("category")
    if category is not None and (
        not isinstance(category, str) or not TAG_RE.fullmatch(category)
    ):
        errors.append("category must be lowercase kebab-case when present")

    license_name = manifest.get("license")
    if license_name is not None and (
        not isinstance(license_name, str)
        or not license_name.strip()
        or len(license_name) > 80
    ):
        errors.append("license must be a non-empty string when present")

    source = manifest.get("source")
    if not isinstance(source, dict):
        errors.append("source must be an object")
        source = {}
    source_unknown = sorted(
        set(source) - {"repository", "revision", "entrypoint", "files"}
    )
    errors.extend(f"Unsupported source field: {field}" for field in source_unknown)

    repository = source.get("repository")
    repo_match = (
        REPOSITORY_RE.fullmatch(repository)
        if isinstance(repository, str)
        else None
    )
    if not repo_match:
        errors.append("source.repository must be a GitHub owner/repository")

    revision = source.get("revision")
    if not isinstance(revision, str) or not REVISION_RE.fullmatch(revision):
        errors.append("source.revision must be a full lowercase 40-character commit")

    entrypoint = safe_relative_path(source.get("entrypoint"))
    if not entrypoint or PurePosixPath(entrypoint).name != "SKILL.md":
        errors.append("source.entrypoint must be a safe path ending in SKILL.md")

    files = source.get("files")
    normalized_files: list[tuple[str, str]] = []
    if not isinstance(files, list) or not files:
        errors.append("source.files must be a non-empty list")
    elif len(files) > 64:
        errors.append("source.files may contain at most 64 files")
    else:
        for index, item in enumerate(files):
            if not isinstance(item, dict):
                errors.append(f"source.files[{index}] must be an object")
                continue
            unknown_file_fields = sorted(set(item) - {"path", "sha256", "media_type"})
            errors.extend(
                f"Unsupported source.files[{index}] field: {field}"
                for field in unknown_file_fields
            )
            path = safe_relative_path(item.get("path"))
            digest = normalize_digest(item.get("sha256", ""))
            if not path:
                errors.append(f"source.files[{index}].path is unsafe")
            if not DIGEST_RE.fullmatch(digest):
                errors.append(
                    f"source.files[{index}].sha256 must be a lowercase SHA-256"
                )
            media_type = item.get("media_type")
            if media_type is not None and (
                not isinstance(media_type, str)
                or not media_type.strip()
                or len(media_type) > 120
            ):
                errors.append(
                    f"source.files[{index}].media_type must be a short string"
                )
            if path and DIGEST_RE.fullmatch(digest):
                normalized_files.append((path, digest))

    file_paths = [path for path, _digest in normalized_files]
    if len(file_paths) != len(set(file_paths)):
        errors.append("source.files paths must be unique")
    if entrypoint and file_paths and entrypoint not in file_paths:
        errors.append("source.entrypoint must appear in source.files")
    if entrypoint:
        root = PurePosixPath(entrypoint).parent
        for path in file_paths:
            try:
                PurePosixPath(path).relative_to(root)
            except ValueError:
                errors.append(
                    "every source.files path must stay under the SKILL.md directory"
                )
                break

    install = manifest.get("install")
    if not isinstance(install, dict):
        errors.append("install must be an object")
        install = {}
    install_unknown = sorted(set(install) - {"strategy", "destination"})
    errors.extend(
        f"Unsupported install field: {field}" for field in install_unknown
    )
    if install.get("strategy") != "copy-files":
        errors.append("install.strategy must be 'copy-files'")
    destination = safe_relative_path(install.get("destination"))
    if not destination:
        errors.append("install.destination must be a safe relative path")
    elif parsed_name and PurePosixPath(destination).name != parsed_name[1]:
        errors.append("install.destination must end with the skill slug")

    conformance = manifest.get("protocol_conformance")
    if not isinstance(conformance, dict):
        errors.append("protocol_conformance must be an object")
        conformance = {}
    conformance_unknown = sorted(
        set(conformance) - {"profile", "status", "evidence"}
    )
    errors.extend(
        f"Unsupported protocol_conformance field: {field}"
        for field in conformance_unknown
    )
    if conformance.get("status") != "not_assessed":
        errors.append(
            "public submissions must set protocol_conformance.status to "
            "'not_assessed'; catalog admission is not protocol certification"
        )
    profile = conformance.get("profile")
    if profile is not None and (
        not isinstance(profile, str) or not profile.strip() or len(profile) > 80
    ):
        errors.append("protocol_conformance.profile must be null or a short string")
    evidence = conformance.get("evidence", [])
    if evidence != []:
        errors.append(
            "public submissions cannot self-assert protocol conformance evidence"
        )

    compatibility = manifest.get("compatibility")
    if compatibility is not None:
        if not isinstance(compatibility, dict):
            errors.append("compatibility must be an object when present")
        else:
            compatibility_unknown = sorted(
                set(compatibility) - {"rapp_protocol"}
            )
            errors.extend(
                f"Unsupported compatibility field: {field}"
                for field in compatibility_unknown
            )
            if compatibility.get("rapp_protocol") not in {
                "required",
                "optional",
                "not-applicable",
            }:
                errors.append(
                    "compatibility.rapp_protocol must be required, optional, "
                    "or not-applicable"
                )

    relationships = manifest.get("relationships", [])
    if not isinstance(relationships, list):
        errors.append("relationships must be a list when present")
    else:
        for index, relationship in enumerate(relationships):
            if not isinstance(relationship, dict):
                errors.append(f"relationships[{index}] must be an object")
                continue
            if set(relationship) != {"type", "artifact_type", "name"}:
                errors.append(
                    f"relationships[{index}] must contain type, artifact_type, name"
                )
                continue
            if relationship["type"] not in {
                "projection_of",
                "companion_to",
                "supersedes",
            }:
                errors.append(f"relationships[{index}].type is unsupported")
            if relationship["artifact_type"] not in {
                "agent",
                "skill",
                "rapplication",
            }:
                errors.append(
                    f"relationships[{index}].artifact_type is unsupported"
                )
            if not isinstance(relationship["name"], str) or not relationship[
                "name"
            ].strip():
                errors.append(f"relationships[{index}].name is required")

    if expected_path is not None and parsed_name:
        expected = canonical_manifest_path(
            manifest["name"],
            root=expected_path.parents[2],
        )
        if expected.resolve() != expected_path.resolve():
            errors.append("manifest path does not match its namespaced identity")

    return errors


def load_manifest(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SkillMetadataError(f"{path}: invalid JSON: {exc}") from exc
    errors = validate_manifest(value, expected_path=path)
    if errors:
        raise SkillMetadataError(f"{path}: {'; '.join(errors)}")
    return value


def source_url(repository: str, revision: str, path: str) -> str:
    return (
        f"https://raw.githubusercontent.com/{repository}/{revision}/{path}"
    )


def _fetch_bytes(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "rar-skill-ingest/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        declared = response.headers.get("Content-Length")
        if declared and int(declared) > MAX_FILE_BYTES:
            raise SkillMetadataError(f"source file exceeds {MAX_FILE_BYTES} bytes")
        data = response.read(MAX_FILE_BYTES + 1)
    if len(data) > MAX_FILE_BYTES:
        raise SkillMetadataError(f"source file exceeds {MAX_FILE_BYTES} bytes")
    return data


FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---", re.DOTALL)


def parse_frontmatter(markdown: str) -> dict[str, str]:
    match = FRONTMATTER_RE.match(markdown)
    if not match:
        return {}
    fields: dict[str, str] = {}
    key: str | None = None
    for line in match.group(1).splitlines():
        if re.match(r"^[A-Za-z_-]+:", line):
            key, _, value = line.partition(":")
            value = value.strip().strip("\"'")
            if value in {">", "|", ">-", "|-", ">+", "|+"}:
                value = ""
            fields[key.strip()] = value
        elif key and line.startswith(("  ", "\t")):
            fields[key] = (fields[key] + " " + line.strip()).strip()
    return fields


def fetch_source_files(
    manifest: dict,
    *,
    fetcher=None,
) -> dict[str, bytes]:
    errors = validate_manifest(manifest)
    if errors:
        raise SkillMetadataError("; ".join(errors))
    fetcher = fetcher or _fetch_bytes
    source = manifest["source"]
    fetched: dict[str, bytes] = {}
    total = 0
    for item in source["files"]:
        path = item["path"]
        url = source_url(source["repository"], source["revision"], path)
        try:
            data = fetcher(url)
        except (OSError, ValueError, urllib.error.URLError) as exc:
            raise SkillMetadataError(f"could not fetch {path}: {exc}") from exc
        total += len(data)
        if total > MAX_TOTAL_BYTES:
            raise SkillMetadataError(
                f"skill source exceeds {MAX_TOTAL_BYTES} total bytes"
            )
        actual = sha256_bytes(data)
        expected = normalize_digest(item["sha256"])
        if actual != expected:
            raise SkillMetadataError(
                f"{path}: SHA-256 mismatch (expected {expected}, got {actual})"
            )
        fetched[path] = data

    entrypoint = source["entrypoint"]
    try:
        frontmatter = parse_frontmatter(fetched[entrypoint].decode("utf-8"))
    except UnicodeDecodeError as exc:
        raise SkillMetadataError("SKILL.md must be UTF-8") from exc
    slug = parse_skill_name(manifest["name"])[1]
    if frontmatter.get("name") != slug:
        raise SkillMetadataError(
            f"SKILL.md frontmatter name must be '{slug}'"
        )
    if not frontmatter.get("description"):
        raise SkillMetadataError("SKILL.md frontmatter description is required")
    return fetched


def _search_terms(*values: object) -> list[str]:
    terms: list[str] = []
    seen: set[str] = set()
    for value in values:
        if isinstance(value, list):
            text = " ".join(str(item) for item in value)
        else:
            text = str(value or "")
        for token in re.findall(r"[a-z0-9]+", text.lower()):
            if (
                len(token) <= 1
                or token in SEARCH_STOPWORDS
                or token in seen
            ):
                continue
            seen.add(token)
            terms.append(token)
            if len(terms) == 32:
                return terms
    return terms


def _review_state(manifest: dict, path: Path, lifecycle: dict) -> dict:
    name = manifest["name"]
    record = (lifecycle.get("skills") or {}).get(name)
    if not isinstance(record, dict) or record.get("status") != "active":
        raise SkillMetadataError(
            f"{path}: accepted skills require an active front-door lifecycle record"
        )
    relative = path.relative_to(REPO_ROOT).as_posix()
    digest = sha256_bytes(path.read_bytes())
    if (
        record.get("canonical_path") != relative
        or record.get("sha256") != digest
        or record.get("version") != manifest["version"]
    ):
        raise SkillMetadataError(
            f"{path}: lifecycle projection does not match canonical manifest"
        )
    receipt_id = str(record.get("latest_receipt") or "")
    prefix = "rar_skill_"
    if not receipt_id.startswith(prefix):
        raise SkillMetadataError(f"{path}: lifecycle has no skill receipt")
    receipt_path = RECEIPTS_DIR / f"{receipt_id.removeprefix(prefix)}.json"
    if not receipt_path.exists():
        raise SkillMetadataError(f"{path}: skill receipt is missing")
    try:
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SkillMetadataError(f"{receipt_path}: invalid receipt: {exc}") from exc
    if (
        receipt.get("schema") != "rar-skill-receipt/1.0"
        or receipt.get("id") != receipt_id
        or receipt.get("skill") != name
        or receipt.get("canonical_path") != relative
        or (receipt.get("artifact") or {}).get("digest") != digest
    ):
        raise SkillMetadataError(f"{receipt_path}: receipt does not bind the manifest")
    return {
        "status": "notarized",
        "receipt": receipt_id,
        "revision_id": receipt.get("revision_id", ""),
        "accepted_at": receipt.get("created_at", ""),
    }


def _published_record(
    manifest: dict,
    path: Path,
    lifecycle: dict,
) -> dict:
    publisher, slug = parse_skill_name(manifest["name"])
    source = manifest["source"]
    files = [
        {
            **item,
            "sha256": normalize_digest(item["sha256"]),
            "url": source_url(
                source["repository"],
                source["revision"],
                item["path"],
            ),
        }
        for item in source["files"]
    ]
    entrypoint_file = next(
        item for item in files if item["path"] == source["entrypoint"]
    )
    relative_manifest = path.relative_to(REPO_ROOT).as_posix()
    return {
        "artifact_type": "skill",
        "catalog_origin": "reviewed-submission",
        "name": manifest["name"],
        "namespace": publisher,
        "slug": slug,
        "version": manifest["version"],
        "display_name": manifest["display_name"],
        "description": manifest["description"],
        "author": manifest["author"],
        "tags": manifest["tags"],
        "category": manifest.get("category", ""),
        "license": manifest.get("license", ""),
        "compatibility": manifest.get("compatibility", {}),
        "protocol_conformance": manifest["protocol_conformance"],
        "relationships": manifest.get("relationships", []),
        "review": _review_state(manifest, path, lifecycle),
        "search_terms": _search_terms(
            manifest["name"],
            manifest["display_name"],
            manifest["description"],
            manifest["tags"],
            manifest.get("category", ""),
        ),
        "manifest": {
            "path": relative_manifest,
            "url": f"{RAW_BASE}/{relative_manifest}",
            "sha256": sha256_bytes(path.read_bytes()),
            "hash_algorithm": MANIFEST_HASH_ALGORITHM,
        },
        "source": {
            "repository": source["repository"],
            "revision": source["revision"],
            "entrypoint": source["entrypoint"],
            "entrypoint_url": entrypoint_file["url"],
            "files": files,
            "hash_algorithm": FILE_HASH_ALGORITHM,
        },
        "install": {
            **manifest["install"],
            "entrypoint": PurePosixPath(source["entrypoint"]).name,
            "verify": "sha256-before-use",
        },
    }


def _scout_file_path(url: str) -> str:
    marker = "/main/"
    if marker not in url:
        return ""
    return url.split(marker, 1)[1]


def _projection_record(record: dict) -> dict | None:
    skill_name = str(record.get("skill_name") or "")
    if not TAG_RE.fullmatch(skill_name):
        return None
    files = []
    for item in record.get("files") or []:
        path = _scout_file_path(str(item.get("url") or ""))
        digest = normalize_digest(item.get("sha256", ""))
        if not path or not DIGEST_RE.fullmatch(digest):
            return None
        files.append(
            {
                "path": path,
                "sha256": digest,
                "url": str(item["url"]),
            }
        )
    entrypoint = next(
        (item for item in files if PurePosixPath(item["path"]).name == "SKILL.md"),
        None,
    )
    if not files or entrypoint is None:
        return None

    source_kind = str(record.get("source_kind") or "")
    identity = str(record.get("identity") or "")
    relationship_type = (
        "rapplication" if source_kind == "federated-rapplication" else "agent"
    )
    relationships = []
    if identity:
        relationships.append(
            {
                "type": "projection_of",
                "artifact_type": relationship_type,
                "name": identity,
            }
        )
    return {
        "artifact_type": "skill",
        "catalog_origin": "generated-projection",
        "name": f"@rar-scout/{skill_name}",
        "namespace": "@rar-scout",
        "slug": skill_name,
        "version": str(record.get("version") or "0.0.0"),
        "display_name": skill_name,
        "description": str(record.get("description") or ""),
        "author": "RAR Scout projection",
        "tags": sorted(
            {
                "scout",
                "projection",
                str(record.get("channel") or "native"),
            }
        ),
        "category": "projection",
        "license": "",
        "compatibility": {},
        "protocol_conformance": {
            "profile": None,
            "status": "not_assessed",
            "evidence": [],
        },
        "relationships": relationships,
        "search_terms": _search_terms(
            skill_name,
            identity,
            record.get("description", ""),
            record.get("channel", ""),
        ),
        "manifest": None,
        "source": {
            "repository": "kody-w/RAR",
            "revision": None,
            "source_kind": source_kind,
            "input_revision": record.get("source_commit"),
            "artifact_sha256": normalize_digest(record.get("source_sha256", "")),
            "entrypoint": entrypoint["path"],
            "entrypoint_url": entrypoint["url"],
            "files": files,
            "hash_algorithm": FILE_HASH_ALGORITHM,
            "projection_generator": {
                "schema": "rar-scout/1.0",
                "toaster_commit": None,
            },
        },
        "install": {
            "strategy": "scout-import",
            "import_url": str(record.get("import_url") or ""),
            "bundle": str(record.get("bundle") or ""),
            "skill_name": skill_name,
            "entrypoint": "SKILL.md",
            "verify": "sha256-before-use",
        },
    }


def discover_published_manifests() -> list[tuple[Path, dict]]:
    if not SKILLS_DIR.exists():
        return []
    found = []
    for path in sorted(SKILLS_DIR.glob("@*/*/manifest.json")):
        found.append((path, load_manifest(path)))
    return found


def load_scout_projections() -> tuple[list[dict], dict]:
    if not SCOUT_CATALOG.exists():
        return [], {}
    try:
        source = json.loads(SCOUT_CATALOG.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SkillMetadataError(f"{SCOUT_CATALOG}: invalid JSON: {exc}") from exc
    if source.get("schema") != "rar-scout-catalog/1.0":
        raise SkillMetadataError("scout catalog has an unsupported schema")
    toaster = source.get("toaster") or {}
    records = []
    for source_record in source.get("skills") or []:
        record = _projection_record(source_record)
        if record is None:
            raise SkillMetadataError(
                f"invalid Scout skill projection: {source_record.get('skill_name')}"
            )
        record["source"]["projection_generator"]["toaster_commit"] = toaster.get(
            "commit"
        )
        records.append(record)
    return records, toaster


def build_catalog() -> dict:
    if LIFECYCLE_FILE.exists():
        try:
            lifecycle = json.loads(LIFECYCLE_FILE.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise SkillMetadataError(
                f"{LIFECYCLE_FILE}: invalid lifecycle JSON: {exc}"
            ) from exc
    else:
        lifecycle = {"schema": "rar-skill-lifecycle/1.0", "skills": {}}
    if lifecycle.get("schema") != "rar-skill-lifecycle/1.0":
        raise SkillMetadataError("skill lifecycle has an unsupported schema")

    published = [
        _published_record(manifest, path, lifecycle)
        for path, manifest in discover_published_manifests()
    ]
    projections, toaster = load_scout_projections()
    records = sorted(
        published + projections,
        key=lambda item: (item["name"], item["catalog_origin"]),
    )
    names = [record["name"] for record in records]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        raise SkillMetadataError(
            f"duplicate skill identities: {', '.join(duplicates[:5])}"
        )

    input_hashes = {
        "canonical_manifests": sha256_bytes(
            canonical_json(
                [
                    {
                        "path": path.relative_to(REPO_ROOT).as_posix(),
                        "sha256": sha256_bytes(path.read_bytes()),
                    }
                    for path, _manifest in discover_published_manifests()
                ]
            ).encode("utf-8")
        ),
        "scout_catalog": (
            sha256_bytes(SCOUT_CATALOG.read_bytes())
            if SCOUT_CATALOG.exists()
            else None
        ),
        "skill_lifecycle": (
            sha256_bytes(LIFECYCLE_FILE.read_bytes())
            if LIFECYCLE_FILE.exists()
            else None
        ),
    }
    return {
        "schema": CATALOG_SCHEMA,
        "artifact_type": "skill-catalog",
        "description": (
            "Static catalog of reviewed portable skills and generated Scout "
            "projections. Skill artifact kind is independent from protocol "
            "conformance; catalog admission never implies runtime or "
            "authenticated RAPP/1 compliance."
        ),
        "self_url": f"{RAW_BASE}/api/v1/skills.json",
        "site_url": f"{PAGES_BASE}/skills.html",
        "hashing": {
            "manifest": MANIFEST_HASH_ALGORITHM,
            "files": FILE_HASH_ALGORITHM,
        },
        "inputs": {
            **input_hashes,
            "scout_toaster": toaster or None,
        },
        "counts": {
            "total": len(records),
            "reviewed_submissions": len(published),
            "generated_projections": len(projections),
        },
        "skills": records,
    }


def serialized_catalog() -> bytes:
    return (
        json.dumps(build_catalog(), indent=2, ensure_ascii=False, sort_keys=True)
        + "\n"
    ).encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail when api/v1/skills.json is not the deterministic projection",
    )
    args = parser.parse_args()
    try:
        rendered = serialized_catalog()
    except SkillMetadataError as exc:
        print(f"[skills] {exc}", file=sys.stderr)
        return 1

    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_bytes() != rendered:
            print(
                "[skills] api/v1/skills.json is stale; run "
                "python3 scripts/build_skills_catalog.py",
                file=sys.stderr,
            )
            return 1
        print("[skills] catalog is current")
        return 0

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(rendered)
    catalog = json.loads(rendered)
    print(
        "[skills] wrote "
        f"{catalog['counts']['total']} skills "
        f"({catalog['counts']['reviewed_submissions']} reviewed, "
        f"{catalog['counts']['generated_projections']} projections) "
        f"to {OUTPUT.relative_to(REPO_ROOT)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
