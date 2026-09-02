---
name: "rar-cowork-cookbook-ppt-exec-evaluate-marketing-financials"
description: "Generates an executive-ready PowerPoint deck on evaluate marketing financials status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_evaluate_marketing_financials", "rar_sha256": "731160328cc1b649265a0b9b52dd023253b8f440483687aee6c40653f354d982", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_evaluate_marketing_financials_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-evaluate-marketing-financials:2f96e39571ee13cf801d4d12696d1e0a5800c3121f33ff70c0d3db8782e87dfd", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_evaluate_marketing_financials`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_evaluate_marketing_financials_agent.py` is
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
