---
name: "rar-cowork-cookbook-ppt-exec-perform-market-research"
description: "Generates an executive-ready PowerPoint deck on perform market research status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_perform_market_research", "rar_sha256": "a0cdecacd2e5f642c47ab1d19c1166d7f9ea46d79ce49b78fe399df262654de1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_perform_market_research_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-perform-market-research:7123a2c0ad5ed56af0b23119620563041423dfceecb9e9f112eeaf1e59896d89", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_perform_market_research`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_perform_market_research_agent.py` is
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
