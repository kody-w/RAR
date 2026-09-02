---
name: "rar-cowork-cookbook-adaptive-card-design-bills-of-materials"
description: "Produces a reusable Adaptive Card JSON snapshot of design bills of materials status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_design_bills_of_materials", "rar_sha256": "7d55f3b6af8ec1adf7cf34159d8c1f47164dadccf4cf33863ad87b04bf5a3040", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_design_bills_of_materials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-design-bills-of-materials:476c2499a07ccf242f6cd9650ea997e3934ebf9ef5ce2cddb02b1fd519dc840a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_design_bills_of_materials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_design_bills_of_materials_agent.py` is
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

Design bills of materials Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of design bills of materials status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-design-bills-of-materials
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
      "description": "The process to automate.",
      "type": "string"
    },
    "trigger": {
      "description": "Optional. What starts it \u2014 schedule, event or manual.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_design_bills_of_materials_agent.py` and embedded as the fenced Python below (sha256 7d55f3b6af8ec1ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_design_bills_of_materials_agent.py` first:

```bash
python3 adaptive_card_design_bills_of_materials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_design_bills_of_materials_agent.py   # or on stdin
python3 adaptive_card_design_bills_of_materials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Design bills of materials Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of design bills of materials status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-design-bills-of-materials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_design_bills_of_materials',
    "version": '2.0.0',
    "display_name": 'Design bills of materials Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of design bills of materials status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-design-bills-of-materials',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-design-bills-of-materials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '498ac3992bbe93e8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/design-bills-of-materials'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/adaptive-card-design-bills-of-materials', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardDesignBillsOfMaterials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardDesignBillsOfMaterials'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'The process to automate.', 'type': 'string'}, 'trigger': {'description': 'Optional. What starts it — schedule, event or manual.', 'type': 'string'}},
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
    print(AdaptiveCardDesignBillsOfMaterials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
