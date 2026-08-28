---
name: "rar-cowork-cookbook-adaptive-card-define-organizational-structure"
description: "Produces a reusable Adaptive Card JSON snapshot of define organizational structure status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_organizational_structure", "rar_sha256": "2859d56fb9024aa6fbbcd9dec79647bf61a625715976c1cded1756f1f2205d2f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_define_organizational_structure`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_define_organizational_structure_agent.py` and in the RCI capsule.

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

Define organizational structure Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define organizational structure status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-organizational-structure
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_organizational_structure_agent.py` and embedded as the fenced Python below (sha256 2859d56fb9024aa6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_organizational_structure_agent.py` first:

```bash
python3 adaptive_card_define_organizational_structure_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_define_organizational_structure_agent.py   # or on stdin
python3 adaptive_card_define_organizational_structure_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define organizational structure Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of define organizational structure status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-define-organizational-structure
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_define_organizational_structure',
    "version": '2.0.1',
    "display_name": 'Define organizational structure Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of define organizational structure status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
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
        "upstream_slug": 'adaptive-card-define-organizational-structure',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-define-organizational-structure',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8fc94787f9c893f4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/develop-people-strategy/define-organizational-structure'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/adaptive-card-define-organizational-structure', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.5, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['word:define', 'word:structure'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class AdaptiveCardDefineOrganizationalStructure(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDefineOrganizationalStructure'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(AdaptiveCardDefineOrganizationalStructure().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
