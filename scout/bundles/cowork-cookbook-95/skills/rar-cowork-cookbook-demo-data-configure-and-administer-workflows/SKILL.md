---
name: "rar-cowork-cookbook-demo-data-configure-and-administer-workflows"
description: "Generates and creates realistic demo records for configure and administer workflows in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_administer_workflows", "rar_sha256": "570c5c1b71ec5e51d2939a27515b5239823737c899fa6222fc9a714bf5685e9a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_configure_and_administer_workflows_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-configure-and-administer-workflows:d3284224757ec04031bab388abea00f985a741cb34a34d37aec61e9e998664c9", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_configure_and_administer_workflows`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_configure_and_administer_workflows_agent.py` is
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

Configure and administer workflows Demo Data Generator — Generates and creates realistic demo records for configure and administer workflows in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-administer-workflows
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_configure_and_administer_workflows_agent.py` and embedded as the fenced Python below (sha256 570c5c1b71ec5e51…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_configure_and_administer_workflows_agent.py` first:

```bash
python3 demo_data_configure_and_administer_workflows_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_configure_and_administer_workflows_agent.py   # or on stdin
python3 demo_data_configure_and_administer_workflows_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and administer workflows Demo Data Generator — Generates and creates realistic demo records for configure and administer workflows in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-administer-workflows
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_configure_and_administer_workflows',
    "version": '2.0.0',
    "display_name": 'Configure and administer workflows Demo Data Generator',
    "description": 'Generates and creates realistic demo records for configure and administer workflows in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-configure-and-administer-workflows',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-configure-and-administer-workflows',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b2942a4d3e78e957',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-administer-workflows'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-configure-and-administer-workflows', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataConfigureAndAdministerWorkflows(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConfigureAndAdministerWorkflows'
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
    print(DemoDataConfigureAndAdministerWorkflows().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
