---
name: "rar-cowork-cookbook-case-heatmap-html"
description: "Builds an interactive HTML heatmap of customer service cases by product category \u00d7 priority \u00d7 age bucket, with drill-through tooltips."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/case_heatmap_html", "rar_sha256": "2bd63f3015231a03db6f4ae00f8c70d31ffc59fba1275b20a4d55353cddd92cf", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "case_heatmap_html_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/case-heatmap-html:30f9db3927141b16c276d8dd2b2fb8c157bd249f21975b41d1c7d68fc31f441e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/case_heatmap_html`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `case_heatmap_html_agent.py` is
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
