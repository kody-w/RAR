---
name: "rar-cat-agent-skills-holiday-recap"
description: "Catch up after annual leave in one pass \u2014 a single prioritised briefing of the mail, meetings, and Teams conversations you missed, with deep links and one-click follow-up actions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/holiday_recap", "rar_sha256": "0b187c270dc5fe3382fefdb070aeb9946a808706a8dce261c598b2bb9883407b", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Suparna Banerjee", "tags": ["productivity", "outlook", "teams", "email", "meetings", "calendar", "summarization", "catch_up"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `holiday_recap_agent.py` and embedded as the fenced Python below (sha256 0b187c270dc5fe33…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `holiday_recap_agent.py` first:

```bash
python3 holiday_recap_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 holiday_recap_agent.py   # or on stdin
python3 holiday_recap_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/holiday_recap_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/holiday_recap_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/holiday_recap/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
