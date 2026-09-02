---
name: "rar-cowork-cookbook-adaptive-card-procure-software-licenses-and-add-ons"
description: "Produces a reusable Adaptive Card JSON snapshot of procure software licenses and add-ons status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_procure_software_licenses_and_add_ons", "rar_sha256": "9b5a68f3396abdd058951e9d54ab44c3aa60e88cc550c615ee2baee0e6951f73", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_procure_software_licenses_and_add_ons_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-procure-software-licenses-and-add-ons:e3c44a432acac4a3fae3a2bb10906f1cd09e70babf4facf122aec84e9e084141", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_procure_software_licenses_and_add_ons`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_procure_software_licenses_and_add_ons_agent.py` is
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
