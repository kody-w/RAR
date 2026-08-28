---
name: "rar-cowork-cookbook-d365-concept-to-market-prepare-marketing-campaigns"
description: "A Dynamics 365 F&SCM expert scoped to the Prepare marketing campaigns area (a level-2 subdomain of Concept to market) - covers 7 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_concept_to_market_prepare_marketing_campaigns", "rar_sha256": "c32ab9325a7332daad73d110b7e4b242dfdc79e8a725b0bbdc5b91481d9b0177", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_concept_to_market_prepare_marketing_campaigns_agent.py` and embedded as the fenced Python below (sha256 c32ab9325a7332da…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_concept_to_market_prepare_marketing_campaigns_agent.py` first:

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
    "version": '2.0.0',
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
