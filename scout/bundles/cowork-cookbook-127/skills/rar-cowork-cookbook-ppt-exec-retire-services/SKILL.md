---
name: "rar-cowork-cookbook-ppt-exec-retire-services"
description: "Generates an executive-ready PowerPoint deck on retire services status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_retire_services", "rar_sha256": "255c4ff7aa4462dc9525477b2fecc06d96d5998449b209e1fe46f844d4d9011b", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_retire_services_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-retire-services:6e5c617a3b5328fb9d4170970d6df5a1c60e5b1ef5569483510301a4ee913f15", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_retire_services`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_retire_services_agent.py` is
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

Retire services Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on retire services status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-retire-services
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_retire_services_agent.py` and embedded as the fenced Python below (sha256 255c4ff7aa4462dc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_retire_services_agent.py` first:

```bash
python3 ppt_exec_retire_services_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_retire_services_agent.py   # or on stdin
python3 ppt_exec_retire_services_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Retire services Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on retire services status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-retire-services
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_retire_services',
    "version": '2.0.0',
    "display_name": 'Retire services Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on retire services status, complete with charts and talking-point notes.',
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
        "upstream_slug": 'ppt-exec-retire-services',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-retire-services',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a7f781ce74f21f2e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-service-offerings/retire-services'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/ppt-exec-retire-services', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecRetireServices(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecRetireServices'
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
    print(PptExecRetireServices().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
