---
name: "rar-cowork-cookbook-adaptive-card-purge-and-archive-business-data"
description: "Produces a reusable Adaptive Card JSON snapshot of purge and archive business data status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_purge_and_archive_business_data", "rar_sha256": "0590cbe558a0a2fb3bde22426c2ac340bb33d08c41d8757ba528ec0b64fc30bb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_purge_and_archive_business_data_agent.py` and embedded as the fenced Python below (sha256 0590cbe558a0a2fb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_purge_and_archive_business_data_agent.py` first:

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
    "version": '2.0.0',
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
