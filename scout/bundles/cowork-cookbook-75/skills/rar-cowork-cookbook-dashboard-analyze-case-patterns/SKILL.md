---
name: "rar-cowork-cookbook-dashboard-analyze-case-patterns"
description: "Produces a self-contained interactive HTML dashboard for analyze case patterns - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_case_patterns", "rar_sha256": "96a807ac2b8a848e69580841ce2d746e42a9f77a8d88cf93bcf2f520afea04ad", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_analyze_case_patterns`. The original RAPP
agent is preserved byte-for-byte in `dashboard_analyze_case_patterns_agent.py` and in the RCI capsule.

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

Analyze case patterns Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for analyze case patterns - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-case-patterns
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_analyze_case_patterns_agent.py` and embedded as the fenced Python below (sha256 96a807ac2b8a848e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_analyze_case_patterns_agent.py` first:

```bash
python3 dashboard_analyze_case_patterns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_analyze_case_patterns_agent.py   # or on stdin
python3 dashboard_analyze_case_patterns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze case patterns Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for analyze case patterns - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-analyze-case-patterns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_analyze_case_patterns',
    "version": '2.0.0',
    "display_name": 'Analyze case patterns Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for analyze case patterns - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-analyze-case-patterns',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-analyze-case-patterns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'cef59d0bee80d872',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance/analyze-case-patterns'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-analyze-case-patterns', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardAnalyzeCasePatterns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardAnalyzeCasePatterns'
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
    print(DashboardAnalyzeCasePatterns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
