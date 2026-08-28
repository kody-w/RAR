---
name: "rar-cowork-cookbook-map-a-customer-journey-for-a-campaign"
description: "Turn a campaign brief into a clear, visual customer journey the team can rally around - instead of arguing over interpretations of the same Word doc."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/map_a_customer_journey_for_a_campaign", "rar_sha256": "5a9c0404398e2d71ab253f6abf6eeace82fa05d2a2f0ba85c6b58e635752a7e5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "miro"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/map_a_customer_journey_for_a_campaign`. The original RAPP
agent is preserved byte-for-byte in `map_a_customer_journey_for_a_campaign_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `map_a_customer_journey_for_a_campaign_agent.py` and embedded as the fenced Python below (sha256 5a9c0404398e2d71…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `map_a_customer_journey_for_a_campaign_agent.py` first:

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
    "version": '2.0.1',
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
