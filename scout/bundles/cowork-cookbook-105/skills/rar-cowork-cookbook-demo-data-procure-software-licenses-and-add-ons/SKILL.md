---
name: "rar-cowork-cookbook-demo-data-procure-software-licenses-and-add-ons"
description: "Generates and creates realistic demo records for procure software licenses and add-ons in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_procure_software_licenses_and_add_ons", "rar_sha256": "cf6753bb4be5969f73b778fa7b281a6849f26fe91d2a5bed6960c83ee41cbbce", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_procure_software_licenses_and_add_ons`. The original RAPP
agent is preserved byte-for-byte in `demo_data_procure_software_licenses_and_add_ons_agent.py` and in the RCI capsule.

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

Procure software licenses and add-ons Demo Data Generator — Generates and creates realistic demo records for procure software licenses and add-ons in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-procure-software-licenses-and-add-ons
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_procure_software_licenses_and_add_ons_agent.py` and embedded as the fenced Python below (sha256 cf6753bb4be5969f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_procure_software_licenses_and_add_ons_agent.py` first:

```bash
python3 demo_data_procure_software_licenses_and_add_ons_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_procure_software_licenses_and_add_ons_agent.py   # or on stdin
python3 demo_data_procure_software_licenses_and_add_ons_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Procure software licenses and add-ons Demo Data Generator — Generates and creates realistic demo records for procure software licenses and add-ons in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-procure-software-licenses-and-add-ons
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_procure_software_licenses_and_add_ons',
    "version": '2.0.1',
    "display_name": 'Procure software licenses and add-ons Demo Data Generator',
    "description": 'Generates and creates realistic demo records for procure software licenses and add-ons in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-procure-software-licenses-and-add-ons',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-procure-software-licenses-and-add-ons',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd8835e170c19de4e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/procure-software-licenses-and-add-ons'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-procure-software-licenses-and-add-ons', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataProcureSoftwareLicensesAndAddOns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataProcureSoftwareLicensesAndAddOns'
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
    print(DemoDataProcureSoftwareLicensesAndAddOns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
