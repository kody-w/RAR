---
name: "rar-cowork-cookbook-teams-update-test-software-releases"
description: "Drafts a Teams channel post on test software releases status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_test_software_releases", "rar_sha256": "31dbe431bc6adb83a17e6b9e39d2e9321de96dde6221d9f942a8c07cc9b7a9c4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "teams_update_test_software_releases_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/teams-update-test-software-releases:07db3a586c4ee2cccd868669acf4dcd303573b4f57b53b27cee3c52c091c7585", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/teams_update_test_software_releases`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `teams_update_test_software_releases_agent.py` is
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

Test software releases Teams Channel Update — Drafts a Teams channel post on test software releases status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-test-software-releases
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_test_software_releases_agent.py` and embedded as the fenced Python below (sha256 31dbe431bc6adb83…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_test_software_releases_agent.py` first:

```bash
python3 teams_update_test_software_releases_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_test_software_releases_agent.py   # or on stdin
python3 teams_update_test_software_releases_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Test software releases Teams Channel Update — Drafts a Teams channel post on test software releases status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-test-software-releases
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_test_software_releases',
    "version": '2.0.0',
    "display_name": 'Test software releases Teams Channel Update',
    "description": 'Drafts a Teams channel post on test software releases status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-test-software-releases',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-test-software-releases',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '3dfcfb92b6e69f2e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/uptake-software-releases/test-software-releases'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-test-software-releases', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class TeamsUpdateTestSoftwareReleases(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateTestSoftwareReleases'
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
    print(TeamsUpdateTestSoftwareReleases().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
