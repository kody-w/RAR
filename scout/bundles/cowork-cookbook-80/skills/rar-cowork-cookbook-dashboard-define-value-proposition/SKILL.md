---
name: "rar-cowork-cookbook-dashboard-define-value-proposition"
description: "Produces a self-contained interactive HTML dashboard for define value proposition - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_value_proposition", "rar_sha256": "d9ea5de747af06104265904738710fb59dc80792fe5683cc557e8f41bb327404", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_define_value_proposition`. The original RAPP
agent is preserved byte-for-byte in `dashboard_define_value_proposition_agent.py` and in the RCI capsule.

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

Define value proposition Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define value proposition - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-value-proposition
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_value_proposition_agent.py` and embedded as the fenced Python below (sha256 d9ea5de747af0610…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_value_proposition_agent.py` first:

```bash
python3 dashboard_define_value_proposition_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_define_value_proposition_agent.py   # or on stdin
python3 dashboard_define_value_proposition_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define value proposition Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for define value proposition - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-define-value-proposition
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_define_value_proposition',
    "version": '2.0.1',
    "display_name": 'Define value proposition Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for define value proposition - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-define-value-proposition',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-define-value-proposition',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '005dc69ef673e75a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/define-value-proposition'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-define-value-proposition', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DashboardDefineValueProposition(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardDefineValueProposition'
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
    print(DashboardDefineValueProposition().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
