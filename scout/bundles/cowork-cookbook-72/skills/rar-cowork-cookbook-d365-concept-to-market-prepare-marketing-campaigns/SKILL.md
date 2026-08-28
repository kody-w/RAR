---
name: "rar-cowork-cookbook-d365-concept-to-market-prepare-marketing-campaigns"
description: "A Dynamics 365 F&SCM expert scoped to the Prepare marketing campaigns area (a level-2 subdomain of Concept to market) - covers 7 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_concept_to_market_prepare_marketing_campaigns", "rar_sha256": "a885e38bffb1fb82ed9efd8ffb9eb70aa22095ca13c9ce295658acc236858ef1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_concept_to_market_prepare_marketing_campaigns`. The original RAPP
agent is preserved byte-for-byte in `d365_concept_to_market_prepare_marketing_campaigns_agent.py` and in the RCI capsule.

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

D365 Prepare marketing campaigns Expert — A Dynamics 365 F&SCM expert scoped to the Prepare marketing campaigns area (a level-2 subdomain of Concept to market) - covers 7 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-concept-to-market-prepare-marketing-campaigns
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_concept_to_market_prepare_marketing_campaigns_agent.py` and embedded as the fenced Python below (sha256 a885e38bffb1fb82…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_concept_to_market_prepare_marketing_campaigns_agent.py` first:

```bash
python3 d365_concept_to_market_prepare_marketing_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_concept_to_market_prepare_marketing_campaigns_agent.py   # or on stdin
python3 d365_concept_to_market_prepare_marketing_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Prepare marketing campaigns Expert — A Dynamics 365 F&SCM expert scoped to the Prepare marketing campaigns area (a level-2 subdomain of Concept to market) - covers 7 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-concept-to-market-prepare-marketing-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_concept_to_market_prepare_marketing_campaigns',
    "version": '2.0.1',
    "display_name": 'D365 Prepare marketing campaigns Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Prepare marketing campaigns area (a level-2 subdomain of Concept to market) - covers 7 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'd365-concept-to-market-prepare-marketing-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-concept-to-market-prepare-marketing-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c25165bfc1c8869c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'concept-to-market/d365-concept-to-market-prepare-marketing-campaigns', 'uses_skills': {'custom': ['d365-concept-to-market-prepare-marketing-campaigns'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class D365ConceptToMarketPrepareMarketingCampaigns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ConceptToMarketPrepareMarketingCampaigns'
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
    print(D365ConceptToMarketPrepareMarketingCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
