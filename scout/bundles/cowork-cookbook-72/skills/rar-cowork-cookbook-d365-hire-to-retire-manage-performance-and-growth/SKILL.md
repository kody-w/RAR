---
name: "rar-cowork-cookbook-d365-hire-to-retire-manage-performance-and-growth"
description: "A Dynamics 365 F&SCM expert scoped to the Manage performance and growth area (a level-2 subdomain of Hire to retire) - covers 10 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_hire_to_retire_manage_performance_and_growth", "rar_sha256": "ccd68817ce7de4d98db50adcfd8ebdc5df8520c2af38f7e46bd08f455bc1961e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_hire_to_retire_manage_performance_and_growth_agent.py` and embedded as the fenced Python below (sha256 ccd68817ce7de4d9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_hire_to_retire_manage_performance_and_growth_agent.py` first:

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
    "version": '2.0.0',
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
