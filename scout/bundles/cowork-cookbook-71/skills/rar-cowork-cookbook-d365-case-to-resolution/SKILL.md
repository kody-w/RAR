---
name: "rar-cowork-cookbook-d365-case-to-resolution"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Case to resolution end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_case_to_resolution", "rar_sha256": "9c937b4b0264515e811f96196f22e326b3cf9795511e0a84931c5381509a28f7", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_case_to_resolution`. The original RAPP
agent is preserved byte-for-byte in `d365_case_to_resolution_agent.py` and in the RCI capsule.

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

D365 Case to resolution Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Case to resolution end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-case-to-resolution
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_case_to_resolution_agent.py` and embedded as the fenced Python below (sha256 9c937b4b0264515e…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_case_to_resolution_agent.py` first:

```bash
python3 d365_case_to_resolution_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_case_to_resolution_agent.py   # or on stdin
python3 d365_case_to_resolution_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Case to resolution Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Case to resolution end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-case-to-resolution
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_case_to_resolution',
    "version": '2.0.0',
    "display_name": 'D365 Case to resolution Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Case to resolution end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-case-to-resolution',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-case-to-resolution',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6c365a36303644e3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'case-to-resolution/d365-case-to-resolution', 'uses_skills': {'custom': ['d365-case-to-resolution'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365CaseToResolution(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365CaseToResolution'
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
    print(D365CaseToResolution().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
