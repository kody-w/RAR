---
name: "rar-cowork-cookbook-demo-data-analyze-asset-leases"
description: "Generates and creates realistic demo records for analyze asset leases in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_analyze_asset_leases", "rar_sha256": "d7b8351476427c0f6f0a69afdf36bfc3a73401339545f863168874d60b7eef85", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_analyze_asset_leases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-analyze-asset-leases:a542d8d2b1a91ff7afddf00836c948279b30bcd6ca7bcea33af1a804b4745412", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_analyze_asset_leases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_analyze_asset_leases_agent.py` is
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

Analyze asset leases Demo Data Generator — Generates and creates realistic demo records for analyze asset leases in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-asset-leases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_analyze_asset_leases_agent.py` and embedded as the fenced Python below (sha256 d7b8351476427c0f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_analyze_asset_leases_agent.py` first:

```bash
python3 demo_data_analyze_asset_leases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_analyze_asset_leases_agent.py   # or on stdin
python3 demo_data_analyze_asset_leases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze asset leases Demo Data Generator — Generates and creates realistic demo records for analyze asset leases in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-analyze-asset-leases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_analyze_asset_leases',
    "version": '2.0.0',
    "display_name": 'Analyze asset leases Demo Data Generator',
    "description": 'Generates and creates realistic demo records for analyze asset leases in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-analyze-asset-leases',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-analyze-asset-leases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '545fbb21e2912353',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/analyze-asset-leases'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-analyze-asset-leases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataAnalyzeAssetLeases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAnalyzeAssetLeases'
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
    print(DemoDataAnalyzeAssetLeases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
