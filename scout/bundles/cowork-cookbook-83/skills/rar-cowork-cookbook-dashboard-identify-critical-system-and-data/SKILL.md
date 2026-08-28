---
name: "rar-cowork-cookbook-dashboard-identify-critical-system-and-data"
description: "Produces a self-contained interactive HTML dashboard for identify critical system and data - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_critical_system_and_data", "rar_sha256": "285c39a6607ba50de777bea33d1f55b616975e3bac293c373eaef467ef94357d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_identify_critical_system_and_data`. The original RAPP
agent is preserved byte-for-byte in `dashboard_identify_critical_system_and_data_agent.py` and in the RCI capsule.

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

Identify critical system and data Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify critical system and data - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-critical-system-and-data
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_critical_system_and_data_agent.py` and embedded as the fenced Python below (sha256 285c39a6607ba50d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_critical_system_and_data_agent.py` first:

```bash
python3 dashboard_identify_critical_system_and_data_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_identify_critical_system_and_data_agent.py   # or on stdin
python3 dashboard_identify_critical_system_and_data_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify critical system and data Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify critical system and data - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-critical-system-and-data
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_identify_critical_system_and_data',
    "version": '2.0.0',
    "display_name": 'Identify critical system and data Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for identify critical system and data - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-identify-critical-system-and-data',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-identify-critical-system-and-data',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '37341c8e6ac97ae6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/define-business-continuity-plan/identify-critical-system-and-data'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-identify-critical-system-and-data', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardIdentifyCriticalSystemAndData(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIdentifyCriticalSystemAndData'
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
    print(DashboardIdentifyCriticalSystemAndData().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
