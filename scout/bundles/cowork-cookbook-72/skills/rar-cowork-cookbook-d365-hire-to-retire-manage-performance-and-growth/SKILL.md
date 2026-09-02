---
name: "rar-cowork-cookbook-d365-hire-to-retire-manage-performance-and-growth"
description: "A Dynamics 365 F&SCM expert scoped to the Manage performance and growth area (a level-2 subdomain of Hire to retire) - covers 10 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_hire_to_retire_manage_performance_and_growth", "rar_sha256": "ccd68817ce7de4d98db50adcfd8ebdc5df8520c2af38f7e46bd08f455bc1961e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_hire_to_retire_manage_performance_and_growth_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-hire-to-retire-manage-performance-and-growth:418dc15a57a28c724054340e10f5628a99d9566237049e2cb04f77f70b9e1618", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_hire_to_retire_manage_performance_and_growth`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_hire_to_retire_manage_performance_and_growth_agent.py` is
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
