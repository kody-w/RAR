---
name: "rar-cowork-cookbook-win-loss-theme-analysis"
description: "Analyzes closed opportunities to surface recurring themes in why deals are won and lost, grouped by reason, competitor, value band, and stage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/win_loss_theme_analysis", "rar_sha256": "4e7fae5dd8196e93920041cfd62ad65f601a58337437a6e88b6a28c65cbd06bf", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "advanced", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/win_loss_theme_analysis`. The original RAPP
agent is preserved byte-for-byte in `win_loss_theme_analysis_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `win_loss_theme_analysis_agent.py` and embedded as the fenced Python below (sha256 4e7fae5dd8196e93…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `win_loss_theme_analysis_agent.py` first:

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
    "version": '2.0.1',
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
