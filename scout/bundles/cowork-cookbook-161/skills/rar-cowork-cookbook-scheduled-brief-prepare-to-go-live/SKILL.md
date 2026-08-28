---
name: "rar-cowork-cookbook-scheduled-brief-prepare-to-go-live"
description: "Schedulable morning-brief email summarizing prepare to go live for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_prepare_to_go_live", "rar_sha256": "43555b388702ee2000daf0c00bc277e4a60164ad697ac3c8217e4fb569b08f10", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_prepare_to_go_live_agent.py` and embedded as the fenced Python below (sha256 43555b388702ee20…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_prepare_to_go_live_agent.py` first:

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
    "version": '2.0.0',
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
