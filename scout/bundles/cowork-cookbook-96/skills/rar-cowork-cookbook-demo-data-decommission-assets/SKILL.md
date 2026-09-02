---
name: "rar-cowork-cookbook-demo-data-decommission-assets"
description: "Generates and creates realistic demo records for decommission assets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_decommission_assets", "rar_sha256": "8776a17318a7ed46872d59d14eb7e06c689a4775fe89c7011556202d5e1a7b79", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_decommission_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-decommission-assets:0dba96e79d227ba69695e7fbb307fe077b83e9787882309732b22f6b8df74e1a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_decommission_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_decommission_assets_agent.py` is
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

Decommission assets Demo Data Generator — Generates and creates realistic demo records for decommission assets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-decommission-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_decommission_assets_agent.py` and embedded as the fenced Python below (sha256 8776a17318a7ed46…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_decommission_assets_agent.py` first:

```bash
python3 demo_data_decommission_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_decommission_assets_agent.py   # or on stdin
python3 demo_data_decommission_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Decommission assets Demo Data Generator — Generates and creates realistic demo records for decommission assets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-decommission-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_decommission_assets',
    "version": '2.0.0',
    "display_name": 'Decommission assets Demo Data Generator',
    "description": 'Generates and creates realistic demo records for decommission assets in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-decommission-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-decommission-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '7efcbac5fb26e303',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/dispose-of-assets/decommission-assets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-decommission-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDecommissionAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDecommissionAssets'
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
    print(DemoDataDecommissionAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
