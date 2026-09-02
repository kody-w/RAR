---
name: "rar-cowork-cookbook-customer-adoption-materials"
description: "Build a role-relevant learning curriculum for a customer - structured, sourced, and deployment-ready."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/customer_adoption_materials", "rar_sha256": "54fa4622b85df72e5a5aab85fd1fca7a124a986ebb243cfd7225b508fe1c6697", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "customer_adoption_materials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/customer-adoption-materials:97417e69e9c40ce1dbea3d16a7902b5d0d9fc5b3ec96d186df0836f4fe263fc9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "read_only"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/customer_adoption_materials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `customer_adoption_materials_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
