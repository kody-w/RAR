---
name: "rar-cowork-cookbook-d365-hire-to-retire-manage-performance-and-growth"
description: "A Dynamics 365 F&SCM expert scoped to the Manage performance and growth area (a level-2 subdomain of Hire to retire) - covers 10 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_hire_to_retire_manage_performance_and_growth", "rar_sha256": "ebc4904e5c284eb7b6e45fcf94fbb86cf78925e5fd55d0c912378e01c04b059c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_hire_to_retire_manage_performance_and_growth`. The original RAPP
agent is preserved byte-for-byte in `d365_hire_to_retire_manage_performance_and_growth_agent.py` and in the RCI capsule.

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

D365 Manage performance and growth Expert — A Dynamics 365 F&SCM expert scoped to the Manage performance and growth area (a level-2 subdomain of Hire to retire) - covers 10 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-hire-to-retire-manage-performance-and-growth
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_hire_to_retire_manage_performance_and_growth_agent.py` and embedded as the fenced Python below (sha256 ebc4904e5c284eb7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_hire_to_retire_manage_performance_and_growth_agent.py` first:

```bash
python3 d365_hire_to_retire_manage_performance_and_growth_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_hire_to_retire_manage_performance_and_growth_agent.py   # or on stdin
python3 d365_hire_to_retire_manage_performance_and_growth_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage performance and growth Expert — A Dynamics 365 F&SCM expert scoped to the Manage performance and growth area (a level-2 subdomain of Hire to retire) - covers 10 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-hire-to-retire-manage-performance-and-growth
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_hire_to_retire_manage_performance_and_growth',
    "version": '2.0.1',
    "display_name": 'D365 Manage performance and growth Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Manage performance and growth area (a level-2 subdomain of Hire to retire) - covers 10 L3 processes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'd365-hire-to-retire-manage-performance-and-growth',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-hire-to-retire-manage-performance-and-growth',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f642ef9126450244',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'hire-to-retire/d365-hire-to-retire-manage-performance-and-growth', 'uses_skills': {'custom': ['d365-hire-to-retire-manage-performance-and-growth'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class D365HireToRetireManagePerformanceAndGrowth(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365HireToRetireManagePerformanceAndGrowth'
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
    print(D365HireToRetireManagePerformanceAndGrowth().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
