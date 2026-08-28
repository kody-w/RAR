---
name: "rar-cowork-cookbook-dashboard-define-compensation-policies"
description: "Produces a self-contained interactive HTML dashboard for define compensation policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_compensation_policies", "rar_sha256": "15bb8f6e15a41f60ec1cbb77dc9eda415e34d6342705380b970ce5409c180dcd", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_compensation_policies_agent.py` and embedded as the fenced Python below (sha256 15bb8f6e15a41f60…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_compensation_policies_agent.py` first:

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
    "version": '2.0.0',
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
