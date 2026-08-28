---
name: "rar-cowork-cookbook-dashboard-retire-software-licenses"
description: "Produces a self-contained interactive HTML dashboard for retire software licenses - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_retire_software_licenses", "rar_sha256": "40747695a6645e36dd7b210407872d73f7679186109f5b5f9e0a852f86ac505c", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_retire_software_licenses`. The original RAPP
agent is preserved byte-for-byte in `dashboard_retire_software_licenses_agent.py` and in the RCI capsule.

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

Retire software licenses Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for retire software licenses - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-retire-software-licenses
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_retire_software_licenses_agent.py` and embedded as the fenced Python below (sha256 40747695a6645e36…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_retire_software_licenses_agent.py` first:

```bash
python3 dashboard_retire_software_licenses_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_retire_software_licenses_agent.py   # or on stdin
python3 dashboard_retire_software_licenses_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire software licenses Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for retire software licenses - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-retire-software-licenses
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_retire_software_licenses',
    "version": '2.0.0',
    "display_name": 'Retire software licenses Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for retire software licenses - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-retire-software-licenses',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-retire-software-licenses',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '93cd5747bf498122',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-licensing-and-entitlements/retire-software-licenses'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-retire-software-licenses', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardRetireSoftwareLicenses(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardRetireSoftwareLicenses'
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
    print(DashboardRetireSoftwareLicenses().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
