---
name: "rar-cowork-cookbook-teams-update-define-integration-strategy"
description: "Summarizes the current state of define integration strategy from Dynamics 365 F&SCM for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON file for review; does not post anything."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_integration_strategy", "rar_sha256": "61d15394933902260ea8879fb9cb5e549bd78e805725fb41cce17de476f69446", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_integration_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_integration_strategy_agent.py` and in the RCI capsule.

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

Define integration strategy Teams Channel Update — Summarizes the current state of define integration strategy from Dynamics 365 F&SCM for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON file for review; does not post anything.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-integration-strategy
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
    "card_filename": {
      "description": "Output filename for the Adaptive Card JSON, e.g. teams-update-define-integration-strategy-2026-05-24-card.json.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "legal_entity": {
      "description": "D365 legal entity to report on, e.g. USMF.",
      "type": "string"
    },
    "operation": {
      "description": "What to do: run, prompt, plan, checklist, describe.",
      "enum": [
        "run",
        "prompt",
        "plan",
        "checklist",
        "describe"
      ],
      "type": "string"
    },
    "topic": {
      "description": "Initiative or workstream to summarize, e.g. define integration strategy.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_integration_strategy_agent.py` and embedded as the fenced Python below (sha256 61d1539493390226…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_integration_strategy_agent.py` first:

```bash
python3 teams_update_define_integration_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_integration_strategy_agent.py   # or on stdin
python3 teams_update_define_integration_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define integration strategy Teams Channel Update — Summarizes the current state of define integration strategy from Dynamics 365 F&SCM for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON file for review; does not post anything.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

This entry carries the upstream recipe itself, under its licence and with
attribution: the prompt verbatim, the prerequisites, the step-by-step and
the expected output. Toasting made it deterministic — the same call returns
the same recipe every time — and callable from any Brainstem. The upstream
library remains the authority for the recipe and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-integration-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_integration_strategy',
    "version": '3.0.3',
    "display_name": 'Define integration strategy Teams Channel Update',
    "description": 'Summarizes the current state of define integration strategy from Dynamics 365 F&SCM for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON file for review; does not post anything.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-define-integration-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-integration-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a418da66cfe0f73a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/implement-solutions/define-integration-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-define-integration-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Dynamics 365 F&SCM access with the appropriate role', 'Prerequisite: Cowork D365 ERP plugin enabled', 'Output matches: See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.'], 'confidence': 1.0, 'deliverable': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'card_filename': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-integration-strategy-2026-05-24-card.json.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'legal_entity': 'D365 legal entity to report on, e.g. USMF.', 'topic': 'Initiative or workstream to summarize, e.g. define integration strategy.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': "Replaces 'check the spreadsheet' Teams pings with a glanceable card the team can act on directly - reducing back-and-forth and decision latency.", 'expected_output': 'See the prompt for the specific deliverable(s). All generated files land in `Documents/Cowork/output/` in OneDrive.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Dynamics 365 F&SCM access with the appropriate role', 'Cowork D365 ERP plugin enabled'], 'prompt': "Using the Dynamics 365 ERP plugin against legal entity USMF, summarize the current state of define integration strategy. Produce: (a) a Communications-ready Teams channel post (markdown) with a 2-sentence summary and 3 bullet highlights; (b) an Adaptive Card JSON 'teams-update-define-integration-strategy-2026-05-24-card.json' showing KPIs, status indicators, and quick-action buttons (e.g., 'View detail', 'Open in D365'). Do not post the card on my behalf - save the artifacts for me to review.", 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'Reads define integration strategy, produces a Communications-ready Teams post + an Adaptive Card with quick-action buttons.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Summarizes the current state of define integration strategy from Dynamics 365 F&SCM for a legal entity and saves a Teams-ready markdown post plus an Adaptive Card JSON file for review; does not post anything.', 'example_request': "Draft a Teams update on our define integration strategy status for USMF with an Adaptive Card — don't post it, just save it.", 'inputs': [{'description': 'D365 legal entity to report on, e.g. USMF.', 'name': 'legal_entity'}, {'description': 'Initiative or workstream to summarize, e.g. define integration strategy.', 'name': 'topic'}, {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-integration-strategy-2026-05-24-card.json.', 'name': 'card_filename'}], 'model': 'claude-opus-5', 'when_to_use': 'Call when a user wants a drafted Teams channel update with an Adaptive Card on define integration strategy status from D365 ERP data, saved for manual review.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and confirm the Dynamics 365 ERP plugin is toggled on for your session.', 'Paste the prompt from `prompt.md` into a new task.', 'Review the generated output and adjust scope as needed.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class TeamsUpdateDefineIntegrationStrategy(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineIntegrationStrategy'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'card_filename': {'description': 'Output filename for the Adaptive Card JSON, e.g. teams-update-define-integration-strategy-2026-05-24-card.json.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'legal_entity': {'description': 'D365 legal entity to report on, e.g. USMF.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'topic': {'description': 'Initiative or workstream to summarize, e.g. define integration strategy.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
    print(TeamsUpdateDefineIntegrationStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/916a9OiWLbmX3HeEzFVdcxMuaPZcSIGAUVAkJsolR1Z3O93ELBO/ffZqHmp7uye7on5NFZUqrD32uv6PGu9+Pub3XdR2bx9fNN8u1js7SyLI79Z2IW3oMuhbFLwVqYO+H/hlkXXxE7flU379u7N81u3iasuLot5e5/ndhPf/XbRRf7C7ZvGL7pF29mdvyiDhecHceEv4qLzw8aeN4F74IMfTougKfMFMxV2HrvtAiXwxe5/avRxEZRAkUXmh3a2AMLibnro1do3cIq90H07b983vu1NC3B26pVDsajKtltUWQ8WFAvKs4F+N39B24234DVZWgRx5j8EN/4t9oe/LLwSCCvK7rnTLqYuiovwAzDQH+28yvz27eOvf333FoPPbx9/f3MzuwWX3h6nG5UHTGAeth2+maa9LANCMrsIweoKiAV+evdW+Q04PQeXgEcWr28/t34WvFv853+mg92E7S8fPxWL1+vT2/yf2hcPt3al3Xa+t3DtynbiDHjkw4LKBntqgT1d3xSzX4BfZwueO79JKqvFf833fn4e8iH0u58/vZVAhYfOn95+WQC3fHpr+vnzh1lK9fMvH7Jy8Juff/kmp+2dxHe7WRjQ+sPn1/eXWLDw29I4WHzWTiz9Oqvx3bjygfDv7JtfT9Vf4l4u+fxc/HNZvVv8WPJsz38BfZ956AC5PxYLfAB2vn1Iyrj4+XVGU978wi5c/+df/pFYN/LdNIvb7l+S++tTcASSEXjr5ZJf3j3C99fF8mXbV5n/+NgKJMy/YwlY/uW4r476R7Ifkf0b0RnI3PZrLH8o7kcblv+1+PUf2vbPNrxbBJ/eGD8DVdnYTuZ/XPz+SJFff/K+Xfzpr38A0f9HMVrZN+5DwufcLuLAb7vPn3/9qX1c/umvv/7UVyCLQZ1+7pvsRzJ/5NfHOX/y4GvVz3/eC843irSYMedrDS1+L6v/0fzxYXG2s9j7dr39uPi+EufXcjEb8eXQpwu+q8YW6PqdH395+wMgUAGs6d3HbYAf//Efi2PsNmVbBt1Cc8u+W4AAd3Huz8rrUdwu4icYA6jzmzYGjn2tA/k/R3jWGEDzb//LfSD9e/eF9KtuxrbP/QPcPj+R+/N3yP35C3L/9mGhA/llE4dxAUBapU6nT4UdzsgPzq4av/WbG8ArZ+r896Cs388fAAksfvtXj/j8kPahmn57YH/8xEGVPswY2PaZ/2G21oz84mWbC3DfH323BwdlpQu0miG/fQe80JYZ4IJu9kybxlm28GKAMoDOnrwCvPdxFvbbb785dht9Kp6gjS6ePNeuwIKv6izevwfmBVkcRt2nwnejcvHT73/8tPjvxT/b9RA+n3ECJPKKDdDwwUyg1vocLANhA4EGQPKIze9/vJwMxBSAmEEk4yB+sSzI1dT3vnhc46j3CE4sHB94Gng5r8qmA0ywiLsPi0Ow+KovOHS+NXNFNJOe51d+4fmFOwGpNjDnqydnXmxBQNpgerfoW/9x6m9OYz9UzEHR291viyN9AsxUZuCfWc1nA2AXZRED93/Nh+d1IKT5qV1sv4j4sJDm7FxUdmNXUWO/zgjsZ1zmDuC1HQi3F4U/fCpmKvZnVz1S5ekesAh4xn2F9P2D5t0S9CSF1345+7HGnvlTf/Bo86loX2VgN3MoXEAL4NCwj72ZHP7ySqk2KvvMe/gPaDpLekXBe0XlkYPMP+lwHs3Cgo6AR/1s8ewaFp96BIKxxf9vndPsC2q/V9k9pbPMgpV09fqM0dxAzqY9e85ZqVncox6/NTRfQOsLdn8qshgkXDP95bnyocZrzRMP+wYEQqXUh3yQViBGs9xH1s9Z3DRzvdifii8k8Q644IGIwJUAIkAJzZn75cD57hdNI4AD8/dvDcMjS4BLgDtBZi+q3slA1gW+7zm2mwKtZq9+CS0ogUcIhyh2oz9ZNUcFZBqQvwBKxKAWQQg+fAXu590vqv9p47Mvmrc8esYeFG7zEAD08GcF50APcQfwy+6e/Tqw8+NDCDAjr7rZdgckErD0edFv/LqP27ibYfLpV78CUP1+fn9aOl/1xwpUC3AWqImqB959VNEMMDnoeoAOIFVBUeVxAboA4JSXEx4C7XyGBAC5rzb1KfFx+WWQ/yi9mb6+bJwNmffMHcEz00GOfY8c+o/SBMjL5xWPc/82076eNsue0bMFCJj7X+8+W4cPT/Z/theLL3I//t1A9PO/NzM9+Nz4cwJ8XERdV7UfV6snB3+h4A8Au1ZPXdsnHb9/cuX7Jxy8/w4O3n+Bgz/Jf5r+cfHv6fgnEa8a+biAP0AfoPmW+Mqx1wu4hH6/vb7H5rufCtX/hrDg+DIH6s0BnAD/f6XDL0sAJ4YNACiw+EmP7cyqAyDyBx+AaHwqvk/6uegA3RThnKRt+R0YPPoCUADP4H2lLXCr6MDZ3txVhv480T1KpPXfPhZ9lr17A7Dp/+uT3MxQ+Zzg7TwGglICvVoX+49voFK9z7MyT5G//81wLD8KZvFlwdd0+3uUfbfwP4QfFv9qxN8jEEK8h/D3CPZ+1uFD0gJCBMp2UzWb9hwF5+bxgWhj9wPdHh/s7MOC8QF6Zu33ZfJivpn5v6vmZzRAFFzgg3eLWcl2Zmpg3+yeGQnsFpQWMPOHujx46fOTl/5eIWamsT9R19xWPDoWgJUvBxnacfdD2V876L8XbIJmZZbllR9n3n73gkPwDqaed4uvAwyw6DVSPv4KUPRgWv91Hp7mJHhsmT+APeDt66avfxBx/Le//kCvrqxi9+91OhRxF9uPHAAOnOvylfFAz/ZLY/Cy+Z80Aj9wBTjzAeuAHGf1v/nlm3blY86btQPWdM8/S/z+BnLcBiG1X1n+GhTAcoCC79u5IVoBPAAHgu/PygX3/q9HiJecNrJB6woEEbAH4+gG26DoBkIQAvLt9ZrcBM7GdXAfxzaOR679NYSTCB44GOy6Pkx6PkYSAbHBMALIe+LA57n7i2fdZsWAS94Dx/rfboNL3suopxGzx75OLLPxL9t+f3MIDKzksPZAPV/0agM7K1R0xuayLKDluMOharJslmM6Xl7pcOHFWhHsN50vjwWnTELo+VTaaqwShiZLTfVmd+QI/oTQQeWtyT4MqYPR8HeIcMaJPmoIA5Ob23197/IzjubMkTSPxnSJu53WKJU1ZmHlYaVkO65B8jpoVgU8y+uKDfiO8+n7cu34q3gl1S2+2612fqY6mXmoJ0GpjYzvBMqh8/gAaRfVuarWpjOcnldiyAuCeOevTs56w5+vVmkqh4xtciVU4nXfpfs07cQ7LXTicIwRIxGvtA1v9sjFqNfpdDmk65phkx0EJbl1mbJRSNvDbb/CN8v1rm0xw5gwY+ePfYG1ZXhnoXqAjohJiJ439rcDFxLg/BWKLD3vhN6hFbveBDf0Rt60lQ+514mkKCeFTfweVnF8jaIksqO7bMR6H1mOoCq4Fyb9dkjXtqCMgT3u3XCN0OzVOJyzsx0dbhxKZG0m0kIVtgVXxbib0Vtvp+9a39krtogbPb9JlplWQrHO8UN6O4qNRMiXplnuRvFmOzff2nn1WctLV5SH4R6HdMj5O6xLk9DQCDOOlOE2qEc+25m2FecNWZRetLyZQRo6o2WV9J1SslUEFwafkkiE4hWa9LohCWsfL8O0Ng2czQy7xuQsVNRdU0lk0++Gk7VLzbV9iGU8HZmAXk3Gzd5QohlOiB0RlXKC7TFJ+4yHbV+oQLCyE3E/92m0rJimPWhKW9fHeh3CnG/B9MVgxJ6Pt8urReSCbt33/vY+kVV+RVkmOaYFJV80g0i5DbzHd6G97yj2tKexaLWP1xdrf07hhCrX9kRpLaeMVaTAU0XZ0JHxj3l/8YyG9dNUj5ewuXeds7M6m2eTpZvDBauGFZ16MJ8Sd4KYsFFYAUThVtdC67GtGoTkBmNcVh99TDlGrRnsnPJoRktk42C6cBePnX9PcVnhMQspok2ejyemZrAK0dZNEsI6tgr0qNucCm+NTlbX3dc653pxepXgiE/IO7cKT2vZOsG1056wJPFOTbtcgqGMybAavgp67PB8s4W6cFdUot+Z+2nHlC0mrkx+P4oH2K4o9siHwUEJO35zw9QzlhhnnsbkPLKkW6TEinDn+UI/u0VjMXCOQ9tU4gUQ3htbieIWiozIaAiJZ9gtxoaXE3LYbk/jEaGknqtcCk7WpkMLiObreO6xy/s1xxM0FljBwbxgH8DH4iocjVBIsiNV8mZY8petsD9X9LkaWWJk2WUbbhJE8Hj04PQHYyllheHxitrCaALj1yXK2NIlOMqndT2hwag1iZpfhnsiCfWAIUjYYjqDFVQclZ2gTJW9xWL5cCH143gsibOk44HqqbFD1dqhbCdGRJyk2ho5jAhh6RQTatT2LVXPHSWx+7qNOXfdudpJPMUx3DX3fWHdSE7LDghzrK4twBaesc5x7PUUFdyUPqOqsw9NaNZxYkY7acRY2y1BFvAOLogpZUo5UTrC66PbyLdEGxTxzYUJRdWZ5bpBjW3gtsdQdEXAOD1dJptcwizNREB2yjwLtYU2xuP5etXr3RazLwcaTUZp6545VjM04RgXkbXsLBVxg+2N27nXYYS5I3f3IDPjmw61ikFRIUsRfdcjy82dBD1VaRHq2eKUgZbG/l7wkxYommPGfuBKeAOzZEaSV1Tak3dBMo+X7e2eH9KrgbSFON6W7ga6xhfX2uQUBYP80oVSbaUI9pitvEf5xCVb6tzIOnS+k9jFZLXjZleafB+JdKwcHVZhkMMgXY5hLDXSRdys8G3I27igpAbvq3d466yYU6VEBC1bTTVLTSwdyZozrynsSIWqSsUax6bnjFUiNu8imFvLCDRFqhUarHO4eM1dEq72xYVbMvWxUNMTXVk6dLQez2Yz2q2NQYdePGzXsgY80xbxpDrFlhLkW6FPoBSb9TIwllS1O/B1wtHYStdqjtKzaLpLUtEafj6oXQwwn0tWWwwtvU0/hKjVHq6yVqArZISi5dI0sTO1NAM0TJszamlnzGuLIo/wQ0cLrNTWxpXa4/7EKk3cMKMb5dz5Kh5kqT2NQ2Gcpa6gBDzHEjOUPbwV2vokx4y8X2rKDb6OjN0xm1GLfKiOkEk5TNF5mxp7VVmXXb9WBtGRK22438csEhTM54pWc0471qH3Qd1Wx6XsO6wLX3vznIRuGw8s0u/7icuk2CtsREOQm3Q3bbI66xtnM6zrg5BGKgpZ/JB1m/31qhQXy2ojEJMhqsPLbbXR0laiMjnZtYAIukp20gBl7xm9B8V82GVbjYqmcLge9ZYgY8KJg5g+5FfzhI399bbndtp+LHB6u7JS00z9ixtlhHtfS/DkUxJxVpjQQc/BlKmHw07ZXm+HULwYOIMIV55JNqZw0EqST5V9I6a7yIj3+vam9TuxxkEZnGL80rbaJIwQa7rnlJCpVMT28knEJJ8efTrVTPsSIZ3ArBMx7ZNRpsREnqZaOKJc7EoaL1NrdTnSon7c1fTy3niWNRiH4+o67MTYPPpDEHmDAyttrLq9QJd3ywo30DiIg77y+4pVljrduSjUOcO1IhHBNmNE3OYHOcOkeNBcJ/QZ6prIvkBULAvzkEKh1I0wdvYZU8ulD1XydhlRdcVvL+ZZyYjibN6Ap3N+fdmaoMXPFaO12qFeHk1yB3D6VI5EGauANvgTe2e3RS4x+3q9h24r+xCdDvAWgoTVJkOweNvEJ4RXRq7ydK9BlNiLz2Yc97emOZY9Ci1LZcfxSRR5OSLimJBDRpxyx/OmQruIafQkuN4dfqKNglnit6KKTH8PmjLOEPkk4OusFu82oF6eIfNEsU+maaqNY4Xpsah7hadtUBFFgvLno9E6cNgLoUq3xnm5rZp4SVv9+oRQfc0fnCk8XKHUgPMlF5Xh0OpWtIHWydSSpK2WVyOD4B4nrS0Trpl7fZ7qK7NlSQhh/TazID1Zei06pACDeMSVanFExyQMd+W1kCPrpheOX6ck01LWjq1CU8nODaOuqmOgcMmYV0hP38emz0lxdbuvxKEsp0i84stWpzL+hG5OtnPmoXMpn+/LgyqKuQSaHiWgmEpIxT6LslFc+S1eTnfKvxrMaUr5WMg8l2a1SjRiFlOgpiIwaIdeA7oUK1rTrzzVU7mwKw4DYrmXG9eZJFJvaB4ScQFeuRIJS9wdx5byBRpU0EfgQIuzuZeaIaKhEfM0cmf5gnjEJDQnoeIqYgKv4JMlQfZxZejtXjnUxsCuFToQrtFGFrW8qBojwytkMLpxb2J3jkA5r4vru8rZdEBFZLTb4yq89FdkvXXXPWt4TH67aq4y7vX+EDKYTDigaXRkmKA5B0ktYqvjxblX8WrY6JVaLzutQs/nLrDOd6ESTzTX9nv63BXmSoitUvKEzDg5yzXIAmK6aM1OqNkmg2O6GsztgFXQxFmHdYZTZQRJ9TaFokQIBcGylAt6FWwcprNUOXhRv3U3p/V4cTT32B7QnUGFOhcGhJz0vHoQt6MUy8MyuQp7PFjymA9AgQmCXmugDQHlkypUcF5L/kXc6V6PJBa/1QsbDEj7jVCt7N2ZarDb7lDeMN3Rx6qHub2Xio60PO2hNoLrowMaLFzubIHmd5rJbU6eH+pKpmyt+GKuzTjALsuGuzbKlVtGBXPZaOw20ywxzLWADHLccxNV6McjliARt7ZNYbwag3lnKJPkjayLqz0unJTpAuaTyM4BiKbZ7rjicwNm8j2YkfK+Xzsa31lbqznurrubaFHZqbwS/vHaxwnvXaP1UW4bnxc8rbwCALtWmZSAeWeby4IrKC4mVsk23WHHrO/Y9tJAgFUauqRiXQUsdtvsocNdvLpJeAr84MSi0KVnrsL50PqutrZ2xc00ZN9r5A0ynB2y5E4EdT1arKmopn62lTidOtEukHMtCH24I3n0eoXh3uslrx98iBjkkJIrHstOl07E/PranwUydOEz6G7OgNtvYNw+6s75tJzIJdRWaivTR4qKHFVpdiZhFqBHbOBRHaPamprkth/gTTbiYdwLqiDXNFXvohsapWd7j3fXYDLIw+ZIbkKz0W7aEGmQI+mlmybW6XBYi7o0yiq3h9s4wSphw6d4FEuV0Y5gCN0NmgfRxVYxsaFHlNVlI65LeMdcxdJcokEotq6BQEefbeXEqGjeQQHuwbXdDUzkcaRxr01cJmB+T+1lNzcI2O0JdbdFsoI1U2K1V5mhP7hd6/lYzSZnCFOkUVUPezwzUSZJ3eNt2fjHMysYuwmbYCvpB4BxQbmJb0eGaewby0C7WJkOl3O15uzClLw9gV24A67q8JYcJH1qGPxu5Y6M7Mj+zEm9pJ/sXTAhoFldM4h61JGddl4Cmtg1LRNTRKAiQTKOJDKY0ial75JOrxl0xQw2tx8MpGl8Whb9dsf36KUwThzecaUa3LIb0989F8wIXoTBOMpFauPRHt0d8DtxOl9uHgUYy7I3U4AdqDoGBAzxoI/GN1B7UAhsd72UJikKZFzQwWAtcaW/R1V2hFatvoZIibp4HGoE63t3Ganjsco9ppwQC92WtGbHYiOMG7xNzKXm76ru1Bgr6CjHAgqv4PhuXQIfGQmmu5oouyUFGBNrH8IjvF+dlnQrcVdyfTYPU9JNJ8bfM2S7WmHLzWo4bK715GbmXQpWMb/Z70UDHzjLE4lN1nqC5LKlH9Q5cpaR44lpzfDYJQNrBLooeyecVX0elkXdTVi2jzqejcj8hNG0zlnbvS+tLL5YZSXKl6a4Ro+IRQh3zSjWqKP4XiIwSEdd6cQgj92E5rTsjthodcQAobdVYTrxWKixvM7GIG33aeyX5onkCIIgN9KQ6tXpbqIhrZNdd8x1Bo53PAab29VpZC/HO1ntV+RAXHF8DReXC6e2tHdSBSQJ3EJdFju7tjZgGrw6t/Zeea1ySEO2SkP3dFtd9hcvt9YKNBrKtrYJmDOpHAbTPcCuHG5qxMRXHS35skvH00Yxj6SVq+QJsc8ocrSS4b6Gj5PvX05GqnqijoUOeYjP6p4T0yo8Mem4Upa+YZyNkpVDa1jpsQn4kJUEyNtLd78l50HAQkukFXQwMZihXtwNJOHRIdCgJAb8gihL9+RHIeEA/th7/CnIxI3PAILxlyTennZH9uKqtdViJ5c0oEG5nYlYumxu7FHGCw/LOU+KguwmV6ponKGjffQCn90wcsXFNHHJMUGI+qEdd3c/yi6nq8uwd6i6nXLIsi5LxhrwbkefpDq8W2SD2EuHAImXjr15k/e6pR5Y04NgNQtFnAtRJ0waAaNJbB3Lo3xB+wIAOB3wLlwnPipHR9qF8RRBIoSHt0e7mtQuK/wY5H3a1ZfD1Y5Gpy0iQuAz4nQRuURCqWtYM05Jnfa3dr+1qFWfrNLjparp68SFq97l1Y3hwMfD6rKFYzyP1NuVgkbSG1hhv1k6cAPwue4LyV+nnIUWDgDxpECuIK56j4N1B7ewegdGG3hwapOcRsEWMdk+rh2O4edea32TD6CbGhpH3sQ0UsBQaY22xxEXLgouEh/0rNLjk4BhVUvZa0bXN601YbA1NvClU7HBbhJTdvZHQvEHvLEgqCm2qJhBwbjj+rpNOB7NOWU3aW4ZtzxUwNHt3I+FyVx3em7cTw0aeerqxA8gQYb6rMiT44eCdFhq3vo0tObOIiIlYZbUjmnqFZtTpWHLnhhQBbVOY62pL4y2oSDX1bilObrWOUxXgu56rNeg8pq7XkSq1TMf3laHG78S+k3cwNpN9DknPEDeKBVYibOabBAW5zJBHZJIJCWbjazuzcvNzhhi7UMBt773iWh3d2EtaOHGRDqnb29D4thrSghuZsxtUSenU587OZ0AAQ+Nt8ZRuytBmkujqzPvMJly62dJPonYSmoYs7R1MXG9FT3IW79A0rueoMUSH9Om8EtGvaz1y36UkWx39TRlMjgMWdNLx986HEVvbqAPqZiNRDEmdKKVHYmndILVRC+pqGKSjZK2HKbma3cdVQXNogds4yFBZeIYvTahFary6X0ZHUu7EU9rAQaDqXgrmgszFhs5d9IcUvbA/oN0EJGL7FO6GtqSgWnkhlxBq3TgmJNWWBeVJAfLELOmYLmb48TkWXYh4tbdNZ8oQaOjb7F1R/Q+YSESm93Pxfmk6mRa4wmYX+GDVMgtxzATT8FY2UeeY1gBkiLo0pHjTbIeBNXZEEzWaUsFZVeDiYssQLHtkOt7tfPxqOBP+bK/82QChrMISjB16zRpEBrxgMasKlHLIBlaiukg+yStC4TUQF9osRau3/fKMsBQHdu366MFIygxoKCP3XLt+qxspnApgopuXf5UE/GJhTeERfbNqQHpjOY3MiQ3nYnZqHwR0U3q0MyFkAbHvdWo0i+Zbc/lQbhPi4Ss4cultoxiZ0gEutMtZ3UeOC/QfF2Wyk2EL+HWIO55Y9DogCJ40597DG5c4ggqfNRWRxdqaMhvIab1yJUTIhziiVx78yOxW/s9frbJGw7Qt0qSLYO7Hq2UFGc0xdqqwjqnBOZ+Vi06sCQP8gvmVtaYRcL1kB64pN+CpkK529takQSmxgL4sKRowUGc/ILSO7dj/dvtzjlJQZOrDF1dE6jcbJkAZU69d+jAoIfLQuqWnH0f/Zs7yfx1IsdThKduBbPnozzItpuHGEpsGrLyVsFYjLbB9MMud1c1dV3WvDTmqWIKl/EC5TJZXLqrPJHGbn/btApGXpJBJy8D5nW0ElLU27u3b09J3/7t34DNT2/+nz0oej7v+fK7jscjPt/2Pj7O+vjvq/bXd2+NGwPFng/H2qwPX4+X/ubR2Pt/9eHuLGV6/szqy8Pb53Przg7nHyW/xYXXg8XT57bMHr/yADsAns0/YGzn37i64P37Z5bfGwW+2t7zpxp+87krPz8fEM7XZ12a3Pfib19fqs0POV8/NvqMEvhnv6lmu1+/EwDmoh+gD+jbH/8bcsAH2VcuAAA= -->
