---
name: "rar-cowork-cookbook-teams-update-define-service-terms"
description: "Drafts a Teams channel post on define service terms status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_service_terms", "rar_sha256": "3c15c4428f3f6b97158a26eb30023a0c394fe1d3864d2b22f9761b094d6a1de1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_service_terms_agent.py` and embedded as the fenced Python below (sha256 3c15c4428f3f6b97…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_service_terms_agent.py` first:

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
    "version": '2.0.0',
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
