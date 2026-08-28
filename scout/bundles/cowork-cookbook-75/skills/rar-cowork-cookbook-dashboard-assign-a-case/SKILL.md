---
name: "rar-cowork-cookbook-dashboard-assign-a-case"
description: "Produces a self-contained interactive HTML dashboard for assign a case - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_assign_a_case", "rar_sha256": "02b9fd019e05fdbd800c1dea40c9449688009182dd8bda3c8a187202b0951ab8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_assign_a_case`. The original RAPP
agent is preserved byte-for-byte in `dashboard_assign_a_case_agent.py` and in the RCI capsule.

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

Assign a case Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for assign a case - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-assign-a-case
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_assign_a_case_agent.py` and embedded as the fenced Python below (sha256 02b9fd019e05fdbd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_assign_a_case_agent.py` first:

```bash
python3 dashboard_assign_a_case_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_assign_a_case_agent.py   # or on stdin
python3 dashboard_assign_a_case_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assign a case Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for assign a case - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-assign-a-case
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_assign_a_case',
    "version": '2.0.1',
    "display_name": 'Assign a case Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for assign a case - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-assign-a-case',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-assign-a-case',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0eac7efdfc4f2899',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/intake-cases/assign-a-case'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-assign-a-case', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardAssignACase(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAssignACase'
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
    print(DashboardAssignACase().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
