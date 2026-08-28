---
name: "rar-cowork-cookbook-adaptive-card-define-organizational-structure"
description: "Produces a reusable Adaptive Card JSON snapshot of define organizational structure status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_define_organizational_structure", "rar_sha256": "94005c733c2b325ec32c47282fe11342a43e4ebc48466185a9d31c10021077bd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_define_organizational_structure_agent.py` and embedded as the fenced Python below (sha256 94005c733c2b325e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_define_organizational_structure_agent.py` first:

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
    "version": '2.0.0',
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
