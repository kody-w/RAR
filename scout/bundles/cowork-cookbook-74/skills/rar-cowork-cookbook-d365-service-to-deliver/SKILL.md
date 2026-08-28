---
name: "rar-cowork-cookbook-d365-service-to-deliver"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Service to deliver end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_service_to_deliver", "rar_sha256": "e8e6ca1940488fb9c26e2687fd61f7cba46981c7eec5ab615d77882f359c68a1", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_service_to_deliver`. The original RAPP
agent is preserved byte-for-byte in `d365_service_to_deliver_agent.py` and in the RCI capsule.

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

D365 Service to deliver Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Service to deliver end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-service-to-deliver
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_service_to_deliver_agent.py` and embedded as the fenced Python below (sha256 e8e6ca1940488fb9…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_service_to_deliver_agent.py` first:

```bash
python3 d365_service_to_deliver_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_service_to_deliver_agent.py   # or on stdin
python3 d365_service_to_deliver_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Service to deliver Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Service to deliver end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-service-to-deliver
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_service_to_deliver',
    "version": '2.0.1',
    "display_name": 'D365 Service to deliver Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Service to deliver end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'service_to_deliver', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-service-to-deliver',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-service-to-deliver',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd8f32c481828d42f',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['service-to-deliver'], 'process_tags': ['service-to-deliver'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'service-to-deliver/d365-service-to-deliver', 'uses_skills': {'custom': ['d365-service-to-deliver'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365ServiceToDeliver(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ServiceToDeliver'
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
    print(D365ServiceToDeliver().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
