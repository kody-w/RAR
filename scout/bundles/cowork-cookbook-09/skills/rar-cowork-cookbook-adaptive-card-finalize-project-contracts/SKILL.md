---
name: "rar-cowork-cookbook-adaptive-card-finalize-project-contracts"
description: "Produces a reusable Adaptive Card JSON snapshot of finalize project contracts status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_finalize_project_contracts", "rar_sha256": "dfff56e9f2c4fb3b67ccb70f52321fe9ef033fc41708180e5c91e1737fe093c9", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_finalize_project_contracts_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-finalize-project-contracts:e1048a7b220b53fd3f6f483c7548772e0b5f9480adefad818a13c375d342146d", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_finalize_project_contracts`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_finalize_project_contracts_agent.py` is
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

Finalize project contracts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of finalize project contracts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-finalize-project-contracts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_finalize_project_contracts_agent.py` and embedded as the fenced Python below (sha256 dfff56e9f2c4fb3b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_finalize_project_contracts_agent.py` first:

```bash
python3 adaptive_card_finalize_project_contracts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_finalize_project_contracts_agent.py   # or on stdin
python3 adaptive_card_finalize_project_contracts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Finalize project contracts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of finalize project contracts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-finalize-project-contracts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_finalize_project_contracts',
    "version": '2.0.0',
    "display_name": 'Finalize project contracts Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of finalize project contracts status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-finalize-project-contracts',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-finalize-project-contracts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '073edc4c07ce92a3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit/manage-project-contracts/finalize-project-contracts'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'project-to-profit/adaptive-card-finalize-project-contracts', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardFinalizeProjectContracts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardFinalizeProjectContracts'
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
    print(AdaptiveCardFinalizeProjectContracts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
