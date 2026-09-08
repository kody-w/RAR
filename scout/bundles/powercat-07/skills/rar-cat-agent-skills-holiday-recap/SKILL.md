---
name: "rar-cat-agent-skills-holiday-recap"
description: "Catch up after annual leave in one pass \u2014 a single prioritised briefing of the mail, meetings, and Teams conversations you missed, with deep links and one-click follow-up actions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/holiday_recap", "rar_sha256": "2c2f3afcaaf83a61a8e802af8b22881c167e51e5fb4b813636c06dc77ce2e32a", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Suparna Banerjee", "tags": ["productivity", "outlook", "teams", "email", "meetings", "calendar", "summarization", "catch_up"]}
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
