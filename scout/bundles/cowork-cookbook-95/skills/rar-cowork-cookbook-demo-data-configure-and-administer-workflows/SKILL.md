---
name: "rar-cowork-cookbook-demo-data-configure-and-administer-workflows"
description: "Generates and creates realistic demo records for configure and administer workflows in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_administer_workflows", "rar_sha256": "ce5507580e12dfbae2be2067ffbad431fafc9130494e0a6f53fb7d0aeef47cca", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_configure_and_administer_workflows_agent.py` and embedded as the fenced Python below (sha256 ce5507580e12dfba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_configure_and_administer_workflows_agent.py` first:

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
    "version": '2.0.1',
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
