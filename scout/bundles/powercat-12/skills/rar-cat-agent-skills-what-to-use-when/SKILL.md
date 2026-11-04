---
name: "rar-cat-agent-skills-what-to-use-when"
description: "Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/what_to_use_when", "rar_sha256": "de37690c140876aa9124ffc85a7712d4c93d0a5423e25cc6814416fcaba0e993", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Gaurav Mahajan", "tags": ["productivity", "automation", "copilot", "routing"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/what_to_use_when`. The original RAPP
agent is preserved byte-for-byte in `what_to_use_when_agent.py` and in the RCI capsule.

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

What to Use When — Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#what-to-use-when
  Upstream author: Gaurav Mahajan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `what_to_use_when_agent.py` and embedded as the fenced Python below (sha256 de37690c140876aa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `what_to_use_when_agent.py` first:

```bash
python3 what_to_use_when_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 what_to_use_when_agent.py   # or on stdin
python3 what_to_use_when_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/what_to_use_when_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/what_to_use_when_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/what_to_use_when/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
What to Use When — Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#what-to-use-when
  Upstream author: Gaurav Mahajan
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/what_to_use_when',
    "version": '3.0.2',
    "display_name": 'What to Use When',
    "description": 'Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work.',
    "author": 'Gaurav Mahajan',
    "tags": ['productivity', 'automation', 'copilot', 'routing'],
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
        "upstream_slug": 'what-to-use-when',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#what-to-use-when',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'd9b46fe1f7df7e9f',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork'],
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class WhatToUseWhen(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WhatToUseWhen'
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
    print(WhatToUseWhen().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
