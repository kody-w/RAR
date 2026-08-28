---
name: "rar-cowork-cookbook-dashboard-establish-support-procedures-and-policies"
description: "Produces a self-contained interactive HTML dashboard for establish support procedures and policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_establish_support_procedures_and_policies", "rar_sha256": "c9353a2bd73b351452ad841945bf33640bbd3508feca99b357d30a8e7702a99d", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_establish_support_procedures_and_policies`. The original RAPP
agent is preserved byte-for-byte in `dashboard_establish_support_procedures_and_policies_agent.py` and in the RCI capsule.

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

Establish support procedures and policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for establish support procedures and policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-establish-support-procedures-and-policies
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_establish_support_procedures_and_policies_agent.py` and embedded as the fenced Python below (sha256 c9353a2bd73b3514…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_establish_support_procedures_and_policies_agent.py` first:

```bash
python3 dashboard_establish_support_procedures_and_policies_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_establish_support_procedures_and_policies_agent.py   # or on stdin
python3 dashboard_establish_support_procedures_and_policies_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Establish support procedures and policies Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for establish support procedures and policies - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-establish-support-procedures-and-policies
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_establish_support_procedures_and_policies',
    "version": '2.0.0',
    "display_name": 'Establish support procedures and policies Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for establish support procedures and policies - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-establish-support-procedures-and-policies',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-establish-support-procedures-and-policies',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1874609b20a9d64b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/support-systems/establish-support-procedures-and-policies'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/dashboard-establish-support-procedures-and-policies', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardEstablishSupportProceduresAndPolicies(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardEstablishSupportProceduresAndPolicies'
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
    print(DashboardEstablishSupportProceduresAndPolicies().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
