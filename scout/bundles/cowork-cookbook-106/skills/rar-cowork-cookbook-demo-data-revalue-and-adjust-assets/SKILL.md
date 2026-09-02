---
name: "rar-cowork-cookbook-demo-data-revalue-and-adjust-assets"
description: "Generates and creates realistic demo records for revalue and adjust assets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_revalue_and_adjust_assets", "rar_sha256": "dd2201aaffb5423469ce69ed52b2ffa00ec4e7ccc991eb1bce0ff21cbadfec6a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_revalue_and_adjust_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-revalue-and-adjust-assets:1e32be151fe0cc5ebbd8e46999ed36246d3001e9f8c6f981279e4166e70fdc65", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_revalue_and_adjust_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_revalue_and_adjust_assets_agent.py` is
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

Revalue and adjust assets Demo Data Generator — Generates and creates realistic demo records for revalue and adjust assets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-revalue-and-adjust-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_revalue_and_adjust_assets_agent.py` and embedded as the fenced Python below (sha256 dd2201aaffb54234…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_revalue_and_adjust_assets_agent.py` first:

```bash
python3 demo_data_revalue_and_adjust_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_revalue_and_adjust_assets_agent.py   # or on stdin
python3 demo_data_revalue_and_adjust_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Revalue and adjust assets Demo Data Generator — Generates and creates realistic demo records for revalue and adjust assets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-revalue-and-adjust-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_revalue_and_adjust_assets',
    "version": '2.0.0',
    "display_name": 'Revalue and adjust assets Demo Data Generator',
    "description": 'Generates and creates realistic demo records for revalue and adjust assets in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-revalue-and-adjust-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-revalue-and-adjust-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '245435da6cb52210',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/manage-active-assets/revalue-and-adjust-assets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-revalue-and-adjust-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataRevalueAndAdjustAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataRevalueAndAdjustAssets'
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
    print(DemoDataRevalueAndAdjustAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
