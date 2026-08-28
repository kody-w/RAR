---
name: "rar-cowork-cookbook-adaptive-card-retire-software-licenses"
description: "Produces a reusable Adaptive Card JSON snapshot of retire software licenses status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_retire_software_licenses", "rar_sha256": "a9ee66e7003ceb7928106fab5f656814098acc8c9daf9242e444f54123fe7e11", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_retire_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_retire_software_licenses_agent.py` and in the RCI capsule.

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

Retire software licenses Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of retire software licenses status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-retire-software-licenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_retire_software_licenses_agent.py` and embedded as the fenced Python below (sha256 a9ee66e7003ceb79…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_retire_software_licenses_agent.py` first:

```bash
python3 adaptive_card_retire_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_retire_software_licenses_agent.py   # or on stdin
python3 adaptive_card_retire_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire software licenses Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of retire software licenses status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-retire-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_retire_software_licenses',
    "version": '2.0.1',
    "display_name": 'Retire software licenses Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of retire software licenses status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-retire-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-retire-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '72c97e6e532c689e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/retire-software-licenses'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-retire-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardRetireSoftwareLicenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardRetireSoftwareLicenses'
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
    print(AdaptiveCardRetireSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
