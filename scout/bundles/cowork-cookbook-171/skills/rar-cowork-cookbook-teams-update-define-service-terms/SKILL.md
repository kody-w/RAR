---
name: "rar-cowork-cookbook-teams-update-define-service-terms"
description: "Drafts a Teams channel post on define service terms status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_service_terms", "rar_sha256": "3c15c4428f3f6b97158a26eb30023a0c394fe1d3864d2b22f9761b094d6a1de1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_define_service_terms_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-define-service-terms:c0f1f34a4583605ef71afb38e18751b18f651964dbd57e4393b474c8e2ed542f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_define_service_terms`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_define_service_terms_agent.py` is
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
