---
name: "rar-cowork-cookbook-d365-design-to-retire"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Design to retire end-to-end process - covers 5 L2 areas and 31 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_design_to_retire", "rar_sha256": "85da9c25c268510c497787dc947417a6833e04b2e2b592131ab8466bbbf8b2c7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_design_to_retire_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-design-to-retire:6c02d100342287a92eff8969cb48f11085b74635482ba1b2d4a4079eb5ab6a9f", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_design_to_retire`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_design_to_retire_agent.py` is
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

D365 Design to retire Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Design to retire end-to-end process - covers 5 L2 areas and 31 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-design-to-retire
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_design_to_retire_agent.py` and embedded as the fenced Python below (sha256 85da9c25c268510c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_design_to_retire_agent.py` first:

```bash
python3 d365_design_to_retire_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_design_to_retire_agent.py   # or on stdin
python3 d365_design_to_retire_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Design to retire Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Design to retire end-to-end process - covers 5 L2 areas and 31 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-design-to-retire
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_design_to_retire',
    "version": '2.0.0',
    "display_name": 'D365 Design to retire Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Design to retire end-to-end process - covers 5 L2 areas and 31 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-design-to-retire',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-design-to-retire',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '69050b81ed34c5f5',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'design-to-retire/d365-design-to-retire', 'uses_skills': {'custom': ['d365-design-to-retire'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class D365DesignToRetire(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365DesignToRetire'
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
    print(D365DesignToRetire().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
