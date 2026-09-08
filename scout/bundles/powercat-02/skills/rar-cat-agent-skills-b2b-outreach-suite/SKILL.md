---
name: "rar-cat-agent-skills-b2b-outreach-suite"
description: "A six-playbook toolkit for agentic B2B sales outreach: prospect research briefings, cold emails, LinkedIn/social DMs, follow-up cadences, ad copywriting, and objection handling. Configurable via a company profile template, works for any industry, market, and language."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/b2b_outreach_suite", "rar_sha256": "b50fc4375cf3ba5d548b20ed337a1afea0fbc564076f6cab1da021097fb34fd0", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.2", "author": "Marcel", "tags": ["sales_enablement", "email", "linkedin", "writing", "marketing", "content"]}
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
