---
name: "rar-cat-agent-skills-iterative-file-editing"
description: "In Copilot Studio, re-sending an edited file under the same name fails to deliver it \u2014 the change is made but never reaches the user. This skill gives each iteration a new version-numbered filename (report_v1.docx, report_v2.docx\u2026) so every update actually lands in the chat as its own attachment."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/iterative_file_editing", "rar_sha256": "a4d257098864c459b987e5f2d613b74b9ce2dfca94886c34306fbb4869d073db", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Adi Leibowitz", "tags": ["files", "iteration", "workflow", "collaboration", "productivity"]}
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
