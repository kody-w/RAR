---
name: "rar-cowork-cookbook-demo-data-migrate-to-new-versions-of-software"
description: "Generates and creates realistic demo records for migrate to new versions of software in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_migrate_to_new_versions_of_software", "rar_sha256": "c76c356a87ff1de3a6e271c3b5985be4620434a34315daba6e5095a7df0646db", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_migrate_to_new_versions_of_software`. The original RAPP
agent is preserved byte-for-byte in `demo_data_migrate_to_new_versions_of_software_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_migrate_to_new_versions_of_software_agent.py` and embedded as the fenced Python below (sha256 c76c356a87ff1de3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_migrate_to_new_versions_of_software_agent.py` first:

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
    "version": '2.0.1',
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
