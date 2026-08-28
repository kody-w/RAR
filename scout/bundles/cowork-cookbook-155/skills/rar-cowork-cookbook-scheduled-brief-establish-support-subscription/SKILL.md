---
name: "rar-cowork-cookbook-scheduled-brief-establish-support-subscription"
description: "Schedulable morning-brief email summarizing establish support subscription for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_establish_support_subscription", "rar_sha256": "825e18373b4821e6dce0b910f78fb59b0e2d84fa9b137a8221594f57da42a36a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_establish_support_subscription`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_establish_support_subscription_agent.py` and in the RCI capsule.

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

Establish support subscription Scheduled Email Brief — Schedulable morning-brief email summarizing establish support subscription for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-establish-support-subscription
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_establish_support_subscription_agent.py` and embedded as the fenced Python below (sha256 825e18373b4821e6…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_establish_support_subscription_agent.py` first:

```bash
python3 scheduled_brief_establish_support_subscription_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_establish_support_subscription_agent.py   # or on stdin
python3 scheduled_brief_establish_support_subscription_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish support subscription Scheduled Email Brief — Schedulable morning-brief email summarizing establish support subscription for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-establish-support-subscription
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_establish_support_subscription',
    "version": '2.0.0',
    "display_name": 'Establish support subscription Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing establish support subscription for the responsible owner; designed to run daily or weekly.',
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
        "upstream_slug": 'scheduled-brief-establish-support-subscription',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-establish-support-subscription',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ff709b778cef6226',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/establish-support-subscription'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/scheduled-brief-establish-support-subscription', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefEstablishSupportSubscription(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefEstablishSupportSubscription'
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
    print(ScheduledBriefEstablishSupportSubscription().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
