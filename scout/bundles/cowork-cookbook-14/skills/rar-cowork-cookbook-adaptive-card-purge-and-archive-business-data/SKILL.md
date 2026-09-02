---
name: "rar-cowork-cookbook-adaptive-card-purge-and-archive-business-data"
description: "Produces a reusable Adaptive Card JSON snapshot of purge and archive business data status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_purge_and_archive_business_data", "rar_sha256": "0590cbe558a0a2fb3bde22426c2ac340bb33d08c41d8757ba528ec0b64fc30bb", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_purge_and_archive_business_data_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-purge-and-archive-business-data:e7965d0c8da6837f590e04880c6c636fe98731b816d2a956ee80816d907c97af", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_purge_and_archive_business_data`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_purge_and_archive_business_data_agent.py` is
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
