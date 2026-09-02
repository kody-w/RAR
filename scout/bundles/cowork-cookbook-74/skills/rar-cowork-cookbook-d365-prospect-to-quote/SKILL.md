---
name: "rar-cowork-cookbook-d365-prospect-to-quote"
description: "A Dynamics 365 Finance & Supply Chain Management expert scoped to the Prospect to quote end-to-end process - covers 6 L2 areas and 22 L3 processes from the Microsoft Business Process Catalog."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/d365_prospect_to_quote", "rar_sha256": "69dea2746bbd3920e8b6b2b7448aa692cacf4dab7c9d0f9c019dd1b3d79f3f16", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "d365_prospect_to_quote_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/d365-prospect-to-quote:a52abd47fb75adf8213c4c0c30a7862bcac39084f04985413769b1f39b5b1da8", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_skill", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/d365_prospect_to_quote`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `d365_prospect_to_quote_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

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
