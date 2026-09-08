---
name: "rar-cowork-cookbook-partner-and-channel-activation-kit"
description: "Adapts existing launch materials into a partner and channel activation kit \u2014 partner one-pager, co-marketing talking points, FAQ, and email template in Word plus a social pack in Excel \u2014 and drafts routing emails for rev"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/partner_and_channel_activation_kit", "rar_sha256": "e0401888bfe929e84aa8ced188cd230b12d28a50e89f295b3fbc8bc4f618b637", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "read_only"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/partner_and_channel_activation_kit`. The original RAPP
agent is preserved byte-for-byte in `partner_and_channel_activation_kit_agent.py` and in the RCI capsule.

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

Partner and channel activation kit — Adapts existing launch materials into a partner and channel activation kit — partner one-pager, co-marketing talking points, FAQ, and email template in Word plus a social pack in Excel — and drafts routing emails for rev

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
  Upstream entry : https://coworkcookbook.com/recipes/partner-and-channel-activation-kit
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
    "channel_marketing_owner": {
      "description": "Person to receive the drafted channel readiness email.",
      "type": "string"
    },
    "context": {
      "description": "Optional. Details the recipe should use \u2014 the record, scope, dates or filters it asks for.",
      "type": "string"
    },
    "messaging_doc": {
      "description": "Document containing the approved messaging.",
      "type": "string"
    },
    "onedrive_folder": {
      "description": "OneDrive folder holding the latest launch materials.",
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
    "partner_marketing_owner": {
      "description": "Person to receive the drafted partner-facing review email.",
      "type": "string"
    },
    "product_or_campaign_name": {
      "description": "Name of the product or campaign being activated.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `partner_and_channel_activation_kit_agent.py` and embedded as the fenced Python below (sha256 e0401888bfe929e8…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `partner_and_channel_activation_kit_agent.py` first:

```bash
python3 partner_and_channel_activation_kit_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 partner_and_channel_activation_kit_agent.py   # or on stdin
python3 partner_and_channel_activation_kit_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Partner and channel activation kit — Adapts existing launch materials into a partner and channel activation kit — partner one-pager, co-marketing talking points, FAQ, and email template in Word plus a social pack in Excel — and drafts routing emails for rev

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
  Upstream entry : https://coworkcookbook.com/recipes/partner-and-channel-activation-kit
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/partner_and_channel_activation_kit',
    "version": '3.0.3',
    "display_name": 'Partner and channel activation kit',
    "description": 'Adapts existing launch materials into a partner and channel activation kit — partner one-pager, co-marketing talking points, FAQ, and email template in Word plus a social pack in Excel — and drafts routing emails for rev',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'intermediate', 'read_only'],
    "category": 'general',
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
        "upstream_slug": 'partner-and-channel-activation-kit',
        "upstream_url": 'https://coworkcookbook.com/recipes/partner-and-channel-activation-kit',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': "Recipe content is CC BY 4.0 (share and adapt with attribution) and code is MIT. RAR carries each recipe's prompt, prerequisites, steps and expected output verbatim with attribution, so the toasted agent runs the real recipe; bundles and screenshots stay upstream.", 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '761f62d78a320e87',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'none', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/prepare-marketing-campaigns/create-marketing-material'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/partner-and-channel-activation-kit', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Excel', 'Email', 'Communications'], 'plugin': []}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'recipe', 'checks': ['Prerequisite: Microsoft 365 Copilot licence with access to Cowork', 'Output matches: A partner-ready and channel-ready activation kit across Word and Excel, plus a routing plan so partner, field, and channel marketing can move fast.'], 'confidence': 1.0, 'deliverable': 'A partner-ready and channel-ready activation kit across Word and Excel, plus a routing plan so partner, field, and channel marketing can move fast.', 'operations': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'params': {'channel_marketing_owner': 'Person to receive the drafted channel readiness email.', 'context': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'messaging_doc': 'Document containing the approved messaging.', 'onedrive_folder': 'OneDrive folder holding the latest launch materials.', 'partner_marketing_owner': 'Person to receive the drafted partner-facing review email.', 'product_or_campaign_name': 'Name of the product or campaign being activated.'}, 'recipe': {'authors': ['Sean Galliher'], 'business_value': 'Adapt the [Product/Campaign name] launch materials for partners and channel teams and route them for review. A partner-ready and channel-ready activation kit across Word and Excel, plus a routing plan so partner, field, and channel marketing can move fast.', 'expected_output': 'A partner-ready and channel-ready activation kit across Word and Excel, plus a routing plan so partner, field, and channel marketing can move fast.', 'platform': 'Microsoft 365 Copilot Cowork', 'prerequisites': ['Microsoft 365 Copilot licence with access to Cowork'], 'prompt': '[Product/Campaign name] is moving into partner and channel activation. I need the launch materials adapted so partner marketing and the channel teams can execute without translation.\n\nSource:\n\nLatest launch materials in [OneDrive folder]\n\nApproved messaging in [Messaging doc]\n\nPrior partner-facing communications for tone reference\n\nCreate the following:\n\nPartner one-pager (Word)\n\nCo-marketing talking points (Word)\n\nPartner FAQ (Word)\n\nPartner email template (Word)\n\nChannel-ready social pack - three LinkedIn variants and two X variants with creative guidance (Excel)\n\nRoute:\n\nDraft email to [Partner marketing owner] for partner-facing review\n\nDraft email to [Channel marketing owner] for channel readiness', 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'tenant_caveat': '', 'verified_against': '', 'what_it_does': 'A partner-ready and channel-ready activation kit across Word and Excel, plus a routing plan so partner, field, and channel marketing can move fast.'}, 'refined_by': 'claude-opus-5', 'refinement': {'description': 'Adapts existing launch materials into a partner and channel activation kit — partner one-pager, co-marketing talking points, FAQ, and email template in Word plus a social pack in Excel — and drafts routing emails for rev', 'example_request': 'Adapt the Contoso Fabric launch materials into a partner and channel activation kit and route them for review.', 'inputs': [{'description': 'Name of the product or campaign being activated.', 'name': 'product_or_campaign_name'}, {'description': 'OneDrive folder holding the latest launch materials.', 'name': 'onedrive_folder'}, {'description': 'Document containing the approved messaging.', 'name': 'messaging_doc'}, {'description': 'Person to receive the drafted partner-facing review email.', 'name': 'partner_marketing_owner'}, {'description': 'Person to receive the drafted channel readiness email.', 'name': 'channel_marketing_owner'}], 'model': 'claude-opus-5', 'when_to_use': 'Use when a launch or campaign is moving into partner and channel activation and approved materials need reworking for partner marketing and channel teams.'}, 'signals': ['recipe:prompt', 'refined'], 'steps': ['Open Cowork and start a new task.', 'Paste the prompt from `prompt.md`, replacing anything in square brackets with your own values.', 'Review the plan Cowork proposes before letting it run.', 'Check any drafted email or calendar change before approving it — the prompt holds them for review rather than sending.'], 'subject_label': 'context for the recipe', 'verb': 'Run'}


class PartnerAndChannelActivationKit(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PartnerAndChannelActivationKit'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'channel_marketing_owner': {'description': 'Person to receive the drafted channel readiness email.', 'type': 'string'}, 'context': {'description': 'Optional. Details the recipe should use — the record, scope, dates or filters it asks for.', 'type': 'string'}, 'messaging_doc': {'description': 'Document containing the approved messaging.', 'type': 'string'}, 'onedrive_folder': {'description': 'OneDrive folder holding the latest launch materials.', 'type': 'string'}, 'operation': {'description': 'What to do: run, prompt, plan, checklist, describe.', 'enum': ['run', 'prompt', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'partner_marketing_owner': {'description': 'Person to receive the drafted partner-facing review email.', 'type': 'string'}, 'product_or_campaign_name': {'description': 'Name of the product or campaign being activated.', 'type': 'string'}},
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
    print(PartnerAndChannelActivationKit().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
