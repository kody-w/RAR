---
name: "rar-cowork-cookbook-scheduled-brief-maintain-quality-certifications"
description: "Schedulable morning-brief email summarizing maintain quality certifications for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_maintain_quality_certifications", "rar_sha256": "de519da18eca68cfa18427347caa14bc42b37fd1e6b4c5dbfba1b1aba2713b94", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "inventory_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_maintain_quality_certifications`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_maintain_quality_certifications_agent.py` and in the RCI capsule.

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

Maintain quality certifications Scheduled Email Brief — Schedulable morning-brief email summarizing maintain quality certifications for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-maintain-quality-certifications
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_maintain_quality_certifications_agent.py` and embedded as the fenced Python below (sha256 de519da18eca68cf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_maintain_quality_certifications_agent.py` first:

```bash
python3 scheduled_brief_maintain_quality_certifications_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_maintain_quality_certifications_agent.py   # or on stdin
python3 scheduled_brief_maintain_quality_certifications_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain quality certifications Scheduled Email Brief — Schedulable morning-brief email summarizing maintain quality certifications for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-maintain-quality-certifications
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_maintain_quality_certifications',
    "version": '2.0.1',
    "display_name": 'Maintain quality certifications Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing maintain quality certifications for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'inventory_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-maintain-quality-certifications',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-maintain-quality-certifications',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2c2ec1d0cea81b1a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['inventory-to-deliver'], 'process_tags': ['inventory-to-deliver/manage-inventory-quality/maintain-quality-certifications'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'inventory-to-deliver/scheduled-brief-maintain-quality-certifications', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefMaintainQualityCertifications(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMaintainQualityCertifications'
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
    print(ScheduledBriefMaintainQualityCertifications().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
