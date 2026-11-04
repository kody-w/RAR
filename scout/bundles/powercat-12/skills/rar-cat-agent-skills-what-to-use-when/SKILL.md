---
name: "rar-cat-agent-skills-what-to-use-when"
description: "Routes single-output requests to the best-fit included Microsoft 365 Copilot 1p agents and reserves Cowork for long-running or multi-output work."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/what_to_use_when", "rar_sha256": "de37690c140876aa9124ffc85a7712d4c93d0a5423e25cc6814416fcaba0e993", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Gaurav Mahajan", "tags": ["productivity", "automation", "copilot", "routing"]}
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
