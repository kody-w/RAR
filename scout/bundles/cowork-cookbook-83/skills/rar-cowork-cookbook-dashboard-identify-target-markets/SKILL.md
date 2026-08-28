---
name: "rar-cowork-cookbook-dashboard-identify-target-markets"
description: "Produces a self-contained interactive HTML dashboard for identify target markets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_target_markets", "rar_sha256": "d331aede0c5e83de1de4c98d74151e38b34bda5520451e110e0f4782a2c7d13a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_identify_target_markets`. The original RAPP
agent is preserved byte-for-byte in `dashboard_identify_target_markets_agent.py` and in the RCI capsule.

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

Identify target markets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify target markets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-target-markets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_target_markets_agent.py` and embedded as the fenced Python below (sha256 d331aede0c5e83de…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_target_markets_agent.py` first:

```bash
python3 dashboard_identify_target_markets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_identify_target_markets_agent.py   # or on stdin
python3 dashboard_identify_target_markets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify target markets Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify target markets - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-target-markets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_identify_target_markets',
    "version": '2.0.0',
    "display_name": 'Identify target markets Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for identify target markets - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-identify-target-markets',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-identify-target-markets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e22838d4d5320f15',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/identify-target-markets'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-identify-target-markets', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardIdentifyTargetMarkets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIdentifyTargetMarkets'
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
    print(DashboardIdentifyTargetMarkets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
