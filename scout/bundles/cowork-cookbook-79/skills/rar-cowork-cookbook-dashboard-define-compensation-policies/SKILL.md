---
name: "rar-cowork-cookbook-dashboard-define-compensation-policies"
description: "Produces a self-contained interactive HTML dashboard for define compensation policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_compensation_policies", "rar_sha256": "5e86efe2c1fb61cbfa41e9fdbfe9420a7bb89a47bcff021f21c2d261a4da63fa", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_compensation_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_compensation_policies_agent.py` and in the RCI capsule.

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

Define compensation policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define compensation policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-compensation-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_compensation_policies_agent.py` and embedded as the fenced Python below (sha256 5e86efe2c1fb61cb…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_compensation_policies_agent.py` first:

```bash
python3 dashboard_define_compensation_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_compensation_policies_agent.py   # or on stdin
python3 dashboard_define_compensation_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define compensation policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define compensation policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-compensation-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_compensation_policies',
    "version": '2.0.1',
    "display_name": 'Define compensation policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define compensation policies - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-define-compensation-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-compensation-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'f97eddf00a8af006',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-compensation-and-benefits/define-compensation-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/dashboard-define-compensation-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardDefineCompensationPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineCompensationPolicies'
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
    print(DashboardDefineCompensationPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
