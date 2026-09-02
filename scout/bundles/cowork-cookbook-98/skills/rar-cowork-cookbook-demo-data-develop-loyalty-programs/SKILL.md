---
name: "rar-cowork-cookbook-demo-data-develop-loyalty-programs"
description: "Generates and creates realistic demo records for develop loyalty programs in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_develop_loyalty_programs", "rar_sha256": "3278be9c760e820a97473196aebab3c3cedf0d92ca7a34274bdb2d441b95d294", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "demo_data_develop_loyalty_programs_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/demo-data-develop-loyalty-programs:923bbe15ba680037f6c45775830630ce7aca78db79b09ca3d35ffbec3fdd19fb", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/demo_data_develop_loyalty_programs`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `demo_data_develop_loyalty_programs_agent.py` is
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

Develop loyalty programs Demo Data Generator — Generates and creates realistic demo records for develop loyalty programs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-loyalty-programs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_develop_loyalty_programs_agent.py` and embedded as the fenced Python below (sha256 3278be9c760e820a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_develop_loyalty_programs_agent.py` first:

```bash
python3 demo_data_develop_loyalty_programs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_develop_loyalty_programs_agent.py   # or on stdin
python3 demo_data_develop_loyalty_programs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop loyalty programs Demo Data Generator — Generates and creates realistic demo records for develop loyalty programs in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-develop-loyalty-programs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_develop_loyalty_programs',
    "version": '2.0.0',
    "display_name": 'Develop loyalty programs Demo Data Generator',
    "description": 'Generates and creates realistic demo records for develop loyalty programs in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-develop-loyalty-programs',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-develop-loyalty-programs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e110ebf1fbfcd5d6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/develop-loyalty-programs'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/demo-data-develop-loyalty-programs', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataDevelopLoyaltyPrograms(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataDevelopLoyaltyPrograms'
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
    print(DemoDataDevelopLoyaltyPrograms().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
