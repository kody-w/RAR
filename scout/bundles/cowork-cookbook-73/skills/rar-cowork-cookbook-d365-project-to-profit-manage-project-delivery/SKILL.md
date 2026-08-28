---
name: "rar-cowork-cookbook-d365-project-to-profit-manage-project-delivery"
description: "A Dynamics 365 F&SCM expert scoped to the Manage project delivery area (a level-2 subdomain of Project to profit) - covers 11 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_project_to_profit_manage_project_delivery", "rar_sha256": "c025ba108ce87f2c322cb5a725e2f59010f43e8518a4871e4097ac04c7df686f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_project_to_profit_manage_project_delivery`. The original RAPP
agent is preserved byte-for-byte in `d365_project_to_profit_manage_project_delivery_agent.py` and in the RCI capsule.

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

D365 Manage project delivery Expert — A Dynamics 365 F&SCM expert scoped to the Manage project delivery area (a level-2 subdomain of Project to profit) - covers 11 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-project-to-profit-manage-project-delivery
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_project_to_profit_manage_project_delivery_agent.py` and embedded as the fenced Python below (sha256 c025ba108ce87f2c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_project_to_profit_manage_project_delivery_agent.py` first:

```bash
python3 d365_project_to_profit_manage_project_delivery_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_project_to_profit_manage_project_delivery_agent.py   # or on stdin
python3 d365_project_to_profit_manage_project_delivery_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Manage project delivery Expert — A Dynamics 365 F&SCM expert scoped to the Manage project delivery area (a level-2 subdomain of Project to profit) - covers 11 L3 processes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-project-to-profit-manage-project-delivery
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_project_to_profit_manage_project_delivery',
    "version": '2.0.0',
    "display_name": 'D365 Manage project delivery Expert',
    "description": 'A Dynamics 365 F&SCM expert scoped to the Manage project delivery area (a level-2 subdomain of Project to profit) - covers 11 L3 processes.',
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
        "upstream_slug": 'd365-project-to-profit-manage-project-delivery',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-project-to-profit-manage-project-delivery',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e18efa2eacc20039',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-delivery'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'project-to-profit/d365-project-to-profit-manage-project-delivery', 'uses_skills': {'custom': ['d365-project-to-profit-manage-project-delivery'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365ProjectToProfitManageProjectDelivery(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ProjectToProfitManageProjectDelivery'
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
    print(D365ProjectToProfitManageProjectDelivery().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
