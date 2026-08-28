---
name: "rar-cowork-cookbook-case-heatmap-html"
description: "Builds an interactive HTML heatmap of customer service cases by product category \u00d7 priority \u00d7 age bucket, with drill-through tooltips."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/case_heatmap_html", "rar_sha256": "2bd63f3015231a03db6f4ae00f8c70d31ffc59fba1275b20a4d55353cddd92cf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/case_heatmap_html`. The original RAPP
agent is preserved byte-for-byte in `case_heatmap_html_agent.py` and in the RCI capsule.

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

Customer Service Case Heatmap (HTML) — Builds an interactive HTML heatmap of customer service cases by product category × priority × age bucket, with drill-through tooltips.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/case-heatmap-html
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `case_heatmap_html_agent.py` and embedded as the fenced Python below (sha256 2bd63f3015231a03…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `case_heatmap_html_agent.py` first:

```bash
python3 case_heatmap_html_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 case_heatmap_html_agent.py   # or on stdin
python3 case_heatmap_html_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Customer Service Case Heatmap (HTML) — Builds an interactive HTML heatmap of customer service cases by product category × priority × age bucket, with drill-through tooltips.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/case-heatmap-html
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/case_heatmap_html',
    "version": '2.0.0',
    "display_name": 'Customer Service Case Heatmap (HTML)',
    "description": 'Builds an interactive HTML heatmap of customer service cases by product category × priority × age bucket, with drill-through tooltips.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'case-heatmap-html',
        "upstream_url": 'https://coworkcookbook.com/recipes/case-heatmap-html',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd2e6ac1bee32eafe',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-23', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/analyze-case-performance'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/case-heatmap-html', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class CaseHeatmapHtml(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CaseHeatmapHtml'
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
    print(CaseHeatmapHtml().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
