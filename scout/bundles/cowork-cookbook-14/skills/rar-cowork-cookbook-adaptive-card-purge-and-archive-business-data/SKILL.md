---
name: "rar-cowork-cookbook-adaptive-card-purge-and-archive-business-data"
description: "Produces a reusable Adaptive Card JSON snapshot of purge and archive business data status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_purge_and_archive_business_data", "rar_sha256": "004632443252509fee87772efce9b45263df98705ebf8a036ab3beb1171ac27d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_purge_and_archive_business_data`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_purge_and_archive_business_data_agent.py` and in the RCI capsule.

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

Purge and archive business data Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of purge and archive business data status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-purge-and-archive-business-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_purge_and_archive_business_data_agent.py` and embedded as the fenced Python below (sha256 004632443252509f…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_purge_and_archive_business_data_agent.py` first:

```bash
python3 adaptive_card_purge_and_archive_business_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_purge_and_archive_business_data_agent.py   # or on stdin
python3 adaptive_card_purge_and_archive_business_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Purge and archive business data Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of purge and archive business data status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-purge-and-archive-business-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_purge_and_archive_business_data',
    "version": '2.0.1',
    "display_name": 'Purge and archive business data Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of purge and archive business data status for embedding in dashboards, emails, or Teams.',
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
        "upstream_slug": 'adaptive-card-purge-and-archive-business-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-purge-and-archive-business-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '23930e1820d879f7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/purge-and-archive-business-data'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-purge-and-archive-business-data', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardPurgeAndArchiveBusinessData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardPurgeAndArchiveBusinessData'
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
    print(AdaptiveCardPurgeAndArchiveBusinessData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
