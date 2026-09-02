---
name: "rar-cowork-cookbook-scheduled-brief-update-product-assortments"
description: "Schedulable morning-brief email summarizing update product assortments for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_update_product_assortments", "rar_sha256": "719d1435448b882a0b118936ff186200b7525f98ccf1250b9aa6a14d338fb105", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "scheduled_brief_update_product_assortments_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/scheduled-brief-update-product-assortments:c375adad1dd7cf7e668cf211d1593dab0e95c10ef9db83a12b2cab360a049ee3", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/scheduled_brief_update_product_assortments`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `scheduled_brief_update_product_assortments_agent.py` is
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

Update product assortments Scheduled Email Brief — Schedulable morning-brief email summarizing update product assortments for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-update-product-assortments
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_update_product_assortments_agent.py` and embedded as the fenced Python below (sha256 719d1435448b882a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_update_product_assortments_agent.py` first:

```bash
python3 scheduled_brief_update_product_assortments_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_update_product_assortments_agent.py   # or on stdin
python3 scheduled_brief_update_product_assortments_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Update product assortments Scheduled Email Brief — Schedulable morning-brief email summarizing update product assortments for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-update-product-assortments
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_update_product_assortments',
    "version": '2.0.0',
    "display_name": 'Update product assortments Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing update product assortments for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-update-product-assortments',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-update-product-assortments',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '644a6f20dfcedd34',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/manage-active-products/update-product-assortments'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/scheduled-brief-update-product-assortments', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefUpdateProductAssortments(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefUpdateProductAssortments'
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
    print(ScheduledBriefUpdateProductAssortments().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
