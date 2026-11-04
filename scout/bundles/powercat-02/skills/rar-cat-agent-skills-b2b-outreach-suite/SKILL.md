---
name: "rar-cat-agent-skills-b2b-outreach-suite"
description: "A six-playbook toolkit for agentic B2B sales outreach: prospect research briefings, cold emails, LinkedIn/social DMs, follow-up cadences, ad copywriting, and objection handling. Configurable via a company profile template, works for any industry, market, and language."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/b2b_outreach_suite", "rar_sha256": "8cc4246e1e7974a219004eefc17de83bb2b40c83523cc4f89c47d14275832397", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Marcel", "tags": ["sales_enablement", "email", "linkedin", "writing", "marketing", "content"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `b2b_outreach_suite_agent.py` and embedded as the fenced Python below (sha256 8cc4246e1e7974a2…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `b2b_outreach_suite_agent.py` first:

```bash
python3 b2b_outreach_suite_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 b2b_outreach_suite_agent.py   # or on stdin
python3 b2b_outreach_suite_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/b2b_outreach_suite_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/b2b_outreach_suite_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/b2b_outreach_suite/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
