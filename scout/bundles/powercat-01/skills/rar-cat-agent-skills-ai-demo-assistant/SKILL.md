---
name: "rar-cat-agent-skills-ai-demo-assistant"
description: "Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo \u2014 fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_demo_assistant", "rar_sha256": "81d3ff99c254c9028c88fe4f843eb0a271892a3a97fac80c6b6a2340a0acb687", "source_kind": "rar-agent", "source_commit": "bc0f16918fee9b223608e0f3967fa6e32ed8000b", "version": "3.0.2", "author": "Doak Moore", "tags": ["demo", "copilot", "microsoft_365", "sales_enablement", "content", "productivity"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ai_demo_assistant_agent.py` and embedded as the fenced Python below (sha256 81d3ff99c254c902…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ai_demo_assistant_agent.py` first:

```bash
python3 ai_demo_assistant_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ai_demo_assistant_agent.py   # or on stdin
python3 ai_demo_assistant_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/ai_demo_assistant_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/ai_demo_assistant_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/ai_demo_assistant/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
