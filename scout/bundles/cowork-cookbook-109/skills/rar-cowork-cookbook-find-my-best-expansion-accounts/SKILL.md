---
name: "rar-cowork-cookbook-find-my-best-expansion-accounts"
description: "Surface the accounts most likely to grow - and arrive at each one with the expansion case already built."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/find_my_best_expansion_accounts", "rar_sha256": "173643220b7c6bb75a7e6e15a60d7c7d621a4669c4c9c907769e2f2c97cc3e67", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/find_my_best_expansion_accounts`. The original RAPP
agent is preserved byte-for-byte in `find_my_best_expansion_accounts_agent.py` and in the RCI capsule.

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

Find my best expansion accounts — Surface the accounts most likely to grow - and arrive at each one with the expansion case already built.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/find-my-best-expansion-accounts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `find_my_best_expansion_accounts_agent.py` and embedded as the fenced Python below (sha256 173643220b7c6bb7…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `find_my_best_expansion_accounts_agent.py` first:

```bash
python3 find_my_best_expansion_accounts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 find_my_best_expansion_accounts_agent.py   # or on stdin
python3 find_my_best_expansion_accounts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Find my best expansion accounts — Surface the accounts most likely to grow - and arrive at each one with the expansion case already built.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/find-my-best-expansion-accounts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/find_my_best_expansion_accounts',
    "version": '2.0.0',
    "display_name": 'Find my best expansion accounts',
    "description": 'Surface the accounts most likely to grow - and arrive at each one with the expansion case already built.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_sales'],
    "category": 'integrations',
    "quality_tier": 'community',
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cowork-cookbook',
        "source_name": 'Cowork Cookbook',
        "source_url": 'https://coworkcookbook.com/',
        "upstream_slug": 'find-my-best-expansion-accounts',
        "upstream_url": 'https://coworkcookbook.com/recipes/find-my-best-expansion-accounts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'c9d998441be5b302',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/estimate-and-quote-sales/conduct-upsell-cross-sell-or-repeat-sale-prompt'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/find-my-best-expansion-accounts', 'uses_skills': {'custom': [], 'ootb': ['Communications'], 'plugin': []}, 'verification_status': 'draft'},
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


class FindMyBestExpansionAccounts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'FindMyBestExpansionAccounts'
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
    print(FindMyBestExpansionAccounts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
