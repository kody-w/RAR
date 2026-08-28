---
name: "rar-cowork-cookbook-teams-update-test-software-releases"
description: "Drafts a Teams channel post on test software releases status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_test_software_releases", "rar_sha256": "31dbe431bc6adb83a17e6b9e39d2e9321de96dde6221d9f942a8c07cc9b7a9c4", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_test_software_releases`. The original RAPP
agent is preserved byte-for-byte in `teams_update_test_software_releases_agent.py` and in the RCI capsule.

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
