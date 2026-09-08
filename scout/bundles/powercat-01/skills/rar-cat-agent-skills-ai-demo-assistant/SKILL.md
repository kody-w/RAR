---
name: "rar-cat-agent-skills-ai-demo-assistant"
description: "Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo \u2014 fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_demo_assistant", "rar_sha256": "0165c6ce3d00a88f977723874a6fb0151cd850b987b27b34359d4a8f111f09c2", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Doak Moore", "tags": ["demo", "copilot", "microsoft_365", "sales_enablement", "content", "productivity"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/ai_demo_assistant`. The original RAPP
agent is preserved byte-for-byte in `ai_demo_assistant_agent.py` and in the RCI capsule.

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

AI Demo Assistant — Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo — fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-demo-assistant
  Upstream author: Doak Moore
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ai_demo_assistant_agent.py` and embedded as the fenced Python below (sha256 0165c6ce3d00a88f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ai_demo_assistant_agent.py` first:

```bash
python3 ai_demo_assistant_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ai_demo_assistant_agent.py   # or on stdin
python3 ai_demo_assistant_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
AI Demo Assistant — Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo — fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#ai-demo-assistant
  Upstream author: Doak Moore
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/ai_demo_assistant',
    "version": '3.0.2',
    "display_name": 'AI Demo Assistant',
    "description": 'Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo — fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams.',
    "author": 'Doak Moore',
    "tags": ['demo', 'copilot', 'microsoft_365', 'sales_enablement', 'content', 'productivity'],
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
        "upstream_slug": 'ai-demo-assistant',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#ai-demo-assistant',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'c768346e949547d4',
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.5, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:content'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class AiDemoAssistant(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AiDemoAssistant'
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
    print(AiDemoAssistant().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
