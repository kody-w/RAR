---
name: "rar-cowork-cookbook-bulk-update-analyze-service-profitability"
description: "Applies a bulk field update across analyze service profitability records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_analyze_service_profitability", "rar_sha256": "ec6f9b012356b7e6de1f9a2f65e3b562926219de397f9b74e308bc613f3f0b06", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_analyze_service_profitability_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-analyze-service-profitability:d27adf880025dc9023a5de2d4c6570e9b145b6a5c9e10f1c0ded3d31db2d242f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_analyze_service_profitability`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_analyze_service_profitability_agent.py` is
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

Analyze service profitability Bulk Field Update — Applies a bulk field update across analyze service profitability records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-service-profitability
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_analyze_service_profitability_agent.py` and embedded as the fenced Python below (sha256 ec6f9b012356b7e6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_analyze_service_profitability_agent.py` first:

```bash
python3 bulk_update_analyze_service_profitability_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_analyze_service_profitability_agent.py   # or on stdin
python3 bulk_update_analyze_service_profitability_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze service profitability Bulk Field Update — Applies a bulk field update across analyze service profitability records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-analyze-service-profitability
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_analyze_service_profitability',
    "version": '2.0.0',
    "display_name": 'Analyze service profitability Bulk Field Update',
    "description": 'Applies a bulk field update across analyze service profitability records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-analyze-service-profitability',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-analyze-service-profitability',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ee3dd1b7e3ce0ba',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/analyze-service-profitability'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/bulk-update-analyze-service-profitability', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.857, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateAnalyzeServiceProfitability(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAnalyzeServiceProfitability'
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
    print(BulkUpdateAnalyzeServiceProfitability().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
