---
name: "rar-cowork-cookbook-scheduled-brief-respond-to-non-compliance"
description: "Schedulable morning-brief email summarizing respond to non-compliance for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_respond_to_non_compliance", "rar_sha256": "12bd4be5cc9fba4d2b4a9868fd210927e23accc607d0373d0c7ee4cfbae1d689", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_respond_to_non_compliance`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_respond_to_non_compliance_agent.py` and in the RCI capsule.

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

Respond to non-compliance Scheduled Email Brief — Schedulable morning-brief email summarizing respond to non-compliance for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-respond-to-non-compliance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_respond_to_non_compliance_agent.py` and embedded as the fenced Python below (sha256 12bd4be5cc9fba4d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_respond_to_non_compliance_agent.py` first:

```bash
python3 scheduled_brief_respond_to_non_compliance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_respond_to_non_compliance_agent.py   # or on stdin
python3 scheduled_brief_respond_to_non_compliance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Respond to non-compliance Scheduled Email Brief — Schedulable morning-brief email summarizing respond to non-compliance for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-respond-to-non-compliance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_respond_to_non_compliance',
    "version": '2.0.0',
    "display_name": 'Respond to non-compliance Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing respond to non-compliance for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-respond-to-non-compliance',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-respond-to-non-compliance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f4e47da48fdf961c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-compliance/respond-to-non-compliance'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-respond-to-non-compliance', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefRespondToNonCompliance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefRespondToNonCompliance'
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
    print(ScheduledBriefRespondToNonCompliance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
