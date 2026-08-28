---
name: "rar-cowork-cookbook-dashboard-establish-support-procedures-and-policies"
description: "Produces a self-contained interactive HTML dashboard for establish support procedures and policies - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_establish_support_procedures_and_policies", "rar_sha256": "d479ea2b3b8bf75b116c4dd29ec7c40bb136e308327af4b551e73ab4087453ba", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_establish_support_procedures_and_policies_agent.py` and embedded as the fenced Python below (sha256 d479ea2b3b8bf75b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_establish_support_procedures_and_policies_agent.py` first:

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
    "version": '2.0.1',
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
