---
name: "rar-cat-agent-skills-ai-demo-assistant"
description: "Turns a customer name, line of business, and personas into a ready-to-seed Microsoft 365 Copilot demo \u2014 fictional Word/PowerPoint/Excel example files plus a full delivery and provisioning plan, with optional one-click seeding to OneDrive and Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/ai_demo_assistant", "rar_sha256": "81d3ff99c254c9028c88fe4f843eb0a271892a3a97fac80c6b6a2340a0acb687", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Doak Moore", "tags": ["demo", "copilot", "microsoft_365", "sales_enablement", "content", "productivity"]}
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
