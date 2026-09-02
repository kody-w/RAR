---
name: "rar-cowork-cookbook-ppt-exec-identify-target-markets"
description: "Generates an executive-ready PowerPoint deck on identify target markets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_target_markets", "rar_sha256": "1ecd9e88a9751b5bba8aae2fc444650ce18e3e172e10c82f47ea6d8db4bfb82a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_identify_target_markets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-identify-target-markets:6db0cb5c0f77bc8adc8d7bec56b1476bcf6e210c833f9d80d1ae275ea365850a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_identify_target_markets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_identify_target_markets_agent.py` is
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_target_markets_agent.py` and embedded as the fenced Python below (sha256 1ecd9e88a9751b5b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_target_markets_agent.py` first:

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
    "version": '2.0.0',
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
