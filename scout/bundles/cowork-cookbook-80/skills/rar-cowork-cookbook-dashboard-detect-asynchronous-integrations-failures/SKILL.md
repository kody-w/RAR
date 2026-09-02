---
name: "rar-cowork-cookbook-dashboard-detect-asynchronous-integrations-failures"
description: "Produces a self-contained interactive HTML dashboard for detect asynchronous integrations failures - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_detect_asynchronous_integrations_failures", "rar_sha256": "7e702586be20e23a082d458ebe15e578714247a843201816c94830f56828b174", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_detect_asynchronous_integrations_failures_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-detect-asynchronous-integrations-failures:f60b27afb855c379924ad6941161035110c37eb34c502efaed941bca67e87c98", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_detect_asynchronous_integrations_failures`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_detect_asynchronous_integrations_failures_agent.py` is
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
