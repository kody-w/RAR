---
name: "rar-cowork-cookbook-scheduled-brief-develop-service-catalogs"
description: "Schedulable morning-brief email summarizing develop service catalogs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_service_catalogs", "rar_sha256": "12f60a986a0054eafc8b09058591b2ddbf30a265e664da92ecda0eaad82891af", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_service_catalogs`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_service_catalogs_agent.py` and in the RCI capsule.

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
