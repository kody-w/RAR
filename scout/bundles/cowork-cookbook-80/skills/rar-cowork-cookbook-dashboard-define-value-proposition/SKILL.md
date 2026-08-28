---
name: "rar-cowork-cookbook-dashboard-define-value-proposition"
description: "Produces a self-contained interactive HTML dashboard for define value proposition - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_define_value_proposition", "rar_sha256": "07343858009ee9fe20afc23218e03a00f9fd7b25066cd8430f54e1e74136d031", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_define_value_proposition_agent.py` and embedded as the fenced Python below (sha256 07343858009ee9fe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_define_value_proposition_agent.py` first:

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
    "version": '2.0.0',
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
