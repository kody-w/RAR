"""Share-safe publication gate for the public RAPP Projects projection."""

from __future__ import annotations

import base64
import gzip
import ipaddress
import json
from pathlib import Path
import re

import pytest


ROOT = Path(__file__).resolve().parent.parent
SCOUT = ROOT / "scout"
IDENTITY = "@kody-w/rapp_projects"
SKILL_NAME = "rar-kody-w-rapp-projects"
SOURCE = ROOT / "agents" / "@kody-w" / "rapp_projects_agent.py"
CATALOG_PATH = SCOUT / "catalog" / "catalog.json"
WORKFLOW_ROOT = SCOUT / "workflows" / SKILL_NAME
CAPSULE = re.compile(r"<!--\s*rci-capsule:v1:([A-Za-z0-9+/=]+)\s*-->")

GENERIC_PATH_PARTS = {
    "<name>",
    "<user>",
    "<username>",
    "{name}",
    "{user}",
    "{username}",
    "name",
    "path",
    "user",
    "username",
}
GENERIC_HANDLES = {
    "abstractmethod",
    "classmethod",
    "contextmanager",
    "dataclass",
    "example",
    "overload",
    "owner",
    "property",
    "publisher",
    "rapp",
    "staticmethod",
    "yourname",
}
GENERIC_VALUES = re.compile(
    r"(?:<[^>]+>|\{[^}]+\}|sample|example|demo|placeholder|"
    r"project[-_ ]?(?:name|slug|title)|rapp projects|^main$|^head$)",
    re.IGNORECASE,
)
PRIVATE_METADATA_KEYS = (
    "source_chain",
    "private_source",
    "origin_path",
    "source_transcript",
    "conversation_id",
    "session_id",
    "task_id",
    "worktree",
    "source_head",
)
PROJECT_VALUE_KEYS = (
    "project_slug",
    "project_title",
    "project_head",
    "private_project",
    "source_project",
    "source_title",
    "source_branch",
)


def primary_skill_dir(record: dict) -> Path:
    if record["bundle"] == "starter":
        return SCOUT / "starter" / "skills" / record["skill_name"]
    return (
        SCOUT
        / "bundles"
        / record["bundle"]
        / "skills"
        / record["skill_name"]
    )


def _mask_spans(text: str, spans: list[tuple[int, int]]) -> str:
    masked = list(text)
    for start, end in spans:
        masked[start:end] = " " * (end - start)
    return "".join(masked)


def _balanced_mapping_end(text: str, start: int) -> int:
    opening = text.find("{", start)
    if opening < 0:
        return start
    depth = 0
    quote = ""
    escaped = False
    for index in range(opening, len(text)):
        char = text[index]
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = ""
            continue
        if char in {"'", '"'}:
            quote = char
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index + 1
    return start


def _publisher_safe_text(text: str, role: str) -> str:
    if role == "metadata":
        return text.replace("kody-w", "publisher")

    text = text.replace(IDENTITY, "@publisher/rapp_projects")
    text = text.replace(SKILL_NAME, "rar-publisher-rapp-projects")

    spans: list[tuple[int, int]] = []
    if text.startswith("---"):
        frontmatter_end = text.find("\n---", 3)
        if frontmatter_end >= 0:
            spans.append((0, frontmatter_end + 4))

    for match in re.finditer(r"__manifest__\s*=", text):
        end = _balanced_mapping_end(text, match.start())
        if end > match.start():
            spans.append((match.start(), end))

    for match in re.finditer(
        r"https://raw\.githubusercontent\.com/kody-w/"
        r"[A-Za-z0-9_.-]+/[^\s\"'<>]+",
        text,
    ):
        spans.append(match.span())

    return _mask_spans(text, spans)


def scan_public_text(label: str, text: str, role: str = "content") -> list[str]:
    """Return privacy findings without relying on repository-specific code."""

    findings: list[str] = []

    def add(category: str, detail: str) -> None:
        findings.append(f"{label}: {category}: {detail}")

    publisher_checked = _publisher_safe_text(text, role)
    if re.search(r"(?<![A-Za-z0-9-])kody-w(?![A-Za-z0-9-])", publisher_checked):
        add("publisher identity", "kody-w is outside manifest metadata or a raw URL")

    for pattern, platform in (
        (r"(?<![\w<{}])/(?:Users|home)/([^/\s\"']+)", "POSIX"),
        (r"(?i)\b[A-Z]:\\Users\\([^\\\s\"']+)", "Windows"),
    ):
        for match in re.finditer(pattern, text):
            if match.group(1).lower() not in GENERIC_PATH_PARTS:
                add("personal absolute path", f"{platform} home directory")

    for match in re.finditer(r"(?<![\w.-])@([A-Za-z0-9][A-Za-z0-9-]{1,38})", text):
        handle = match.group(1)
        if handle == "kody-w":
            continue
        if handle.lower() not in GENERIC_HANDLES:
            add("username", f"non-generic @{handle} handle")

    for match in re.finditer(
        r"(?i)[\"'](?:user_?name|github_?user|owner_?name)[\"']"
        r"\s*:\s*[\"']([^\"']+)[\"']",
        text,
    ):
        if match.group(1).lower() not in GENERIC_PATH_PARTS:
            add("username", "concrete username field")

    if re.search(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", text, re.IGNORECASE):
        add("email", "email address")

    phone = re.search(
        r"(?<!\d)(?:\+?1[\s.-]?)?(?:\(\d{3}\)|\d{3})"
        r"[\s.-]\d{3}[\s.-]\d{4}(?!\d)",
        text,
    )
    if phone:
        add("phone", "telephone number")

    if re.search(
        r"\b[A-Z][A-Za-z0-9&.'-]*(?:\s+[A-Z][A-Za-z0-9&.'-]*){0,4}"
        r"\s+(?:Inc\.?|LLC|Ltd\.?|Corp\.?|Corporation|Company|PLC)\b",
        text,
    ):
        add("customer/company", "named legal entity")

    for match in re.finditer(
        r"(?i)[\"'](?:customer_?name|company_?name|tenant_?name|client_?name)"
        r"[\"']\s*:\s*[\"']([^\"']+)[\"']",
        text,
    ):
        if not GENERIC_VALUES.search(match.group(1)):
            add("customer/company", "concrete organization field")

    for private_name in ("RapterBox", "Wildhaven"):
        if re.search(rf"\b{private_name}\b", text, re.IGNORECASE):
            add("private brand", private_name)

    project_keys = "|".join(PROJECT_VALUE_KEYS)
    for match in re.finditer(
        rf"(?i)[\"'](?:{project_keys})[\"']\s*:\s*[\"']([^\"']+)[\"']",
        text,
    ):
        if not GENERIC_VALUES.search(match.group(1)):
            add("private project", f"concrete {match.group(0).split(':', 1)[0]}")
    for match in re.finditer(
        rf"(?im)^\s*(?:{project_keys})\s*=\s*[\"']([^\"']+)[\"']",
        text,
    ):
        if not GENERIC_VALUES.search(match.group(1)):
            add("private project", "concrete project assignment")

    secret_assignment = re.search(
        r"(?i)[\"']?(?:api_?key|access_?token|auth_?token|password|secret)"
        r"[\"']?\s*(?::|=)\s*[\"'](?!<|\{|example|placeholder|redacted)"
        r"([^\"'\s]{8,})[\"']",
        text,
    )
    token_shape = re.search(
        r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|"
        r"sk-[A-Za-z0-9]{20,}|AKIA[A-Z0-9]{16})\b",
        text,
    )
    if secret_assignment or token_shape:
        add("token/secret", "credential-shaped value")

    metadata_keys = "|".join(PRIVATE_METADATA_KEYS)
    if re.search(
        rf"(?i)[\"'](?:{metadata_keys})[\"']\s*(?::|=)"
        rf"(?!\s*(?:None|null|[\"']?(?:<|\{{|demo|example|optional|"
        rf"placeholder|redacted|sample)))",
        text,
    ):
        add("source chain", "private provenance/session metadata")

    host_patterns = (
        r"(?i)\b(?:localhost|[A-Za-z0-9-]+\.local|"
        r"[A-Za-z0-9-]+\.(?:lan|corp|internal))\b",
        r"(?i)\b(?:[A-Za-z0-9]+-(?:macbook|desktop|workstation|laptop)"
        r"(?:-[A-Za-z0-9]+)*|(?:macbook|desktop|workstation|laptop)"
        r"-[A-Za-z0-9][A-Za-z0-9-]*)\b",
    )
    if any(re.search(pattern, text) for pattern in host_patterns):
        add("local hostname", "local-only host")

    for candidate in re.findall(r"(?<![\d.])(?:\d{1,3}\.){3}\d{1,3}(?![\d.])", text):
        try:
            address = ipaddress.ip_address(candidate)
        except ValueError:
            continue
        if address.is_private or address.is_loopback or address.is_link_local:
            add("private network", candidate)

    if re.search(r"\bkodywildfeuer\b", text, re.IGNORECASE):
        add("username", "personal account name")

    return findings


def _capsule_documents(label: str, skill_text: str) -> list[tuple[str, str, str]]:
    documents: list[tuple[str, str, str]] = []
    for index, encoded in enumerate(CAPSULE.findall(skill_text), start=1):
        capsule = json.loads(gzip.decompress(base64.b64decode(encoded)))
        for key in ("description", "instructions", "system_context"):
            value = capsule.get(key)
            if isinstance(value, str):
                documents.append((f"{label} capsule {index}.{key}", value, "content"))
        if isinstance(capsule.get("examples"), list):
            documents.append((
                f"{label} capsule {index}.examples",
                json.dumps(capsule["examples"], sort_keys=True),
                "content",
            ))
        if isinstance(capsule.get("impl"), dict):
            documents.append((
                f"{label} capsule {index}.impl",
                json.dumps(capsule["impl"], sort_keys=True),
                "source",
            ))
        metadata = {
            key: value
            for key, value in capsule.items()
            if key not in {
                "description",
                "examples",
                "impl",
                "instructions",
                "preserved",
                "system_context",
            }
        }
        documents.append((
            f"{label} capsule {index}.metadata",
            json.dumps(metadata, sort_keys=True),
            "metadata",
        ))
        preserved = capsule.get("preserved", {}).get("agent", {})
        if preserved.get("b64"):
            source = gzip.decompress(base64.b64decode(preserved["b64"]))
            documents.append((
                f"{label} capsule {index}.preserved agent",
                source.decode("utf-8"),
                "source",
            ))
    return documents


def publication_documents() -> list[tuple[str, str, str]]:
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    [skill_record] = [
        item for item in catalog["skills"] if item["identity"] == IDENTITY
    ]
    [workflow_record] = [
        item for item in catalog["workflows"] if item["identity"] == IDENTITY
    ]

    skill_root = primary_skill_dir(skill_record)
    workflow_skill = WORKFLOW_ROOT / "skills" / SKILL_NAME
    paths = [
        ("canonical agent", SOURCE, "source"),
        ("generated skill", skill_root / "SKILL.md", "skill"),
        ("generated agent copy", skill_root / SOURCE.name, "source"),
        ("generated lock", skill_root / "rapp" / "agent.lock.json", "metadata"),
        (
            "workflow descriptor",
            WORKFLOW_ROOT / f"workflow--{SKILL_NAME}.json",
            "content",
        ),
        ("workflow README", WORKFLOW_ROOT / "README.md", "content"),
        ("workflow skill copy", workflow_skill / "SKILL.md", "skill"),
        ("workflow agent copy", workflow_skill / SOURCE.name, "source"),
        (
            "workflow lock copy",
            workflow_skill / "rapp" / "agent.lock.json",
            "metadata",
        ),
    ]
    for label, path, _role in paths:
        assert path.is_file(), f"missing publication surface: {label} ({path})"

    documents = [
        (label, path.read_text(encoding="utf-8"), role)
        for label, path, role in paths
    ]
    documents.extend([
        (
            "catalog skill record",
            json.dumps(skill_record, sort_keys=True),
            "metadata",
        ),
        (
            "catalog workflow record",
            json.dumps(workflow_record, sort_keys=True),
            "metadata",
        ),
    ])

    doc_paths = []
    for path in (ROOT / "docs").rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {
            ".json",
            ".md",
            ".txt",
            ".yaml",
            ".yml",
        }:
            continue
        text = path.read_text(encoding="utf-8")
        if IDENTITY in text or SKILL_NAME in text or "RAPP Projects" in text:
            doc_paths.append((path, text))
    assert doc_paths, "RAPP Projects must have a public docs record"
    documents.extend(
        (
            f"docs/{path.relative_to(ROOT / 'docs')}",
            text,
            "metadata" if path.suffix.lower() == ".json" else "content",
        )
        for path, text in doc_paths
    )

    for label, text, _role in list(documents):
        if label.endswith("skill") or "skill copy" in label:
            documents.extend(_capsule_documents(label, text))
    return documents


def test_rapp_projects_publication_is_share_safe():
    findings = []
    for label, text, role in publication_documents():
        findings.extend(scan_public_text(label, text, role))
    assert not findings, "private data reached a public surface:\n" + "\n".join(findings)


SAFE_GENERIC_EXAMPLES = r"""
Use <project-root>, /path/to/project, or C:\path\to\project.
The public identity is @publisher/rapp_projects and depends on @rapp/basic_agent.
{"project_slug": "sample_project", "customer_name": "<customer>"}
https://raw.githubusercontent.com/kody-w/RAR/main/agents/%40kody-w/rapp_projects_agent.py
"""


def test_privacy_scanner_accepts_generic_examples_and_public_identity_locations():
    manifest = '__manifest__ = {"name": "@kody-w/rapp_projects"}'
    schema = '{"session_id": {"type": "string"}}'
    assert scan_public_text("generic examples", SAFE_GENERIC_EXAMPLES) == []
    assert scan_public_text("manifest", manifest, "source") == []
    assert scan_public_text("tool schema", schema, "source") == []
    assert scan_public_text(
        "catalog",
        '{"identity": "@kody-w/rapp_projects"}',
        "metadata",
    ) == []
    assert any(
        ": source chain:" in finding
        for finding in scan_public_text(
            "concrete session",
            '{"session_id": "private-session-value"}',
            "source",
        )
    )


SEEDED_MUTATIONS = [
    ("personal absolute path", 'root = "/Users/alice/secret-project"'),
    ("personal absolute path", r'root = "C:\Users\alice\secret-project"'),
    ("username", '{"username": "alice-smith"}'),
    ("username", "Maintainer: @alice-smith"),
    ("email", "Contact alice.smith@northwind.example"),
    ("phone", "Call +1 (425) 555-0199"),
    ("customer/company", "Prepared for Northwind Biotech LLC"),
    ("customer/company", '{"customer_name": "Northwind Biotech"}'),
    ("private brand", "RapterBox Mk1 handoff"),
    ("private brand", "Wildhaven production plan"),
    ("private project", '{"project_slug": "renewal-war-room"}'),
    ("private project", '{"project_title": "Project Nightingale"}'),
    ("token/secret", "github_token = 'ghp_abcdefghijklmnopqrstuvwxyz123456'"),
    ("source chain", '{"source_chain": ["private-repo@deadbeef"]}'),
    ("local hostname", "http://kody-macbook-pro.local:8080"),
    ("private network", "service_url = 'http://192.168.10.42:8080'"),
    ("publisher identity", "Built by kody-w for local use"),
]


@pytest.mark.parametrize(("category", "mutation"), SEEDED_MUTATIONS)
def test_privacy_scanner_goes_red_for_seeded_mutations(category, mutation):
    assert scan_public_text("clean baseline", SAFE_GENERIC_EXAMPLES) == []
    findings = scan_public_text(
        f"seeded {category}",
        f"{SAFE_GENERIC_EXAMPLES}\n{mutation}",
    )
    assert any(f": {category}:" in finding for finding in findings), findings
