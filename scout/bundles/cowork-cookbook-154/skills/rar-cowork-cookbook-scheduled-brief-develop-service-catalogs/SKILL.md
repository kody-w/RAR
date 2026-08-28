---
name: "rar-cowork-cookbook-scheduled-brief-develop-service-catalogs"
description: "Schedulable morning-brief email summarizing develop service catalogs for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_service_catalogs", "rar_sha256": "33eb738c71befa0534486dd0027c60d8999debd78aca029edc80586b32cbb6d5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_service_catalogs_agent.py` and embedded as the fenced Python below (sha256 33eb738c71befa05…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_service_catalogs_agent.py` first:

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
    "version": '2.0.1',
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
