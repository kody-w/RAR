---
name: "rar-cowork-cookbook-d365-prospect-to-quote"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Prospect to quote end-to-end process - covers 6 L2 areas and 22 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_prospect_to_quote", "rar_sha256": "69dea2746bbd3920e8b6b2b7448aa692cacf4dab7c9d0f9c019dd1b3d79f3f16", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/d365_prospect_to_quote`. The original RAPP
agent is preserved byte-for-byte in `d365_prospect_to_quote_agent.py` and in the RCI capsule.

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

D365 Prospect to quote Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Prospect to quote end-to-end process - covers 6 L2 areas and 22 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-prospect-to-quote
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `d365_prospect_to_quote_agent.py` and embedded as the fenced Python below (sha256 69dea2746bbd3920…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `d365_prospect_to_quote_agent.py` first:

```bash
python3 d365_prospect_to_quote_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 d365_prospect_to_quote_agent.py   # or on stdin
python3 d365_prospect_to_quote_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
D365 Prospect to quote Expert — A Dynamics 365 Finance & Supply Chain Management expert scoped to the Prospect to quote end-to-end process - covers 6 L2 areas and 22 L3 processes from the Microsoft Business Process Catalog.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/d365-prospect-to-quote
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/d365_prospect_to_quote',
    "version": '2.0.0',
    "display_name": 'D365 Prospect to quote Expert',
    "description": 'A Dynamics 365 Finance & Supply Chain Management expert scoped to the Prospect to quote end-to-end process - covers 6 L2 areas and 22 L3 processes from the Microsoft Business Process Catalog.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_skill', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'd365-prospect-to-quote',
        "upstream_url": 'https://coworkcookbook.com/recipes/d365-prospect-to-quote',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '6bcc88d358dc10c9',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-24', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote'], 'recipe_category': 'other', 'recipe_type': 'prompt+skill', 'upstream_path': 'prospect-to-quote/d365-prospect-to-quote', 'uses_skills': {'custom': ['d365-prospect-to-quote'], 'ootb': [], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class D365ProspectToQuote(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'D365ProspectToQuote'
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
    print(D365ProspectToQuote().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
