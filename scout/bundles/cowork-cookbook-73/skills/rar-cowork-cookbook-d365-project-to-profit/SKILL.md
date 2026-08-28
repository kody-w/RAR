---
name: "rar-cowork-cookbook-d365-project-to-profit"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Project to profit end-to-end process - covers 6 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_project_to_profit", "rar_sha256": "41b76fb761d51b54fbf65b6d3dee6dfca788d55f0dbebef3cc240d79d80194a6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_project_to_profit_agent.py` and embedded as the fenced Python below (sha256 41b76fb761d51b54…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_project_to_profit_agent.py` first:

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
    "version": '2.0.1',
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
