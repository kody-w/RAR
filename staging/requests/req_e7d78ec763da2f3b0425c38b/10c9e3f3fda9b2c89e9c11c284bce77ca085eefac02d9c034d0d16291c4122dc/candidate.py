"""RAPP Roadside: deterministic, local-only RAPP setup support.

The agent diagnoses sanitized observations, recommends exactly one bounded
next action, can apply one allow-listed repair to a sanitized copy, and can
retest against canonical assertions derived from a verified diagnosis.
Maintainer-side work is handed to RAPP Pit Crew.
"""

from __future__ import annotations

import hashlib
import json
import os
import platform as host_platform
import re
import shutil
import stat
import sys
from pathlib import Path

try:
    from agents.basic_agent import BasicAgent
except ImportError:
    class BasicAgent:
        def __init__(self, name=None, metadata=None):
            if name is not None:
                self.name = name
            if metadata is not None:
                self.metadata = metadata

        def perform(self, **kwargs):
            return "Not implemented."

        def to_tool(self):
            return {
                "type": "function",
                "function": {
                    "name": self.name,
                    "description": self.metadata.get("description", ""),
                    "parameters": self.metadata.get("parameters", {}),
                },
            }


__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@kody-w/rar_installer_troubleshooter_agent",
    "version": "1.0.0",
    "display_name": "RAPP Roadside",
    "maintainer_system": "RAPP Pit Crew",
    "machine_issue_artifact": "Roadside Frame",
    "closed_loop": "RAPP Roadside Closed Loop",
    "issue_signature_domain": "rapp-roadside:issue-signature/v1",
    "protocol_identity_retained": True,
    "description": (
        "Diagnoses RAPP setup from sanitized local observations, emits exactly "
        "one bounded next action, optionally applies an allow-listed repair "
        "to a sanitized copy, and retests canonical verified assertions without "
        "collecting credentials or changing the Grail. Routes maintainer work "
        "to RAPP Pit Crew, treats reporting-AI text/logs as hostile data, "
        "binds exact replay and supply-chain bytes, quarantines unsafe reports, "
        "uses bounded sharded cells with measured backpressure, and verifies "
        "the RAPP Roadside Closed Loop through customer confirmation."
    ),
    "author": "kody-w",
    "repository": "https://github.com/kody-w/rapp-roadside",
    "license": "MIT",
    "copyright": "2026 kody-w",
    "telemetry": False,
    "network_default": False,
    "participation": "voluntary",
    "closed_loop": "RAPP Roadside Closed Loop",
    "issue_signature_domain": "rapp-roadside:issue-signature/v1",
    "tags": [
        "rapp",
        "installer",
        "troubleshooting",
        "local-first",
        "deterministic",
        "toasted",
    ],
    "category": "devtools",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
}

REPORT_SCHEMA = "rar-installer-troubleshooter/report-1"
RETEST_SCHEMA = "rar-installer-troubleshooter/retest-1"
FIX_SCHEMA = "rar-installer-troubleshooter/fix-receipt-1"
CAPABILITY_SCHEMA = "rar-installer-troubleshooter/capability-1"
APPROVAL_SCHEMA = "rapp-roadside/repair-approval-1"
CONFIRMATION_SCHEMA = "rapp-roadside/customer-confirmation-1"
STABLE_MAIN_IDENTITY = "kody-w/rapp-roadside@main"
INSTALLER_FRAME_VERSION = "rapp-roadside-installer-frame/1.0"
ISSUE_SIGNATURE_DOMAIN = "rapp-roadside:issue-signature/v1"
WIRE = {
    "method": "POST",
    "path": "/chat",
    "request_field": "user_input",
    "success_keys": ["response", "agent_logs", "session_id"],
}
SENSITIVE_KEY = re.compile(
    r"(?:^|[_-])(?:api[_-]?key|authorization|bearer|credential|oauth|"
    r"pass(?:word)?|private[_-]?key|secret|session[_-]?cookie|token)(?:$|[_-])",
    re.IGNORECASE,
)
SENSITIVE_VALUE = re.compile(
    r"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|"
    r"bearer\s+[A-Za-z0-9._~+/-]{12,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)",
    re.IGNORECASE,
)
EXCLUDED_PATH_PART = re.compile(
    r"(?:^|[._-])(?:auth|credential|oauth|password|private|secret|token|key)"
    r"(?:$|[._-])",
    re.IGNORECASE,
)
EXCLUDED_NAMES = {
    ".copilot_session",
    ".copilot_token",
    ".env",
    ".git",
    ".brainstem_data",
    "__pycache__",
    "node_modules",
    "venv",
    ".venv",
}
COPY_SUFFIXES = {
    ".cmd",
    ".css",
    ".html",
    ".json",
    ".md",
    ".ps1",
    ".py",
    ".sh",
    ".txt",
    ".yaml",
    ".yml",
}
COPY_NAMES = {"brainstem", "LICENSE", "VERSION"}
MAX_COPY_FILES = 1000
MAX_COPY_BYTES = 20_000_000
HASH64 = re.compile(r"^[0-9a-f]{64}$")
COMMIT40 = re.compile(r"^[0-9a-f]{40}$")
ATTACHMENT_MEDIA = {
    "application/json": ".json",
    "text/markdown": ".md",
    "text/plain": ".txt",
    "text/x-log": ".log",
}
MAX_ATTACHMENTS = 8
MAX_ATTACHMENT_BYTES = 2_000_000
MAX_ATTACHMENT_TOTAL_BYTES = 8_000_000
COPY_REPAIR_ACTIONS = {
    "normalize-windows-launchers-copy",
    "restore-launcher-executable-copy",
    "restore-launcher-files-copy",
    "synchronize-installer-mirrors-copy",
}
COPY_REPAIR_FILES = {
    "normalize-windows-launchers-copy": (
        "install.ps1",
        "install.cmd",
    ),
    "restore-launcher-executable-copy": (
        "start.sh",
        "installer/brainstem",
    ),
    "restore-launcher-files-copy": (
        "installer/brainstem",
        "installer/brainstem.cmd",
        "installer/brainstem-boot.cjs",
    ),
    "synchronize-installer-mirrors-copy": (
        "install.sh",
        "install.ps1",
        "install.cmd",
    ),
}
SENSITIVE_ASSIGNMENT = re.compile(
    rb"(?i)(?:api[_-]?key|authorization|bearer|credential|oauth|"
    rb"pass(?:word)?|private[_-]?key|secret|session[_-]?cookie|token)"
    rb"\s*[:=]\s*[^\s,;]+"
)
NONPUBLIC_PATH = re.compile(
    rb"(?:/"
    + b"Users/"
    + rb"[^/\s]+|/home/[^/\s]+|/var/|/private/var/|"
    + rb"[A-Za-z]:\\"
    + b"Users"
    + rb"\\[^\\\s]+)"
)
PROTECTED_REPAIR_ROOTS = (
    Path("/etc"),
    Path("/private"),
    Path("/System"),
    Path("/usr"),
    Path("/var"),
)
ENVIRONMENT_FIELDS = (
    "architecture",
    "certificate_state",
    "clock_state",
    "filesystem",
    "locale",
    "managed_policy",
    "os_build",
    "proxy_state",
    "security_product_state",
    "shell",
)
BINDING_FIELDS = (
    "catalog_sha256",
    "dependency_lock_sha256",
    "installer_release_frame_sha256",
    "ring_manifest_sha256",
    "source_tree_sha256",
)


def _canonical_json(value):
    return json.dumps(
        value,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )


def _pretty(value):
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True)


def _sha256_bytes(value):
    return hashlib.sha256(value).hexdigest()


def _content_id(value):
    return _sha256_bytes(_canonical_json(value).encode("utf-8"))


def _load_json(path_value):
    path = Path(str(path_value)).expanduser().resolve()
    data = path.read_bytes()
    if len(data) > 1_000_000:
        raise ValueError("JSON input exceeds the 1 MiB local limit")
    result = json.loads(data.decode("utf-8"))
    if not isinstance(result, dict):
        raise TypeError("JSON input must be one object")
    return result


def _assert_no_sensitive_input(value, location="$"):
    if isinstance(value, dict):
        for key, item in value.items():
            key_text = str(key)
            if SENSITIVE_KEY.search(key_text):
                raise ValueError(
                    f"sensitive input field is not accepted: {location}.{key_text}"
                )
            _assert_no_sensitive_input(item, f"{location}.{key_text}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _assert_no_sensitive_input(item, f"{location}[{index}]")
    elif isinstance(value, str):
        if SENSITIVE_VALUE.search(value):
            raise ValueError(
                f"credential-like value is not accepted at {location}"
            )
        if value.startswith(("http://", "https://")) and not value.startswith(
            (
                "http://127.0.0.1",
                "http://localhost",
                "http://[::1]",
            )
        ):
            raise ValueError(
                f"non-loopback URL is not accepted at {location}"
            )


def _require_object_shape(value, required, optional, location):
    if not isinstance(value, dict):
        raise TypeError(f"{location} must be an object")
    missing = sorted(set(required) - set(value))
    extra = sorted(set(value) - set(required) - set(optional))
    if missing:
        raise ValueError(f"{location} is missing fields: {', '.join(missing)}")
    if extra:
        raise ValueError(f"{location} has unsupported fields: {', '.join(extra)}")


def _validate_observation_shape(observations):
    _require_object_shape(
        observations,
        {
            "case_id",
            "platform",
            "setup_elapsed_seconds",
            "setup_stage",
            "source",
            "launcher",
            "python",
            "health",
            "chat",
            "installers",
            "repository",
            "safety",
        },
        {
            "attachments",
            "bindings",
            "cell",
            "environment",
            "failure_code",
            "probe_url",
            "probe_mode",
            "replay",
            "reporting_ai",
            "signature_phase",
            "signature_input_hashes",
            "transport",
        },
        "observations",
    )
    shapes = {
        "source": {"present"},
        "launcher": {"present", "executable"},
        "python": {"version"},
        "health": {"status", "http_status"},
        "chat": {
            "method",
            "path",
            "request_field",
            "http_status",
            "response_keys",
        },
        "installers": {"docs_mirrors_match"},
        "repository": {"direct_main_change_requested"},
        "safety": {"external_network_observed", "grail_modified"},
    }
    for key, required in shapes.items():
        _require_object_shape(observations[key], required, set(), f"observations.{key}")
    for location, value in (
        ("source.present", observations["source"]["present"]),
        ("launcher.present", observations["launcher"]["present"]),
        ("launcher.executable", observations["launcher"]["executable"]),
        (
            "installers.docs_mirrors_match",
            observations["installers"]["docs_mirrors_match"],
        ),
        (
            "repository.direct_main_change_requested",
            observations["repository"]["direct_main_change_requested"],
        ),
        (
            "safety.external_network_observed",
            observations["safety"]["external_network_observed"],
        ),
        ("safety.grail_modified", observations["safety"]["grail_modified"]),
    ):
        if not isinstance(value, bool):
            raise TypeError(f"observations.{location} must be boolean")
    if not isinstance(observations["chat"]["response_keys"], list):
        raise TypeError("observations.chat.response_keys must be an array")
    for field in ("failure_code", "signature_phase"):
        if field in observations and not re.fullmatch(
            r"[a-z0-9]+(?:-[a-z0-9]+)*",
            str(observations[field]),
        ):
            raise ValueError(f"observations.{field} must be lowercase kebab-case")
    if "signature_input_hashes" in observations:
        hashes = observations["signature_input_hashes"]
        if (
            not isinstance(hashes, list)
            or len(hashes) != 2
            or any(not isinstance(item, str) or not HASH64.fullmatch(item) for item in hashes)
        ):
            raise ValueError(
                "observations.signature_input_hashes must contain exactly two SHA-256 values"
            )
    if observations.get("probe_mode", "direct") not in {
        "direct",
        "follow-up",
        "inventory",
    }:
        raise ValueError(
            "observations.probe_mode must be direct, inventory, or follow-up"
        )


def _optional_object(value, required, location):
    if value is None:
        return None
    _require_object_shape(value, required, set(), location)
    return value


def _normalize_unknown_context(observations):
    environment = observations.get("environment")
    if environment is None:
        environment = {field: "unknown" for field in ENVIRONMENT_FIELDS}
        environment_reported = False
    else:
        _optional_object(
            environment,
            set(ENVIRONMENT_FIELDS),
            "observations.environment",
        )
        environment = {
            field: str(environment[field] or "unknown").strip().lower()
            for field in ENVIRONMENT_FIELDS
        }
        environment_reported = True

    bindings = observations.get("bindings")
    if bindings is None:
        bindings = {
            "ring": None,
            "installer_release_frame_version": None,
            "source_commit": None,
            "installer_sha256s": {},
            "unreported_fields": sorted(
                {
                    "ring",
                    "installer_release_frame_version",
                    "source_commit",
                    "installer_sha256s",
                    *BINDING_FIELDS,
                }
            ),
            **{field: None for field in BINDING_FIELDS},
        }
        bindings_reported = False
    else:
        _optional_object(
            bindings,
            {
                "catalog_sha256",
                "dependency_lock_sha256",
                "installer_sha256s",
                "installer_release_frame_sha256",
                "installer_release_frame_version",
                "ring",
                "ring_manifest_sha256",
                "source_commit",
                "source_tree_sha256",
                "unreported_fields",
            },
            "observations.bindings",
        )
        if not isinstance(bindings["installer_sha256s"], dict):
            raise TypeError("observations.bindings.installer_sha256s must be an object")
        if (
            not isinstance(bindings["unreported_fields"], list)
            or not all(
                isinstance(item, str)
                for item in bindings["unreported_fields"]
            )
        ):
            raise TypeError(
                "observations.bindings.unreported_fields must be a string array"
            )
        bindings = dict(bindings)
        expected_unreported = {
            key
            for key, value in bindings.items()
            if key != "unreported_fields" and (value is None or value == {})
        }
        if set(bindings["unreported_fields"]) != expected_unreported:
            raise ValueError(
                "observations.bindings.unreported_fields must exactly name unavailable bindings"
            )
        bindings_reported = True

    reporting_ai = observations.get("reporting_ai")
    if reporting_ai is None:
        reporting_ai = {
            "text_present": False,
            "text_sha256": None,
            "text_bytes": 0,
            "log_count": 0,
            "log_sha256s": [],
            "instruction_markers_detected": False,
            "observed_claim_ids": [],
            "inferred_claim_ids": [],
        }
    else:
        _optional_object(
            reporting_ai,
            {
                "inferred_claim_ids",
                "instruction_markers_detected",
                "log_count",
                "log_sha256s",
                "observed_claim_ids",
                "text_bytes",
                "text_present",
                "text_sha256",
            },
            "observations.reporting_ai",
        )
        reporting_ai = dict(reporting_ai)

    attachments = observations.get("attachments") or []
    if not isinstance(attachments, list):
        raise TypeError("observations.attachments must be an array")

    replay = observations.get("replay")
    if replay is None:
        replay = {
            "argv": [],
            "logical_cwd": "<unreported>",
            "input_sha256": "unknown",
            "before_state_sha256": "unknown",
            "phase": "unknown",
            "duration_ms": None,
            "output_sha256": "unknown",
            "output_bytes": None,
        }
        replay_reported = False
    else:
        _optional_object(
            replay,
            {
                "argv",
                "before_state_sha256",
                "duration_ms",
                "input_sha256",
                "logical_cwd",
                "output_bytes",
                "output_sha256",
                "phase",
            },
            "observations.replay",
        )
        if not isinstance(replay["argv"], list) or not all(
            isinstance(item, str) for item in replay["argv"]
        ):
            raise TypeError("observations.replay.argv must be a string array")
        replay = dict(replay)
        replay_reported = True

    transport = observations.get("transport")
    if transport is None:
        transport = {
            "report_id": "unknown",
            "created_epoch": None,
            "received_epoch": None,
            "ttl_seconds": 86_400,
            "source_cell_id": "local-untransported",
            "source_verified": True,
            "frame_verified": True,
            "trust_weight_bps": 10_000,
            "dedupe_count": 0,
            "rate_window_seconds": 3600,
            "rate_count": 1,
            "rate_limit": 3,
            "correlation_id": None,
            "correlation_disclosed": True,
        }
        transport_reported = False
    else:
        _optional_object(
            transport,
            {
                "correlation_disclosed",
                "correlation_id",
                "created_epoch",
                "dedupe_count",
                "frame_verified",
                "rate_count",
                "rate_limit",
                "rate_window_seconds",
                "received_epoch",
                "report_id",
                "source_cell_id",
                "source_verified",
                "trust_weight_bps",
                "ttl_seconds",
            },
            "observations.transport",
        )
        transport = dict(transport)
        transport_reported = True

    cell = observations.get("cell")
    if cell is None:
        cell = {
            "cell_id": "local-roadside-cell",
            "shard_key_sha256": _content_id(
                {"case_id": observations.get("case_id")}
            ),
            "queue_depth": 0,
            "backpressure_threshold": 8,
            "max_queue_depth": 32,
            "local_raw_retention_seconds": 0,
            "global_raw_data_store": False,
            "global_lock": False,
            "global_exchange": "verified-signatures-frames-aggregate-evidence-only",
            "hot_cache_hits": 0,
            "negative_cache_hits": 0,
            "fairness_lane": "normal",
            "marginal_information_gain_bps": 0,
        }
        cell_reported = False
    else:
        _optional_object(
            cell,
            {
                "backpressure_threshold",
                "cell_id",
                "global_exchange",
                "global_lock",
                "global_raw_data_store",
                "hot_cache_hits",
                "local_raw_retention_seconds",
                "marginal_information_gain_bps",
                "max_queue_depth",
                "negative_cache_hits",
                "queue_depth",
                "shard_key_sha256",
                "fairness_lane",
            },
            "observations.cell",
        )
        cell = dict(cell)
        cell_reported = True

    return {
        "environment": environment,
        "environment_reported": environment_reported,
        "bindings": bindings,
        "bindings_reported": bindings_reported,
        "reporting_ai": reporting_ai,
        "attachments": attachments,
        "replay": replay,
        "replay_reported": replay_reported,
        "transport": transport,
        "transport_reported": transport_reported,
        "cell": cell,
        "cell_reported": cell_reported,
    }


def _unknown_hash(value):
    return not isinstance(value, str) or not HASH64.fullmatch(value)


def _context_findings(context):
    quarantine = []
    reporting = context["reporting_ai"]
    if reporting.get("instruction_markers_detected") is True:
        quarantine.append("hostile-instruction-marker")
    if reporting.get("text_present"):
        if _unknown_hash(reporting.get("text_sha256")):
            quarantine.append("reporting-ai-text-hash-missing")
        if not isinstance(reporting.get("text_bytes"), int) or not 0 <= reporting.get(
            "text_bytes", -1
        ) <= 1_000_000:
            quarantine.append("reporting-ai-text-size-invalid")
    log_hashes = reporting.get("log_sha256s")
    if not isinstance(log_hashes, list) or any(
        not isinstance(item, str) or not HASH64.fullmatch(item)
        for item in (log_hashes if isinstance(log_hashes, list) else [])
    ):
        quarantine.append("reporting-ai-log-hash-invalid")
    if reporting.get("log_count") != len(log_hashes or []):
        quarantine.append("reporting-ai-log-count-mismatch")
    observed_claims = reporting.get("observed_claim_ids")
    inferred_claims = reporting.get("inferred_claim_ids")
    if (
        not isinstance(observed_claims, list)
        or not isinstance(inferred_claims, list)
        or not all(isinstance(item, str) for item in observed_claims)
        or not all(isinstance(item, str) for item in inferred_claims)
        or set(observed_claims).intersection(inferred_claims)
    ):
        quarantine.append("observed-inferred-partition-invalid")

    attachments = context["attachments"]
    if len(attachments) > MAX_ATTACHMENTS:
        quarantine.append("attachment-count-exceeded")
    attachment_total = 0
    attachment_records = []
    for index, item in enumerate(attachments):
        if not isinstance(item, dict):
            quarantine.append(f"attachment-{index}-not-object")
            continue
        required = {"name", "media_type", "sha256", "bytes"}
        if set(item) != required:
            quarantine.append(f"attachment-{index}-shape")
            continue
        name = str(item["name"])
        media_type = str(item["media_type"])
        size = item["bytes"]
        digest = str(item["sha256"])
        expected_suffix = ATTACHMENT_MEDIA.get(media_type)
        if (
            "/" in name
            or "\\" in name
            or name.startswith(".")
            or expected_suffix is None
            or not name.lower().endswith(expected_suffix)
        ):
            quarantine.append(f"attachment-{index}-type")
        if not isinstance(size, int) or size < 0 or size > MAX_ATTACHMENT_BYTES:
            quarantine.append(f"attachment-{index}-size")
            size = 0
        if not HASH64.fullmatch(digest):
            quarantine.append(f"attachment-{index}-hash")
        attachment_total += size
        attachment_records.append(
            {
                "name": name,
                "media_type": media_type,
                "sha256": digest,
                "bytes": size,
            }
        )
    if attachment_total > MAX_ATTACHMENT_TOTAL_BYTES:
        quarantine.append("attachment-total-size-exceeded")

    transport = context["transport"]
    if context["transport_reported"]:
        report_id = str(transport.get("report_id") or "")
        if not HASH64.fullmatch(report_id):
            quarantine.append("report-id-invalid")
        if transport.get("source_verified") is not True:
            quarantine.append("source-unverified")
        if transport.get("frame_verified") is not True:
            quarantine.append("frame-unverified")
        trust_weight = transport.get("trust_weight_bps")
        if not isinstance(trust_weight, int) or not 0 <= trust_weight <= 10_000:
            quarantine.append("trust-weight-invalid")
        if int(transport.get("dedupe_count") or 0) > 0:
            quarantine.append("duplicate-report")
        if int(transport.get("rate_count") or 0) > int(
            transport.get("rate_limit") or 0
        ):
            quarantine.append("rate-limit-exceeded")
        created = transport.get("created_epoch")
        received = transport.get("received_epoch")
        ttl = int(transport.get("ttl_seconds") or 0)
        if (
            not isinstance(created, int)
            or not isinstance(received, int)
            or ttl < 1
            or received < created
            or received - created > ttl
        ):
            quarantine.append("stale-or-invalid-ttl")
        if (
            transport.get("correlation_id") is not None
            and transport.get("correlation_disclosed") is not True
        ):
            quarantine.append("undisclosed-correlation")

    replay = context["replay"]
    if context["replay_reported"]:
        argv = replay.get("argv")
        logical_cwd = str(replay.get("logical_cwd") or "")
        replay_valid = (
            isinstance(argv, list)
            and 1 <= len(argv) <= 32
            and all(
                isinstance(item, str)
                and 0 < len(item) <= 512
                and not item.startswith(("/", "\\"))
                and not re.match(r"^[A-Za-z]:[\\/]", item)
                and ".." not in Path(item).parts
                for item in argv
            )
            and logical_cwd.startswith("<")
            and logical_cwd.endswith(">")
            and len(logical_cwd) <= 80
            and isinstance(replay.get("input_sha256"), str)
            and HASH64.fullmatch(replay["input_sha256"])
            and isinstance(replay.get("before_state_sha256"), str)
            and HASH64.fullmatch(replay["before_state_sha256"])
            and isinstance(replay.get("output_sha256"), str)
            and HASH64.fullmatch(replay["output_sha256"])
            and isinstance(replay.get("duration_ms"), int)
            and 0 <= replay["duration_ms"] <= 3_600_000
            and isinstance(replay.get("output_bytes"), int)
            and 0 <= replay["output_bytes"] <= 1_000_000
            and isinstance(replay.get("phase"), str)
            and bool(replay["phase"])
        )
        if not replay_valid:
            quarantine.append("replay-manifest-invalid")

    environment_unknowns = [
        field
        for field, value in context["environment"].items()
        if str(value).lower() in {"unknown", "unreported"}
    ]
    bindings = context["bindings"]
    binding_unknowns = [
        field for field in BINDING_FIELDS if _unknown_hash(bindings.get(field))
    ]
    source_commit = str(bindings.get("source_commit") or "")
    if not COMMIT40.fullmatch(source_commit):
        binding_unknowns.append("source_commit")
    if str(bindings.get("ring") or "") not in {
        "stable-main",
        "canary",
        "beta",
        "dev",
    }:
        binding_unknowns.append("ring")
    if (
        context["bindings_reported"]
        and bindings.get("installer_release_frame_version") is not None
        and bindings.get("installer_release_frame_version")
        != INSTALLER_FRAME_VERSION
    ):
        quarantine.append("installer-frame-version-mismatch")
    installer_hashes = bindings.get("installer_sha256s") or {}
    if set(installer_hashes) != {"install.cmd", "install.ps1", "install.sh"} or any(
        name not in {"install.cmd", "install.ps1", "install.sh"}
        or not isinstance(digest, str)
        or not HASH64.fullmatch(digest)
        for name, digest in installer_hashes.items()
    ):
        binding_unknowns.append("installer_sha256s")
    binding_unknowns.extend(bindings.get("unreported_fields") or [])

    cell = context["cell"]
    queue_depth = int(cell.get("queue_depth") or 0)
    threshold = int(cell.get("backpressure_threshold") or 0)
    max_depth = int(cell.get("max_queue_depth") or 0)
    if (
        cell.get("global_lock") is not False
        or cell.get("global_raw_data_store") is not False
        or cell.get("global_exchange")
        != "verified-signatures-frames-aggregate-evidence-only"
    ):
        quarantine.append("unsafe-global-coordination")
    if not isinstance(cell.get("shard_key_sha256"), str) or not HASH64.fullmatch(
        cell["shard_key_sha256"]
    ):
        quarantine.append("cell-shard-key-invalid")
    if (
        queue_depth < 0
        or threshold < 1
        or max_depth < threshold
        or queue_depth > max_depth
    ):
        quarantine.append("invalid-cell-bounds")
    for field in ("hot_cache_hits", "negative_cache_hits"):
        if not isinstance(cell.get(field), int) or cell[field] < 0:
            quarantine.append(f"{field}-invalid")
    if cell.get("fairness_lane") not in {"normal", "protected", "rare"}:
        quarantine.append("fairness-lane-invalid")
    information_gain = cell.get("marginal_information_gain_bps")
    if (
        not isinstance(information_gain, int)
        or not 0 <= information_gain <= 10_000
    ):
        quarantine.append("marginal-information-gain-invalid")

    return {
        "quarantine_reasons": sorted(set(quarantine)),
        "attachments": attachment_records,
        "attachment_total_bytes": attachment_total,
        "environment_unknowns": sorted(environment_unknowns),
        "binding_unknowns": sorted(set(binding_unknowns)),
        "queue_depth": queue_depth,
        "backpressure_threshold": threshold,
        "max_queue_depth": max_depth,
    }


def _issue_signature(observations, context, platform_name, phase):
    bindings = context["bindings"]
    environment = context["environment"]
    replay = context["replay"]
    fields = {
        "installer_release_frame_version": bindings.get(
            "installer_release_frame_version"
        ),
        "installer_release_frame_sha256": bindings.get(
            "installer_release_frame_sha256"
        ),
        "ring": bindings.get("ring"),
        "ring_manifest_sha256": bindings.get("ring_manifest_sha256"),
        "source_commit": bindings.get("source_commit"),
        "installer_sha256s": bindings.get("installer_sha256s"),
        "phase": str(observations.get("signature_phase") or phase),
        "fixed_code": str(
            observations.get("failure_code") or "unclassified"
        ),
        "environment_classes": {
            "platform": platform_name,
            "os_build": environment.get("os_build"),
            "managed_policy": environment.get("managed_policy"),
            "filesystem": environment.get("filesystem"),
            "shell": environment.get("shell"),
        },
        "input_hashes": (
            observations.get("signature_input_hashes")
            if isinstance(observations.get("signature_input_hashes"), list)
            else [
                replay.get("input_sha256"),
                replay.get("before_state_sha256"),
            ]
        ),
    }
    signature = _sha256_bytes(
        ISSUE_SIGNATURE_DOMAIN.encode("utf-8")
        + b"\n"
        + _canonical_json(fields).encode("utf-8")
    )
    return {"domain": ISSUE_SIGNATURE_DOMAIN, "sha256": signature, "fields": fields}


def _normalize_platform(value):
    text = str(value or "").strip().lower()
    aliases = {
        "darwin": "macos",
        "mac": "macos",
        "osx": "macos",
        "win32": "windows",
        "win": "windows",
    }
    text = aliases.get(text, text)
    if text not in {"linux", "macos", "windows"}:
        raise ValueError("platform must be linux, macos, or windows")
    return text


def _platform_command(platform_name, command):
    if platform_name == "windows":
        return ["py", "-3"] + command
    return ["python3"] + command


def _bool_path(mapping, *keys, default=False):
    current = mapping
    for key in keys:
        if not isinstance(current, dict):
            return default
        current = current.get(key)
    return current if isinstance(current, bool) else default


def _value_path(mapping, *keys, default=None):
    current = mapping
    for key in keys:
        if not isinstance(current, dict):
            return default
        current = current.get(key)
    return default if current is None else current


def _python_supported(version):
    match = re.fullmatch(r"(\d+)\.(\d+)(?:\.\d+)?", str(version or ""))
    if not match:
        return False
    major, minor = (int(part) for part in match.groups())
    return major == 3 and minor >= 11


def _base_report(observations):
    case_id = str(observations.get("case_id") or "local-rapp-setup").strip()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", case_id):
        raise ValueError("case_id must be lowercase kebab-case")
    platform_name = _normalize_platform(observations.get("platform"))
    return {
        "schema": REPORT_SCHEMA,
        "support_system": "RAPP Roadside",
        "machine_issue_artifact": "Roadside Frame",
        "closed_loop": "RAPP Roadside Closed Loop",
        "issue_signature_domain": ISSUE_SIGNATURE_DOMAIN,
        "case_id": case_id,
        "platform": platform_name,
        "target": {
            "stable_main_identity": STABLE_MAIN_IDENTITY,
            "release_rule": (
                "RAPP Roadside diagnoses locally. RAPP Pit Crew changes go "
                "through an isolated checkout and a release merge; never push "
                "directly to main."
            ),
        },
        "invariants": {
            "grail_modified": False,
            "wire": WIRE,
            "new_rest_routes_allowed": False,
        },
        "privacy": {
            "credentials_collected": False,
            "external_network_used": False,
            "telemetry": False,
            "report_contains_log_bodies": False,
            "local_copy_only": True,
        },
    }


def _bounded_action(
    action_id,
    title,
    reason,
    platform_name,
    command,
    timeout_seconds,
    writes,
    expected,
):
    if timeout_seconds < 1 or timeout_seconds > 300:
        raise ValueError("bounded action timeout must be 1-300 seconds")
    return {
        "id": action_id,
        "title": title,
        "reason": reason,
        "command_argv": _platform_command(platform_name, command),
        "timeout_seconds": timeout_seconds,
        "writes": writes,
        "expected": expected,
        "alternatives": [],
    }


def _diagnose(observations):
    _assert_no_sensitive_input(observations)
    _validate_observation_shape(observations)
    context = _normalize_unknown_context(observations)
    context_findings = _context_findings(context)
    report = _base_report(observations)
    platform_name = report["platform"]
    probe_mode = str(observations.get("probe_mode") or "direct")
    elapsed = int(observations.get("setup_elapsed_seconds") or 0)
    if elapsed < 0 or elapsed > 86_400:
        raise ValueError("setup_elapsed_seconds must be between 0 and 86400")

    source_present = _bool_path(observations, "source", "present")
    launcher_present = _bool_path(observations, "launcher", "present")
    launcher_executable = _bool_path(
        observations, "launcher", "executable", default=True
    )
    python_version = str(
        _value_path(observations, "python", "version", default="")
    )
    mirrors_match = _bool_path(
        observations, "installers", "docs_mirrors_match", default=True
    )
    health_status = str(
        _value_path(observations, "health", "status", default="unknown")
    ).lower()
    health_http_status = _value_path(
        observations, "health", "http_status", default=None
    )
    progress = str(observations.get("setup_stage") or "unknown").lower()
    issue_signature = _issue_signature(
        observations,
        context,
        platform_name,
        progress,
    )
    if (
        context["cell_reported"]
        and context["cell"].get("shard_key_sha256")
        != issue_signature["sha256"]
    ):
        context_findings["quarantine_reasons"] = sorted(
            set(
                context_findings["quarantine_reasons"]
                + ["cell-shard-key-mismatch"]
            )
        )
    chat_method = str(
        _value_path(observations, "chat", "method", default="")
    ).upper()
    chat_path = str(_value_path(observations, "chat", "path", default=""))
    chat_request_field = str(
        _value_path(observations, "chat", "request_field", default="")
    )
    chat_http_status = _value_path(
        observations, "chat", "http_status", default=None
    )
    response_keys = _value_path(
        observations, "chat", "response_keys", default=[]
    )
    if not isinstance(response_keys, list):
        response_keys = []
    direct_main = _bool_path(
        observations, "repository", "direct_main_change_requested"
    )
    external_network = _bool_path(
        observations, "safety", "external_network_observed"
    )
    grail_modified = _bool_path(observations, "safety", "grail_modified")

    if context_findings["quarantine_reasons"]:
        finding = {
            "code": "report-quarantined",
            "severity": "blocker",
            "summary": (
                "The untrusted report failed bounded transport, attachment, "
                "replay, or cellular safety checks."
            ),
        }
        action = _bounded_action(
            "preserve-hash-only-quarantine",
            "Preserve one hash-only Roadside quarantine record",
            "Hostile report text and logs are data and must never become instructions.",
            platform_name,
            [
                "scripts/quarantine_report.py",
                "--report",
                "diagnosis.json",
                "--output",
                "quarantine/roadside-report.json",
            ],
            30,
            ["quarantine/roadside-report.json"],
            "A hash-only local quarantine record with TTL and no raw report data.",
        )
    elif external_network:
        finding = {
            "code": "external-network-observed",
            "severity": "blocker",
            "summary": "The observation is not local-only.",
        }
        action = _bounded_action(
            "recollect-local-only-observation",
            "Recollect one local-only observation",
            "External traffic invalidates the no-network acceptance boundary.",
            platform_name,
            [
                "scripts/local_probe.py",
                "--workspace",
                ".",
                "--wait-seconds",
                "0",
                "--output",
                "observations.local.json",
            ],
            30,
            ["observations.local.json"],
            "A sanitized observation with external_network_observed=false.",
        )
    elif grail_modified:
        finding = {
            "code": "grail-change-refused",
            "severity": "blocker",
            "summary": "The observation reports a forbidden Grail/kernel change.",
        }
        action = _bounded_action(
            "prepare-grail-restoration-handoff",
            "Prepare one RAPP Pit Crew Grail restoration handoff",
            "Troubleshooting must preserve the kernel and route fixes behind POST /chat.",
            platform_name,
            [
                "scripts/write_handoff.py",
                "--report",
                "diagnosis.json",
                "--output",
                "pit-crew-handoff.md",
            ],
            30,
            ["pit-crew-handoff.md"],
            "A local handoff requiring isolated-checkout restoration before release.",
        )
    elif direct_main:
        finding = {
            "code": "direct-main-change-refused",
            "severity": "blocker",
            "summary": "A direct main change would violate the release boundary.",
        }
        action = _bounded_action(
            "prepare-isolated-checkout-handoff",
            "Prepare one RAPP Pit Crew isolated-checkout handoff",
            "Stable main is a target identity, not a writable troubleshooting area.",
            platform_name,
            [
                "scripts/write_handoff.py",
                "--report",
                "diagnosis.json",
                "--output",
                "pit-crew-handoff.md",
            ],
            30,
            ["pit-crew-handoff.md"],
            "A handoff that requires feature/fix checkout validation and release merge.",
        )
    elif (
        context["cell_reported"]
        and context_findings["queue_depth"]
        >= context_findings["backpressure_threshold"]
    ):
        finding = {
            "code": "roadside-cell-backpressure",
            "severity": "medium",
            "summary": (
                "The bounded local Roadside cell reached its measured "
                "backpressure threshold."
            ),
        }
        action = _bounded_action(
            "defer-with-cell-backpressure",
            "Defer one report in its existing shard",
            "Horizontal cellular scaling must not create a global lock or raw-data store.",
            platform_name,
            [
                "scripts/quarantine_report.py",
                "--report",
                "diagnosis.json",
                "--output",
                "quarantine/backpressure.json",
            ],
            30,
            ["quarantine/backpressure.json"],
            "A local hash-only deferral record preserving shard and queue measurements.",
        )
    elif (
        context["environment_reported"]
        and probe_mode != "follow-up"
        and set(context_findings["environment_unknowns"]).intersection(
            {"filesystem", "managed_policy", "os_build", "shell"}
        )
    ):
        finding = {
            "code": "platform-policy-unknown",
            "severity": "medium",
            "summary": (
                "Critical platform or managed-device policy capabilities are "
                "unknown and no catch-all diagnosis is safe."
            ),
        }
        action = _bounded_action(
            "capture-platform-policy-capabilities",
            "Capture one explicit platform and policy capability probe",
            "Unknown OS, shell, filesystem, or policy state must be exposed honestly.",
            platform_name,
            [
                "scripts/local_probe.py",
                "--workspace",
                ".",
                "--wait-seconds",
                "0",
                "--output",
                "observations.capabilities.json",
                "--follow-up",
            ],
            30,
            ["observations.capabilities.json"],
            "A sanitized observation with explicit values or explicit unsupported states.",
        )
    elif (
        context["bindings_reported"]
        and context_findings["binding_unknowns"]
        and probe_mode != "follow-up"
    ):
        finding = {
            "code": "exact-byte-bindings-incomplete",
            "severity": "high",
            "summary": (
                "Ring, source, dependency, catalog, or installer bytes are not "
                "fully content-addressed."
            ),
        }
        action = _bounded_action(
            "capture-exact-byte-bindings",
            "Capture one exact local byte-binding manifest",
            "RAPP Pit Crew cannot reproduce or release against mutable labels.",
            platform_name,
            [
                "scripts/local_probe.py",
                "--workspace",
                ".",
                "--wait-seconds",
                "0",
                "--output",
                "observations.bindings.json",
                "--follow-up",
            ],
            30,
            ["observations.bindings.json"],
            "Ring, source, dependency, catalog, and installer hashes are exact or explicitly unsupported.",
        )
    elif (
        probe_mode == "follow-up"
        and (
            set(context_findings["environment_unknowns"]).intersection(
                {"filesystem", "managed_policy", "os_build", "shell"}
            )
            or context_findings["binding_unknowns"]
        )
    ):
        finding = {
            "code": "evidence-incomplete-after-follow-up",
            "severity": "medium",
            "summary": (
                "One bounded follow-up completed, but some local evidence is "
                "unavailable and must not be invented."
            ),
        }
        action = _bounded_action(
            "prepare-incomplete-evidence-handoff",
            "Prepare one incomplete-evidence RAPP Pit Crew handoff",
            "The local probe must not repeat indefinitely or fabricate unavailable fields.",
            platform_name,
            [
                "scripts/write_handoff.py",
                "--report",
                "diagnosis.json",
                "--output",
                "pit-crew-handoff.md",
            ],
            30,
            ["pit-crew-handoff.md"],
            "One inert handoff marks unavailable evidence and requires independent reproduction.",
        )
    elif not source_present:
        finding = {
            "code": "local-source-not-found",
            "severity": "high",
            "summary": "No local RAPP source directory was observed.",
        }
        action = _bounded_action(
            "locate-local-source",
            "Locate one existing local RAPP source",
            "Fresh download is outside this local-only troubleshooting run.",
            platform_name,
            [
                "scripts/local_probe.py",
                "--workspace",
                ".",
                "--wait-seconds",
                "0",
                "--output",
                "observations.local.json",
            ],
            30,
            ["observations.local.json"],
            "source.present=true without external traffic.",
        )
    elif not _python_supported(python_version):
        finding = {
            "code": "python-3-11-required",
            "severity": "high",
            "summary": "The observed Python does not meet the Python 3.11+ target.",
        }
        action = _bounded_action(
            "verify-python-3-11",
            "Verify one local Python 3.11+ interpreter",
            "Installer behavior is not comparable on an unsupported interpreter.",
            platform_name,
            [
                "scripts/local_probe.py",
                "--workspace",
                ".",
                "--wait-seconds",
                "0",
                "--output",
                "observations.python.json",
            ],
            30,
            ["observations.python.json"],
            "python.version reports 3.11 or newer.",
        )
    elif not launcher_present:
        finding = {
            "code": "policy-launcher-missing",
            "severity": "high",
            "summary": "The local policy-clean Brainstem launcher is missing.",
        }
        action = _bounded_action(
            "prepare-launcher-checkout-handoff",
            "Prepare one RAPP Pit Crew launcher checkout handoff",
            "Missing canonical launcher files require RAPP Pit Crew review, not synthesis.",
            platform_name,
            [
                "scripts/write_handoff.py",
                "--report",
                "diagnosis.json",
                "--output",
                "pit-crew-handoff.md",
            ],
            30,
            ["pit-crew-handoff.md"],
            "A local RAPP Pit Crew isolated-checkout/release-merge handoff.",
        )
    elif platform_name != "windows" and not launcher_executable:
        finding = {
            "code": "launcher-not-executable",
            "severity": "high",
            "summary": "The local launcher lacks its executable bit.",
        }
        action = _bounded_action(
            "restore-launcher-executable-copy",
            "Prepare one human-approved launcher repair",
            "RAPP Roadside must not apply a repair without explicit reversible-copy approval.",
            platform_name,
            [
                "scripts/run_agent.py",
                "--json",
                (
                    '{"operation":"prepare_repair","action_id":'
                    '"restore-launcher-executable-copy","source_dir":".",'
                    '"copy_dir":"../rapp-repair-copy"}'
                ),
            ],
            30,
            [],
            "A human may approve a source-bound repair in a new sibling copy.",
        )
    elif not mirrors_match:
        finding = {
            "code": "installer-mirror-drift",
            "severity": "high",
            "summary": "Root installers and docs mirrors are not byte-identical.",
        }
        action = _bounded_action(
            "synchronize-installer-mirrors-copy",
            "Prepare one human-approved installer-mirror repair",
            "Sacred installer bytes require explicit reversible-copy approval.",
            platform_name,
            [
                "scripts/run_agent.py",
                "--json",
                (
                    '{"operation":"prepare_repair","action_id":'
                    '"synchronize-installer-mirrors-copy","source_dir":".",'
                    '"copy_dir":"../rapp-repair-copy"}'
                ),
            ],
            30,
            [],
            "A human may approve a source-bound repair in a new sibling copy.",
        )
    elif (
        health_status in {"starting", "pending", "unknown", "unreachable"}
        and elapsed <= 180
        and progress
        in {
            "agent-dependency-install",
            "creating-venv",
            "installing-requirements",
            "starting-server",
        }
    ):
        finding = {
            "code": "slow-first-boot-progressing",
            "severity": "medium",
            "summary": (
                "The bounded first boot is slow but still reports a known "
                "forward-progress stage."
            ),
        }
        action = _bounded_action(
            "bounded-wait-and-local-retest",
            "Wait 120 seconds, then run one exact local retest",
            "A progressing first boot should not be restarted or reinstalled prematurely.",
            platform_name,
            [
                "scripts/local_probe.py",
                "--workspace",
                ".",
                "--wait-seconds",
                "120",
                "--check-chat",
                "--allow-loopback",
                "--output",
                "observations.after.json",
            ],
            150,
            ["observations.after.json"],
            "GET /health is ok and POST /chat returns the success envelope.",
        )
    elif health_status != "ok" or health_http_status != 200:
        finding = {
            "code": "brainstem-not-ready-after-bound",
            "severity": "high",
            "summary": "Brainstem did not become healthy inside the first-boot bound.",
        }
        action = _bounded_action(
            "capture-local-stage-snapshot",
            "Capture one sanitized local stage snapshot",
            "The next useful fact is the stalled stage, not another reinstall.",
            platform_name,
            [
                "scripts/local_probe.py",
                "--workspace",
                ".",
                "--wait-seconds",
                "0",
                "--output",
                "observations.stalled.json",
            ],
            30,
            ["observations.stalled.json"],
            "A redacted local observation suitable for RAPP Pit Crew triage.",
        )
    elif (
        chat_method != WIRE["method"]
        or chat_path != WIRE["path"]
        or chat_request_field != WIRE["request_field"]
        or chat_http_status != 200
        or not set(WIRE["success_keys"]).issubset(set(response_keys))
    ):
        finding = {
            "code": "post-chat-contract-not-proven",
            "severity": "high",
            "summary": "Health is ready, but the canonical POST /chat wire is not proven.",
        }
        action = _bounded_action(
            "retest-canonical-post-chat",
            "Run one canonical POST /chat retest",
            "No sibling endpoint or Grail change is permitted.",
            platform_name,
            [
                "scripts/local_probe.py",
                "--workspace",
                ".",
                "--wait-seconds",
                "0",
                "--check-chat",
                "--allow-loopback",
                "--output",
                "observations.chat.json",
            ],
            30,
            ["observations.chat.json"],
            "POST /chat accepts user_input and returns exactly the required success fields.",
        )
    else:
        finding = {
            "code": "local-setup-proven",
            "severity": "info",
            "summary": "Local health and the canonical POST /chat envelope are proven.",
        }
        action = _bounded_action(
            "archive-local-evidence",
            "Archive one deterministic local evidence report",
            "The setup is proven; publication remains the parent RAR reviewer's action.",
            platform_name,
            [
                "scripts/write_handoff.py",
                "--report",
                "diagnosis.json",
                "--output",
                "share with kody.md",
            ],
            30,
            ["share with kody.md"],
            "A local review handoff with no upload or public action.",
        )

    report["observation_summary"] = {
        "probe_mode": probe_mode,
        "setup_elapsed_seconds": elapsed,
        "setup_stage": progress,
        "source_present": source_present,
        "launcher_present": launcher_present,
        "python_version": python_version,
        "health_status": health_status,
        "health_http_status": health_http_status,
        "chat_method": chat_method or None,
        "chat_path": chat_path or None,
        "chat_request_field": chat_request_field or None,
        "chat_http_status": chat_http_status,
        "chat_response_keys": sorted(str(key) for key in response_keys),
        "installer_docs_mirrors_match": mirrors_match,
    }
    report["finding"] = finding
    report["issue_signature"] = {
        **issue_signature,
        "queue_key": True,
        "dedupe_key": True,
        "identity_included": False,
        "raw_logs_included": False,
    }
    report["evidence_partition"] = {
        "observed": {
            "fields": sorted(report["observation_summary"]),
            "reporting_ai_claim_ids": sorted(
                str(item)
                for item in context["reporting_ai"].get(
                    "observed_claim_ids", []
                )
            ),
            "attachments": context_findings["attachments"],
        },
        "inferred": {
            "finding_code": finding["code"],
            "basis": [
                "bounded deterministic decision order",
                "sanitized observed fields only",
            ],
            "reporting_ai_claim_ids": sorted(
                str(item)
                for item in context["reporting_ai"].get(
                    "inferred_claim_ids", []
                )
            ),
        },
        "raw_reporting_ai_text_or_logs_retained": False,
        "embedded_instructions_executed": False,
    }
    report["platform_policy_unknowns"] = {
        "reported": context["environment_reported"],
        "values": context["environment"],
        "unknown_fields": context_findings["environment_unknowns"],
        "catch_all_diagnosis_used": False,
    }
    report["byte_bindings"] = {
        "reported": context["bindings_reported"],
        "values": context["bindings"],
        "unknown_fields": context_findings["binding_unknowns"],
        "exact": not context_findings["binding_unknowns"],
    }
    report["replay_manifest"] = {
        "reported": context["replay_reported"],
        **context["replay"],
        "raw_private_path_exported": False,
    }
    transport = context["transport"]
    age_seconds = (
        transport["received_epoch"] - transport["created_epoch"]
        if isinstance(transport.get("created_epoch"), int)
        and isinstance(transport.get("received_epoch"), int)
        else None
    )
    report["report_controls"] = {
        "transport_reported": context["transport_reported"],
        "source_cell_id": transport.get("source_cell_id"),
        "source_verified": transport.get("source_verified"),
        "frame_verified": transport.get("frame_verified"),
        "trust_weight_bps": transport.get("trust_weight_bps"),
        "dedupe_key": issue_signature["sha256"],
        "dedupe_count": transport.get("dedupe_count"),
        "ttl_seconds": transport.get("ttl_seconds"),
        "age_seconds": age_seconds,
        "rate": {
            "count": transport.get("rate_count"),
            "limit": transport.get("rate_limit"),
            "window_seconds": transport.get("rate_window_seconds"),
        },
        "correlation": {
            "id_present": transport.get("correlation_id") is not None,
            "disclosed": transport.get("correlation_disclosed"),
        },
        "quarantined": bool(context_findings["quarantine_reasons"]),
        "quarantine_reasons": context_findings["quarantine_reasons"],
        "raw_report_data_globalized": False,
    }
    cell = context["cell"]
    max_depth = max(1, context_findings["max_queue_depth"])
    report["scaling"] = {
        "claim": "horizontal-cellular-scaling",
        "unbounded_or_infinite_claim": False,
        "cell_reported": context["cell_reported"],
        "cell_id": cell.get("cell_id"),
        "shard_key_sha256": cell.get("shard_key_sha256"),
        "global_lock": False,
        "global_raw_data_store": False,
        "global_exchange": (
            "verified-signatures-frames-aggregate-evidence-only"
        ),
        "measured_backpressure": {
            "queue_depth": context_findings["queue_depth"],
            "threshold": context_findings["backpressure_threshold"],
            "max_queue_depth": context_findings["max_queue_depth"],
            "utilization_basis_points": (
                context_findings["queue_depth"] * 10_000 // max_depth
            ),
            "active": (
                context_findings["queue_depth"]
                >= context_findings["backpressure_threshold"]
            ),
        },
        "local_raw_retention_seconds": cell.get(
            "local_raw_retention_seconds"
        ),
        "cache_measurements": {
            "hot_cache_hits": cell.get("hot_cache_hits"),
            "negative_cache_hits": cell.get("negative_cache_hits"),
        },
        "fairness_lane": cell.get("fairness_lane"),
        "marginal_information_gain_bps": cell.get(
            "marginal_information_gain_bps"
        ),
    }
    report["release_readiness"] = {
        "eligible": (
            not context_findings["quarantine_reasons"]
            and not context_findings["binding_unknowns"]
            and context["replay_reported"]
            and finding["code"] == "local-setup-proven"
            and not set(context_findings["environment_unknowns"]).intersection(
                {"filesystem", "managed_policy", "os_build", "shell"}
            )
        ),
        "required_gate": (
            "RAPP Pit Crew isolated-checkout-Canary-Nightly-Alpha-Beta"
        ),
        "stable_main_direct_push": False,
    }
    report["closed_loop"] = {
        "contract": "rapp/closed-loop.json",
        "name": "RAPP Roadside Closed Loop",
        "customer_state": (
            "stopped-without-change"
            if finding["code"] == "report-quarantined"
            else "user-review"
            if finding["code"] == "local-setup-proven"
            else "diagnose-locally"
        ),
        "next_bounded_action": action["id"],
        "repair_requires_human_approval": True,
        "share_with_kody_inert": True,
        "roadside_frame_embedded": True,
        "automatic_actions": {
            "teams_send": False,
            "git_push": False,
            "main_edit": False,
            "production_deploy": False,
            "destructive_customer_repair": False,
            "maintainer_feedback_network_send": False,
        },
    }
    report["next_action"] = action
    report["retest"] = {
        "mode": "canonical-from-verified-diagnosis",
        "assertions": _canonical_retest_assertions(report),
        "hardening": {
            "require_valid_replay": True,
            "require_transport_screen": True,
            "require_same_ring_source_dependency_catalog_bytes": True,
            "require_same_shard": True,
            "reject_supplied_assertion_drift": True,
        },
    }
    report["maintainer_handoff"] = {
        "system": "RAPP Pit Crew",
        "closed_loop_contract": "rapp/closed-loop.json",
        "repository": "kody-w/rapp-roadside",
        "base": "main",
        "required_flow": [
            "intake the hash-only Roadside Frame and independently reproduce",
            "create an isolated feature/fix checkout from stable main",
            "import the exact failing replay as a named regression test",
            "apply and retest the reviewed change in that checkout",
            "pass platform and ring matrices plus clean-machine installer tests",
            "promote one-way through Canary, Nightly, Alpha, then Beta soak",
            "perform a no-fast-forward release merge with rollback evidence",
            "bump VERSION only in the release merge when appropriate",
            "link issue, fix, test, and ring hashes in the release frame",
            "have the customer rerun the identical released test",
            "accept only successful confirmation as the verified resolution record",
        ],
        "bounded_follow_up_limit": 1,
        "soak_order": ["Canary", "Nightly", "Alpha", "Beta"],
        "forbidden": [
            "direct push to main",
            "new REST route beside POST /chat",
            "Grail/kernel rewrite",
            "credential collection",
        ],
    }
    report_without_id = dict(report)
    report["report_id"] = _content_id(report_without_id)
    return report


def _path_value(mapping, dotted_path):
    current = mapping
    for part in dotted_path.split("."):
        if not isinstance(current, dict) or part not in current:
            return None
        current = current[part]
    return current


def _canonical_retest_assertions(diagnosis):
    bindings = _value_path(
        diagnosis, "byte_bindings", "values", default={}
    )
    environment = _value_path(
        diagnosis, "platform_policy_unknowns", "values", default={}
    )
    return [
        {"path": "health.status", "equals": "ok"},
        {"path": "health.http_status", "equals": 200},
        {"path": "chat.method", "equals": WIRE["method"]},
        {"path": "chat.path", "equals": WIRE["path"]},
        {"path": "chat.request_field", "equals": WIRE["request_field"]},
        {"path": "chat.http_status", "equals": 200},
        {
            "path": "chat.response_keys",
            "contains_all": list(WIRE["success_keys"]),
        },
        {"path": "safety.grail_modified", "equals": False},
        {"path": "safety.external_network_observed", "equals": False},
        {"path": "bindings.ring", "equals": bindings.get("ring")},
        {
            "path": "bindings.installer_release_frame_version",
            "equals": bindings.get("installer_release_frame_version"),
        },
        {
            "path": "bindings.installer_release_frame_sha256",
            "equals": bindings.get("installer_release_frame_sha256"),
        },
        {
            "path": "bindings.ring_manifest_sha256",
            "equals": bindings.get("ring_manifest_sha256"),
        },
        {
            "path": "bindings.source_commit",
            "equals": bindings.get("source_commit"),
        },
        {
            "path": "bindings.source_tree_sha256",
            "equals": bindings.get("source_tree_sha256"),
        },
        {
            "path": "bindings.dependency_lock_sha256",
            "equals": bindings.get("dependency_lock_sha256"),
        },
        {
            "path": "bindings.catalog_sha256",
            "equals": bindings.get("catalog_sha256"),
        },
        {
            "path": "bindings.installer_sha256s",
            "equals": bindings.get("installer_sha256s"),
        },
        {
            "path": "environment.os_build",
            "equals": environment.get("os_build"),
        },
        {
            "path": "environment.managed_policy",
            "equals": environment.get("managed_policy"),
        },
        {
            "path": "environment.filesystem",
            "equals": environment.get("filesystem"),
        },
        {
            "path": "environment.shell",
            "equals": environment.get("shell"),
        },
        {
            "path": "cell.shard_key_sha256",
            "equals": _value_path(
                diagnosis, "scaling", "shard_key_sha256", default=None
            ),
        },
    ]


def _validate_diagnosis(diagnosis):
    _require_object_shape(
        diagnosis,
        {
            "byte_bindings",
            "case_id",
            "closed_loop",
            "evidence_partition",
            "finding",
            "invariants",
            "issue_signature",
            "issue_signature_domain",
            "machine_issue_artifact",
            "maintainer_handoff",
            "next_action",
            "observation_summary",
            "platform",
            "platform_policy_unknowns",
            "privacy",
            "release_readiness",
            "replay_manifest",
            "report_controls",
            "report_id",
            "retest",
            "scaling",
            "schema",
            "support_system",
            "target",
        },
        set(),
        "diagnosis",
    )
    report_id = diagnosis.get("report_id")
    if not isinstance(report_id, str) or not HASH64.fullmatch(report_id):
        raise ValueError("diagnosis.report_id must be a SHA-256 value")
    content = dict(diagnosis)
    content.pop("report_id")
    if _content_id(content) != report_id:
        raise ValueError("diagnosis report_id does not match its complete content")
    if (
        diagnosis.get("schema") != REPORT_SCHEMA
        or diagnosis.get("support_system") != "RAPP Roadside"
        or diagnosis.get("machine_issue_artifact") != "Roadside Frame"
        or diagnosis.get("issue_signature_domain") != ISSUE_SIGNATURE_DOMAIN
    ):
        raise ValueError("diagnosis protocol identity mismatch")
    if diagnosis.get("platform") not in {"linux", "macos", "windows"}:
        raise ValueError("diagnosis platform is invalid")
    if not re.fullmatch(
        r"[a-z0-9]+(?:-[a-z0-9]+)*",
        str(diagnosis.get("case_id") or ""),
    ):
        raise ValueError("diagnosis case_id is invalid")

    _require_object_shape(
        diagnosis["target"],
        {"release_rule", "stable_main_identity"},
        set(),
        "diagnosis.target",
    )
    if diagnosis["target"]["stable_main_identity"] != STABLE_MAIN_IDENTITY:
        raise ValueError("diagnosis stable target mismatch")
    _require_object_shape(
        diagnosis["invariants"],
        {"grail_modified", "new_rest_routes_allowed", "wire"},
        set(),
        "diagnosis.invariants",
    )
    if (
        diagnosis["invariants"]["grail_modified"] is not False
        or diagnosis["invariants"]["new_rest_routes_allowed"] is not False
        or diagnosis["invariants"]["wire"] != WIRE
    ):
        raise ValueError("diagnosis safety invariants are invalid")
    _require_object_shape(
        diagnosis["privacy"],
        {
            "credentials_collected",
            "external_network_used",
            "local_copy_only",
            "report_contains_log_bodies",
            "telemetry",
        },
        set(),
        "diagnosis.privacy",
    )
    if any(
        diagnosis["privacy"][field] is not expected
        for field, expected in {
            "credentials_collected": False,
            "external_network_used": False,
            "local_copy_only": True,
            "report_contains_log_bodies": False,
            "telemetry": False,
        }.items()
    ):
        raise ValueError("diagnosis privacy boundary is invalid")
    _require_object_shape(
        diagnosis["observation_summary"],
        {
            "chat_http_status",
            "chat_method",
            "chat_path",
            "chat_request_field",
            "chat_response_keys",
            "health_http_status",
            "health_status",
            "installer_docs_mirrors_match",
            "launcher_present",
            "probe_mode",
            "python_version",
            "setup_elapsed_seconds",
            "setup_stage",
            "source_present",
        },
        set(),
        "diagnosis.observation_summary",
    )
    _require_object_shape(
        diagnosis["finding"],
        {"code", "severity", "summary"},
        set(),
        "diagnosis.finding",
    )
    signature = diagnosis["issue_signature"]
    _require_object_shape(
        signature,
        {
            "dedupe_key",
            "domain",
            "fields",
            "identity_included",
            "queue_key",
            "raw_logs_included",
            "sha256",
        },
        set(),
        "diagnosis.issue_signature",
    )
    if (
        signature.get("domain") != ISSUE_SIGNATURE_DOMAIN
        or signature.get("identity_included") is not False
        or signature.get("raw_logs_included") is not False
        or signature.get("queue_key") is not True
        or signature.get("dedupe_key") is not True
    ):
        raise ValueError("diagnosis issue signature controls are invalid")
    expected_signature = _sha256_bytes(
        ISSUE_SIGNATURE_DOMAIN.encode("utf-8")
        + b"\n"
        + _canonical_json(signature["fields"]).encode("utf-8")
    )
    if signature.get("sha256") != expected_signature:
        raise ValueError("diagnosis issue signature does not match its fields")

    _require_object_shape(
        diagnosis["evidence_partition"],
        {
            "embedded_instructions_executed",
            "inferred",
            "observed",
            "raw_reporting_ai_text_or_logs_retained",
        },
        set(),
        "diagnosis.evidence_partition",
    )
    if (
        diagnosis["evidence_partition"]["embedded_instructions_executed"]
        is not False
        or diagnosis["evidence_partition"][
            "raw_reporting_ai_text_or_logs_retained"
        ]
        is not False
    ):
        raise ValueError("diagnosis evidence partition is unsafe")
    _require_object_shape(
        diagnosis["platform_policy_unknowns"],
        {"catch_all_diagnosis_used", "reported", "unknown_fields", "values"},
        set(),
        "diagnosis.platform_policy_unknowns",
    )
    _require_object_shape(
        diagnosis["platform_policy_unknowns"]["values"],
        set(ENVIRONMENT_FIELDS),
        set(),
        "diagnosis.platform_policy_unknowns.values",
    )
    if diagnosis["platform_policy_unknowns"]["catch_all_diagnosis_used"] is not False:
        raise ValueError("diagnosis may not use a catch-all result")
    _require_object_shape(
        diagnosis["byte_bindings"],
        {"exact", "reported", "unknown_fields", "values"},
        set(),
        "diagnosis.byte_bindings",
    )
    _require_object_shape(
        diagnosis["byte_bindings"]["values"],
        {
            "catalog_sha256",
            "dependency_lock_sha256",
            "installer_release_frame_sha256",
            "installer_release_frame_version",
            "installer_sha256s",
            "ring",
            "ring_manifest_sha256",
            "source_commit",
            "source_tree_sha256",
            "unreported_fields",
        },
        set(),
        "diagnosis.byte_bindings.values",
    )
    if not isinstance(
        diagnosis["byte_bindings"]["values"]["unreported_fields"], list
    ):
        raise TypeError("diagnosis byte binding unreported_fields must be an array")
    _require_object_shape(
        diagnosis["replay_manifest"],
        {
            "argv",
            "before_state_sha256",
            "duration_ms",
            "input_sha256",
            "logical_cwd",
            "output_bytes",
            "output_sha256",
            "phase",
            "raw_private_path_exported",
            "reported",
        },
        set(),
        "diagnosis.replay_manifest",
    )
    if diagnosis["replay_manifest"]["raw_private_path_exported"] is not False:
        raise ValueError("diagnosis replay manifest exports a private path")
    _require_object_shape(
        diagnosis["report_controls"],
        {
            "age_seconds",
            "correlation",
            "dedupe_count",
            "dedupe_key",
            "frame_verified",
            "quarantine_reasons",
            "quarantined",
            "rate",
            "raw_report_data_globalized",
            "source_cell_id",
            "source_verified",
            "transport_reported",
            "trust_weight_bps",
            "ttl_seconds",
        },
        set(),
        "diagnosis.report_controls",
    )
    if diagnosis["report_controls"]["raw_report_data_globalized"] is not False:
        raise ValueError("diagnosis globalized raw report data")
    _require_object_shape(
        diagnosis["scaling"],
        {
            "cache_measurements",
            "cell_id",
            "cell_reported",
            "claim",
            "fairness_lane",
            "global_exchange",
            "global_lock",
            "global_raw_data_store",
            "local_raw_retention_seconds",
            "marginal_information_gain_bps",
            "measured_backpressure",
            "shard_key_sha256",
            "unbounded_or_infinite_claim",
        },
        set(),
        "diagnosis.scaling",
    )
    if (
        diagnosis["scaling"]["global_lock"] is not False
        or diagnosis["scaling"]["global_raw_data_store"] is not False
        or diagnosis["scaling"]["unbounded_or_infinite_claim"] is not False
    ):
        raise ValueError("diagnosis scaling boundary is invalid")
    _require_object_shape(
        diagnosis["release_readiness"],
        {"eligible", "required_gate", "stable_main_direct_push"},
        set(),
        "diagnosis.release_readiness",
    )
    if diagnosis["release_readiness"]["stable_main_direct_push"] is not False:
        raise ValueError("diagnosis permits direct main changes")
    _require_object_shape(
        diagnosis["closed_loop"],
        {
            "automatic_actions",
            "contract",
            "customer_state",
            "name",
            "next_bounded_action",
            "repair_requires_human_approval",
            "roadside_frame_embedded",
            "share_with_kody_inert",
        },
        set(),
        "diagnosis.closed_loop",
    )
    _require_object_shape(
        diagnosis["closed_loop"]["automatic_actions"],
        {
            "destructive_customer_repair",
            "git_push",
            "main_edit",
            "maintainer_feedback_network_send",
            "production_deploy",
            "teams_send",
        },
        set(),
        "diagnosis.closed_loop.automatic_actions",
    )
    if (
        diagnosis["closed_loop"]["repair_requires_human_approval"] is not True
        or diagnosis["closed_loop"]["roadside_frame_embedded"] is not True
        or diagnosis["closed_loop"]["share_with_kody_inert"] is not True
        or any(diagnosis["closed_loop"]["automatic_actions"].values())
    ):
        raise ValueError("diagnosis closed-loop controls are invalid")
    _require_object_shape(
        diagnosis["next_action"],
        {
            "alternatives",
            "command_argv",
            "expected",
            "id",
            "reason",
            "timeout_seconds",
            "title",
            "writes",
        },
        set(),
        "diagnosis.next_action",
    )
    if (
        not isinstance(diagnosis["next_action"]["command_argv"], list)
        or not diagnosis["next_action"]["command_argv"]
        or diagnosis["next_action"]["alternatives"] != []
        or not isinstance(diagnosis["next_action"]["timeout_seconds"], int)
        or not 1 <= diagnosis["next_action"]["timeout_seconds"] <= 300
    ):
        raise ValueError("diagnosis bounded action is invalid")
    _require_object_shape(
        diagnosis["retest"],
        {"assertions", "hardening", "mode"},
        set(),
        "diagnosis.retest",
    )
    if diagnosis["retest"]["mode"] != "canonical-from-verified-diagnosis":
        raise ValueError("diagnosis retest mode is invalid")
    _require_object_shape(
        diagnosis["retest"]["hardening"],
        {
            "reject_supplied_assertion_drift",
            "require_same_ring_source_dependency_catalog_bytes",
            "require_same_shard",
            "require_transport_screen",
            "require_valid_replay",
        },
        set(),
        "diagnosis.retest.hardening",
    )
    if not all(diagnosis["retest"]["hardening"].values()):
        raise ValueError("diagnosis retest hardening is incomplete")
    canonical_assertions = _canonical_retest_assertions(diagnosis)
    if diagnosis["retest"]["assertions"] != canonical_assertions:
        raise ValueError(
            "diagnosis supplied assertions differ from canonical assertions"
        )
    _require_object_shape(
        diagnosis["maintainer_handoff"],
        {
            "base",
            "bounded_follow_up_limit",
            "closed_loop_contract",
            "forbidden",
            "repository",
            "required_flow",
            "soak_order",
            "system",
        },
        set(),
        "diagnosis.maintainer_handoff",
    )
    if (
        diagnosis["maintainer_handoff"]["system"] != "RAPP Pit Crew"
        or diagnosis["maintainer_handoff"]["bounded_follow_up_limit"] != 1
    ):
        raise ValueError("diagnosis maintainer handoff is invalid")
    return canonical_assertions


def _retest(diagnosis, observations):
    _assert_no_sensitive_input(diagnosis)
    _assert_no_sensitive_input(observations)
    _validate_observation_shape(observations)
    context = _normalize_unknown_context(observations)
    context_findings = _context_findings(context)
    assertions = _validate_diagnosis(diagnosis)
    results = []
    for assertion in assertions:
        path = str(assertion.get("path") or "")
        actual = _path_value(observations, path)
        if "equals" in assertion:
            expected = assertion["equals"]
            passed = actual == expected
        elif "contains_all" in assertion:
            expected = assertion["contains_all"]
            passed = isinstance(actual, list) and set(expected).issubset(
                set(actual)
            )
        else:
            expected = None
            passed = False
        results.append(
            {
                "path": path,
                "expected": expected,
                "actual": actual,
                "passed": passed,
            }
        )
    hardening_passed = (
        context["replay_reported"]
        and context["transport_reported"]
        and not context_findings["quarantine_reasons"]
    )
    results.append(
        {
            "path": "hardening.replay_transport_and_quarantine",
            "expected": "valid exact replay and non-quarantined transport",
            "actual": context_findings["quarantine_reasons"],
            "passed": hardening_passed,
        }
    )
    payload = {
        "schema": RETEST_SCHEMA,
        "support_system": "RAPP Roadside",
        "maintainer_system": "RAPP Pit Crew",
        "machine_issue_artifact": "Roadside Frame",
        "participation": "voluntary",
        "case_id": diagnosis.get("case_id"),
        "diagnosis_report_id": diagnosis.get("report_id"),
        "status": "PASS" if all(item["passed"] for item in results) else "FAIL",
        "assertions": results,
        "replay_manifest": context["replay"],
        "byte_bindings": context["bindings"],
        "report_controls": {
            "quarantined": bool(context_findings["quarantine_reasons"]),
            "quarantine_reasons": context_findings["quarantine_reasons"],
        },
        "wire_preserved": WIRE,
        "grail_modified": False,
        "credentials_collected": False,
        "external_network_used_by_agent": False,
        "telemetry": False,
    }
    payload["retest_id"] = _content_id(payload)
    return payload


def _confirm_release(diagnosis, confirmation):
    _assert_no_sensitive_input(diagnosis)
    _validate_diagnosis(diagnosis)
    if not isinstance(confirmation, dict):
        raise TypeError("confirmation must be an object")
    _require_object_shape(
        confirmation,
        {
            "customer",
            "duplicate_count",
            "issue_signature",
            "local_fix_sha256",
            "novel_result_verified",
            "release_frame",
            "roadside_frame_hash",
        },
        set(),
        "confirmation",
    )
    customer = confirmation["customer"]
    release = confirmation["release_frame"]
    _require_object_shape(
        customer,
        {
            "retest_id",
            "rollback_available",
            "rollback_tested",
            "status",
            "test_sha256",
        },
        set(),
        "confirmation.customer",
    )
    _require_object_shape(
        release,
        {
            "affected_commit",
            "fix_sha256",
            "human_approved",
            "issue_signature",
            "merge_target",
            "regression_test_sha256",
            "rings",
            "roadside_frame_hash",
            "schema",
        },
        set(),
        "confirmation.release_frame",
    )
    reasons = []
    expected_signature = _value_path(
        diagnosis, "issue_signature", "sha256", default=None
    )
    if confirmation.get("issue_signature") != expected_signature:
        reasons.append("issue-signature-mismatch")
    for label, value in (
        ("local-fix", confirmation.get("local_fix_sha256")),
        ("released-fix", release.get("fix_sha256")),
        ("released-test", release.get("regression_test_sha256")),
        ("customer-test", customer.get("test_sha256")),
        ("roadside-frame", release.get("roadside_frame_hash")),
        ("expected-roadside-frame", confirmation.get("roadside_frame_hash")),
    ):
        if not isinstance(value, str) or not HASH64.fullmatch(value):
            reasons.append(f"{label}-hash-invalid")
    if confirmation.get("local_fix_sha256") != release.get("fix_sha256"):
        reasons.append("local-fix-differs-from-released-fix")
    if customer.get("test_sha256") != release.get("regression_test_sha256"):
        reasons.append("customer-test-differs-from-released-test")
    if confirmation.get("roadside_frame_hash") != release.get(
        "roadside_frame_hash"
    ):
        reasons.append("release-frame-roadside-link-mismatch")
    if customer.get("status") != "PASS":
        reasons.append("customer-confirmation-failed")
    if (
        customer.get("rollback_available") is not True
        or customer.get("rollback_tested") is not True
    ):
        reasons.append("rollback-not-proven")
    if release.get("schema") != "rapp-roadside/release-frame-1":
        reasons.append("release-frame-schema-mismatch")
    if release.get("issue_signature") != expected_signature:
        reasons.append("release-frame-issue-signature-mismatch")
    if release.get("affected_commit") != _value_path(
        diagnosis, "byte_bindings", "values", "source_commit", default=None
    ):
        reasons.append("affected-commit-mismatch")
    if release.get("merge_target") != "main":
        reasons.append("release-merge-target-mismatch")
    if release.get("human_approved") is not True:
        reasons.append("release-not-human-approved")
    rings = release.get("rings")
    expected_rings = ["Canary", "Nightly", "Alpha", "Beta"]
    if (
        not isinstance(rings, list)
        or [item.get("name") for item in rings if isinstance(item, dict)]
        != expected_rings
        or any(
            set(item) != {"name", "artifact_sha256", "status"}
            or item.get("status") != "PASS"
            or not isinstance(item.get("artifact_sha256"), str)
            or not HASH64.fullmatch(item["artifact_sha256"])
            for item in (rings if isinstance(rings, list) else [])
        )
    ):
        reasons.append("ring-soak-proof-invalid")
    duplicate_count = confirmation.get("duplicate_count")
    if not isinstance(duplicate_count, int) or duplicate_count < 0:
        reasons.append("duplicate-count-invalid")
    if not isinstance(confirmation.get("novel_result_verified"), bool):
        reasons.append("novel-result-verification-invalid")
    reasons = sorted(set(reasons))
    confirmed = not reasons
    verified_resolution = None
    if confirmed:
        resolution_payload = {
            "issue_signature": expected_signature,
            "release_frame_sha256": _content_id(release),
            "customer_retest_id": customer.get("retest_id"),
            "customer_test_sha256": customer.get("test_sha256"),
        }
        verified_resolution = {
            "status": "verified-resolution",
            "resolution_id": _content_id(resolution_payload),
            "inputs": resolution_payload,
            "maintainer_feedback_disposition": (
                "novel-verified-inert-feed-record"
                if confirmation["novel_result_verified"]
                and duplicate_count == 0
                else "duplicate-aggregate-evidence-without-re-mining"
            ),
            "automatic_network_send": False,
        }
    result = {
        "schema": CONFIRMATION_SCHEMA,
        "status": "CONFIRMED" if confirmed else "FAIL",
        "issue_signature": expected_signature,
        "failure_reasons": reasons,
        "verified_resolution": verified_resolution,
        "next_action": (
            None
            if confirmed
            else {
                "id": "review-and-rollback-to-last-verified-release",
                "title": "Human reviews the mismatch and chooses rollback",
                "timeout_seconds": 300,
                "automatic": False,
                "destructive": False,
                "alternatives": [],
            }
        ),
        "automatic_actions": {
            "teams_send": False,
            "git_push": False,
            "main_edit": False,
            "production_deploy": False,
            "destructive_customer_repair": False,
            "maintainer_feedback_network_send": False,
        },
        "telemetry": False,
        "network_used": False,
    }
    result["confirmation_id"] = _content_id(result)
    return result


def _is_excluded(relative):
    for part in relative.parts:
        if part in EXCLUDED_NAMES:
            return True
        if part != ".env.example" and EXCLUDED_PATH_PART.search(part):
            return True
    return False


def _resolved_path_hash(path):
    return _content_id({"resolved_path": str(path.resolve())})


def _validate_repair_paths(source, destination):
    source = source.resolve()
    destination = destination.resolve()
    if not source.is_dir():
        raise ValueError("source_dir must be an existing directory")
    if any(
        source == root.resolve() or root.resolve() in source.parents
        for root in PROTECTED_REPAIR_ROOTS
    ):
        raise ValueError("source_dir must not be a protected system directory")
    if destination.exists():
        raise ValueError("copy_dir must not already exist")
    if source == destination:
        raise ValueError("copy_dir must differ from source_dir")
    if destination.parent != source.parent:
        raise ValueError("copy_dir must be a new sibling of source_dir")
    return source, destination


def _selected_repair_files(action_id, source):
    selected = []
    for relative_text in COPY_REPAIR_FILES[action_id]:
        relative = Path(relative_text)
        path = source / relative
        if path.is_symlink():
            raise ValueError(f"repair source file must not be a symlink: {relative_text}")
        if path.is_file():
            selected.append((relative, path))
    if not selected:
        raise ValueError("no allow-listed source files are available for this repair")
    return selected


def _scan_repair_files(action_id, source):
    selected = _selected_repair_files(action_id, source)
    total_bytes = 0
    records = []
    for relative, path in selected:
        data = path.read_bytes()
        total_bytes += len(data)
        if total_bytes > MAX_COPY_BYTES:
            raise ValueError("repair source exceeds the local safety bound")
        if b"\x00" in data:
            raise ValueError(f"repair source is not plain text: {relative.as_posix()}")
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError as error:
            raise ValueError(
                f"repair source is not UTF-8 text: {relative.as_posix()}"
            ) from error
        if (
            SENSITIVE_VALUE.search(text)
            or SENSITIVE_ASSIGNMENT.search(data)
            or NONPUBLIC_PATH.search(data)
        ):
            raise ValueError(
                f"repair source contains sensitive or nonpublic data: {relative.as_posix()}"
            )
        records.append(
            {
                "path": relative.as_posix(),
                "sha256": _sha256_bytes(data),
                "bytes": len(data),
            }
        )
    return selected, records, total_bytes


def _repair_source_fingerprint(action_id, source):
    _, records, _ = _scan_repair_files(action_id, source)
    return _content_id(records)


def _safe_copy(action_id, source, destination):
    source, destination = _validate_repair_paths(source, destination)
    selected, records, total_bytes = _scan_repair_files(action_id, source)
    selected_names = {relative.as_posix() for relative, _ in selected}
    excluded = []
    for path in sorted(source.rglob("*")):
        if path.is_dir():
            continue
        relative = path.relative_to(source)
        if relative.as_posix() not in selected_names:
            excluded.append(relative.as_posix())
    destination.mkdir()
    copied = []
    for relative, path in selected:
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        copied.append(relative.as_posix())
    return copied, sorted(set(excluded)), total_bytes, _content_id(records)


def _prepare_repair_approval(action_id, source_dir, copy_dir):
    source = Path(str(source_dir)).expanduser().resolve()
    destination = Path(str(copy_dir)).expanduser().resolve()
    if action_id not in COPY_REPAIR_ACTIONS:
        raise ValueError("action_id is not an allow-listed copy repair")
    source, destination = _validate_repair_paths(source, destination)
    source_fingerprint = _repair_source_fingerprint(action_id, source)
    return {
        "schema": APPROVAL_SCHEMA,
        "support_system": "RAPP Roadside",
        "maintainer_system": "RAPP Pit Crew",
        "status": "approval-required",
        "instructions": (
            "A human must review the diagnosis and this binding, then change "
            "only human_approved to true before fix_copy."
        ),
        "approval": {
            "human_approved": False,
            "action_id": action_id,
            "source_fingerprint": source_fingerprint,
            "source_path_sha256": _resolved_path_hash(source),
            "destination_path_sha256": _resolved_path_hash(destination),
            "reversible": True,
            "activation": "copy-only-no-activation",
        },
        "source_path_exported": False,
        "copy_path_exported": False,
    }


def _apply_copy_fix(action_id, source_dir, copy_dir, approval):
    source = Path(str(source_dir)).expanduser().resolve()
    destination = Path(str(copy_dir)).expanduser().resolve()
    if action_id not in COPY_REPAIR_ACTIONS:
        raise ValueError("action_id is not an allow-listed copy repair")
    source, destination = _validate_repair_paths(source, destination)
    source_fingerprint = _repair_source_fingerprint(action_id, source)
    source_path_sha256 = _resolved_path_hash(source)
    destination_path_sha256 = _resolved_path_hash(destination)
    if not isinstance(approval, dict):
        raise ValueError("fix_copy requires explicit human approval")
    _require_object_shape(
        approval,
        {
            "action_id",
            "activation",
            "destination_path_sha256",
            "human_approved",
            "reversible",
            "source_fingerprint",
            "source_path_sha256",
        },
        set(),
        "approval",
    )
    if (
        approval.get("human_approved") is not True
        or approval.get("reversible") is not True
        or approval.get("activation") != "copy-only-no-activation"
        or approval.get("action_id") != action_id
        or approval.get("source_fingerprint") != source_fingerprint
        or approval.get("source_path_sha256") != source_path_sha256
        or approval.get("destination_path_sha256")
        != destination_path_sha256
    ):
        raise ValueError(
            "human approval must bind the action, exact source bytes, resolved "
            "source and destination paths, reversibility, and no-activation scope"
        )
    try:
        copied, excluded, total_bytes, copied_source_fingerprint = _safe_copy(
            action_id, source, destination
        )
        if copied_source_fingerprint != source_fingerprint:
            raise RuntimeError("source fingerprint changed before copy creation")
        changed = []
        if action_id == "restore-launcher-files-copy":
            launchers = [
                destination / "installer" / "brainstem",
                destination / "installer" / "brainstem.cmd",
                destination / "installer" / "brainstem-boot.cjs",
            ]
            present = [path for path in launchers if path.is_file()]
            if not present:
                raise ValueError(
                    "no existing local launcher files were available to copy"
                )
        elif action_id == "restore-launcher-executable-copy":
            for relative in ("start.sh", "installer/brainstem"):
                target = destination / relative
                if target.is_file():
                    mode = target.stat().st_mode
                    target.chmod(mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
                    changed.append(relative)
            if not changed:
                raise ValueError("no copied Unix launcher was found")
        elif action_id == "synchronize-installer-mirrors-copy":
            for filename in ("install.sh", "install.ps1", "install.cmd"):
                root = destination / filename
                mirror = destination / "docs" / filename
                if root.is_file():
                    mirror.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(root, mirror)
                    changed.append(f"docs/{filename}")
            if not changed:
                raise ValueError("no copied root installer was found")
        elif action_id == "normalize-windows-launchers-copy":
            for relative in ("install.ps1", "install.cmd"):
                target = destination / relative
                if target.is_file():
                    text = target.read_text(encoding="utf-8").replace("\r\n", "\n")
                    target.write_bytes(text.replace("\n", "\r\n").encode("utf-8"))
                    changed.append(relative)
            if not changed:
                raise ValueError("no copied Windows launcher was found")
        if _repair_source_fingerprint(action_id, source) != source_fingerprint:
            raise RuntimeError("source fingerprint changed during copy repair")
    except Exception:
        if destination.exists():
            shutil.rmtree(destination)
        raise

    destination_fingerprint = _tree_fingerprint(destination)
    receipt = {
        "schema": FIX_SCHEMA,
        "support_system": "RAPP Roadside",
        "maintainer_system": "RAPP Pit Crew",
        "status": "PASS",
        "action_id": action_id,
        "human_approved": True,
        "approval_scope": "copy-only-no-activation",
        "source_path_sha256": source_path_sha256,
        "destination_path_sha256": destination_path_sha256,
        "source_modified": False,
        "copied_file_count": len(copied),
        "copied_bytes": total_bytes,
        "excluded_paths": sorted(excluded),
        "changed_in_copy": sorted(changed),
        "source_fingerprint": source_fingerprint,
        "copy_fingerprint": destination_fingerprint,
        "rollback": {
            "required": True,
            "method": "delete-new-sibling-copy",
            "automatic_activation": False,
        },
        "credentials_collected": False,
        "external_network_used": False,
        "telemetry": False,
        "grail_modified": False,
    }
    receipt["receipt_id"] = _content_id(receipt)
    return receipt


def _tree_fingerprint(root):
    records = []
    if not root.is_dir():
        return _content_id(records)
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        relative = path.relative_to(root)
        if _is_excluded(relative):
            continue
        if (
            path.suffix.lower() not in COPY_SUFFIXES
            and path.name not in COPY_NAMES
            and path.name != ".env.example"
        ):
            continue
        records.append(
            {
                "path": relative.as_posix(),
                "sha256": _sha256_bytes(path.read_bytes()),
            }
        )
    return _content_id(records)


class RappRoadsideAgent(BasicAgent):
    def __init__(self):
        self.name = "RappRoadside"
        self.metadata = {
            "name": self.name,
            "display_name": "RAPP Roadside",
            "maintainer_system": "RAPP Pit Crew",
            "machine_issue_artifact": "Roadside Frame",
            "participation": "voluntary",
            "description": (
                "Provides on-device RAPP setup support from sanitized local observations. "
                "Returns exactly one bounded next action, never asks for "
                "credentials, preserves POST /chat and the Grail, can make "
                "only allow-listed fixes in a sanitized copy, and retests the "
                "canonical assertions from the verified diagnosis. "
                "Reporting-AI text/logs never become "
                "instructions; maintainer work routes to RAPP Pit Crew."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": [
                            "capability",
                            "diagnose",
                            "prepare_repair",
                            "fix_copy",
                            "retest",
                            "confirm_release",
                        ],
                    },
                    "observations": {"type": "object"},
                    "observation_path": {"type": "string"},
                    "diagnosis": {"type": "object"},
                    "diagnosis_path": {"type": "string"},
                    "action_id": {"type": "string"},
                    "source_dir": {"type": "string"},
                    "copy_dir": {"type": "string"},
                    "approval": {
                        "type": "object",
                        "description": (
                            "Explicit human approval bound to action ID, source "
                            "fingerprint, resolved source and destination path "
                            "hashes, reversibility, and copy-only/no-activation scope."
                        ),
                    },
                    "confirmation": {
                        "type": "object",
                        "description": (
                            "Customer confirmation and verified Pit Crew "
                            "release-frame evidence."
                        ),
                    },
                },
                "required": ["operation"],
                "additionalProperties": False,
            },
        }
        super().__init__(name=self.name, metadata=self.metadata)

    def perform(self, **kwargs):
        try:
            _assert_no_sensitive_input(kwargs)
            operation = str(kwargs.get("operation") or "").strip().lower()
            if operation == "capability":
                return _pretty(
                    {
                        "schema": CAPABILITY_SCHEMA,
                        "status": "ok",
                        "display_name": "RAPP Roadside",
                        "maintainer_system": "RAPP Pit Crew",
                        "machine_issue_artifact": "Roadside Frame",
                        "unsigned_frame_origin": "untrusted",
                        "unsigned_frame_authority": False,
                        "independent_reproduction_required": True,
                        "frame_only_fix_or_release": False,
                        "protocol_schema_ids_retained": True,
                        "operations": [
                            "capability",
                            "diagnose",
                            "prepare_repair",
                            "fix_copy",
                            "retest",
                            "confirm_release",
                        ],
                        "wire": WIRE,
                        "stable_main_identity": STABLE_MAIN_IDENTITY,
                        "safety": {
                            "credentials_collected": False,
                            "external_network": "refused; loopback probe is a separate explicit companion",
                            "source_writes": False,
                            "repair_file_scope": "exact-action-allowlist",
                            "precreation_content_scan": True,
                            "copy_repairs": sorted(
                                [
                                    "normalize-windows-launchers-copy",
                                    "restore-launcher-executable-copy",
                                    "restore-launcher-files-copy",
                                    "synchronize-installer-mirrors-copy",
                                ]
                            ),
                        },
                    }
                )
            if operation == "diagnose":
                observations = kwargs.get("observations")
                if observations is None and kwargs.get("observation_path"):
                    observations = _load_json(kwargs["observation_path"])
                if not isinstance(observations, dict):
                    raise TypeError(
                        "diagnose requires observations or observation_path"
                    )
                return _pretty(_diagnose(observations))
            if operation == "retest":
                diagnosis = kwargs.get("diagnosis")
                if diagnosis is None and kwargs.get("diagnosis_path"):
                    diagnosis = _load_json(kwargs["diagnosis_path"])
                observations = kwargs.get("observations")
                if observations is None and kwargs.get("observation_path"):
                    observations = _load_json(kwargs["observation_path"])
                if not isinstance(diagnosis, dict) or not isinstance(
                    observations, dict
                ):
                    raise TypeError(
                        "retest requires diagnosis and observations objects or paths"
                    )
                return _pretty(_retest(diagnosis, observations))
            if operation == "prepare_repair":
                return _pretty(
                    _prepare_repair_approval(
                        str(kwargs.get("action_id") or ""),
                        kwargs.get("source_dir"),
                        kwargs.get("copy_dir"),
                    )
                )
            if operation == "confirm_release":
                diagnosis = kwargs.get("diagnosis")
                if diagnosis is None and kwargs.get("diagnosis_path"):
                    diagnosis = _load_json(kwargs["diagnosis_path"])
                if not isinstance(diagnosis, dict):
                    raise TypeError(
                        "confirm_release requires diagnosis or diagnosis_path"
                    )
                return _pretty(
                    _confirm_release(diagnosis, kwargs.get("confirmation"))
                )
            if operation == "fix_copy":
                return _pretty(
                    _apply_copy_fix(
                        str(kwargs.get("action_id") or ""),
                        kwargs.get("source_dir"),
                        kwargs.get("copy_dir"),
                        kwargs.get("approval"),
                    )
                )
            return _pretty(
                {
                    "status": "error",
                    "code": "unknown-operation",
                    "message": (
                        "operation must be capability, diagnose, prepare_repair, "
                        "fix_copy, retest, or confirm_release"
                    ),
                }
            )
        except (
            OSError,
            RuntimeError,
            ValueError,
            TypeError,
            json.JSONDecodeError,
        ) as error:
            return _pretty(
                {
                    "status": "error",
                    "code": type(error).__name__,
                    "message": str(error),
                    "credentials_collected": False,
                    "external_network_used": False,
                    "source_modified": False,
                    "grail_modified": False,
                }
            )


RarInstallerTroubleshooterAgent = RappRoadsideAgent


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    agent = RappRoadsideAgent()
    if argv and argv[0] == "--tool":
        print(_pretty(agent.to_tool()))
        return 0
    raw = argv[0] if argv else (sys.stdin.read().strip() or "{}")
    try:
        arguments = json.loads(raw)
    except json.JSONDecodeError as error:
        print(
            _pretty(
                {
                    "status": "error",
                    "code": "invalid-json",
                    "message": str(error),
                }
            )
        )
        return 2
    if not isinstance(arguments, dict):
        print(
            _pretty(
                {
                    "status": "error",
                    "code": "invalid-arguments",
                    "message": "Arguments must be one JSON object.",
                }
            )
        )
        return 2
    print(agent.perform(**arguments))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
