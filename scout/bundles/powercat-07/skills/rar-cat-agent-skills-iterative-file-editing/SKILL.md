---
name: "rar-cat-agent-skills-iterative-file-editing"
description: "In Copilot Studio, re-sending an edited file under the same name fails to deliver it \u2014 the change is made but never reaches the user. This skill gives each iteration a new version-numbered filename (report_v1.docx, report_v2.docx\u2026) so every update actually lands in the chat as its own attachment."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/iterative_file_editing", "rar_sha256": "2250fc38fc33af9fc658a7a03db2db27ddcde3a4f9263e061f0a01561369a12e", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Adi Leibowitz", "tags": ["files", "iteration", "workflow", "collaboration", "productivity"]}
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
