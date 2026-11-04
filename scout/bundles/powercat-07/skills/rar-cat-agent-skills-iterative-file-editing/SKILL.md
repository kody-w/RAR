---
name: "rar-cat-agent-skills-iterative-file-editing"
description: "In Copilot Studio, re-sending an edited file under the same name fails to deliver it \u2014 the change is made but never reaches the user. This skill gives each iteration a new version-numbered filename (report_v1.docx, report_v2.docx\u2026) so every update actually lands in the chat as its own attachment."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/iterative_file_editing", "rar_sha256": "2250fc38fc33af9fc658a7a03db2db27ddcde3a4f9263e061f0a01561369a12e", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Adi Leibowitz", "tags": ["files", "iteration", "workflow", "collaboration", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `iterative_file_editing_agent.py` and embedded as the fenced Python below (sha256 2250fc38fc33af9f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `iterative_file_editing_agent.py` first:

```bash
python3 iterative_file_editing_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 iterative_file_editing_agent.py   # or on stdin
python3 iterative_file_editing_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/iterative_file_editing_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/iterative_file_editing_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/iterative_file_editing/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
