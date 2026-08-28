---
name: "rar-cowork-cookbook-ppt-exec-identify-target-markets"
description: "Generates an executive-ready PowerPoint deck on identify target markets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_target_markets", "rar_sha256": "1ecd9e88a9751b5bba8aae2fc444650ce18e3e172e10c82f47ea6d8db4bfb82a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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
