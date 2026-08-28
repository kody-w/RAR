---
name: "rar-cowork-cookbook-d365-source-to-pay"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Source to pay end-to-end process - covers 6 L2 areas and 42 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_source_to_pay", "rar_sha256": "f5304ef42d11beba30d4140ddc976caedb86c6b1880d3aae81f9aeb6c6d85e13", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_source_to_pay`. The original RAPP
agent is preserved byte-for-byte in `d365_source_to_pay_agent.py` and in the RCI capsule.

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

D365 Source to pay Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Source to pay end-to-end process - covers 6 L2 areas and 42 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-source-to-pay
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_source_to_pay_agent.py` and embedded as the fenced Python below (sha256 f5304ef42d11beba…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_source_to_pay_agent.py` first:

```bash
python3 d365_source_to_pay_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_source_to_pay_agent.py   # or on stdin
python3 d365_source_to_pay_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Source to pay Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Source to pay end-to-end process - covers 6 L2 areas and 42 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-source-to-pay
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_source_to_pay',
    "version": '2.0.1',
    "display_name": 'D365 Source to pay Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Source to pay end-to-end process - covers 6 L2 areas and 42 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-source-to-pay',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-source-to-pay',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'efb867aacdb1ca39',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'source-to-pay/d365-source-to-pay', 'uses_skills': {'custom': ['d365-source-to-pay'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365SourceToPay(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365SourceToPay'
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
    print(D365SourceToPay().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
