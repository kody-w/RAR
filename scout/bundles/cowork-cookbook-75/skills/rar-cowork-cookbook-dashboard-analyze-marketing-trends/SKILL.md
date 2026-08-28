---
name: "rar-cowork-cookbook-dashboard-analyze-marketing-trends"
description: "Produces a self-contained interactive HTML dashboard for analyze marketing trends - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_marketing_trends", "rar_sha256": "beeff119eb8b6abf02179be57c177c8ca11963fbf3afc79a1a9244f4d1981eb7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_analyze_marketing_trends_agent.py` and embedded as the fenced Python below (sha256 beeff119eb8b6abf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_analyze_marketing_trends_agent.py` first:

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
    "version": '2.0.0',
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
