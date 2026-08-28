---
name: "rar-cat-agent-skills-iterative-file-editing"
description: "In Copilot Studio, re-sending an edited file under the same name fails to deliver it \u2014 the change is made but never reaches the user. This skill gives each iteration a new version-numbered filename (report_v1.docx, report_v2.docx\u2026) so every update actually lands in the chat as its own attachment."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/iterative_file_editing", "rar_sha256": "cce8b6e20451b55794496c50b14c159915737e03af94e3e7c2d3dcc01b8588f8", "source_kind": "rar-agent", "source_commit": "cdba6310faf6c2aa731f37d58cfe8e921a360080", "version": "2.0.0", "author": "Adi Leibowitz", "tags": ["files", "iteration", "workflow", "collaboration", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/iterative_file_editing`. The original RAPP
agent is preserved byte-for-byte in `iterative_file_editing_agent.py` and in the RCI capsule.

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
