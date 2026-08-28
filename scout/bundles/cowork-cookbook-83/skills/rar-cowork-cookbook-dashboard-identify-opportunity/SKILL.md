---
name: "rar-cowork-cookbook-dashboard-identify-opportunity"
description: "Produces a self-contained interactive HTML dashboard for identify opportunity - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_identify_opportunity", "rar_sha256": "b8cdc28f21820250ace63555cedbb510a5872ee2bebde291a6b3d4da80c36b3d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_identify_opportunity`. The original RAPP
agent is preserved byte-for-byte in `dashboard_identify_opportunity_agent.py` and in the RCI capsule.

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

Identify opportunity Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify opportunity - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-opportunity
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_identify_opportunity_agent.py` and embedded as the fenced Python below (sha256 b8cdc28f21820250…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_identify_opportunity_agent.py` first:

```bash
python3 dashboard_identify_opportunity_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_identify_opportunity_agent.py   # or on stdin
python3 dashboard_identify_opportunity_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify opportunity Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for identify opportunity - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-identify-opportunity
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_identify_opportunity',
    "version": '2.0.1',
    "display_name": 'Identify opportunity Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for identify opportunity - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-identify-opportunity',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-identify-opportunity',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '31e761787878f3dc',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/pursue-opportunities/identify-opportunity'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/dashboard-identify-opportunity', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardIdentifyOpportunity(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardIdentifyOpportunity'
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
    print(DashboardIdentifyOpportunity().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
