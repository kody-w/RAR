---
name: "rar-cowork-cookbook-scheduled-brief-develop-new-services"
description: "Schedulable morning-brief email summarizing develop new services for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_new_services", "rar_sha256": "5fb45ad2fb32a90128021cd56f28b661c1501422e4b8cce72727f7e77ebb9d02", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_develop_new_services`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_develop_new_services_agent.py` and in the RCI capsule.

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
