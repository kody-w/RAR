---
name: "rar-cowork-cookbook-d365-design-to-retire"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Design to retire end-to-end process - covers 5 L2 areas and 31 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_design_to_retire", "rar_sha256": "759d54c6281ade5053813b54ac0d6e6029d651531b7903109412effd552e6bde", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_design_to_retire`. The original RAPP
agent is preserved byte-for-byte in `d365_design_to_retire_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_design_to_retire_agent.py` and embedded as the fenced Python below (sha256 759d54c6281ade50…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_design_to_retire_agent.py` first:

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
    "version": '2.0.1',
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
