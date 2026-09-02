---
name: "rar-cowork-cookbook-d365-project-to-profit"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Project to profit end-to-end process - covers 6 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_project_to_profit", "rar_sha256": "1383c80478ee8daf498233059d1c5812613c320a8c19b722332d1d0704c771b5", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_project_to_profit_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-project-to-profit:21daf5873c02f2386f1cc7edad24e1424e4e661b11b42906ea0dc4b973edc31a", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "project_to_profit", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_project_to_profit`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_project_to_profit_agent.py` is
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

D365 Project to profit Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Project to profit end-to-end process - covers 6 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-project-to-profit
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_project_to_profit_agent.py` and embedded as the fenced Python below (sha256 1383c80478ee8daf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_project_to_profit_agent.py` first:

```bash
python3 d365_project_to_profit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_project_to_profit_agent.py   # or on stdin
python3 d365_project_to_profit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Project to profit Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Project to profit end-to-end process - covers 6 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-project-to-profit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_project_to_profit',
    "version": '2.0.0',
    "display_name": 'D365 Project to profit Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Project to profit end-to-end process - covers 6 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'project_to_profit', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-project-to-profit',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-project-to-profit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b426d18ecbd2b523',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['project-to-profit'], 'process_tags': ['project-to-profit'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'project-to-profit/d365-project-to-profit', 'uses_skills': {'custom': ['d365-project-to-profit'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365ProjectToProfit(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ProjectToProfit'
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
    print(D365ProjectToProfit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
