---
name: "rar-cowork-cookbook-dashboard-detect-asynchronous-integrations-failures"
description: "Produces a self-contained interactive HTML dashboard for detect asynchronous integrations failures - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_detect_asynchronous_integrations_failures", "rar_sha256": "8a98bc0bfeee7a651f7b0a23035cab33267fe2f94837065e75a54f87d3296629", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_detect_asynchronous_integrations_failures_agent.py` and embedded as the fenced Python below (sha256 8a98bc0bfeee7a65…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_detect_asynchronous_integrations_failures_agent.py` first:

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
    "version": '2.0.1',
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
