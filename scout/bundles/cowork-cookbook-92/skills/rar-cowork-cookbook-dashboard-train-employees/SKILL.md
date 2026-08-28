---
name: "rar-cowork-cookbook-dashboard-train-employees"
description: "Produces a self-contained interactive HTML dashboard for train employees - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_train_employees", "rar_sha256": "5f676c615229a6ba6d617401659e55ba7da11346b6ff615ecbfe4eebf054fcfc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_train_employees`. The original RAPP
agent is preserved byte-for-byte in `dashboard_train_employees_agent.py` and in the RCI capsule.

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

Train employees Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for train employees - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-train-employees
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_train_employees_agent.py` and embedded as the fenced Python below (sha256 5f676c615229a6ba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_train_employees_agent.py` first:

```bash
python3 dashboard_train_employees_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_train_employees_agent.py   # or on stdin
python3 dashboard_train_employees_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Train employees Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for train employees - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-train-employees
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_train_employees',
    "version": '2.0.1',
    "display_name": 'Train employees Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for train employees - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-train-employees',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-train-employees',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a18802e620861b87',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/train-employees'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-train-employees', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardTrainEmployees(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardTrainEmployees'
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
    print(DashboardTrainEmployees().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
