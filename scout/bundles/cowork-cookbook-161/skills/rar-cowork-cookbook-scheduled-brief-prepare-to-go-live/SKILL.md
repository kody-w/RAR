---
name: "rar-cowork-cookbook-scheduled-brief-prepare-to-go-live"
description: "Schedulable morning-brief email summarizing prepare to go live for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_prepare_to_go_live", "rar_sha256": "2b674e2e2f2fa7ad73060cafd046ed0bd20c9bb03a107f4d68852f4f1f1419a7", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_prepare_to_go_live`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_prepare_to_go_live_agent.py` and in the RCI capsule.

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

Prepare to go live Scheduled Email Brief — Schedulable morning-brief email summarizing prepare to go live for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-prepare-to-go-live
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_prepare_to_go_live_agent.py` and embedded as the fenced Python below (sha256 2b674e2e2f2fa7ad…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_prepare_to_go_live_agent.py` first:

```bash
python3 scheduled_brief_prepare_to_go_live_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_prepare_to_go_live_agent.py   # or on stdin
python3 scheduled_brief_prepare_to_go_live_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Prepare to go live Scheduled Email Brief — Schedulable morning-brief email summarizing prepare to go live for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-prepare-to-go-live
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_prepare_to_go_live',
    "version": '2.0.1',
    "display_name": 'Prepare to go live Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing prepare to go live for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-prepare-to-go-live',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-prepare-to-go-live',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'dfbcccce34b780bf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/prepare-to-go-live'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-prepare-to-go-live', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefPrepareToGoLive(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefPrepareToGoLive'
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
    print(ScheduledBriefPrepareToGoLive().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
