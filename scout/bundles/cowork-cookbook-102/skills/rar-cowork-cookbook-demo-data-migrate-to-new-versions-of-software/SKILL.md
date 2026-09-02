---
name: "rar-cowork-cookbook-demo-data-migrate-to-new-versions-of-software"
description: "Generates and creates realistic demo records for migrate to new versions of software in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_migrate_to_new_versions_of_software", "rar_sha256": "ddd8aa83b6053462593854d2e4afcc7ac41efa652cc5cdb5e1846e22f6686b67", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_migrate_to_new_versions_of_software_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-migrate-to-new-versions-of-software:dc608328e255b59320518d56abbb996983ddad3b2b09f183160efec8b7501745", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_migrate_to_new_versions_of_software`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_migrate_to_new_versions_of_software_agent.py` is
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

Migrate to new versions of software Demo Data Generator — Generates and creates realistic demo records for migrate to new versions of software in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-migrate-to-new-versions-of-software
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_migrate_to_new_versions_of_software_agent.py` and embedded as the fenced Python below (sha256 ddd8aa83b6053462…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_migrate_to_new_versions_of_software_agent.py` first:

```bash
python3 demo_data_migrate_to_new_versions_of_software_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_migrate_to_new_versions_of_software_agent.py   # or on stdin
python3 demo_data_migrate_to_new_versions_of_software_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Migrate to new versions of software Demo Data Generator — Generates and creates realistic demo records for migrate to new versions of software in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-migrate-to-new-versions-of-software
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_migrate_to_new_versions_of_software',
    "version": '2.0.0',
    "display_name": 'Migrate to new versions of software Demo Data Generator',
    "description": 'Generates and creates realistic demo records for migrate to new versions of software in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-migrate-to-new-versions-of-software',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-migrate-to-new-versions-of-software',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0c7aa945f00c52af',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/migrate-to-new-versions-of-software'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-migrate-to-new-versions-of-software', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataMigrateToNewVersionsOfSoftware(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataMigrateToNewVersionsOfSoftware'
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
    print(DemoDataMigrateToNewVersionsOfSoftware().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
