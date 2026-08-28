---
name: "rar-cowork-cookbook-d365-project-to-profit-manage-project-delivery"
description: "A Dynamics 365 F&SCM expert scoped to the Manage project delivery area (a level-2 subdomain of Project to profit) - covers 11 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_project_to_profit_manage_project_delivery", "rar_sha256": "1caeafbdd584931d729042a43a46dcc8f21cc7e3d49e6e34352317af41410ea8", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_project_to_profit_manage_project_delivery_agent.py` and embedded as the fenced Python below (sha256 1caeafbdd584931d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_project_to_profit_manage_project_delivery_agent.py` first:

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
    "version": '2.0.1',
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
