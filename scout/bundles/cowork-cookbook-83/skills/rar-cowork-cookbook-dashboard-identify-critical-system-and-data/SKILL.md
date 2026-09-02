---
name: "rar-cowork-cookbook-dashboard-identify-critical-system-and-data"
description: "Produces a self-contained interactive HTML dashboard for identify critical system and data - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_critical_system_and_data", "rar_sha256": "285c39a6607ba50de777bea33d1f55b616975e3bac293c373eaef467ef94357d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_identify_critical_system_and_data_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-identify-critical-system-and-data:48cc10d20ce5bc8f806dafbdc1c0892205627efaa13e65dcf917f6dd4a85b730", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_identify_critical_system_and_data`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_identify_critical_system_and_data_agent.py` is
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
