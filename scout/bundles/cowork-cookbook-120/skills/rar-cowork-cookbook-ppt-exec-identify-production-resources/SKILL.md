---
name: "rar-cowork-cookbook-ppt-exec-identify-production-resources"
description: "Generates an executive-ready PowerPoint deck on identify production resources status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_identify_production_resources", "rar_sha256": "e22ad46413af05f943f43acbffbcfd770b21422d6c8943c77d5a995ec9b669c5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_identify_production_resources_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-identify-production-resources:9feee49805e1d5e2bb8ec34a8a57f86e26022a15f6d1895abe0cac2ddf09b4aa", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_identify_production_resources`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_identify_production_resources_agent.py` is
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

Identify production resources Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on identify production resources status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-production-resources
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_identify_production_resources_agent.py` and embedded as the fenced Python below (sha256 e22ad46413af05f9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_identify_production_resources_agent.py` first:

```bash
python3 ppt_exec_identify_production_resources_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_identify_production_resources_agent.py   # or on stdin
python3 ppt_exec_identify_production_resources_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify production resources Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on identify production resources status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-identify-production-resources
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_identify_production_resources',
    "version": '2.0.0',
    "display_name": 'Identify production resources Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on identify production resources status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-identify-production-resources',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-identify-production-resources',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a04d7e7860c40fa3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/identify-production-resources'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/ppt-exec-identify-production-resources', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecIdentifyProductionResources(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecIdentifyProductionResources'
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
    print(PptExecIdentifyProductionResources().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
