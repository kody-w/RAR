---
name: "rar-cowork-cookbook-ppt-exec-define-value-proposition"
description: "Generates an executive-ready PowerPoint deck on define value proposition status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_value_proposition", "rar_sha256": "ba9b7df12ba190aea09c66dff19e1d5f540d9c0a08d5baa00f29b1c53c1b5c62", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_value_proposition_agent.py` and embedded as the fenced Python below (sha256 ba9b7df12ba190ae…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_value_proposition_agent.py` first:

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
    "version": '2.0.0',
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
