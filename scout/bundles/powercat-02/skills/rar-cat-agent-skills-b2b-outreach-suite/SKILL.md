---
name: "rar-cat-agent-skills-b2b-outreach-suite"
description: "A six-playbook toolkit for agentic B2B sales outreach: prospect research briefings, cold emails, LinkedIn/social DMs, follow-up cadences, ad copywriting, and objection handling. Configurable via a company profile template, works for any industry, market, and language."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/b2b_outreach_suite", "rar_sha256": "b50fc4375cf3ba5d548b20ed337a1afea0fbc564076f6cab1da021097fb34fd0", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Marcel", "tags": ["sales_enablement", "email", "linkedin", "writing", "marketing", "content"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/b2b_outreach_suite`. The original RAPP
agent is preserved byte-for-byte in `b2b_outreach_suite_agent.py` and in the RCI capsule.

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

B2B Outreach Suite — A six-playbook toolkit for agentic B2B sales outreach: prospect research briefings, cold emails, LinkedIn/social DMs, follow-up cadences, ad copywriting, and objection handling. Configurable via a company profile template, works for any industry, market, and language.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#b2b-outreach-suite
  Upstream author: Marcel
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `b2b_outreach_suite_agent.py` and embedded as the fenced Python below (sha256 b50fc4375cf3ba5d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `b2b_outreach_suite_agent.py` first:

```bash
python3 b2b_outreach_suite_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 b2b_outreach_suite_agent.py   # or on stdin
python3 b2b_outreach_suite_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
B2B Outreach Suite — A six-playbook toolkit for agentic B2B sales outreach: prospect research briefings, cold emails, LinkedIn/social DMs, follow-up cadences, ad copywriting, and objection handling. Configurable via a company profile template, works for any industry, market, and language.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#b2b-outreach-suite
  Upstream author: Marcel
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/b2b_outreach_suite',
    "version": '3.0.2',
    "display_name": 'B2B Outreach Suite',
    "description": 'A six-playbook toolkit for agentic B2B sales outreach: prospect research briefings, cold emails, LinkedIn/social DMs, follow-up cadences, ad copywriting, and objection handling. Configurable via a company profile template, works for any industry, market, and language.',
    "author": 'Marcel',
    "tags": ['sales_enablement', 'email', 'linkedin', 'writing', 'marketing', 'content'],
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
        "upstream_slug": 'b2b-outreach-suite',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#b2b-outreach-suite',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'b6d141c5052aba20',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Cowork', 'Copilot Studio', 'Scout'],
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.857, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content', 'tag:email', 'tag:writing'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class B2bOutreachSuite(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'B2bOutreachSuite'
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
    print(B2bOutreachSuite().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
