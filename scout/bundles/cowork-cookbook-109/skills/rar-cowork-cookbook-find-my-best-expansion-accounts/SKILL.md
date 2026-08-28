---
name: "rar-cowork-cookbook-find-my-best-expansion-accounts"
description: "Surface the accounts most likely to grow - and arrive at each one with the expansion case already built."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/find_my_best_expansion_accounts", "rar_sha256": "c38f1cb8f7803edfe2464060feb74b81b5e3acb131af0fabf5567d541f2c161d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "intermediate", "integration", "dynamics_365_sales"]}
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `find_my_best_expansion_accounts_agent.py` and embedded as the fenced Python below (sha256 c38f1cb8f7803edf…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `find_my_best_expansion_accounts_agent.py` first:

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
    "version": '2.0.1',
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
