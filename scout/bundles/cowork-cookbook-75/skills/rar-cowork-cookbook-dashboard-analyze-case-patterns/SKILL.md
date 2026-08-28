---
name: "rar-cowork-cookbook-dashboard-analyze-case-patterns"
description: "Produces a self-contained interactive HTML dashboard for analyze case patterns - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_case_patterns", "rar_sha256": "dd179f3a7ef2cd22da439b02901e14f5efdad81a9cd42c71efbafdc9207d5d79", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_analyze_case_patterns_agent.py` and embedded as the fenced Python below (sha256 dd179f3a7ef2cd22…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_analyze_case_patterns_agent.py` first:

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
    "version": '2.0.1',
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
