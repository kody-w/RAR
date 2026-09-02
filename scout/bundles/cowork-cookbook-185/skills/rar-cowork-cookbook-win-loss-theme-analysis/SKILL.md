---
name: "rar-cowork-cookbook-win-loss-theme-analysis"
description: "Analyzes closed opportunities to surface recurring themes in why deals are won and lost, grouped by reason, competitor, value band, and stage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/win_loss_theme_analysis", "rar_sha256": "3c07691b700b5f096ed77c40f7b9b4fe17b139cf9ef6cb54f2c4282259605d50", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "win_loss_theme_analysis_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/win-loss-theme-analysis:ac55972391b35c1b57dfbe106a8f0ed0bcc0b80046d96487f6d30ee9ebe0a66f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/win_loss_theme_analysis`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `win_loss_theme_analysis_agent.py` is
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

Win/Loss Theme Analysis — Analyzes closed opportunities to surface recurring themes in why deals are won and lost, grouped by reason, competitor, value band, and stage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/win-loss-theme-analysis
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `win_loss_theme_analysis_agent.py` and embedded as the fenced Python below (sha256 3c07691b700b5f09…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `win_loss_theme_analysis_agent.py` first:

```bash
python3 win_loss_theme_analysis_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 win_loss_theme_analysis_agent.py   # or on stdin
python3 win_loss_theme_analysis_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Win/Loss Theme Analysis — Analyzes closed opportunities to surface recurring themes in why deals are won and lost, grouped by reason, competitor, value band, and stage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/win-loss-theme-analysis
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/win_loss_theme_analysis',
    "version": '2.0.0',
    "display_name": 'Win/Loss Theme Analysis',
    "description": 'Analyzes closed opportunities to surface recurring themes in why deals are won and lost, grouped by reason, competitor, value band, and stage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'advanced', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'win-loss-theme-analysis',
        "upstream_url": 'https://coworkcookbook.com/recipes/win-loss-theme-analysis',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '47370683e39bcaa4',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/analyze-sales/provide-insights-into-sales-strategies-and-performance'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/win-loss-theme-analysis', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'PowerPoint'], 'plugin': [{'action': 'search', 'plugin': 'dynamics-365-sales'}, {'action': 'describe', 'plugin': 'dynamics-365-sales'}, {'action': 'read_query', 'plugin': 'dynamics-365-sales'}]}, 'verification_status': 'draft'},
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


class WinLossThemeAnalysis(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'WinLossThemeAnalysis'
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
    print(WinLossThemeAnalysis().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
