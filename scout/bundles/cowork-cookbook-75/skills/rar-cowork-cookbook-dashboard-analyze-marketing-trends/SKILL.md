---
name: "rar-cowork-cookbook-dashboard-analyze-marketing-trends"
description: "Produces a self-contained interactive HTML dashboard for analyze marketing trends - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_marketing_trends", "rar_sha256": "beeff119eb8b6abf02179be57c177c8ca11963fbf3afc79a1a9244f4d1981eb7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_analyze_marketing_trends_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-analyze-marketing-trends:635369362ea935dfff405e5dbc24e23426222da6eaebdba845175fc9065bf1e1", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_analyze_marketing_trends`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_analyze_marketing_trends_agent.py` is
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
