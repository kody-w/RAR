---
name: "rar-cowork-cookbook-demo-data-perform-preventative-maintenance"
description: "Generates and creates realistic demo records for perform preventative maintenance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_perform_preventative_maintenance", "rar_sha256": "5d1c969b6f17401395309c9fa4c760cfcca99f6b375ee6b89b4c07a1d9ca5154", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_perform_preventative_maintenance_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-perform-preventative-maintenance:99adc1bcf164d065a907e7c6f5b3987b8582b7e16c749a6e50f3fc26be3fdfd0", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_perform_preventative_maintenance`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_perform_preventative_maintenance_agent.py` is
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

Perform preventative maintenance Demo Data Generator — Generates and creates realistic demo records for perform preventative maintenance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-perform-preventative-maintenance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_perform_preventative_maintenance_agent.py` and embedded as the fenced Python below (sha256 5d1c969b6f174013…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_perform_preventative_maintenance_agent.py` first:

```bash
python3 demo_data_perform_preventative_maintenance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_perform_preventative_maintenance_agent.py   # or on stdin
python3 demo_data_perform_preventative_maintenance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform preventative maintenance Demo Data Generator — Generates and creates realistic demo records for perform preventative maintenance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-perform-preventative-maintenance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_perform_preventative_maintenance',
    "version": '2.0.0',
    "display_name": 'Perform preventative maintenance Demo Data Generator',
    "description": 'Generates and creates realistic demo records for perform preventative maintenance in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-perform-preventative-maintenance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-perform-preventative-maintenance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2cfaaba227dbd5cb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/perform-asset-maintenance/perform-preventative-maintenance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/demo-data-perform-preventative-maintenance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataPerformPreventativeMaintenance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataPerformPreventativeMaintenance'
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
    print(DemoDataPerformPreventativeMaintenance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
