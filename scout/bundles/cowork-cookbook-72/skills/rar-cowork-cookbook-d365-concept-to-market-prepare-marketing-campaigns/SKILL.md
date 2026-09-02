---
name: "rar-cowork-cookbook-d365-concept-to-market-prepare-marketing-campaigns"
description: "A Dynamics 365 F&SCM expert scoped to the Prepare marketing campaigns area (a level-2 subdomain of Concept to market) - covers 7 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_concept_to_market_prepare_marketing_campaigns", "rar_sha256": "c32ab9325a7332daad73d110b7e4b242dfdc79e8a725b0bbdc5b91481d9b0177", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_concept_to_market_prepare_marketing_campaigns_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-concept-to-market-prepare-marketing-campaigns:651508bc5420b7ba12af4cafee6fd02c3b33c4b28677b6a3c3e7e27902febefc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_concept_to_market_prepare_marketing_campaigns`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_concept_to_market_prepare_marketing_campaigns_agent.py` is
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
