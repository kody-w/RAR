---
name: "rar-cowork-cookbook-demo-data-configure-and-manage-surveys"
description: "Generates and creates realistic demo records for configure and manage surveys in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_configure_and_manage_surveys", "rar_sha256": "8c074ac97ead57e1424c3e864dd9d861ea37e330283ef9d06b3e22d2592a0167", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_configure_and_manage_surveys_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-configure-and-manage-surveys:2f8c6fe8315cf0df7d39bbf6dee0cd7a6c78e93e47649b667d70c241fe1e534b", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_configure_and_manage_surveys`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_configure_and_manage_surveys_agent.py` is
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
