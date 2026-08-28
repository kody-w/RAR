---
name: "rar-cowork-cookbook-dashboard-configure-segregation-of-duties"
description: "Produces a self-contained interactive HTML dashboard for configure segregation of duties - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_configure_segregation_of_duties", "rar_sha256": "6156f6787c113ff88beb4d08218b4435a920a4cc28dc5edb317ab350b3204f91", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_configure_segregation_of_duties_agent.py` and embedded as the fenced Python below (sha256 6156f6787c113ff8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_configure_segregation_of_duties_agent.py` first:

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
    "version": '2.0.0',
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
