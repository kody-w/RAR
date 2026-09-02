---
name: "rar-cowork-cookbook-map-a-customer-journey-for-a-campaign"
description: "Turn a campaign brief into a clear, visual customer journey the team can rally around - instead of arguing over interpretations of the same Word doc."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/map_a_customer_journey_for_a_campaign", "rar_sha256": "2810aea892da61f3b34fe3fe5bbc8964b2df8bda2a2250c5112bf951d0da0242", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "map_a_customer_journey_for_a_campaign_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/map-a-customer-journey-for-a-campaign:da45f9b26ea0901d51ae005e772fc957cf0d9d7f6d6638eb59b09bb8582c62fe", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "miro"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/map_a_customer_journey_for_a_campaign`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `map_a_customer_journey_for_a_campaign_agent.py` is
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

Map a customer journey for a campaign — Turn a campaign brief into a clear, visual customer journey the team can rally around - instead of arguing over interpretations of the same Word doc.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/map-a-customer-journey-for-a-campaign
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `map_a_customer_journey_for_a_campaign_agent.py` and embedded as the fenced Python below (sha256 2810aea892da61f3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `map_a_customer_journey_for_a_campaign_agent.py` first:

```bash
python3 map_a_customer_journey_for_a_campaign_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 map_a_customer_journey_for_a_campaign_agent.py   # or on stdin
python3 map_a_customer_journey_for_a_campaign_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Map a customer journey for a campaign — Turn a campaign brief into a clear, visual customer journey the team can rally around - instead of arguing over interpretations of the same Word doc.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/map-a-customer-journey-for-a-campaign
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/map_a_customer_journey_for_a_campaign',
    "version": '2.0.0',
    "display_name": 'Map a customer journey for a campaign',
    "description": 'Turn a campaign brief into a clear, visual customer journey the team can rally around - instead of arguing over interpretations of the same Word doc.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'intermediate', 'integration', 'miro'],
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
        "upstream_slug": 'map-a-customer-journey-for-a-campaign',
        "upstream_url": 'https://coworkcookbook.com/recipes/map-a-customer-journey-for-a-campaign',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c5922a0657bcc4ae',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'miro', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/identify-campaign-audiences'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/map-a-customer-journey-for-a-campaign', 'uses_skills': {'custom': [], 'ootb': [], 'plugin': []}, 'verification_status': 'draft'},
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


class MapACustomerJourneyForACampaign(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'MapACustomerJourneyForACampaign'
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
    print(MapACustomerJourneyForACampaign().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
