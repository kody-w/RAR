---
name: "rar-cowork-cookbook-dashboard-detect-asynchronous-integrations-failures"
description: "Produces a self-contained interactive HTML dashboard for detect asynchronous integrations failures - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_detect_asynchronous_integrations_failures", "rar_sha256": "7e702586be20e23a082d458ebe15e578714247a843201816c94830f56828b174", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_detect_asynchronous_integrations_failures`. The original RAPP
agent is preserved byte-for-byte in `dashboard_detect_asynchronous_integrations_failures_agent.py` and in the RCI capsule.

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

Detect asynchronous integrations failures Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for detect asynchronous integrations failures - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-detect-asynchronous-integrations-failures
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_detect_asynchronous_integrations_failures_agent.py` and embedded as the fenced Python below (sha256 7e702586be20e23a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_detect_asynchronous_integrations_failures_agent.py` first:

```bash
python3 dashboard_detect_asynchronous_integrations_failures_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_detect_asynchronous_integrations_failures_agent.py   # or on stdin
python3 dashboard_detect_asynchronous_integrations_failures_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Detect asynchronous integrations failures Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for detect asynchronous integrations failures - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-detect-asynchronous-integrations-failures
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_detect_asynchronous_integrations_failures',
    "version": '2.0.0',
    "display_name": 'Detect asynchronous integrations failures Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for detect asynchronous integrations failures - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-detect-asynchronous-integrations-failures',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-detect-asynchronous-integrations-failures',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ced60a9e71be9ef3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/monitor-systems-environments-and-capacity/detect-asynchronous-integrations-failures'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-detect-asynchronous-integrations-failures', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardDetectAsynchronousIntegrationsFailures(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDetectAsynchronousIntegrationsFailures'
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
    print(DashboardDetectAsynchronousIntegrationsFailures().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
