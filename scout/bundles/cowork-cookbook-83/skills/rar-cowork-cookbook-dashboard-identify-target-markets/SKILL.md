---
name: "rar-cowork-cookbook-dashboard-identify-target-markets"
description: "Produces a self-contained interactive HTML dashboard for identify target markets - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_target_markets", "rar_sha256": "771a69e9c8a58b1717d9a9bb33e21f171df250cc81946cd401c6e9ba4071b808", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_target_markets_agent.py` and embedded as the fenced Python below (sha256 771a69e9c8a58b17…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_target_markets_agent.py` first:

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
    "version": '2.0.1',
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
