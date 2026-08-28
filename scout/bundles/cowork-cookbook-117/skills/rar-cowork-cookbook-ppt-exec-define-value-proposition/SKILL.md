---
name: "rar-cowork-cookbook-ppt-exec-define-value-proposition"
description: "Generates an executive-ready PowerPoint deck on define value proposition status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_value_proposition", "rar_sha256": "ac08cf1ffd1b06be4fc3f48a98ed774cdae80ae2157fa7aaea4a334b122ea270", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_value_proposition`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_value_proposition_agent.py` and in the RCI capsule.

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

Define value proposition Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define value proposition status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-value-proposition
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_value_proposition_agent.py` and embedded as the fenced Python below (sha256 ac08cf1ffd1b06be…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_value_proposition_agent.py` first:

```bash
python3 ppt_exec_define_value_proposition_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_value_proposition_agent.py   # or on stdin
python3 ppt_exec_define_value_proposition_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define value proposition Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define value proposition status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-value-proposition
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_value_proposition',
    "version": '2.0.1',
    "display_name": 'Define value proposition Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define value proposition status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-define-value-proposition',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-value-proposition',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3901ed681075c767',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/develop-marketing-strategy/define-value-proposition'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-define-value-proposition', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDefineValueProposition(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineValueProposition'
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
    print(PptExecDefineValueProposition().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
