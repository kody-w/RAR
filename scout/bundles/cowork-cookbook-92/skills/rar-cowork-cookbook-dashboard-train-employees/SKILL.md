---
name: "rar-cowork-cookbook-dashboard-train-employees"
description: "Produces a self-contained interactive HTML dashboard for train employees - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_train_employees", "rar_sha256": "d5da57c49c4e0a775574b606314363eed58888460b37702219520cf753dba550", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_train_employees_agent.py` and embedded as the fenced Python below (sha256 d5da57c49c4e0a77…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_train_employees_agent.py` first:

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
    "version": '2.0.0',
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
