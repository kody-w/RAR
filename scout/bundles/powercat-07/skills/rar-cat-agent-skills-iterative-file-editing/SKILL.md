---
name: "rar-cat-agent-skills-iterative-file-editing"
description: "In Copilot Studio, re-sending an edited file under the same name fails to deliver it \u2014 the change is made but never reaches the user. This skill gives each iteration a new version-numbered filename (report_v1.docx, report_v2.docx\u2026) so every update actually lands in the chat as its own attachment."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/iterative_file_editing", "rar_sha256": "cce8b6e20451b55794496c50b14c159915737e03af94e3e7c2d3dcc01b8588f8", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "iterative_file_editing_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cat-agent-skills/iterative-file-editing:11c3d818e24a7b1fbfc5cb8038cc811f19bb3e5ed6c6bbf8f74933e7123bebba", "kind": "skill"}, "version": "2.0.0", "author": "Adi Leibowitz", "tags": ["files", "iteration", "workflow", "collaboration", "productivity"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cat-agent-skills/iterative_file_editing`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `iterative_file_editing_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Iterative File Editing — In Copilot Studio, re-sending an edited file under the same name fails to deliver it — the change is made but never reaches the user. This skill gives each iteration a new version-numbered filename (report_v1.docx, report_v2.docx…) so every update actually lands in the chat as its own attachment.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#iterative-file-editing
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "operation": {
      "description": "What to do: run, plan, checklist, describe.",
      "enum": [
        "run",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "subject": {
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `iterative_file_editing_agent.py` and embedded as the fenced Python below (sha256 cce8b6e20451b557…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `iterative_file_editing_agent.py` first:

```bash
python3 iterative_file_editing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 iterative_file_editing_agent.py   # or on stdin
python3 iterative_file_editing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Iterative File Editing — In Copilot Studio, re-sending an edited file under the same name fails to deliver it — the change is made but never reaches the user. This skill gives each iteration a new version-numbered filename (report_v1.docx, report_v2.docx…) so every update actually lands in the chat as its own attachment.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#iterative-file-editing
  Upstream author: Adi Leibowitz
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/iterative_file_editing',
    "version": '2.0.0',
    "display_name": 'Iterative File Editing',
    "description": 'In Copilot Studio, re-sending an edited file under the same name fails to deliver it — the change is made but never reaches the user. This skill gives each iteration a new version-numbered filename (report_v1.docx, report_v2.docx…) so every update actually lands in the chat as its own attachment.',
    "author": 'Adi Leibowitz',
    "tags": ['files', 'iteration', 'workflow', 'collaboration', 'productivity'],
    "category": 'general',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'iterative-file-editing',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#iterative-file-editing',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'fe1e0e3d17cbdfee',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class IterativeFileEditing(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'IterativeFileEditing'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
                "required": ["operation"],
            },
        }
        super().__init__(self.name, self.metadata)

    # ── helpers ─────────────────────────────────────────────────────────

    def _subject(self, kwargs):
        for key in ("subject", "input", "target", "topic"):
            value = str(kwargs.get(key) or "").strip()
            if value:
                return value
        return ""

    def _header(self, subject):
        label = subject or f"<no {_SPEC['subject_label']} supplied>"
        return f"{_SPEC['verb']}: {label}"

    def _context(self, kwargs):
        extras = []
        for key in _SPEC["params"]:
            if key == "subject":
                continue
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _plan(self, subject, kwargs):
        lines = [self._header(subject)]
        extras = self._context(kwargs)
        if extras:
            lines += ["", "Context:"] + [f"  {e}" for e in extras]
        lines += ["", "Procedure:"]
        lines += [f"  {i}. {step}" for i, step in enumerate(_SPEC["steps"], 1)]
        if not subject:
            lines += [
                "",
                f"Pass subject=\u0022...\u0022 to bind this procedure to a "
                f"specific {_SPEC['subject_label']}.",
            ]
        return lines

    def _checklist(self):
        return ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]]

    def _provenance(self):
        src = __manifest__["source"]
        lines = [
            f"{__manifest__['display_name']} (v{__manifest__['version']})",
            "",
            __manifest__["description"],
            "",
            f"Capability shape: {_SPEC['archetype']} "
            f"(confidence {_SPEC['confidence']})",
        ]
        platforms = __manifest__.get("platforms") or []
        if platforms:
            lines.append("Runs on:          " + ", ".join(platforms))
        lines += [
            "",
            f"Indexed from:     {src['source_name']}",
            f"Upstream entry:   {src['upstream_url']}",
            f"Upstream author:  {__manifest__['author']}",
            "",
            "RAR indexes this capability and implements its method; the "
            "upstream library remains the authority for its own instructions. "
            "Open the link above to get those from the source.",
        ]
        return lines

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if op == "describe":
            return "\n".join(self._provenance())

        if op == "checklist":
            return "\n".join([self._header(subject), ""] + self._checklist())

        if op == "plan":
            return "\n".join(self._plan(subject, kwargs))

        if op == "run":
            lines = self._plan(subject, kwargs)
            lines += [""] + self._checklist()
            lines += ["", f"Deliverable: {_SPEC['deliverable']}"]
            lines += ["", f"Source: {__manifest__['source']['upstream_url']}"]
            return "\n".join(lines)

        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )


if __name__ == "__main__":
    print(IterativeFileEditing().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
