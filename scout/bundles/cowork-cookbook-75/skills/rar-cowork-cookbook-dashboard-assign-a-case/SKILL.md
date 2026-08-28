---
name: "rar-cowork-cookbook-dashboard-assign-a-case"
description: "Produces a self-contained interactive HTML dashboard for assign a case - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_assign_a_case", "rar_sha256": "18cc806b3e7f12d9baf20810f4f47895aa89db9ea435aaa81bcb25819efc0779", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_assign_a_case_agent.py` and embedded as the fenced Python below (sha256 18cc806b3e7f12d9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_assign_a_case_agent.py` first:

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
    "version": '2.0.0',
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
