---
name: "rar-cowork-cookbook-demo-data-analyze-asset-utilization"
description: "Generates and creates realistic demo records for analyze asset utilization in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_asset_utilization", "rar_sha256": "551d95be8bc0d93906c68b0e3e28d3ee93e4463a4927da2f8af5c690ed51a223", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_analyze_asset_utilization_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-analyze-asset-utilization:263355552f488a365ed31c75193a01bd9b6f40c28e3a85041b63ec6680fe0cc7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_analyze_asset_utilization`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_analyze_asset_utilization_agent.py` is
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

Analyze asset utilization Demo Data Generator — Generates and creates realistic demo records for analyze asset utilization in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-asset-utilization
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_asset_utilization_agent.py` and embedded as the fenced Python below (sha256 551d95be8bc0d939…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_asset_utilization_agent.py` first:

```bash
python3 demo_data_analyze_asset_utilization_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_asset_utilization_agent.py   # or on stdin
python3 demo_data_analyze_asset_utilization_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze asset utilization Demo Data Generator — Generates and creates realistic demo records for analyze asset utilization in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-asset-utilization
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_asset_utilization',
    "version": '2.0.0',
    "display_name": 'Analyze asset utilization Demo Data Generator',
    "description": 'Generates and creates realistic demo records for analyze asset utilization in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-analyze-asset-utilization',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-asset-utilization',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4e7e20b22ea04aa6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-asset-utilization'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-analyze-asset-utilization', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataAnalyzeAssetUtilization(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeAssetUtilization'
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
    print(DemoDataAnalyzeAssetUtilization().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
