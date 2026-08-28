---
name: "rar-cowork-cookbook-adaptive-card-retire-software-licenses"
description: "Produces a reusable Adaptive Card JSON snapshot of retire software licenses status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_retire_software_licenses", "rar_sha256": "a8c1332fb3825afa62f243178e5bbc36e1361a0152d852d8c5dfbedd0f11719b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_retire_software_licenses_agent.py` and embedded as the fenced Python below (sha256 a8c1332fb3825afa…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_retire_software_licenses_agent.py` first:

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
    "version": '2.0.0',
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
