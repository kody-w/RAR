---
name: "rar-cowork-cookbook-ppt-exec-develop-tax-strategy"
description: "Generates an executive-ready PowerPoint deck on develop tax strategy status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_tax_strategy", "rar_sha256": "337cb656a47153f9894db52d072586d0a7a9586efc385f4ed79ac6e1e4d2e4a4", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_develop_tax_strategy`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_develop_tax_strategy_agent.py` and in the RCI capsule.

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

Develop tax strategy Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop tax strategy status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-tax-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_tax_strategy_agent.py` and embedded as the fenced Python below (sha256 337cb656a47153f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_tax_strategy_agent.py` first:

```bash
python3 ppt_exec_develop_tax_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_tax_strategy_agent.py   # or on stdin
python3 ppt_exec_develop_tax_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop tax strategy Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop tax strategy status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-tax-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_tax_strategy',
    "version": '2.0.1',
    "display_name": 'Develop tax strategy Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop tax strategy status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-tax-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-tax-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e1c9567716130a91',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-tax-strategy'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-develop-tax-strategy', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecDevelopTaxStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopTaxStrategy'
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
    print(PptExecDevelopTaxStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
