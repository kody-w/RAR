---
name: "rar-cowork-cookbook-scheduled-brief-establish-support-subscription"
description: "Schedulable morning-brief email summarizing establish support subscription for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_establish_support_subscription", "rar_sha256": "8c2a234e79c33f49c7e5b5fdcc8bc5af9550cab57c556205d49ae6fb00fb4ef0", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_establish_support_subscription_agent.py` and embedded as the fenced Python below (sha256 8c2a234e79c33f49…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_establish_support_subscription_agent.py` first:

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
    "version": '2.0.1',
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
