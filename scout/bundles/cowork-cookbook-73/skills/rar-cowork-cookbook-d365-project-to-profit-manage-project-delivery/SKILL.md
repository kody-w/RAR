---
name: "rar-cowork-cookbook-d365-project-to-profit-manage-project-delivery"
description: "A Dynamics 365 F&SCM expert scoped to the Manage project delivery area (a level-2 subdomain of Project to profit) - covers 11 L3 processes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_project_to_profit_manage_project_delivery", "rar_sha256": "c025ba108ce87f2c322cb5a725e2f59010f43e8518a4871e4097ac04c7df686f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_project_to_profit_manage_project_delivery_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-project-to-profit-manage-project-delivery:f72869935a749532c861b48cf19cc2ede939894a0bb87fa5b626cfbaf2cac9ef", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_project_to_profit_manage_project_delivery`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_project_to_profit_manage_project_delivery_agent.py` is
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
