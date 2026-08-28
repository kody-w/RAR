---
name: "rar-cowork-cookbook-adaptive-card-maintain-contacts-and-accounts"
description: "Produces a reusable Adaptive Card JSON snapshot of maintain contacts and accounts status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_maintain_contacts_and_accounts", "rar_sha256": "d4fea7396a00407d9df84e8031fca6f841d9a013cb0747754413ddb579d885ed", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "prospect_to_quote", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_maintain_contacts_and_accounts`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_maintain_contacts_and_accounts_agent.py` and in the RCI capsule.

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

Maintain contacts and accounts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of maintain contacts and accounts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-maintain-contacts-and-accounts
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_maintain_contacts_and_accounts_agent.py` and embedded as the fenced Python below (sha256 d4fea7396a00407d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_maintain_contacts_and_accounts_agent.py` first:

```bash
python3 adaptive_card_maintain_contacts_and_accounts_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_maintain_contacts_and_accounts_agent.py   # or on stdin
python3 adaptive_card_maintain_contacts_and_accounts_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Maintain contacts and accounts Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of maintain contacts and accounts status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-maintain-contacts-and-accounts
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_maintain_contacts_and_accounts',
    "version": '2.0.1',
    "display_name": 'Maintain contacts and accounts Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of maintain contacts and accounts status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'prospect_to_quote', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-maintain-contacts-and-accounts',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-maintain-contacts-and-accounts',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '44265f0fe26455c1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/adaptive-card-maintain-contacts-and-accounts', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class AdaptiveCardMaintainContactsAndAccounts(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardMaintainContactsAndAccounts'
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
    print(AdaptiveCardMaintainContactsAndAccounts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZej1pblX1FFfbBdZIYYBeRbXqsRIISEhAYQCOdbYYbLPA9CyOX/XhdJEeksv/e6Xd0fWnZkCHE5wz7n7HPuVfz2YndtWNQvX16OwM4nkp2mUQjqiZ17E77oizqBv4rEgT8Tt8jbOnK6tqibl08vHmjcOirbqMjh47u68DoXNBN7UoOusZ0UTDjPhrcvYMLbtTdZHdXtpMntsgmLdlL4k8yO8hb+3AXbbtvctdquW3Q5vGhau+2aiV/UE5A5wPOiPJjA1Z7dhE4BJTaf4A07SuFvuEYDdta8QrvA1c7KFDQvX375+6eXCL5/+fLbi5vaDfzo5d2m0aTN0wD+qZ/LPe6pHcpJ7TyAD5QDBCiH1yWooS0Z/MgD/uR59WMDUv/T5D/+I+ntOmh++vI1nzxfX1/G/w5dPmlDMGkLu2mBN3Ht0naiNGqH1wmX9vbQQLzars5H5BqIbx68Pp78JqkoJz+P9358KHkNQPvj15cCmmCP6H99+WkE4OtL3Y3vX0cp5Y8/vaZFD+off/omp+mcGLjtKAxa/fr2vH6KhQu/LY38u9afodRHnB3w9eUPzo2vh92jn/DJl9e4iPIfH4LLuriA3M5d8ONP/0ysGwI3SaOm/T+S+8tDcAhsD/r0NPynT3eQ/z5Bng59yPznaksY1r/iCVz+ru7T5AnUP5N9x/+/iU6jHBbFO+L/UNw/egD5efLLP/XtXz3waeJ/fRFAClO8Hovwy+S3t+NO5H/5wfv24Q9//x2K/t+KORZd7d4lvGV2Hvmgad/efvmhuX/8w99/+aErYa7Bunvr6vQfyfxHuN71fIfgc9WP3z8L9et5khd9PvnI9MlvRflv9e+vk5OdRt63z5svkz/Wy/hCJqMT70ofEPyhZhpo6x9w/Onld0gVOfSmc++3YZX/+79PNpFbF03ht5MjpIV2AgPcRhkYjdfCqJnA/8fargHEtYlGynusg/k/Rni0GPLcr//LvTPpZ/fJpFP7SUJvLmSht3cefHvnwTfIg2/vPPjr60SDOoo6CqLcTicHbrf7mtsByNtRf1mDBtQXyCzO0ILPkJM+j29Govz1r6h5u0t8LYdf7ywcPVjrwMsjYzVdCl5Hr40Q5E8fXdguwBW4HVSWFi60zI8g636CaDRFCkm/HRFqkihNJ15UQziKerjLhih+GYX9+uuvDuTyr/mDYonJo580U7jgw5zJ58/QRT+NgrD9mgM3LCY//Pb7D5P/nPyrp+7CRx07yPrPGEEL7y0I1lyXgbHDjAGHhHKP0W+/P4GGYnLYAGFEIz8Cj4dhzibAe0f9uOQ+49Rs4gCINkQ6K4u6vTen9nUi+5MPe6HS8dbI7GHRtBMPlCD3QO4OUKoN3flAMocdsYGJ2fjDp0nXgLvWX53avpuYweK3218nG34H+0iRwn9GM++L4MNFHkH4P3Li8TkUUv/QTObvIl4n2zFLJ6Vd22VY208dvv2IC+wf749D4fYkB/3XfOydYITqXjIPeOAiiIz7DOnnMeawf2eQH7zmXfd9jT12O+3e9eqvefMsB7seQ+HC9gCVBl3kjU3ib8+UgoNBl3p3/KClo6RnFLxnVO45uPnXY8PxMTZ8P3t87XAUIyf/nwwpoxecJB1EidNEYSJutcP5ge6oZIzCYyqDQ8Jd8r2Svg0O77Tzzr5f8zSCqVIPf3usvMfkuebBaF0NITxwh4cT0Zjfo9x7vo75V9djpttf83ea/wQRunMaDBksbpj8Y869KxzvvlsaQkfH628t/x5fCCXECebkpOycFOaLD4Dn2G4CrarHmntGBCYvGGHuw8gNv/NqAqXDHIHyJ9CICGINW8Edum0B3YQw+3WRfVsejYNU+QiwN4EzLHidGLBsxtRpYK3CaWhcA1H44S5qkgGIMTTxA+EmtMuHMePY+zTQHmNRZDCb/xiB581viX63ZTQfSoW020Is+5GEPXB9RPbDzmesoLFjaj2i9H24n75O/tiP/vY1v9v4wfuw4tN7/n4DZwIrLXvk50hYDSSdDDwTCGbCvWu/Phrvo7N/2PLlT7P+j39tO3Bvpfr3kfsyCdu2bL5Mp4/29979XiFdTGGORCVoPjrh57FFfX4vts/vxfYZKv78Xmzf6XhA9mXy1+z8TsQzwb9MsFf0FR1vKZELxgx+viAs/Of5+TM53v2aH8C3eD+TYiTedICt96MLvS+BrSioQTAufnSlZmxmPeyfdxqGEfmaf+TEs2Igy+fB2EKb4g+VfG/HI9U8YvbeLeCtvIW6vXGoC8C480lH8xvw8iXv0vTTS25n4C/teMbeAPMXwjLumGAtwWmpjcD96mNyGi++3/rdqwzSg1d8GYvt02Sccj9NPgbWT5P3LcR9e5Z3cA/1yzgsjyrhUvjrY+3HvtIBL3D31g7l6MJjXzTOaM/Z+c9GjDUGLYbk3oy2vBftqPFPQuCbIAD1n4Wo9zd2+mQOSO5j947a93pvoJ0enIUgp1/GOoSlBRmzgw/8WQ3UU4Oqg23SG939ht83t4qHL7/fYWgfm8vfXt4Z5BmD5yAJl8NS/dyMjXIKExYqhNeP1IL3/q9GzKcsyH9wrBn3t6QPbJpgZzaKkijtsZ7PkIBBCcx37Rl8j3msjWKE66A0SdMUSWKE5zkUzXoMQ0F/YZzuyfo2TgbRaB9AfUCwGO56xAynKJLFaNxmPZukbdtDGYZGad8Df3w0geT5dPrh5Ijox7Q7gvP0/bcXZ0bClUuykbnHi5+yJ3uGk871aiK3GTg7ObU/5uHVFJrpTKnkoom6iA2uK8WbF3PewT00VL3FYNHobU0lp7m6D5niQCU5lSt5EyteU/L1UXIWG9piZi4yzVVlvSmkmkiaWCAHbL2YYmosHZnh2m51bH9COk1wsVXlWUqPMmnV6xiV0jvP93H1sqbMU7XnqAo9tsBaK5xn+gpNTa+mNj/S2CGskhPOUtN0aS3rk7a4CueDcbSV7X6LXS96pgO+WGFxsGn8abFMYmTh7A6VqlHMdHejZv5FyOm0xFmQ7xCSHFh8H9IhH2xI2rQqsbJzcKq36fqWrlwm0RK2xxnpujRKbX/CC6zPFjaLa9dbeEzkXOvXvBqfsJW2wv1c6bYrflHxV8c2nCbcL+OqXCWJJxkLQk7bVc6pLYjQVD4pC79cmGcHO1yXFbpUBeuYEEy7Ns8dv5hlnHHaLDbMSpJvwyXBhszhT2J6EVA+Xs+D6VYs9uWcqglrWGoaSoK5S+sxEfT8cRueicO+x4/NYmoI7sk2cEUT0VrXSmJVXWM7FuMd3pNn6+TZC0vOV9j+dtj7eG81Ns45zvZwxiKWtA3tsDiZp/igsqnnOIlmzurjsIg5kGeeyq9km17GknCYer1aLlYtSWk3Z4BZyh25IqEoGwE0LuEq4c6dXb0aNrWEIVpqEwTD9pKNNwcrOWKeK50HZLVuSMLmQ+bCKENVYRpnF1cPl5GtzLV4VQ1ViZbeyo+VOCJFhQ1vS34R7pj2ehRltcb3fINpM0m4TVHfPwUZvln7p2iXTNtrq12y2alSUU8cFkqh+h61TUzR8tT9qYU/qeqqPVZiGsEbxmW+S4i1Erj+jbvgFLjNaW5hXEq1LCQB83H+iCIJsUNJ/2wuUCUtLsgt2ls70jsS1qak9Ca2yGVSRheMOp1FYgGH5ROsLvIaG7p7LMnz1loGm2HnMZLc6hyOzqJ9U+mq6pkz4UI2PKV7caVxpFrsvCo2GclekjGQyVIq3GbmN15yWB+E2pNhs5qfm8osLW3NkK6UuFqL0X3tChUiXfICT3u9U8/ZvNfmjC/2mni15E44MzbINLdkzEYuCNKCsTymt9y/AqnfYXwhYQ5veI3P3NhjV2xRJSpXjYgoAy34jGJKdNNco8Te8tt8YXQ6ttY60CwXR5s9lLWx1bdd1MwOCeIkrZAThcqg3WyxzlbxufaxppBBEHv6cSGu8pxGruV8Rk5l78IftKXJUDMGXGdydUWbi7GvZ61d4uWizbVhR+EULL/zsF0srCm1i3DlwiXiQoucI1oXxvZgrtT1wNhhqfMLZbFGJaIAvo7P1QQh02qkqUjzod14DnTJv1gt1ZAJGrjMbTPMw1RPLT1RppYdMt11dTsLiY4A/GAz5GYLwOxmbzfuCh2y44pGeZtYE5SV65sGKYjMPpmrzLrdJCcPBUBZgxKuzyK5y5wqtDWvIQ7X2+oWdnVKmJGvZNpWljlV31onrdCIdEt0Zcb7hupj2cVijxGKDGosUFPk0OTTvhJnZeMb9JE6aLLnq1YliUssyJe5nApEUuyniDQwWUqic0/n7DnlpKdCF+loVWv61NnG/bDEhevuZFjxDBjK9rZRGnGtteg8qIqSaVFOL1quKLlNoNGnxezSK/HRCOYp2MfrRtVXa36xEp19uiFuDjnnuBky3/XzfKv2Xbk4V/tlcVKy+Nid3X5xs9CFNk/qWnYTEYsFY9aXyziOduZ5IedYIdqeQbQDWzOt6geQ22tLnM1uNUu7Zo3PuvXG4NbL9REPZ8hs5x51ENasFnpw0NeC/XmtobutsPNbsbAJ17tObWWemHKBursLUTGg5o4Czc7YXXiV8sogrnss9OLOl7zmuJ5n/XmmEyshk1wEK7ZyeRo6C4vTNZGtpzdov68loskN5aLrTz1PGW2thyVzTsAZ7lzto37YOjrFpxVTHqqmurQYt4yOUZLwS2Ojq3h+SDCvPbH4bB1dl7wt9H2l40ay3p7FU4UnqZv69pZWdKZHEqpdzTJRroQQi3brPiEpR6LFytnjhGmH6xklOXHan3k/rVpObLY2AgcgABKmI862ZuO7M9ieHUE0KnkpUn0Wu+jFYXz3nFG1fwuyQ+6vUKXa0KaUXH2068quB1goi5d5O41EcCQ4q6PCVa230RwlG8+FaVxouEXYM26zHwIec3wj7DfhVRZ1Xt9Z6mnbbnQGRNyNbe2T0FRyqI654yTXWjNRuw/ZPlxUlEJ2QIqSpvNlbxFSqr6U+MTp5ze5bjbZBm5sVjfz4NTXqcoNoWudhrA/0xtFz06HZhkKh3xBcOBo24iy3MWzhJAoUxMPPRVzsCPCOYYXZ8QZbyJVFsn0wq3lnqYI0G4kfraYLgtbE3cNWmAXnMRZRV3N1udUr/eDMD20Vn6OxKCjpOIqnZXuCgw8YFuVCSCDEaVdbBDyDHKP1xIzMqN23ackX3Yu3yPBNcxK7LQwzubAJFTR4r0tladVem7iSO9P8963LelC8lwQ6KmGk6wDG4ewEtSI20X5dHo2s5nTt3Nsfxg25k60w/1mmdJGT0sLSMLmyUvj1BNW/NK/xM5waKcXXKi1hWVyXa8KWwvhklPPck59NDxcy50zcjFOQ+5oGZ1j5+6aVPW1ZUmrDjvR3uzXCVtVbCTN9ZIX+YzDOk4dmro49TDfpsbaOjri1s9lIopYLy9veyI2kwU+d6vTIZ6tT24r5YeU5a4lbzRn3VrPNuG2vyhdstdLrKjdzl4Qt9QNSzx2O8wYLv7eFrnzJvRhqzAChROPhhuXsWrIGbnqSG0ghPQ4XybFhj3lp0RaMdHcOadJyTdWKW4y+uhfhTgv3fLS8WKYkZq932FAnza9dS3XWiR4rkFxG3FFa4HSZBdp7RZmMLc2LLOkcmsT5Hx61GQtPPNIpWQrQrYPSUI1bbFqjmiz5XJtU5CRIsuMoNU8IzUBGySlShsZu6wGPZBkWgyJMpTbKrsoR7fFenObix4tr6/EBcGPWZUi643C75GB99b0jLHng9PjV3yuyJrVKfRqxvQEm+BFd0kW032qN6xhMMBTmgUfbyPtsrBEtkY9ncg7mqL2F74VyA22kINZKm32KIA9K+gPVxf2FmDPQyPaLSKA54t92DrEBnfFKigHZEZeL6sjbqEV4vcVksszK4j50PRci9s6Q1muOWNf2vKK6lM4ZNem11Up7XLFIM3CI9xZC9ZVrCiupPboij2u47p2bHyPgelwPgiNWcQrVAfk4lDx52EzF6IN16mxQxySwNyocOgsvKWJ34r8Kmk7H4ZivlYjulSvg36gU3fl3QrdZdeiUF6rFaT0fYnbJ311OWw9zg6GhGCLQoqn0man2hqFNYHECTR2oo0wPXidsskwebUGN9CTTmY1+5Y2vW3DbrHtZbM7V32K9Bu5y51dc94INM54bg3StcYKW7uO4kTJ2dTqD7K8VhRPZirveFqL8qoJZkLQSPPoyO0oUtj2qZWve2UhbBPyxJzshHZo3D1yTXZQeSSeSUtpsURngTpzaCKwz0m68I7SsLgRoAO7AI1iiYy2vXDJxCg+EN3R6EveRQrOaTvJ4hzO8frU1CoUzFeJhZHKMta91PTX1abgu6vLUiTquyzmrYv4bJB+q8wsOPjQ+CqgYyd2wo3rr4FHspBRfe9Sk0Dq6jiN0ZQBhLKC097mgpAXhXRpUHplcMa9ttuwxoEURcwhlBi3vSwKvd2xrpksGrQeTg0EsummHeW4FxSXMevmQXZ3bFlOiqG1+QLOMMHVYbeMNet1pWwhzBGRU3azZ1gCFXmDdJyiZvJbjW3PK1bDr3DHtiMOu3wZFEojbC9nwqEy1jSaZrc8ZBbieRLFYYOMqBaN9R69NAXWiRPXzy/TKb4mSK5bKg22o80pdFPLV3RNXHTfNARcT4mkvHH03KyWjB0XTKyd82plLZb25mgNPeWwoZBE8d6Sp1adbw+6rKqEvLGQ+ZQLmpjJWN3cM9Bn48AA1jGV1Ito3JRvkYGBhXFFt8uLXWGwOwkchYE8X6mMYmXJwHcH/WiFJjs/ExRWKfGALq9mO1sAOGHYtz3jXY2F5thHBWH2yNJxzJMb+LPLsEvauNrLuH+uD1NLwIi91AlqWnSHyI6YCOwyYxtPz+0B8ZUidKamz5Bbw2bK9aWTsUCqNwFIL32nhlBNCwlWPGIVgmAcc448ad5amnpjHJNgcsWvZLLrNsJNIkzdtQ6s7/WlifDniFMYTMXAQbzgc6d1D+ebt492BFIcXGoRNAdkak3jehMb8z7YOLAa3ZuXNPIwVU8iOcX6OYoR1VqRr8x6cUGiVhEval8K4vQCbovxDLxuFgwpCEZzuhzhrJsm7NROEUYVwp5NGyqm9ks0SuYO7WVehM+vZ+8snglzr3lE2QYNKW4GXCqMXUbzB2OGX3kL7GqFV+ZCurGRNHcFx/WIFL+tnHR7oeijdi7IwYhm9N7LmNhLhf3JWDNqHfM75GgpiV9XKqIZFI0wlkeK8olCwtleFfy5JLRA4ptiv5ku22CzrWYROrVPF5qYG8Ie2DijyIsexZeOHjf1NmxolJgDaqtjdMICoogwITeb2iDhVEMugTInZQbjuSLfzRbBkUUyEjsEh/2uoRDdkUm7DNwlySAJH9NlXs7rW8IU+TkneBmI27rFh7641KCdIsb84KgtQiglkROh1C8acT7tEJ82CrA/XOzuSuNxw56cKX4z8W2hS/iR8BAvgQRMZTMy8YBfIvGUFmgi34SXAQnZS2PCzeoc2ayYgqr4Sp5rlG7QHn6eks6yt2O7vgZbc6maYDgxDhtPBb0X+vU+YE3iyjBTQorkrM05xe3CGTMcp6R2aW+20hoSfuGyfM8PV707M4Iaxja5F+HMhSaZalZhPL/N0Q29mZszZ8+bhcfiDQVUcK2zRt9vOLHlPIE57RLG61HS28W0XHfJaomsCEnIAmUbqCRY8CjOqUvU2lPHXdpW84yTXJWJ9sISr53e3i9VBzXbw02nDrNNQ1aIYzAEDKF/8Veie8rBwCxYwiiutYh2pusrU21NXLYIn+bT5amkA3sRuNGs46uk0RpwNVITqbh1jAymarXuFDun81vXEdyZ5A11UeFsIe9lFG4yUu08s9ols/Cay8DoV5Yq2bixDleWtokNw5O5B6dVvfTi62zLHvHFekdFCcdxP//88ullPKt+njj/j753Hk/+/p8dQD7OCt+/kbofNwPb+3LX9eV/Zt7fP73UbgSNexy+NmkXPI8n/9vR6+e/8p3GKGl4fMU7fqF2bd8P71s7GP+C6SXKva5p6+GtKdLufhD86cXpmvGPKJq354H3y93ZrBxPz79z7nGjKYHbvrXFW9UVLXgZ/9Bh/KYIwB3fx2XwPJz+9OINMIqR27wRM+oN1OXo+PObEugv/oq+Yi+//xcbexCkOCYAAA== -->
