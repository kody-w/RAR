---
name: "rar-cowork-cookbook-teams-update-define-service-terms"
description: "Drafts a Teams channel post on define service terms status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_service_terms", "rar_sha256": "06293b000d0117cae33975ec3dffd3403a7cbbc144d32fd5b3ba85eb8e22a53e", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_service_terms`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_service_terms_agent.py` and in the RCI capsule.

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

Define service terms Teams Channel Update — Drafts a Teams channel post on define service terms status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-service-terms
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_service_terms_agent.py` and embedded as the fenced Python below (sha256 06293b000d0117ca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_service_terms_agent.py` first:

```bash
python3 teams_update_define_service_terms_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_service_terms_agent.py   # or on stdin
python3 teams_update_define_service_terms_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define service terms Teams Channel Update — Drafts a Teams channel post on define service terms status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-service-terms
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_service_terms',
    "version": '2.0.1',
    "display_name": 'Define service terms Teams Channel Update',
    "description": 'Drafts a Teams channel post on define service terms status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-service-terms',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-service-terms',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b9992e02c4c34034',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/define-service-terms'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/teams-update-define-service-terms', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDefineServiceTerms(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineServiceTerms'
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
    print(TeamsUpdateDefineServiceTerms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
