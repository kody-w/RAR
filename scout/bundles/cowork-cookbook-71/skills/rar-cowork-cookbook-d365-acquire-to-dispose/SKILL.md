---
name: "rar-cowork-cookbook-d365-acquire-to-dispose"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Acquire to dispose end-to-end process - covers 6 L2 areas and 43 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_acquire_to_dispose", "rar_sha256": "c12fa47287fb4511c647cfc873118d8f03d95526d0e6f5302836de219278dffe", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_acquire_to_dispose`. The original RAPP
agent is preserved byte-for-byte in `d365_acquire_to_dispose_agent.py` and in the RCI capsule.

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

D365 Acquire to dispose Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Acquire to dispose end-to-end process - covers 6 L2 areas and 43 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_acquire_to_dispose_agent.py` and embedded as the fenced Python below (sha256 c12fa47287fb4511…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_acquire_to_dispose_agent.py` first:

```bash
python3 d365_acquire_to_dispose_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_acquire_to_dispose_agent.py   # or on stdin
python3 d365_acquire_to_dispose_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Acquire to dispose Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Acquire to dispose end-to-end process - covers 6 L2 areas and 43 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-acquire-to-dispose
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_acquire_to_dispose',
    "version": '2.0.0',
    "display_name": 'D365 Acquire to dispose Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Acquire to dispose end-to-end process - covers 6 L2 areas and 43 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-acquire-to-dispose',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-acquire-to-dispose',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9a97a988bf83deb0',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'acquire-to-dispose/d365-acquire-to-dispose', 'uses_skills': {'custom': ['d365-acquire-to-dispose'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365AcquireToDispose(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365AcquireToDispose'
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
    print(D365AcquireToDispose().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
