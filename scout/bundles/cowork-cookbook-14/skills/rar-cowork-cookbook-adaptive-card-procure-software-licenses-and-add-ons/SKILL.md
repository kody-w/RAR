---
name: "rar-cowork-cookbook-adaptive-card-procure-software-licenses-and-add-ons"
description: "Produces a reusable Adaptive Card JSON snapshot of procure software licenses and add-ons status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_procure_software_licenses_and_add_ons", "rar_sha256": "7c1e05398f91fd0121d39ad8480245990cfb8c3c6f70936c1e88e00c68c95169", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_procure_software_licenses_and_add_ons_agent.py` and embedded as the fenced Python below (sha256 7c1e05398f91fd01…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_procure_software_licenses_and_add_ons_agent.py` first:

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
    "version": '2.0.1',
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
