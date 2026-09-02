---
name: "rar-cowork-cookbook-demo-data-source-assets"
description: "Generates and creates realistic demo records for source assets in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_source_assets", "rar_sha256": "b9955707403519ae967b9d3c4e84327425028dd9ae32fd1a78f0e1260caed721", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_source_assets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-source-assets:1f174e95a86a8ace296fdf57871ad6c40126234cd32adfa69036c77ca78fa2f5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_source_assets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_source_assets_agent.py` is
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

Source assets Demo Data Generator — Generates and creates realistic demo records for source assets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-source-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_source_assets_agent.py` and embedded as the fenced Python below (sha256 b9955707403519ae…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_source_assets_agent.py` first:

```bash
python3 demo_data_source_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_source_assets_agent.py   # or on stdin
python3 demo_data_source_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Source assets Demo Data Generator — Generates and creates realistic demo records for source assets in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-source-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_source_assets',
    "version": '2.0.0',
    "display_name": 'Source assets Demo Data Generator',
    "description": 'Generates and creates realistic demo records for source assets in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-source-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-source-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6024437174700283',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/source-assets'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-source-assets', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataSourceAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataSourceAssets'
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
    print(DemoDataSourceAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
