---
name: "rar-cowork-cookbook-dashboard-define-depreciation-and-amortization-policies"
description: "Produces a self-contained interactive HTML dashboard for define depreciation and amortization policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_depreciation_and_amortization_policies", "rar_sha256": "82f97321edaabfe5c308e5fb1a85447e6bf44ed207dd9650eb5b11537e70874b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_define_depreciation_and_amortization_policies_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-define-depreciation-and-amortization-policies:608cfa7dfd6ad630e6ffb59af51dffa906958abeb8db84ba5fa461eccc4302d7", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_define_depreciation_and_amortization_policies`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_define_depreciation_and_amortization_policies_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_depreciation_and_amortization_policies_agent.py` and embedded as the fenced Python below (sha256 82f97321edaabfe5…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_depreciation_and_amortization_policies_agent.py` first:

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
    "version": '2.0.0',
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
