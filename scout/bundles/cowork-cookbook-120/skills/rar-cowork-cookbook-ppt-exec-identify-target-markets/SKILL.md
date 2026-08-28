---
name: "rar-cowork-cookbook-ppt-exec-identify-target-markets"
description: "Generates an executive-ready PowerPoint deck on identify target markets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_target_markets", "rar_sha256": "1613206b2daf06758bdfa087200ce18785a2f304dfae67ece12cdd7c5123f5e5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_identify_target_markets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_identify_target_markets_agent.py` and in the RCI capsule.

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

Identify target markets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on identify target markets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-target-markets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_target_markets_agent.py` and embedded as the fenced Python below (sha256 1613206b2daf0675…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_target_markets_agent.py` first:

```bash
python3 ppt_exec_identify_target_markets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_identify_target_markets_agent.py   # or on stdin
python3 ppt_exec_identify_target_markets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify target markets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on identify target markets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-target-markets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_identify_target_markets',
    "version": '2.0.1',
    "display_name": 'Identify target markets Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on identify target markets status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-identify-target-markets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-identify-target-markets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '1b7d61f1f41488fa',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/identify-target-markets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-identify-target-markets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecIdentifyTargetMarkets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIdentifyTargetMarkets'
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
    print(PptExecIdentifyTargetMarkets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
