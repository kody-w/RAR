---
name: "rar-cowork-cookbook-adaptive-card-procure-software-licenses-and-add-ons"
description: "Produces a reusable Adaptive Card JSON snapshot of procure software licenses and add-ons status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_procure_software_licenses_and_add_ons", "rar_sha256": "9b5a68f3396abdd058951e9d54ab44c3aa60e88cc550c615ee2baee0e6951f73", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_procure_software_licenses_and_add_ons`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_procure_software_licenses_and_add_ons_agent.py` and in the RCI capsule.

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

Procure software licenses and add-ons Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of procure software licenses and add-ons status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-procure-software-licenses-and-add-ons
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_procure_software_licenses_and_add_ons_agent.py` and embedded as the fenced Python below (sha256 9b5a68f3396abdd0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_procure_software_licenses_and_add_ons_agent.py` first:

```bash
python3 adaptive_card_procure_software_licenses_and_add_ons_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_procure_software_licenses_and_add_ons_agent.py   # or on stdin
python3 adaptive_card_procure_software_licenses_and_add_ons_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Procure software licenses and add-ons Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of procure software licenses and add-ons status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-procure-software-licenses-and-add-ons
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_procure_software_licenses_and_add_ons',
    "version": '2.0.0',
    "display_name": 'Procure software licenses and add-ons Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of procure software licenses and add-ons status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'adaptive-card-procure-software-licenses-and-add-ons',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-procure-software-licenses-and-add-ons',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b25085ee02cb2867',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/procure-software-licenses-and-add-ons'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-procure-software-licenses-and-add-ons', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class AdaptiveCardProcureSoftwareLicensesAndAddOns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardProcureSoftwareLicensesAndAddOns'
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
    print(AdaptiveCardProcureSoftwareLicensesAndAddOns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
