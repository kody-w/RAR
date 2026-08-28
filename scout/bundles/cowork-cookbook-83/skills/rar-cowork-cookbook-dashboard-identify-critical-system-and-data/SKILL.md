---
name: "rar-cowork-cookbook-dashboard-identify-critical-system-and-data"
description: "Produces a self-contained interactive HTML dashboard for identify critical system and data - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_critical_system_and_data", "rar_sha256": "bd82924411f5ae28558b7f28c32eeffece4b4212a64569d8686cd13c75bcb929", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_critical_system_and_data_agent.py` and embedded as the fenced Python below (sha256 bd82924411f5ae28…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_critical_system_and_data_agent.py` first:

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
    "version": '2.0.1',
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
