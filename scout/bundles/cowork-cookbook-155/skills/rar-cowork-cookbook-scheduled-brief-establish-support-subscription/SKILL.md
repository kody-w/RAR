---
name: "rar-cowork-cookbook-scheduled-brief-establish-support-subscription"
description: "Schedulable morning-brief email summarizing establish support subscription for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_establish_support_subscription", "rar_sha256": "825e18373b4821e6dce0b910f78fb59b0e2d84fa9b137a8221594f57da42a36a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_establish_support_subscription_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-establish-support-subscription:5ec33f940ae59f611feebf1361f704e88448eba9a078af5092fed1bd936e1a48", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_establish_support_subscription`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_establish_support_subscription_agent.py` is
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
