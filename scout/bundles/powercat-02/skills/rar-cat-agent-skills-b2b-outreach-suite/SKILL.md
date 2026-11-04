---
name: "rar-cat-agent-skills-b2b-outreach-suite"
description: "A six-playbook toolkit for agentic B2B sales outreach: prospect research briefings, cold emails, LinkedIn/social DMs, follow-up cadences, ad copywriting, and objection handling. Configurable via a company profile template, works for any industry, market, and language."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/b2b_outreach_suite", "rar_sha256": "8cc4246e1e7974a219004eefc17de83bb2b40c83523cc4f89c47d14275832397", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Marcel", "tags": ["sales_enablement", "email", "linkedin", "writing", "marketing", "content"]}
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
