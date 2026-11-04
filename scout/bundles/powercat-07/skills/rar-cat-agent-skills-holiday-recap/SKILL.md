---
name: "rar-cat-agent-skills-holiday-recap"
description: "Catch up after annual leave in one pass \u2014 a single prioritised briefing of the mail, meetings, and Teams conversations you missed, with deep links and one-click follow-up actions."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/holiday_recap", "rar_sha256": "0b187c270dc5fe3382fefdb070aeb9946a808706a8dce261c598b2bb9883407b", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Suparna Banerjee", "tags": ["productivity", "outlook", "teams", "email", "meetings", "calendar", "summarization", "catch_up"]}
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
