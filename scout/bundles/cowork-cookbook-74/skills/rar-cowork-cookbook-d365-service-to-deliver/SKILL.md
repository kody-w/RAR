---
name: "rar-cowork-cookbook-d365-service-to-deliver"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Service to deliver end-to-end process - covers 5 L2 areas and 37 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_service_to_deliver", "rar_sha256": "c8140c41fa4d2f40767dbae313c474cd567b3cedfe9798cb9b0e00ace9ea9193", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "service_to_deliver", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_service_to_deliver_agent.py` and embedded as the fenced Python below (sha256 c8140c41fa4d2f40…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_service_to_deliver_agent.py` first:

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
    "version": '2.0.0',
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
