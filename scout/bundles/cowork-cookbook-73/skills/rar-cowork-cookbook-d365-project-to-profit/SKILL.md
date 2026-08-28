---
name: "rar-cowork-cookbook-d365-project-to-profit"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Project to profit end-to-end process - covers 6 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_project_to_profit", "rar_sha256": "1383c80478ee8daf498233059d1c5812613c320a8c19b722332d1d0704c771b5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_project_to_profit`. The original RAPP
agent is preserved byte-for-byte in `d365_project_to_profit_agent.py` and in the RCI capsule.

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

D365 Project to profit Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Project to profit end-to-end process - covers 6 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-project-to-profit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_project_to_profit_agent.py` and embedded as the fenced Python below (sha256 1383c80478ee8daf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_project_to_profit_agent.py` first:

```bash
python3 d365_project_to_profit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_project_to_profit_agent.py   # or on stdin
python3 d365_project_to_profit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Project to profit Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Project to profit end-to-end process - covers 6 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-project-to-profit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_project_to_profit',
    "version": '2.0.0',
    "display_name": 'D365 Project to profit Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Project to profit end-to-end process - covers 6 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'd365-project-to-profit',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-project-to-profit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b426d18ecbd2b523',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'project-to-profit/d365-project-to-profit', 'uses_skills': {'custom': ['d365-project-to-profit'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class D365ProjectToProfit(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ProjectToProfit'
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
    print(D365ProjectToProfit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
