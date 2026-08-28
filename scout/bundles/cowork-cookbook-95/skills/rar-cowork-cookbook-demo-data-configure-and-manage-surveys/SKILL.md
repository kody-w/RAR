---
name: "rar-cowork-cookbook-demo-data-configure-and-manage-surveys"
description: "Generates and creates realistic demo records for configure and manage surveys in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_manage_surveys", "rar_sha256": "8c074ac97ead57e1424c3e864dd9d861ea37e330283ef9d06b3e22d2592a0167", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_configure_and_manage_surveys`. The original RAPP
agent is preserved byte-for-byte in `demo_data_configure_and_manage_surveys_agent.py` and in the RCI capsule.

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

Configure and manage surveys Demo Data Generator — Generates and creates realistic demo records for configure and manage surveys in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-manage-surveys
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_configure_and_manage_surveys_agent.py` and embedded as the fenced Python below (sha256 8c074ac97ead57e1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_configure_and_manage_surveys_agent.py` first:

```bash
python3 demo_data_configure_and_manage_surveys_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_configure_and_manage_surveys_agent.py   # or on stdin
python3 demo_data_configure_and_manage_surveys_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Configure and manage surveys Demo Data Generator — Generates and creates realistic demo records for configure and manage surveys in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-configure-and-manage-surveys
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_configure_and_manage_surveys',
    "version": '2.0.0',
    "display_name": 'Configure and manage surveys Demo Data Generator',
    "description": 'Generates and creates realistic demo records for configure and manage surveys in a sandbox tenant for training and pilot scenarios.',
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
        "upstream_slug": 'demo-data-configure-and-manage-surveys',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-configure-and-manage-surveys',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'beaa1f31b4f3225b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/administer-system-features/configure-and-manage-surveys'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/demo-data-configure-and-manage-surveys', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataConfigureAndManageSurveys(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataConfigureAndManageSurveys'
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
    print(DemoDataConfigureAndManageSurveys().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
