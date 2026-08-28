---
name: "rar-cowork-cookbook-scheduled-brief-manage-sales-channels"
description: "Schedulable morning-brief email summarizing manage sales channels for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_manage_sales_channels", "rar_sha256": "b7cdcc8181ad9314c49ff0052904644b2b70dc030cbd092f55684156f9208093", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_manage_sales_channels`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_manage_sales_channels_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_manage_sales_channels_agent.py` and embedded as the fenced Python below (sha256 b7cdcc8181ad9314…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_manage_sales_channels_agent.py` first:

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
    "version": '2.0.1',
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
