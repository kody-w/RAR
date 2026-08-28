---
name: "rar-cowork-cookbook-dashboard-analyze-marketing-trends"
description: "Produces a self-contained interactive HTML dashboard for analyze marketing trends - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_marketing_trends", "rar_sha256": "035b988cbae05b51231c4ebe43ec65ded4b1c739b13ca4431d85816d1df31746", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_analyze_marketing_trends`. The original RAPP
agent is preserved byte-for-byte in `dashboard_analyze_marketing_trends_agent.py` and in the RCI capsule.

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

Analyze marketing trends Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for analyze marketing trends - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-marketing-trends
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_analyze_marketing_trends_agent.py` and embedded as the fenced Python below (sha256 035b988cbae05b51…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_analyze_marketing_trends_agent.py` first:

```bash
python3 dashboard_analyze_marketing_trends_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_analyze_marketing_trends_agent.py   # or on stdin
python3 dashboard_analyze_marketing_trends_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze marketing trends Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for analyze marketing trends - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-marketing-trends
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_analyze_marketing_trends',
    "version": '2.0.1',
    "display_name": 'Analyze marketing trends Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for analyze marketing trends - opens in any browser, no D365 access needed by the viewer.',
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
        "upstream_slug": 'dashboard-analyze-marketing-trends',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-analyze-marketing-trends',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '05f17b341c4f3445',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/analyze-marketing-trends'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-analyze-marketing-trends', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardAnalyzeMarketingTrends(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAnalyzeMarketingTrends'
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
    print(DashboardAnalyzeMarketingTrends().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
