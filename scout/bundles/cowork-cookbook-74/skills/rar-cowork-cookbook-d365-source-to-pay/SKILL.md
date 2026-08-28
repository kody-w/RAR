---
name: "rar-cowork-cookbook-d365-source-to-pay"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Source to pay end-to-end process - covers 6 L2 areas and 42 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_source_to_pay", "rar_sha256": "3fd89b6e077f77ccffc0bd7908a04c6a6d31944807a03f8a7588656ccff3f6a8", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_source_to_pay_agent.py` and embedded as the fenced Python below (sha256 3fd89b6e077f77cc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_source_to_pay_agent.py` first:

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
    "version": '2.0.0',
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
