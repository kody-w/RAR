---
name: "rar-cowork-cookbook-dashboard-define-depreciation-and-amortization-policies"
description: "Produces a self-contained interactive HTML dashboard for define depreciation and amortization policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_depreciation_and_amortization_policies", "rar_sha256": "3da7d3854626f10a57fe189dd690a4253514210405e1ff0268a10526eadc697b", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_depreciation_and_amortization_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_depreciation_and_amortization_policies_agent.py` and in the RCI capsule.

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

Define depreciation and amortization policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define depreciation and amortization policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-depreciation-and-amortization-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_depreciation_and_amortization_policies_agent.py` and embedded as the fenced Python below (sha256 3da7d3854626f10a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_depreciation_and_amortization_policies_agent.py` first:

```bash
python3 dashboard_define_depreciation_and_amortization_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_depreciation_and_amortization_policies_agent.py   # or on stdin
python3 dashboard_define_depreciation_and_amortization_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define depreciation and amortization policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define depreciation and amortization policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-depreciation-and-amortization-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_depreciation_and_amortization_policies',
    "version": '2.0.1',
    "display_name": 'Define depreciation and amortization policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define depreciation and amortization policies - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-depreciation-and-amortization-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-depreciation-and-amortization-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd56238a3a051b6af',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/define-asset-strategy/define-depreciation-and-amortization-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/dashboard-define-depreciation-and-amortization-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class DashboardDefineDepreciationAndAmortizationPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineDepreciationAndAmortizationPolicies'
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
    print(DashboardDefineDepreciationAndAmortizationPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
