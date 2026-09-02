---
name: "rar-cowork-cookbook-adaptive-card-manage-lead-identification-process"
description: "Produces a reusable Adaptive Card JSON snapshot of manage lead identification process status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_manage_lead_identification_process", "rar_sha256": "220ce750fe28fe689919c7ce9d09bea3cbc52a7088bec1ebd5de12f59a139bc1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "adaptive_card_manage_lead_identification_process_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/adaptive-card-manage-lead-identification-process:62c1511b5beb4eee800dce70ac1c40ff660185361741799646b87da85db2b9a4", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/adaptive_card_manage_lead_identification_process`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `adaptive_card_manage_lead_identification_process_agent.py` is
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

Manage lead identification process Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage lead identification process status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-lead-identification-process
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_manage_lead_identification_process_agent.py` and embedded as the fenced Python below (sha256 220ce750fe28fe68…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_manage_lead_identification_process_agent.py` first:

```bash
python3 adaptive_card_manage_lead_identification_process_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_manage_lead_identification_process_agent.py   # or on stdin
python3 adaptive_card_manage_lead_identification_process_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage lead identification process Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of manage lead identification process status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-manage-lead-identification-process
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_manage_lead_identification_process',
    "version": '2.0.0',
    "display_name": 'Manage lead identification process Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of manage lead identification process status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-manage-lead-identification-process',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-manage-lead-identification-process',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a7e721ba734d6b92',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/manage-lead-identification-process'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-manage-lead-identification-process', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardManageLeadIdentificationProcess(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardManageLeadIdentificationProcess'
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
    print(AdaptiveCardManageLeadIdentificationProcess().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
