---
name: "rar-cowork-cookbook-ppt-exec-evaluate-marketing-financials"
description: "Generates an executive-ready PowerPoint deck on evaluate marketing financials status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_evaluate_marketing_financials", "rar_sha256": "731160328cc1b649265a0b9b52dd023253b8f440483687aee6c40653f354d982", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_evaluate_marketing_financials_agent.py` and embedded as the fenced Python below (sha256 731160328cc1b649…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_evaluate_marketing_financials_agent.py` first:

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
    "version": '2.0.0',
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
