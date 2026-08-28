---
name: "rar-cowork-cookbook-scheduled-brief-respond-to-non-compliance"
description: "Schedulable morning-brief email summarizing respond to non-compliance for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_respond_to_non_compliance", "rar_sha256": "a69634d4a7a4d11ccf9daa6e59e60e30cf56f73f7c3a27dae657297e4852b69e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_respond_to_non_compliance_agent.py` and embedded as the fenced Python below (sha256 a69634d4a7a4d11c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_respond_to_non_compliance_agent.py` first:

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
    "version": '2.0.1',
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
