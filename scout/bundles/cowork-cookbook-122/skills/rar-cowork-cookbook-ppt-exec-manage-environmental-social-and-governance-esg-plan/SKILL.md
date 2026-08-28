---
name: "rar-cowork-cookbook-ppt-exec-manage-environmental-social-and-governance-esg-plan"
description: "Generates an executive-ready PowerPoint deck on manage environmental, social, and governance (ESG) plan status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_environmental_social_and_governance_esg_plan", "rar_sha256": "9f283418d0b7e24dabb4e9bc662d78e1ee80fb83210cd9a28efc9119ac9dd1f9", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_manage_environmental_social_and_governance_esg_plan`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py` and in the RCI capsule.

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

Manage environmental, social, and governance (ESG) plan Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage environmental, social, and governance (ESG) plan status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-environmental-social-and-governance-esg-plan
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py` and embedded as the fenced Python below (sha256 9f283418d0b7e24d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py` first:

```bash
python3 ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py   # or on stdin
python3 ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage environmental, social, and governance (ESG) plan Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on manage environmental, social, and governance (ESG) plan status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-manage-environmental-social-and-governance-esg-plan
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_manage_environmental_social_and_governance_esg_plan',
    "version": '2.0.1',
    "display_name": 'Manage environmental, social, and governance (ESG) plan Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on manage environmental, social, and governance (ESG) plan status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'forecast_to_plan', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-manage-environmental-social-and-governance-esg-plan',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-manage-environmental-social-and-governance-esg-plan',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '901e05fbed772744',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['forecast-to-plan'], 'process_tags': ['forecast-to-plan/develop-business-strategy/manage-environmental-social-and-governance-esg-plan'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'forecast-to-plan/ppt-exec-manage-environmental-social-and-governance-esg-plan', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class PptExecManageEnvironmentalSocialAndGovernanceEsgPlan(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecManageEnvironmentalSocialAndGovernanceEsgPlan'
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
    print(PptExecManageEnvironmentalSocialAndGovernanceEsgPlan().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
