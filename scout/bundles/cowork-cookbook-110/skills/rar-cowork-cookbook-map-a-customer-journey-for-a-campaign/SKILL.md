---
name: "rar-cowork-cookbook-map-a-customer-journey-for-a-campaign"
description: "Turn a campaign brief into a clear, visual customer journey the team can rally around - instead of arguing over interpretations of the same Word doc."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/map_a_customer_journey_for_a_campaign", "rar_sha256": "2810aea892da61f3b34fe3fe5bbc8964b2df8bda2a2250c5112bf951d0da0242", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "integration", "miro"]}
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
