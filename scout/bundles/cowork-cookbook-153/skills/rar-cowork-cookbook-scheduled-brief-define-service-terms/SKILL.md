---
name: "rar-cowork-cookbook-scheduled-brief-define-service-terms"
description: "Schedulable morning-brief email summarizing define service terms for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_define_service_terms", "rar_sha256": "a0409bcc96518293e36a8dec10f286fbcab75ba1b2fa70abe47cf4149488b7a9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_define_service_terms_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-define-service-terms:ecc6f5123de04245f8debb5344d380b43372b9acfc4511533a426cd10da2af69", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_define_service_terms`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_define_service_terms_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_define_service_terms_agent.py` and embedded as the fenced Python below (sha256 a0409bcc96518293…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_define_service_terms_agent.py` first:

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
    "version": '2.0.0',
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
