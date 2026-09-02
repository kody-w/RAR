---
name: "rar-cowork-cookbook-demo-data-procure-software-licenses-and-add-ons"
description: "Generates and creates realistic demo records for procure software licenses and add-ons in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_procure_software_licenses_and_add_ons", "rar_sha256": "4463ed1f00bc8ad341b27bd4a9f0204243f2ee176eb374dca123787d5b944485", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_procure_software_licenses_and_add_ons_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-procure-software-licenses-and-add-ons:cc4750c0f84ae8a47480dbea605fede00f7695e6c62e52388db1d8a4156c6d4e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_procure_software_licenses_and_add_ons`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_procure_software_licenses_and_add_ons_agent.py` is
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
