---
name: "rar-cowork-cookbook-ppt-exec-evaluate-marketing-financials"
description: "Generates an executive-ready PowerPoint deck on evaluate marketing financials status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_evaluate_marketing_financials", "rar_sha256": "aaf10b83a27dbd73fbcb2a9ed86cbdea76d7ac197079e9a180cd9926204f94c1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_evaluate_marketing_financials`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_evaluate_marketing_financials_agent.py` and in the RCI capsule.

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

Evaluate marketing financials Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on evaluate marketing financials status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-evaluate-marketing-financials
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_evaluate_marketing_financials_agent.py` and embedded as the fenced Python below (sha256 aaf10b83a27dbd73…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_evaluate_marketing_financials_agent.py` first:

```bash
python3 ppt_exec_evaluate_marketing_financials_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_evaluate_marketing_financials_agent.py   # or on stdin
python3 ppt_exec_evaluate_marketing_financials_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Evaluate marketing financials Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on evaluate marketing financials status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-evaluate-marketing-financials
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_evaluate_marketing_financials',
    "version": '2.0.1',
    "display_name": 'Evaluate marketing financials Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on evaluate marketing financials status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-evaluate-marketing-financials',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-evaluate-marketing-financials',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '4f691718dad53456',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/evaluate-marketing-financials'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-evaluate-marketing-financials', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecEvaluateMarketingFinancials(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecEvaluateMarketingFinancials'
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
    print(PptExecEvaluateMarketingFinancials().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
