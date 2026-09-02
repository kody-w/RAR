---
name: "rar-cowork-cookbook-bulk-update-oversee-active-campaigns"
description: "Applies a bulk field update across oversee active campaigns records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_oversee_active_campaigns", "rar_sha256": "7034ec9aed4277ca28fa607f48752fdc0e694a2d26760e9c2792994136917618", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_oversee_active_campaigns_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-oversee-active-campaigns:19632a39775a3f2896aa1e1cf306a1461ca2420e9629cea8fedba00c14a3e5e6", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_oversee_active_campaigns`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_oversee_active_campaigns_agent.py` is
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

Oversee active campaigns Bulk Field Update — Applies a bulk field update across oversee active campaigns records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-oversee-active-campaigns
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_oversee_active_campaigns_agent.py` and embedded as the fenced Python below (sha256 7034ec9aed4277ca…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_oversee_active_campaigns_agent.py` first:

```bash
python3 bulk_update_oversee_active_campaigns_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_oversee_active_campaigns_agent.py   # or on stdin
python3 bulk_update_oversee_active_campaigns_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Oversee active campaigns Bulk Field Update — Applies a bulk field update across oversee active campaigns records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-oversee-active-campaigns
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_oversee_active_campaigns',
    "version": '2.0.0',
    "display_name": 'Oversee active campaigns Bulk Field Update',
    "description": 'Applies a bulk field update across oversee active campaigns records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-oversee-active-campaigns',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-oversee-active-campaigns',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '992a2378405713c5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/manage-marketing-campaigns/oversee-active-campaigns'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/bulk-update-oversee-active-campaigns', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateOverseeActiveCampaigns(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateOverseeActiveCampaigns'
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
    print(BulkUpdateOverseeActiveCampaigns().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
