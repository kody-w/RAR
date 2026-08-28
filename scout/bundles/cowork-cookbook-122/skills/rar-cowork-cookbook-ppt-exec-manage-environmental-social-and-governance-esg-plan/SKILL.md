---
name: "rar-cowork-cookbook-ppt-exec-manage-environmental-social-and-governance-esg-plan"
description: "Generates an executive-ready PowerPoint deck on manage environmental, social, and governance (ESG) plan status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_manage_environmental_social_and_governance_esg_plan", "rar_sha256": "c0f15ed6368786168f195e8f0ae518311845b248f5a0a7cf3a7f3fcf3057eaae", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "forecast_to_plan", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py` and embedded as the fenced Python below (sha256 c0f15ed636878616…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_manage_environmental_social_and_governance_esg_plan_agent.py` first:

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
    "version": '2.0.0',
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
