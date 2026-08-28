---
name: "rar-cowork-cookbook-demo-data-configure-and-administer-workflows"
description: "Generates and creates realistic demo records for configure and administer workflows in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_administer_workflows", "rar_sha256": "570c5c1b71ec5e51d2939a27515b5239823737c899fa6222fc9a714bf5685e9a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_configure_and_administer_workflows`. The original RAPP
agent is preserved byte-for-byte in `demo_data_configure_and_administer_workflows_agent.py` and in the RCI capsule.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the linked
agent SHA-256 before importing it. If preflight reports a host dependency that
Scout cannot satisfy, use the `brainstem_chat` MCP tool to run the canonical
agent in the user's Brainstem. Never paraphrase the factory or agent into a new
implementation. The generic direct-file commands in the generated Toaster
section are recovery guidance; Scout should prefer the verified runner.

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
