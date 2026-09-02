---
name: "rar-cowork-cookbook-scheduled-brief-develop-service-catalogs"
description: "Schedulable morning-brief email summarizing develop service catalogs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_service_catalogs", "rar_sha256": "12f60a986a0054eafc8b09058591b2ddbf30a265e664da92ecda0eaad82891af", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_develop_service_catalogs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-develop-service-catalogs:dc7c232ec30663ab1b4ee37ab8d57385c98d7b5c1f3837b087c3ce79e3a8ba4f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_develop_service_catalogs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_develop_service_catalogs_agent.py` is
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

Develop service catalogs Scheduled Email Brief — Schedulable morning-brief email summarizing develop service catalogs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-service-catalogs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_service_catalogs_agent.py` and embedded as the fenced Python below (sha256 12f60a986a0054ea…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_service_catalogs_agent.py` first:

```bash
python3 scheduled_brief_develop_service_catalogs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_service_catalogs_agent.py   # or on stdin
python3 scheduled_brief_develop_service_catalogs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop service catalogs Scheduled Email Brief — Schedulable morning-brief email summarizing develop service catalogs for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-service-catalogs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_service_catalogs',
    "version": '2.0.0',
    "display_name": 'Develop service catalogs Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing develop service catalogs for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-develop-service-catalogs',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-service-catalogs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5d02119abd75f25c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver/develop-service-strategy/develop-service-catalogs'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'service-to-deliver/scheduled-brief-develop-service-catalogs', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefDevelopServiceCatalogs(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopServiceCatalogs'
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
    print(ScheduledBriefDevelopServiceCatalogs().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
