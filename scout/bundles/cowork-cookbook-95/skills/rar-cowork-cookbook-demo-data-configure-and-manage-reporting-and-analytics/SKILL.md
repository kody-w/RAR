---
name: "rar-cowork-cookbook-demo-data-configure-and-manage-reporting-and-analytics"
description: "Generates and creates realistic demo records for configure and manage reporting and analytics in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_manage_reporting_and_analytics", "rar_sha256": "f9d8017e84e075d08cbbf806739c00eba86951c70534fde20d566f85701214f8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_configure_and_manage_reporting_and_analytics`. The original RAPP
agent is preserved byte-for-byte in `demo_data_configure_and_manage_reporting_and_analytics_agent.py` and in the RCI capsule.

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

Configure and manage reporting and analytics Demo Data Generator — Generates and creates realistic demo records for configure and manage reporting and analytics in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-manage-reporting-and-analytics
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_configure_and_manage_reporting_and_analytics_agent.py` and embedded as the fenced Python below (sha256 f9d8017e84e075d0…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_configure_and_manage_reporting_and_analytics_agent.py` first:

```bash
python3 demo_data_configure_and_manage_reporting_and_analytics_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_configure_and_manage_reporting_and_analytics_agent.py   # or on stdin
python3 demo_data_configure_and_manage_reporting_and_analytics_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage reporting and analytics Demo Data Generator — Generates and creates realistic demo records for configure and manage reporting and analytics in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-manage-reporting-and-analytics
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_configure_and_manage_reporting_and_analytics',
    "version": '2.0.1',
    "display_name": 'Configure and manage reporting and analytics Demo Data Generator',
    "description": 'Generates and creates realistic demo records for configure and manage reporting and analytics in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-configure-and-manage-reporting-and-analytics',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-configure-and-manage-reporting-and-analytics',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '8be9fae2c476db92',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-reporting-and-analytics'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-configure-and-manage-reporting-and-analytics', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataConfigureAndManageReportingAndAnalytics(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConfigureAndManageReportingAndAnalytics'
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
    print(DemoDataConfigureAndManageReportingAndAnalytics().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
