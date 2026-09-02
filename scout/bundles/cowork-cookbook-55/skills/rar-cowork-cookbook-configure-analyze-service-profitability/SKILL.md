---
name: "rar-cowork-cookbook-configure-analyze-service-profitability"
description: "Applies a bulk configuration change to analyze service profitability from an input Excel file, with validation and rollback support."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/configure_analyze_service_profitability", "rar_sha256": "941f62698fa88e7d393f87ac8a217b4a55b58f6681c1cbdb46bc06a7684dcc19", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "configure_analyze_service_profitability_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/configure-analyze-service-profitability:db401a486c5b3c4d111adb09dd8a5d655513563e8b3cbf5bf7f35b6fbd78c0d6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "configure", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/configure_analyze_service_profitability`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `configure_analyze_service_profitability_agent.py` is
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

Analyze service profitability Configuration Bulk Setup — Applies a bulk configuration change to analyze service profitability from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-service-profitability
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `configure_analyze_service_profitability_agent.py` and embedded as the fenced Python below (sha256 941f62698fa88e7d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `configure_analyze_service_profitability_agent.py` first:

```bash
python3 configure_analyze_service_profitability_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 configure_analyze_service_profitability_agent.py   # or on stdin
python3 configure_analyze_service_profitability_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze service profitability Configuration Bulk Setup — Applies a bulk configuration change to analyze service profitability from an input Excel file, with validation and rollback support.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/configure-analyze-service-profitability
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/configure_analyze_service_profitability',
    "version": '2.0.0',
    "display_name": 'Analyze service profitability Configuration Bulk Setup',
    "description": 'Applies a bulk configuration change to analyze service profitability from an input Excel file, with validation and rollback support.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'configure', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'configure-analyze-service-profitability',
        "upstream_url": 'https://coworkcookbook.com/recipes/configure-analyze-service-profitability',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a87566e086587ccd',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/analyze-service-performance/analyze-service-profitability'], 'recipe_category': 'configure', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/configure-analyze-service-profitability', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}, {'action': 'form_open_menu_item', 'plugin': 'dynamics-365-erp'}, {'action': 'form_set_control_values', 'plugin': 'dynamics-365-erp'}, {'action': 'form_save_form', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ConfigureAnalyzeServiceProfitability(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ConfigureAnalyzeServiceProfitability'
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
    print(ConfigureAnalyzeServiceProfitability().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
