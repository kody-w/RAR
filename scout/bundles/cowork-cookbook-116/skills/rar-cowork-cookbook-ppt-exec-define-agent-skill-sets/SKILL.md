---
name: "rar-cowork-cookbook-ppt-exec-define-agent-skill-sets"
description: "Generates an executive-ready PowerPoint deck on define agent skill sets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_agent_skill_sets", "rar_sha256": "8fff37fe77b6a6b98ad00f9283ab4840319fd90d4368fd6478cad33fb405525f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_define_agent_skill_sets_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-define-agent-skill-sets:b4b0958d87d8e868273746900cc04227f7e62c2b36b5b53ce575eb15c062e718", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_define_agent_skill_sets`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_define_agent_skill_sets_agent.py` is
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

Define agent skill sets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define agent skill sets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-agent-skill-sets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_agent_skill_sets_agent.py` and embedded as the fenced Python below (sha256 8fff37fe77b6a6b9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_agent_skill_sets_agent.py` first:

```bash
python3 ppt_exec_define_agent_skill_sets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_agent_skill_sets_agent.py   # or on stdin
python3 ppt_exec_define_agent_skill_sets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define agent skill sets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define agent skill sets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-agent-skill-sets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_agent_skill_sets',
    "version": '2.0.0',
    "display_name": 'Define agent skill sets Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define agent skill sets status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-agent-skill-sets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-agent-skill-sets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bcca733912a2e7cf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-agent-skill-sets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-define-agent-skill-sets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecDefineAgentSkillSets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineAgentSkillSets'
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
    print(PptExecDefineAgentSkillSets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
