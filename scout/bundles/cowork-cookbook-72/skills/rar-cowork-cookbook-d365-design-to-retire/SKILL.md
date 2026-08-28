---
name: "rar-cowork-cookbook-d365-design-to-retire"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Design to retire end-to-end process - covers 5 L2 areas and 31 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_design_to_retire", "rar_sha256": "85da9c25c268510c497787dc947417a6833e04b2e2b592131ab8466bbbf8b2c7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
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
