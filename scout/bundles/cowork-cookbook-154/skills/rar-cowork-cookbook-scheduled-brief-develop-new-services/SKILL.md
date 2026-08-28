---
name: "rar-cowork-cookbook-scheduled-brief-develop-new-services"
description: "Schedulable morning-brief email summarizing develop new services for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_develop_new_services", "rar_sha256": "d012ffd5009ee75a21179a8f0b0d1af0ae0f7d8231345c3f3c5a4be69a620ce1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_develop_new_services_agent.py` and embedded as the fenced Python below (sha256 d012ffd5009ee75a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_develop_new_services_agent.py` first:

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
    "version": '2.0.1',
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
