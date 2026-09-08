---
name: "rar-cowork-cookbook-partner-and-channel-activation-kit"
description: "Adapts existing launch materials into a partner and channel activation kit \u2014 partner one-pager, co-marketing talking points, FAQ, and email template in Word plus a social pack in Excel \u2014 and drafts routing emails for rev"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/partner_and_channel_activation_kit", "rar_sha256": "e0401888bfe929e84aa8ced188cd230b12d28a50e89f295b3fbc8bc4f618b637", "source_kind": "rar-agent", "source_commit": "597f0992f4120ddef24dd8686c5720a9ba5b59ab", "version": "3.0.3", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "intermediate", "read_only"]}
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
