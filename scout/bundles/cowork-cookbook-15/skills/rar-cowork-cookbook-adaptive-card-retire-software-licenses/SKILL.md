---
name: "rar-cowork-cookbook-adaptive-card-retire-software-licenses"
description: "Produces a reusable Adaptive Card JSON snapshot of retire software licenses status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_retire_software_licenses", "rar_sha256": "a8c1332fb3825afa62f243178e5bbc36e1361a0152d852d8c5dfbedd0f11719b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_retire_software_licenses_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-retire-software-licenses:35f03ceb7644c91fdad283f050d308b13ddcc08f90c85be8adfe92954449b3aa", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_retire_software_licenses`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_retire_software_licenses_agent.py` is
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
