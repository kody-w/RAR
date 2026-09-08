---
name: "rar-cat-agent-skills-iterative-file-editing"
description: "In Copilot Studio, re-sending an edited file under the same name fails to deliver it \u2014 the change is made but never reaches the user. This skill gives each iteration a new version-numbered filename (report_v1.docx, report_v2.docx\u2026) so every update actually lands in the chat as its own attachment."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/iterative_file_editing", "rar_sha256": "a4d257098864c459b987e5f2d613b74b9ce2dfca94886c34306fbb4869d073db", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Adi Leibowitz", "tags": ["files", "iteration", "workflow", "collaboration", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `iterative_file_editing_agent.py` and embedded as the fenced Python below (sha256 a4d257098864c459…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `iterative_file_editing_agent.py` first:

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
    "version": '3.0.2',
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
