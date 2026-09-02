---
name: "rar-cowork-cookbook-bulk-update-develop-marketing-strategy"
description: "Applies a bulk field update across develop marketing strategy records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_develop_marketing_strategy", "rar_sha256": "61693a862c5ebae1e5055e9a218bde2a330aba90f0b2b30a524cd403361844b4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_develop_marketing_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-develop-marketing-strategy:83708e916d0838c3ecb867b07c97b868aa20e412016037da9e873a465e79eee8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_develop_marketing_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_develop_marketing_strategy_agent.py` is
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

Develop marketing strategy Bulk Field Update — Applies a bulk field update across develop marketing strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-marketing-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_develop_marketing_strategy_agent.py` and embedded as the fenced Python below (sha256 61693a862c5ebae1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_develop_marketing_strategy_agent.py` first:

```bash
python3 bulk_update_develop_marketing_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_develop_marketing_strategy_agent.py   # or on stdin
python3 bulk_update_develop_marketing_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop marketing strategy Bulk Field Update — Applies a bulk field update across develop marketing strategy records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-develop-marketing-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_develop_marketing_strategy',
    "version": '2.0.0',
    "display_name": 'Develop marketing strategy Bulk Field Update',
    "description": 'Applies a bulk field update across develop marketing strategy records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-develop-marketing-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-develop-marketing-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '01a4f08b1fadbd08',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/develop-marketing-strategy'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/bulk-update-develop-marketing-strategy', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateDevelopMarketingStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateDevelopMarketingStrategy'
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
    print(BulkUpdateDevelopMarketingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
