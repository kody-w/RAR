---
name: "rar-cowork-cookbook-ppt-exec-perform-market-research"
description: "Generates an executive-ready PowerPoint deck on perform market research status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_perform_market_research", "rar_sha256": "a0cdecacd2e5f642c47ab1d19c1166d7f9ea46d79ce49b78fe399df262654de1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_perform_market_research_agent.py` and embedded as the fenced Python below (sha256 a0cdecacd2e5f642…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_perform_market_research_agent.py` first:

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
    "version": '2.0.0',
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
