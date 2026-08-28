---
name: "rar-cowork-cookbook-customer-adoption-materials"
description: "Build a role-relevant learning curriculum for a customer - structured, sourced, and deployment-ready."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_adoption_materials", "rar_sha256": "54fa4622b85df72e5a5aab85fd1fca7a124a986ebb243cfd7225b508fe1c6697", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/customer_adoption_materials`. The original RAPP
agent is preserved byte-for-byte in `customer_adoption_materials_agent.py` and in the RCI capsule.

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

Customer adoption materials — Build a role-relevant learning curriculum for a customer - structured, sourced, and deployment-ready.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/customer-adoption-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
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
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `customer_adoption_materials_agent.py` and embedded as the fenced Python below (sha256 54fa4622b85df72e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `customer_adoption_materials_agent.py` first:

```bash
python3 customer_adoption_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 customer_adoption_materials_agent.py   # or on stdin
python3 customer_adoption_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Customer adoption materials — Build a role-relevant learning curriculum for a customer - structured, sourced, and deployment-ready.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/customer-adoption-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/customer_adoption_materials',
    "version": '2.0.0',
    "display_name": 'Customer adoption materials',
    "description": 'Build a role-relevant learning curriculum for a customer - structured, sourced, and deployment-ready.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'read_only'],
    "category": 'general',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'customer-adoption-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/customer-adoption-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c4f7910726ce044d',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-post-sale-follow-up'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/customer-adoption-materials', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint'], 'plugin': []}, 'verification_status': 'draft'},
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Microsoft 365 Copilot Cowork'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability. The upstream entry supplies the WHAT; this procedure
# is RAR's own method for that shape of work, generated by
# @kody-w/skill_toaster_agent from the metadata we hold. No upstream text is
# reproduced here — see the module docstring.
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class CustomerAdoptionMaterials(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CustomerAdoptionMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

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
    print(CustomerAdoptionMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
