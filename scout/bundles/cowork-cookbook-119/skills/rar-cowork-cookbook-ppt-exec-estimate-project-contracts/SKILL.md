---
name: "rar-cowork-cookbook-ppt-exec-estimate-project-contracts"
description: "Generates an executive-ready PowerPoint deck on estimate project contracts status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_estimate_project_contracts", "rar_sha256": "3d476d24300181b86ee4093487881fc221d299eddd4e6dbd019cdad2417c27c9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_estimate_project_contracts`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_estimate_project_contracts_agent.py` and in the RCI capsule.

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
