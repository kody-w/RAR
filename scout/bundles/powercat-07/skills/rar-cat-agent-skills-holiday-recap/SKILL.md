---
name: "rar-cat-agent-skills-holiday-recap"
description: "Catch up after annual leave in one pass \u2014 a single prioritised briefing of the mail, meetings, and Teams conversations you missed, with deep links and one-click follow-up actions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/holiday_recap", "rar_sha256": "2c2f3afcaaf83a61a8e802af8b22881c167e51e5fb4b813636c06dc77ce2e32a", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Suparna Banerjee", "tags": ["productivity", "outlook", "teams", "email", "meetings", "calendar", "summarization", "catch_up"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/holiday_recap`. The original RAPP
agent is preserved byte-for-byte in `holiday_recap_agent.py` and in the RCI capsule.

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

Holiday Recap — Catch up after annual leave in one pass — a single prioritised briefing of the mail, meetings, and Teams conversations you missed, with deep links and one-click follow-up actions.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#holiday-recap
  Upstream author: Suparna Banerjee
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
      "type": "string"
    },
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `holiday_recap_agent.py` and embedded as the fenced Python below (sha256 2c2f3afcaaf83a61…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `holiday_recap_agent.py` first:

```bash
python3 holiday_recap_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 holiday_recap_agent.py   # or on stdin
python3 holiday_recap_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Holiday Recap — Catch up after annual leave in one pass — a single prioritised briefing of the mail, meetings, and Teams conversations you missed, with deep links and one-click follow-up actions.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#holiday-recap
  Upstream author: Suparna Banerjee
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/holiday_recap',
    "version": '3.0.2',
    "display_name": 'Holiday Recap',
    "description": 'Catch up after annual leave in one pass — a single prioritised briefing of the mail, meetings, and Teams conversations you missed, with deep links and one-click follow-up actions.',
    "author": 'Suparna Banerjee',
    "tags": ['productivity', 'outlook', 'teams', 'email', 'meetings', 'calendar', 'summarization', 'catch_up'],
    "category": 'productivity',
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
        "upstream_slug": 'holiday-recap',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#holiday-recap',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b77bc3573d477e5b',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 1.0, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:email'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class HolidayRecap(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'HolidayRecap'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(HolidayRecap().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
