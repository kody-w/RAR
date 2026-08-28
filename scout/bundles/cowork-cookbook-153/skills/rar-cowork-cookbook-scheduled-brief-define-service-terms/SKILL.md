---
name: "rar-cowork-cookbook-scheduled-brief-define-service-terms"
description: "Schedulable morning-brief email summarizing define service terms for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_service_terms", "rar_sha256": "efb8883e5cec7a4b40c1bd1671e395b6d4487a5003a753760ad037b31bb164f7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_define_service_terms`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_define_service_terms_agent.py` and in the RCI capsule.

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

Define service terms Scheduled Email Brief — Schedulable morning-brief email summarizing define service terms for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-service-terms
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_service_terms_agent.py` and embedded as the fenced Python below (sha256 efb8883e5cec7a4b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_service_terms_agent.py` first:

```bash
python3 scheduled_brief_define_service_terms_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_define_service_terms_agent.py   # or on stdin
python3 scheduled_brief_define_service_terms_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service terms Scheduled Email Brief — Schedulable morning-brief email summarizing define service terms for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-define-service-terms
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_define_service_terms',
    "version": '2.0.1',
    "display_name": 'Define service terms Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing define service terms for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-define-service-terms',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-define-service-terms',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '560e9db5793a4dda',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/define-service-terms'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/scheduled-brief-define-service-terms', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefDefineServiceTerms(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDefineServiceTerms'
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
    print(ScheduledBriefDefineServiceTerms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
