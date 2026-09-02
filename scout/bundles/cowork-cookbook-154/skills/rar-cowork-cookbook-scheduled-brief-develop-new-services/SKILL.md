---
name: "rar-cowork-cookbook-scheduled-brief-develop-new-services"
description: "Schedulable morning-brief email summarizing develop new services for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_new_services", "rar_sha256": "5fb45ad2fb32a90128021cd56f28b661c1501422e4b8cce72727f7e77ebb9d02", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_develop_new_services_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-develop-new-services:b09d59df056911239ee35187c82c853c03336efaa170df0bf0f86d443e55e127", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_develop_new_services`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_develop_new_services_agent.py` is
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

Develop new services Scheduled Email Brief — Schedulable morning-brief email summarizing develop new services for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-new-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_new_services_agent.py` and embedded as the fenced Python below (sha256 5fb45ad2fb32a901…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_new_services_agent.py` first:

```bash
python3 scheduled_brief_develop_new_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_develop_new_services_agent.py   # or on stdin
python3 scheduled_brief_develop_new_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop new services Scheduled Email Brief — Schedulable morning-brief email summarizing develop new services for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-develop-new-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_develop_new_services',
    "version": '2.0.0',
    "display_name": 'Develop new services Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing develop new services for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-develop-new-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-develop-new-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '70723df565fc2fdb',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/develop-new-services'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/scheduled-brief-develop-new-services', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefDevelopNewServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefDevelopNewServices'
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
    print(ScheduledBriefDevelopNewServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
