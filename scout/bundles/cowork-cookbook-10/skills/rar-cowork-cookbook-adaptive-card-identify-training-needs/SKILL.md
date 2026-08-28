---
name: "rar-cowork-cookbook-adaptive-card-identify-training-needs"
description: "Produces a reusable Adaptive Card JSON snapshot of identify training needs status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_identify_training_needs", "rar_sha256": "651b17f02723116a26b14ce3ae5889ff70159edb074a2941c4a0c3031ee6d975", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_identify_training_needs`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_identify_training_needs_agent.py` and in the RCI capsule.

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

Identify training needs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify training needs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-training-needs
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_identify_training_needs_agent.py` and embedded as the fenced Python below (sha256 651b17f02723116a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_identify_training_needs_agent.py` first:

```bash
python3 adaptive_card_identify_training_needs_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_identify_training_needs_agent.py   # or on stdin
python3 adaptive_card_identify_training_needs_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Identify training needs Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of identify training needs status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-identify-training-needs
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_identify_training_needs',
    "version": '2.0.1',
    "display_name": 'Identify training needs Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of identify training needs status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-identify-training-needs',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-identify-training-needs',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0d6a8de63b2a71f8',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/identify-training-needs'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/adaptive-card-identify-training-needs', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardIdentifyTrainingNeeds(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardIdentifyTrainingNeeds'
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
    print(AdaptiveCardIdentifyTrainingNeeds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjxpruX9HUfGh76C6xL33CERchBEISIBAC5Ha02UHsmyTw9X+/iaSqdo+PZ44nJuKqu6qEyHzzXZ/nzUS/vTh9F5fNy+cXPXCKmeBkWRIHzcwp/BlXXssmBX/K1AU/M68suiZx+65s2pePL37Qek1SdUlZgOlqU/q9F7QzZ9YEfeu4WTBjfQfcvgQzzmn8maQr8qwtnKqNy25WhrPED4ouCYdZ1zhJkRTRrAgCv521ndP17Swsm1mQu4HvT7eSYuY7beyWQFT7Edxwkgz8BWMOgZO3r0Ch4ObkVRa0L59//uXjSwLev3z+7cXLnBZ89PKmzKTL+rny4bmwPK0LJGROEYGh1QB8UoDrKmiAFjn4yA/C2fPqhzbIwo+z//iP9Oo0Ufvj5y/F7Pn68jL90/pi1sXBrCudtgv8medUjptkSTe8ztjs6gwtcFHXN8XkrBa4tIheHzO/SSqr2U/TvR8ei7xGQffDl5cSqOBMDv/y8uNk+peXpp/ev05Sqh9+fM3Ka9D88OM3OW3vngOvm4QBrV+/Pq+fYsHAb0OT8L7qT0DqI7Ru8OXlD8ZNr4fek51g5svruUyKHx6Cq6a8BIVTeMEPP/6VWC8OvDRL2u5fkvvzQ3AcOD6w6an4jx/vTv5lBj0Nepf518tWIKx/xxIw/G25j7Ono/5K9t3//0l0lhSgDt48/k/F/bMJ0E+zn//Stv9qwsdZ+OVlGWQguZup7j7Pfvuqqzz38wf/24cffvkdiP5vxehl33h3CV9zp0jCoO2+fv35Q3v/+MMvP3/oK5BroOK+9k32z2T+M7/e1/nOg89RP3w/F6xvFGlRXovZe6bPfiurf2t+f50dnSzxv33efp79sV6mFzSbjHhb9OGCP9RMC3T9gx9/fPkdgEQBrOm9+21Q5f/+77Nd4jVlW4bdTPfKvpuBAHdJHkzKH+KknYH/U203AfBrm0wo9xgH8n+K8KQxgLZf/493B89P3hM8584Tfr56AH++vkHf1zfo+3qHvl9fZwcgvGySKCmcbKaxqvqlcCIweFq4aoI2aC4AUtyhCz4BMPo0vZmw8dd/Sf7Xu6jXavj1DvDJA6c0bj1hVNtnwetkpxkHxdMqD3BCcAu8HqySlR5QKUwAwn4E9rdlBpC9m3zSpkmWzfykAQ4om+EuG/jt8yTs119/dQFufykeoIrNHqTRzsGAd3Vmnz4B28IsieLuSxF4cTn78NvvH2b/d/ZfzboLn9ZQAcI/owI0vPMMqLI+B8NAwECIAYTco/Lb708PAzEFYDkQwyRMgsdkkKVp4L+5WxfZTyhBztwAuBm4OK/KprsTUfc6W4ezd33BotOtCcvjsu1mflAFBXC/B3gtdoA5754sAO21IBXbcPg469vgvuqv7hQhoGIOyt3pfp3tOBUwR5mBX5Oa90FgclkkwP3vyfD4HAhpPrSzxZuI15k85eWschqnihvnuUboPOICGONtOhDuALq9fikmngwmV92L5OEeMAh4xnuG9NMUc8D+OUAEv31b+z7GmfjtcOe55kvRPgvAaaZQeIAQwKJRn/gTLfzjmVKA/fvMv/sPaDpJekbBf0blnoPrv+gN9Edv8H1n8aVHYQSf/f9uQSa9WUHQeIE98MsZLx80++HPqXOa/P5otkAjcJd8r51vzcEbtLwh7JciS0ByNMM/HiPvUXiOeaBW3wCnaax2lw/0B/6c5N4zdMq4pply2/lSvEH5R+CaO26BIIFyBuk+ZdnbgtPdN01jYOh0/Y3W7xEFPgQ5ALJwVvVuBjIkBO5yHS8FWjVTlT1DAdI1mPx7jRMv/s6qGZAOsgLInwElElA3AO7vrpNLYCZwc9iU+bfhydQsVY/I+jPQmgavMxMUypQsLahO0PFMY4AXPtxFzfIA+Bio+O7hNnaqhzJTN/tU0JliUeYgf/8YgefNb6l912VSH0gFCNsBX14nvPWD2yOy73o+YwWUzadivE/6PtxPW2d/5Jx/fCnuOr5DPKjx7J6435wzA7WVt3dQnSCqBTCTB88EAplwZ+bXB7k+2Ptdl89/auF/+Htd/p0uje8j93kWd13Vfp7PHxT3xnCvACDmIEeSKmjf2e7TxEaf3qrs01uVfbpX2XfCH776PPt7Cn4n4pnZn2fIK/wKT7e2iRdMqft8AX9wnxb2J3y6+6XQgm+BfmbDhLHZAOj1nXDehgDWiZogmgY/CKideOsKqPKOuCAUX4r3ZHiWCgD0IprYsi3/UMJ35gWhfUTunRjAraIDa/tTxxYF04Ymm9Rvg5fPRZ9lH18KJw/+xY3MRAAgZYFDpi0QKB/QBHVJcL96b4imi+83cffCAojgl5+n+vo4m5rXj7P3PvTj7G1ncN9vFT3YGv089cDTkmAo+PM+9n2H6AYvYDvWDdWk/GO7M7Vez5b4z0pMZQU0BkDeTrq81em04p+EgDdRFDR/FqLc3zjZEywAnk8UnXRvJd4CPX3Q8AAYv0ylB6oJgGQPJvx5GbBOE9Q94EJ/Mveb/76ZVT5s+f3uhu6xZ/zt5Q00njF49odgOKjOT+3EhnOQqmBBcP1IKnDvf9Y5PoUArANNC5BCEoiLUCGMUiiGIKSDki6CewHmBARNM2FIwQjBAOiGKdxBGRzxcAf2MBhDgoD0GYoA8h75+XXi/WRSLIDDAGMQ1PMxEiUInEEo1GF8B6ccx4dpmoKp0Ae6fJuaAqB8WvuwbnLlexM7eeVp9G8vLomDkSLertnHi5szR4c6bd0utpiG9FlUmzuHUIsVEnWNoFLkuKV83Ud3GYnl9nC2DVZPKy7j1nbkk1hP8ddgnUK2BOXE6rqQDL9CCp4seJrO68FkE/xCeQFJlJt1KZwx9bgSG8SgjMzXV1vApgZXj3i9MX1TXZm6uzUzuvJ0sjmo4wDT84Skq/Tg1G26kfTz6Sg1kTPOC/GGGF3MIYVzdvKVuc+Y240yKZcfsuPS1QTjBDZq3EmWej6SNb9cL2pLpW/VaOk51bnLPQlBm+0RhuaKeGEYUb0xitUcmblyU3qZr9PKya/n00q+HDZWI4LGXGbqzVGyB/iQMleERqRzkDV6vxYgg6xNHYFoTbaE1Lul80XMOV0OVxneWafNzVaJo7WyC4PhaabhNnh9cGzbNc34SDcmT5wzPTuaObxNpQbjya6GUWZVwqKy3DPb8GSa/ZETtsedENS2yJwkQaa3N8mr0M1KH46DuteVVOA8eBVz6RG9+FTpb2VMjEQJsYmUG5LImQ/kNueG7OoWEbayMj9DU0zU9cpSCqKwa76Rb0vPNe2+3ji39VEge2dPKip6Wth1F6HoaAjdqT8pKbzzjaweXGme243DmJhSou3KHkSCyA5RowuKVEhmSfZ2aCQGCvkScmEuohJJ603kCdTJJ+n5+mhTPi22TLXTyMG1ToKFhhUxZqJt8q5Zd5W9Ox/QjT606Knu6MtuOVZ1pi+cVvI8PjRhw8S78Wp4kNwb47UYE8LYrvcWym6XYX+7KbzhFUnGE6BzrIM95DGMNWB8VRPbnjirBkLaUGGOiDAWCRv7m3Nvqa2QJ9u4FS5SNf0Ml8LIIGzXLZaXCiHCqJwnsRXhwbigIom/+E5Z6hd4jioSDXU5Bo9M7Knaxg8ohHWWEnXuNWqtyRsEM/2YzG/ihmk63ZHasJUObeNf43wpyAevFcrlXgj5PhNWebsStlyekRksqpvSu0Wepe1Zcd2DPY9rCvub2QTimltGWNIr+xLj26JMXF6Dk7ZPhatmdNrqILXVMCiF4ilSjdOG1K8MVyzGpjisZcws5zwh8XjA7RWxLE5rdHe5+b2+WKKcrEECQeToSScwzz9nocfhmSN4oYvR89GjF9TRYyVJoG4BZ1twh9ycBsOviyWLcrbmu+now8NlxZ8lVWAB7J7tVaBshuw0T/CteSE7xXMZlNtGSJaGx8FFpb0Xn/WIg9ccoOUAQ9sdlKODeBjOxq2bM+pZbZ1mQ/tSk6FbCM32lJIxl4NzYc44nOLrrmn8SOBYjoHrCjHrI+SKeuZuhs1mbLK2OOb1nuM1u673LXQ+DGlL4DmsFCbBX/IqJDWOYi/iQRwvNVx7jqNJ8wM2sHNQkpppoCSDq/UOwq3bkini2KQTTpiDMpSNTLYc+1DxNakf+ZT2T6duW6qcbI8WRwa9PSYgt4em3Xm0uJfOQ3AhcUcOCgETbykvZ1UqWOcrlsbHvX3zBS03IAOmNQKmdHrDlFmH1bcKcyAO2+x0rMFuAS2S8AEhk90WxyTI4JGFeyINFjZCAb9xRjxSkiGd45O4TZTdVeg25U3bEgl2bJ1ojAj1FoSh3l853cec80Yp4lC1aMhWbKsetSPklBXdwUuPPcI7Plp4VVcmxzkpX2OxZNe91tk7XpS2HN/wTtQJ6NEdOmpNWgthvWA7ZdN3tu14S+OwTc+QuDFXV7zZ7lYmHGunJkpwTezMQFx6NMQ6+6rmVdNbnPJePYXqqHpzBaBq6o1NM99dCgJmQuCdLNUX9i2vPT8M3Ura7MwGR2I/DfRlpJvWoQxO0Ryiee6GEtS5Q0XOrvcLJjtDlpCLBWSokjQP3DOJssHGuukIuWsbjLE9PmUrVBJ1wS/plMqOsXQkO1+qUiag6GC9N0VF6uOW25Yn88iWoSqWdGhzYTxqZ5Q5pJgUK/BCdtcxjByuTKSyhn245jsxsA/zXXDcuYZvUEVZioSTozkL5cfLNgNAToaKEub52TC5gyasDQRNh2XSVOf1aAlW4UNWlXaITGumCJ3ZgG1zPEfUi56SoNUhEfSIbYJeMcVOvR7JtUCsChtGqFrdeEsMvx16WWpvyO1yW0S5zkRKMD+woqMgENhFtqbmjBrJOqhkZMmQb52chjWx95ltp8nX875SOBVyL2kj8KsVszQGEm6DXY5jRHXZo6vUKtfwpnRuwrE5U0ex2++7hdIaI6ZlJJpvcPEgX9eQXBcOv1mokZEksm7vgu2gJizMnDprAYBhbsVLnaAjw1wYxKFKuf1l72qJFdnFak+vqKxNisOZ0HlkqVQm4Ox9g/eAIvYaTXMS0a+TxZFY8czcg0wXDnJ5QNN1UrrCIqN1PtrGI0Jcc71z+bkmncoTHyPzduRxUJwu5C86Zd+Lh3ONnZotdPK2oybLoHG8smbXpMQKTzmsZPj1Pg7oLBMtGmxLDG1FmkRdr6q5Vo4yucuki4FYJh4ZtlNT+/SMj1eZLI72UYh1g9Cw/XaVINeTWWZ4fI6XoQTZmQlFpcwuOLuDJQb1oDQ8nAptuVwwUGHg6MpZSwjsKnFN4JtUhgF4UmNj7021Pgi127ZDNdc9NQxVrGVCaFUKCylv64W1EtE8DE/DGme6ptAdZnkoTjbU59lguQdyzKidZZNHn0QXAwrv2V4W2JUWMJkPCptzNxFr2zuoGLuhJvTDNcT3uZHfliw7CLRhWSPNVMOp2nL99VIujNI1C18AmSEu4c1xvUfq+Kh73kpsxRuVlMLGN7dY7USe3lmbOgguhVPdSgsTgkhYrt0r5kXNMiSEHbSCb+I+Z8W2Db01d0TxOorH0WPkdKuwO8Vlu9S+wbQtwcNSmxs5pKUDiZG6w/qrU8+G2agF6aUQVrhSZ/hWR8aTuLwW2+YkT81EnG1W/RIB20Zd0EHEanwdZcrAbyL7aGyOBmhL4kFpipNoR0W2cdbobaXxB0IAlHId5otcCGFBKFy+mh8yHnQda784ovZiZVVJcjxddCKlkmtiYiiSYmg4Rgfa4gPc0kVsf+jFCyWV4umydOUr61nKCWLX9QbTcIvP2nQ+RHBVKzf03FSyfDzikYa1eZjUJ+bmHg/EhRQA0viId0gtTksMvFowkmytlvGa34TYWSlFLrHdjUHiRebYg2LJqMf6bHpkYHMe6Ct6KG8ds3DnpnpAfY/X43Lfym2/Qiqz27CmXjmtTLD1TaFxl7KyqofFLbd33NQVckIy6tUhyS76Ju9j3Yu8wL/w0Mo+7yjetPi9sD5W66vKrJenc5WN4+Vk9LaMS7lB5o4rd14tyRfV2wZOykdupd7O9gHyCb6vrlsliJcLmOzk/YbfVxAIhJTdzk7kRpscUxfMckGdAQzuJHpe2MtFBDn9smHRqi8W1MGJ+My6Uq20IlRtZ4XL8LC9HI4HF1khaC9F3pLbVuhICWcWGi8CthkrPKW0uZnjlc8Sc7hQOG5c3DTHVzfFrtJLbrEFhLRbRlde12JMvjo7qxy5aj9KnOwhSrs9YehO6ngWCQt5zdXnK2FBBr46wf4IdjVsFes8d03P4ZYYcUU8bHjbKrGturADSRZdQ0L5kvOgkt12teBFrud6+4CkGR67SZrKpTUZQDp/0lasTvRnpNoQZEPY+6g0+XC1hU8YafhbL2f47nq5QDLg7SjAjubJnbu13yQ7hzyqTOmJHVowHEVjEK5uca9mFOqwuHaU7S3gc5lKOtpg1LlwPC4J/a1Wod64JwpWENeoX/sMMsKwOKLq8USBFi7cnxSNP+Wr+CDxw4aARHqLLnYaLpVLc2HJzAVm1U4jtOvODs59pCLLwupBxyQfjlEkSxfKQEW5KJkykefm0b3Fft3Ypjj2Q3dRYK5tRThl1JNVcxQqtyrSKRoB6fO5ej2EYLfi1QM8b+fhzaAvjYtZqq9AF96Zn8RLddgfUL5KxKyPUrpQtdbQyc02Q5LjsLyd5nuFPGiRhISDe42d9fJwqMar4DjhXtlX/SHYHPIwHefb1Begk9Xkx+S6s1iMc+uCO5e0uFTd0dlIxaIMCM+6KIFXjstKity1eTThI6OdBcjmXfrEqu4gX/Ys6kMJ7pLNhrslzIoK1pcFgZpIuLagzquCbHfUF+eRWNwwCvS1OMj9HWompEDUUnUgyDWSBmJWq4zvC+WcRObYEuwA6oNLabK9qLdr8Twy8rn00ZaSKSKXwOYkdOBgp9kD63rmCQ0bJ8AywlntsS11ZofbBTn3ck5Vc5EK13FXpuV1N/fJ1IRXC2gjkx0g0N4btjC81jyC9y4a2NvOlw2cLBbD6TrfwpQxevzmMngXi6fHbr2g7bEcz7fS47wVw+bixVZAf39NxlWRuL3iXRNPuzbm5lI75tqzmECniFZYajiTt0RB7UUjgo0bCmHwNbt6mqitcn1cSPDWoHj0isICTywXlnkhmH3plrJi5+F8sEkdSs0og/B+cEB312J2kvVGPi86yU/c3IEt1Vm2BbwAu5J5HR/izqPPc7HXCFPAz5dT5zUK5naAEso9LiHBkguJI7s7KcAeR7ksLZ64LK7ZEQa99Y5A+q0W9DeqtNkhNZcn3fcD5tqTorWDhgqr+qyn5k43LJdGT3aJItbjCjp3uMRfl1fWuDjbiwwqkAooPmGXmxuTqlrsFc1peYAZnuJ7a3/czSvVDgs4J0WB3i/3TUdFtrkUh9GdIw1bZpgZkghMUc11yOgd3u4YFbmSyHJIstGi09K5dKozl+kdtpF12u3z4MzMAaP37YE6y2joU8yKgSJ0h2aqd8R2p4b0W2efuGuFXhsaqwRC3ZPQuJxjNno2LHMtcIjv3XxSsm5hwtDyYa8uKm6J+KGwXF7xzbqoEU+VbxTfjNstZIJKlG1QN0Tfzp2LwHGrXUCXbBBjJ5plEUG7ZnnvpvnYjWd4Texiq3QHwSy7OdZWARrEIt4ae5Xj47Pv45ZqDME1ppVCo01EDlY+XeLjgma54zVWVwyATuw6lkkN+J/O5f2O9JA9YObYRvd4rupNdehOA8ONmCfdjoyYgd4tXYRzyOEhDmxDAw4atke7jOVthokDrNgmQ1z2JzdsCTP0lmv+Bm2GtahVa8T1cnWtrvbn4wXV+xYiCWt/vVYIrahsWEppuB0zYm/Xh2pT6mzhEs5CnGtry9BuDFHNl+YuxcIQkUZln9aYOSK3wTJIKKJR9ozvGy5lWfann14+vkxH088D5r/3KHk67vtfO3V8HBC+PXK6Hy4Hjv/5vtbnv6nXLx9fGi8BWj3OWFsAzs/DyP90wvrpX3paMYkYHs9pp2dkt+7tWL5zoukrRy9J4fdt1wxf2zLr7we9H1/cvp2++9B+fR5ov9zNy6vpdPw7c+7XOVhuepL6tSu/Pk6Zg5fpOwrTA6DAT75dRs8D6I8v/gCClnjtV4wkvgZNNVn9fA4CjEVf4Vfk5ff/B0qBfVLmJQAA -->
