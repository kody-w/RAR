---
name: "rar-cowork-cookbook-demo-data-procure-software-licenses-and-add-ons"
description: "Generates and creates realistic demo records for procure software licenses and add-ons in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_procure_software_licenses_and_add_ons", "rar_sha256": "4463ed1f00bc8ad341b27bd4a9f0204243f2ee176eb374dca123787d5b944485", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_procure_software_licenses_and_add_ons_agent.py` and embedded as the fenced Python below (sha256 4463ed1f00bc8ad3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_procure_software_licenses_and_add_ons_agent.py` first:

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
    "version": '2.0.0',
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
