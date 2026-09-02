---
name: "rar-cowork-cookbook-ppt-exec-estimate-project-contracts"
description: "Generates an executive-ready PowerPoint deck on estimate project contracts status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_estimate_project_contracts", "rar_sha256": "3d476d24300181b86ee4093487881fc221d299eddd4e6dbd019cdad2417c27c9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_estimate_project_contracts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-estimate-project-contracts:15442a49517528577aeaa120913183713b93b9f01a936fc8641cae7b708514bc", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_estimate_project_contracts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_estimate_project_contracts_agent.py` is
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

Estimate project contracts Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on estimate project contracts status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-estimate-project-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_estimate_project_contracts_agent.py` and embedded as the fenced Python below (sha256 3d476d24300181b8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_estimate_project_contracts_agent.py` first:

```bash
python3 ppt_exec_estimate_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_estimate_project_contracts_agent.py   # or on stdin
python3 ppt_exec_estimate_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Estimate project contracts Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on estimate project contracts status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-estimate-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_estimate_project_contracts',
    "version": '2.0.0',
    "display_name": 'Estimate project contracts Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on estimate project contracts status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-estimate-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-estimate-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c468033aca6fe080',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/estimate-project-contracts'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/ppt-exec-estimate-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecEstimateProjectContracts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecEstimateProjectContracts'
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
    print(PptExecEstimateProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
