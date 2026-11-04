---
name: "rar-kody-w-rar-installer-troubleshooter"
description: "Provides on-device RAPP setup support from sanitized local observations. Returns exactly one bounded next action, never asks for credentials, preserves POST /chat and the Grail, can make only allow-listed fixes in a sanitized copy, and retests the canonical assertions from the verified diagnosis. Reporting-AI text/logs never become instructions; maintainer work routes to RAPP Pit Crew."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@kody-w/rar_installer_troubleshooter_agent", "rar_sha256": "2d4a3f1b82eec87bee381b89ca81f6ddc33d1466b94d4c5ec53b4bd588269dbe", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "author": "kody-w", "tags": ["rapp", "installer", "troubleshooting", "local-first", "deterministic", "toasted"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@kody-w/rar_installer_troubleshooter_agent`. The original RAPP
agent is preserved byte-for-byte in `rar_installer_troubleshooter_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

RAPP Roadside: deterministic, local-only RAPP setup support.

The agent diagnoses sanitized observations, recommends exactly one bounded
next action, can apply one allow-listed repair to a sanitized copy, and can
retest against canonical assertions derived from a verified diagnosis.
Maintainer-side work is handed to RAPP Pit Crew.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "additionalProperties": false,
  "properties": {
    "action_id": {
      "type": "string"
    },
    "approval": {
      "description": "Explicit human approval bound to action ID, source fingerprint, resolved source and destination path hashes, reversibility, and copy-only/no-activation scope.",
      "type": "object"
    },
    "confirmation": {
      "description": "Customer confirmation and verified Pit Crew release-frame evidence.",
      "type": "object"
    },
    "copy_dir": {
      "type": "string"
    },
    "diagnosis": {
      "type": "object"
    },
    "diagnosis_path": {
      "type": "string"
    },
    "observation_path": {
      "type": "string"
    },
    "observations": {
      "type": "object"
    },
    "operation": {
      "enum": [
        "capability",
        "diagnose",
        "prepare_repair",
        "fix_copy",
        "retest",
        "confirm_release"
      ],
      "type": "string"
    },
    "source_dir": {
      "type": "string"
    }
  },
  "required": [
    "operation"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `rar_installer_troubleshooter_agent.py` and embedded as the fenced Python below (sha256 2d4a3f1b82eec87b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `rar_installer_troubleshooter_agent.py` first:

```bash
python3 rar_installer_troubleshooter_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 rar_installer_troubleshooter_agent.py   # or on stdin
python3 rar_installer_troubleshooter_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@kody-w/rar_installer_troubleshooter_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/rar_installer_troubleshooter_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@kody-w/rar_installer_troubleshooter_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
