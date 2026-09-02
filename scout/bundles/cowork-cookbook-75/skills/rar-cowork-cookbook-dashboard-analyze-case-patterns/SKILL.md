---
name: "rar-cowork-cookbook-dashboard-analyze-case-patterns"
description: "Produces a self-contained interactive HTML dashboard for analyze case patterns - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_analyze_case_patterns", "rar_sha256": "96a807ac2b8a848e69580841ce2d746e42a9f77a8d88cf93bcf2f520afea04ad", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_analyze_case_patterns_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-analyze-case-patterns:18471bbc0f8d61e315525932bb345c3fca9f32c04294083d35f8394cdcac5c8e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_analyze_case_patterns`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_analyze_case_patterns_agent.py` is
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
