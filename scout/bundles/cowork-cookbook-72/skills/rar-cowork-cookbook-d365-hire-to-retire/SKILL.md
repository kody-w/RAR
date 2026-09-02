---
name: "rar-cowork-cookbook-d365-hire-to-retire"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Hire to retire end-to-end process - covers 8 L2 areas and 55 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_hire_to_retire", "rar_sha256": "45f50e5967de3de38ffc7d775f5a92b695130c30661356eff7cb68c6af4bd651", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_hire_to_retire_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-hire-to-retire:c240f190afde245a8405b7d1ce9a0b83f826c7722847d375d282d3154630b024", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_hire_to_retire`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_hire_to_retire_agent.py` is
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

D365 Hire to retire Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Hire to retire end-to-end process - covers 8 L2 areas and 55 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-hire-to-retire
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_hire_to_retire_agent.py` and embedded as the fenced Python below (sha256 45f50e5967de3de3…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_hire_to_retire_agent.py` first:

```bash
python3 d365_hire_to_retire_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_hire_to_retire_agent.py   # or on stdin
python3 d365_hire_to_retire_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Hire to retire Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Hire to retire end-to-end process - covers 8 L2 areas and 55 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-hire-to-retire
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_hire_to_retire',
    "version": '2.0.0',
    "display_name": 'D365 Hire to retire Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Hire to retire end-to-end process - covers 8 L2 areas and 55 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-hire-to-retire',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-hire-to-retire',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '2b1ef1a2229f366c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'hire-to-retire/d365-hire-to-retire', 'uses_skills': {'custom': ['d365-hire-to-retire'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365HireToRetire(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365HireToRetire'
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
    print(D365HireToRetire().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
