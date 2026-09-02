---
name: "rar-cowork-cookbook-scheduled-brief-manage-sales-channels"
description: "Schedulable morning-brief email summarizing manage sales channels for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_sales_channels", "rar_sha256": "f7862a1d6b76f23a909e6b010ea8c25a8afdebce6e2a68a96cb16c3aa1b54377", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_manage_sales_channels_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-manage-sales-channels:3395d9803ef89ddb2e32d33985e7b0987379eeb5be25b5052795f08d08e89b2f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_manage_sales_channels`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_manage_sales_channels_agent.py` is
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

Manage sales channels Scheduled Email Brief — Schedulable morning-brief email summarizing manage sales channels for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-sales-channels
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_sales_channels_agent.py` and embedded as the fenced Python below (sha256 f7862a1d6b76f23a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_sales_channels_agent.py` first:

```bash
python3 scheduled_brief_manage_sales_channels_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_manage_sales_channels_agent.py   # or on stdin
python3 scheduled_brief_manage_sales_channels_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage sales channels Scheduled Email Brief — Schedulable morning-brief email summarizing manage sales channels for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-manage-sales-channels
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_manage_sales_channels',
    "version": '2.0.0',
    "display_name": 'Manage sales channels Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing manage sales channels for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-manage-sales-channels',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-manage-sales-channels',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '456c784f560dc125',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/develop-sales-policies/manage-sales-channels'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/scheduled-brief-manage-sales-channels', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class ScheduledBriefManageSalesChannels(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefManageSalesChannels'
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
    print(ScheduledBriefManageSalesChannels().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
