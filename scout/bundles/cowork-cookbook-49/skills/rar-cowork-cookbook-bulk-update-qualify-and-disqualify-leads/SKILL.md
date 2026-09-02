---
name: "rar-cowork-cookbook-bulk-update-qualify-and-disqualify-leads"
description: "Applies a bulk field update across qualify and disqualify leads records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_qualify_and_disqualify_leads", "rar_sha256": "42a0e815a4a7091ed56315f4963a1c658afb535c73ac8b0838b6ea3078a17ff7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_qualify_and_disqualify_leads_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-qualify-and-disqualify-leads:9532f9ee4d5d5b8ab691c7db1299d7c1a42d9d8419d873f989d55b3caa2614ae", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_qualify_and_disqualify_leads`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_qualify_and_disqualify_leads_agent.py` is
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

Qualify and disqualify leads Bulk Field Update — Applies a bulk field update across qualify and disqualify leads records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-qualify-and-disqualify-leads
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_qualify_and_disqualify_leads_agent.py` and embedded as the fenced Python below (sha256 42a0e815a4a7091e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_qualify_and_disqualify_leads_agent.py` first:

```bash
python3 bulk_update_qualify_and_disqualify_leads_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_qualify_and_disqualify_leads_agent.py   # or on stdin
python3 bulk_update_qualify_and_disqualify_leads_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Qualify and disqualify leads Bulk Field Update — Applies a bulk field update across qualify and disqualify leads records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-qualify-and-disqualify-leads
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_qualify_and_disqualify_leads',
    "version": '2.0.0',
    "display_name": 'Qualify and disqualify leads Bulk Field Update',
    "description": 'Applies a bulk field update across qualify and disqualify leads records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-qualify-and-disqualify-leads',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-qualify-and-disqualify-leads',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6ac437cbee3509c9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/identify-and-qualify-leads/qualify-and-disqualify-leads'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/bulk-update-qualify-and-disqualify-leads', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class BulkUpdateQualifyAndDisqualifyLeads(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateQualifyAndDisqualifyLeads'
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
    print(BulkUpdateQualifyAndDisqualifyLeads().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
