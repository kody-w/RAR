---
name: "rar-cowork-cookbook-ppt-exec-define-value-proposition"
description: "Generates an executive-ready PowerPoint deck on define value proposition status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_value_proposition", "rar_sha256": "ba9b7df12ba190aea09c66dff19e1d5f540d9c0a08d5baa00f29b1c53c1b5c62", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_define_value_proposition_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-define-value-proposition:ce1cf62179cee6937c5d8120ebe6607bfbc83fcd09fe11decc163aa25932e03e", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_define_value_proposition`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_define_value_proposition_agent.py` is
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
