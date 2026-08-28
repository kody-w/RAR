---
name: "rar-cowork-cookbook-teams-update-test-software-releases"
description: "Drafts a Teams channel post on test software releases status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_test_software_releases", "rar_sha256": "41031da893df021884b92ef3f2fe8465c93fe718025566f1788907122a4b3e34", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_test_software_releases_agent.py` and embedded as the fenced Python below (sha256 41031da893df0218…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_test_software_releases_agent.py` first:

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
    "version": '2.0.1',
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
