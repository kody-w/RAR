---
name: "rar-cowork-cookbook-dashboard-configure-segregation-of-duties"
description: "Produces a self-contained interactive HTML dashboard for configure segregation of duties - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_segregation_of_duties", "rar_sha256": "a8ed0701dd565bb1005efeef55133663adfffc969a117b56c86cfe1076640886", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_configure_segregation_of_duties`. The original RAPP
agent is preserved byte-for-byte in `dashboard_configure_segregation_of_duties_agent.py` and in the RCI capsule.

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

Configure segregation of duties Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for configure segregation of duties - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-segregation-of-duties
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_segregation_of_duties_agent.py` and embedded as the fenced Python below (sha256 a8ed0701dd565bb1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_segregation_of_duties_agent.py` first:

```bash
python3 dashboard_configure_segregation_of_duties_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_configure_segregation_of_duties_agent.py   # or on stdin
python3 dashboard_configure_segregation_of_duties_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure segregation of duties Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for configure segregation of duties - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-configure-segregation-of-duties
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_configure_segregation_of_duties',
    "version": '2.0.1',
    "display_name": 'Configure segregation of duties Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for configure segregation of duties - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-configure-segregation-of-duties',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-configure-segregation-of-duties',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1bec2c32159369d1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-system-access-and-security/configure-segregation-of-duties'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-configure-segregation-of-duties', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardConfigureSegregationOfDuties(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConfigureSegregationOfDuties'
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
    print(DashboardConfigureSegregationOfDuties().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
