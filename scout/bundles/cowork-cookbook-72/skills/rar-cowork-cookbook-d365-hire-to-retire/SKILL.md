---
name: "rar-cowork-cookbook-d365-hire-to-retire"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Hire to retire end-to-end process - covers 8 L2 areas and 55 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_hire_to_retire", "rar_sha256": "6b48620a01a9d010f1a8118440b0516d9a92220587de40f019db3c1b37346abb", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_hire_to_retire`. The original RAPP
agent is preserved byte-for-byte in `d365_hire_to_retire_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_hire_to_retire_agent.py` and embedded as the fenced Python below (sha256 6b48620a01a9d010…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_hire_to_retire_agent.py` first:

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
    "version": '2.0.1',
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
