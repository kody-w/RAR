---
name: "rar-cowork-cookbook-d365-administer-to-operate"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Administer to operate end-to-end process - covers 13 L2 areas and 132 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_administer_to_operate", "rar_sha256": "7426e52d07d3c45a633a8d0203ed58a64da9533f2b859dddbd2ec23f331fda7a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_administer_to_operate_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-administer-to-operate:d470b1e999faa4e4666e9d7936ad0291e2e86a90fcb515f57514b2f9eb2c98f5", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_administer_to_operate`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_administer_to_operate_agent.py` is
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

D365 Administer to operate Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Administer to operate end-to-end process - covers 13 L2 areas and 132 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-administer-to-operate
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_administer_to_operate_agent.py` and embedded as the fenced Python below (sha256 7426e52d07d3c45a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_administer_to_operate_agent.py` first:

```bash
python3 d365_administer_to_operate_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_administer_to_operate_agent.py   # or on stdin
python3 d365_administer_to_operate_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Administer to operate Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Administer to operate end-to-end process - covers 13 L2 areas and 132 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-administer-to-operate
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_administer_to_operate',
    "version": '2.0.0',
    "display_name": 'D365 Administer to operate Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Administer to operate end-to-end process - covers 13 L2 areas and 132 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
    "category": 'integrations',
    "quality_tier": 'verified',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'd365-administer-to-operate',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-administer-to-operate',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '5a7c78e64d4ef45c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'administer-to-operate/d365-administer-to-operate', 'uses_skills': {'custom': ['d365-administer-to-operate'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class D365AdministerToOperate(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AdministerToOperate'
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
    print(D365AdministerToOperate().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
