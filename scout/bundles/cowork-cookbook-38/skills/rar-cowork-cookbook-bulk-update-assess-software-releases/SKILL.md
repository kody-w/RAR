---
name: "rar-cowork-cookbook-bulk-update-assess-software-releases"
description: "Applies a bulk field update across assess software releases records from an input list, with dry-run preview before commit."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/bulk_update_assess_software_releases", "rar_sha256": "d95b5341ec0fbf7a4788c43ed014ae72cfa49aaff25364bc10e922ed3b97affc", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "bulk_update_assess_software_releases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/bulk-update-assess-software-releases:0b738575fdbece8952a1d2d9bc9e07f0d2cab1a5264800c06e427727ae7b5cff", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "bulk_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/bulk_update_assess_software_releases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `bulk_update_assess_software_releases_agent.py` is
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

Assess software releases Bulk Field Update — Applies a bulk field update across assess software releases records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-assess-software-releases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `bulk_update_assess_software_releases_agent.py` and embedded as the fenced Python below (sha256 d95b5341ec0fbf7a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `bulk_update_assess_software_releases_agent.py` first:

```bash
python3 bulk_update_assess_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 bulk_update_assess_software_releases_agent.py   # or on stdin
python3 bulk_update_assess_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Assess software releases Bulk Field Update — Applies a bulk field update across assess software releases records from an input list, with dry-run preview before commit.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/bulk-update-assess-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/bulk_update_assess_software_releases',
    "version": '2.0.0',
    "display_name": 'Assess software releases Bulk Field Update',
    "description": 'Applies a bulk field update across assess software releases records from an input list, with dry-run preview before commit.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'bulk_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'bulk-update-assess-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/bulk-update-assess-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6a5f400dc7043408',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/assess-software-releases'], 'recipe_category': 'bulk-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/bulk-update-assess-software-releases', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_update_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.75, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class BulkUpdateAssessSoftwareReleases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BulkUpdateAssessSoftwareReleases'
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
    print(BulkUpdateAssessSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
