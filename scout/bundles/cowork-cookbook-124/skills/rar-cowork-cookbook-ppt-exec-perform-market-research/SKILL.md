---
name: "rar-cowork-cookbook-ppt-exec-perform-market-research"
description: "Generates an executive-ready PowerPoint deck on perform market research status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_perform_market_research", "rar_sha256": "232411093a4f3bbd4372cb5174d5d7818ba68c940de34f0b005a1320c095864f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_perform_market_research`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_perform_market_research_agent.py` and in the RCI capsule.

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

Perform market research Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on perform market research status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-perform-market-research
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_perform_market_research_agent.py` and embedded as the fenced Python below (sha256 232411093a4f3bbd…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_perform_market_research_agent.py` first:

```bash
python3 ppt_exec_perform_market_research_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_perform_market_research_agent.py   # or on stdin
python3 ppt_exec_perform_market_research_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Perform market research Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on perform market research status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-perform-market-research
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_perform_market_research',
    "version": '2.0.1',
    "display_name": 'Perform market research Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on perform market research status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-perform-market-research',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-perform-market-research',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'ff0451451c259ab8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/perform-market-research'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-perform-market-research', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecPerformMarketResearch(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecPerformMarketResearch'
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
    print(PptExecPerformMarketResearch().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
