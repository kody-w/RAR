---
name: "rar-cowork-cookbook-ppt-exec-estimate-project-contracts"
description: "Generates an executive-ready PowerPoint deck on estimate project contracts status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_estimate_project_contracts", "rar_sha256": "21bf97fa5ae4e60aca3130d93c34902379df8a379ae203a501927347e3288882", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_estimate_project_contracts_agent.py` and embedded as the fenced Python below (sha256 21bf97fa5ae4e60a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_estimate_project_contracts_agent.py` first:

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
    "version": '2.0.1',
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
