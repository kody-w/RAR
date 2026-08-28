---
name: "rar-cowork-cookbook-ppt-exec-define-agent-skill-sets"
description: "Generates an executive-ready PowerPoint deck on define agent skill sets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_agent_skill_sets", "rar_sha256": "8fff37fe77b6a6b98ad00f9283ab4840319fd90d4368fd6478cad33fb405525f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_agent_skill_sets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_agent_skill_sets_agent.py` and in the RCI capsule.

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
