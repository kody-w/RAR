---
name: "rar-cowork-cookbook-demo-data-configure-and-manage-reporting-and-analytics"
description: "Generates and creates realistic demo records for configure and manage reporting and analytics in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_manage_reporting_and_analytics", "rar_sha256": "e0724f507bde903b718d4a787e4723ed37113a7c0e24eddbed55460418f7b3f1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_configure_and_manage_reporting_and_analytics_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-configure-and-manage-reporting-and-analytics:9e28e7aeb866987e006e6aee46a5f5c79ea8dcf9f8bb181bf78f6fac1a3ac5ca", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_configure_and_manage_reporting_and_analytics`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_configure_and_manage_reporting_and_analytics_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_configure_and_manage_reporting_and_analytics_agent.py` and embedded as the fenced Python below (sha256 e0724f507bde903b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_configure_and_manage_reporting_and_analytics_agent.py` first:

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
    "version": '2.0.0',
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
