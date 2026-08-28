---
name: "rar-cowork-cookbook-teams-update-develop-subcontracting-strategy"
description: "Drafts a Teams channel post on develop subcontracting strategy status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_develop_subcontracting_strategy", "rar_sha256": "d8b8fb0698d21fdac1b096f5d80b5eadde71645662f0ccb5c6ff03efcdcd3df2", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "plan_to_produce", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_develop_subcontracting_strategy`. The original RAPP
agent is preserved byte-for-byte in `teams_update_develop_subcontracting_strategy_agent.py` and in the RCI capsule.

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

Develop subcontracting strategy Teams Channel Update — Drafts a Teams channel post on develop subcontracting strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-subcontracting-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_develop_subcontracting_strategy_agent.py` and embedded as the fenced Python below (sha256 d8b8fb0698d21fda…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_develop_subcontracting_strategy_agent.py` first:

```bash
python3 teams_update_develop_subcontracting_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_develop_subcontracting_strategy_agent.py   # or on stdin
python3 teams_update_develop_subcontracting_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop subcontracting strategy Teams Channel Update — Drafts a Teams channel post on develop subcontracting strategy status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-develop-subcontracting-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_develop_subcontracting_strategy',
    "version": '2.0.0',
    "display_name": 'Develop subcontracting strategy Teams Channel Update',
    "description": 'Drafts a Teams channel post on develop subcontracting strategy status with an interactive Adaptive Card for quick triage.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'teams_update', 'plan_to_produce', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'teams-update-develop-subcontracting-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-develop-subcontracting-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a964139b06681734',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['plan-to-produce'], 'process_tags': ['plan-to-produce/develop-production-strategies/develop-subcontracting-strategy'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'plan-to-produce/teams-update-develop-subcontracting-strategy', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDevelopSubcontractingStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDevelopSubcontractingStrategy'
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
    print(TeamsUpdateDevelopSubcontractingStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjyJLtX2FyPnT1qCrZQapr1+whJCS0AGKV6GqrYgex74Ke/u8TSMqsrul7Z6bnPbOnWhJEhLvHcffjHkH+9mK1TZhXL59fFM/KoI2VJFHoVZCVuRCb93kVgx95bIN/kJNnTRXZbZNX9cvHF9ernSoqmijPwPRVZflNDVmQ6llpDTmhlWVeAhV53UB5Brle5yV5AdWtfRdjOU2UBVANrhovGMCF1bQ11EdNCHRDUdZ49zGdBzGuVdwvWKtyIT+voLKNnBgCtliB9wos8W5WWiRe/fL5l18/vkTg+uXzby9OYtXgq5e7QVrhAkWrhxXKD0YoTxuAoMTKAjCjGAAmGbgvvAroS8FXrudDz7sPtZf4H6F/+7e4t6qg/vnzlwx6fr68TH/kNoOa0IOa3Kobz4Ucq7DsKIma4RVikt4aaqjymrbKJrgAAsCG18fM75IAVH+fnn14KHkNvObDl5ccmGBNgH95+RkCQHx5qdrp+nWSUnz4+TXJe6/68PN3OQDvq+c0kzBg9evX5/1TLBj4fWjk37X+HUh9uNb2vrz8YXHT52H3tE4w8+X1mkfZh4fgoso7L7Myx/vw8z8T64SeEydR3fyP5P7yEBx6lgvW9DT85493kH+FZs8Fvcv852oL4Na/shIw/E3dR+gJ1D+Tfcf/P4lOosyr3xH/h+L+0YTZ36Ff/una/qsJHyH/y8vKS0COVJadeJ+h374q0pr95Sf3+5c//fo7EP3filHytnLuEr6mVhb5Xt18/frLT/X9659+/eWntgCxBjLqa1sl/0jmP8L1rucHBJ+jPvw4F+jXsjjL+wx6j3Tot7z4l+r3V0i3ksj9/n39GfpjvkyfGTQt4k3pA4I/5EwNbP0Djj+//A64IgOraZ37Y5Dl//qv0DFyqrzO/QZSnLxtIODgJkq9yXg1jGoI/J1yuwJMUtURAPY5DsT/5OHJ4tyHvv0f506en5wnecLNxEJf2zsNfX2y4dcf2fDrGxt+e4VUoCOvoiDKrASSGUn6kgGyy5pJf1F5tVd1gFnsofE+AU76NF0A0oS+/RU1X+8SX4vh253uowdrySw/MVbdJt7rtGoj9LLnGh3AzN7Nc1qgLMkdYJkfAdr9CNCo8wQwdDMhVMdRkkBuVAE48mq4ywYofp6Effv2zbbq8Ev2oFgcepSQGgYD3s2BPn0CS/STKAibL5nnhDn002+//wT9O/RfzboLn3RIgPafPgIW7hRRgEDOtSkYBtwHHA4I5e6j335/Ag3EZKDmAY9GfuQ9JoOYjT33DXVly3zCSAqyPYA2QDot8upewKLmFeJ96N1eoHR6NDF7OJU+1yu8zPUyZwBSLbCcdySzvIFqEJi1P3yE2tq7a/1mV9bdxBQkv9V8g46sBOpInoD/JjPvg8DkPIsA/O8x8fgeCKl+qqHlm4hXSJiiFCqsyirCynrq8K2HX0D9eJsOhFtQ5vVfsql4ehNU95R5wAMGAWScp0s/TT4HvUAK+MGt33Tfx1hTtVPvVa/6ktXPdLCqyRUOKA9AadBG7lQk/vYMqTrM28S94wcsnSQ9veA+vXKPwdV/0z08eg722XM8aj30pcUQlID+vzUmk+HMZiOvN4y6XkFrQZUvD0AnRRPwj94L9AX3yffk+d4rvDHNG+F+yZIIREc1/O0x8u6G55gHibUVQE1m5Lt8EAMA0EnuPUSnkKuqKbitL9kbs38EqNxpDOAA8hnE+xRmbwqnp2+WhiBpp/vvVf7uUrBsEAQgDKGitRMQIr7nubY1YRBWU5o9fQDi1ZtSrg8jJ/xhVRCQDsICyJ+cEQFHAfa/QyfkYJnAE36Vp9+HR1PvBKxwWwdYCzpV7xUyQKZM0VKD9AQN0DQGoPDTXRSUegBjYOI7wnVoFQ9jpub2aaA1+SJPp7D5gweeD7/H9t2WyXwg1QJBBrDsJ951vdvDs+92Pn0FjE2nbLxP+tHdz7VCfyxBf/uS3W18p3qQ5MlUvf8ADgQCEMTxxKoTR9WAZ1LvGUAgEu6F+vVRax/F/N2Wz3/q6D/8tab/Xj21Hz33GQqbpqg/w/Cj4r0VvFfAEDCIkajw6kfx+/SoSp+eGffpx4z79JZxP+h4QPYZ+mt2/iDiGeCfIfQVeUWmR4fI8aYIfn4ALOyn5eUTMT39ksned38/g2Li2mQA1fa98LwNAdUnqLxgGvwoRPVUv3pQMu/MCzzyJXuPiWfGTAwUTFWzzv+QyfcKDDz8cOB7gQCPsgbodqc+7rHbSSbza+/lc9YmyceXzEq9v7bLmeoBCGCAy7RNAskEOqQm8u53793SdPPjDu+eZoAf3PzzlG0foamz/Qi9N6kfobdtw31PlrVg3/TL1CBPKsFQ8ON97Pv20fZewJatGYppDY+90NSXPfvlPxsxJRmw2PGmGp+/Z+2k8U9CwEUQeNWfhYj3Cyt5Ugeg+KliR81bwtfAThf0Px8hgCRIRJBbgDJbMOHPaoCeygO8D7h3Wu53/L4vK3+s5fc7DM1jQ/nbyxuFPH3wbB7BcJCrn+qpOMIgYoFCcP+ILfDs/6qtfMoCBAhamWlPO7fnvo1Qi7mLob5rOaiNLCifdOeITQL2dj0apQiSojAfcRybdCjfR3DPd1zHxV0fA/Ie0fp16gaiyT7Mspy5Q6OEu6AtyvFwxMYdD8VQl8Y9hFzg/nzuEQCq96kxYM/noh+LnBB973AncJ5r/+3FpggwckvUPPP4sPBCtyiCtoXQntGUH5TX+RxZFAOSWbSBeyO1VRSXERHL5HbNEConpNk1R0w8sGkkLKXuwjMzeTfrVfrgi4qM1qNIHpbWYZkm12imhoSdzMmx1YKBvUicfN5Hzf5i5sTe31NxnDZzAulnnFKNOjHX8V12kxKDrLL9jVmAKPejBbqA1/28ai1KiDfkhkgtLbQSLr50yOq8Ew5et4k2jWsT52PokNXtLLbJKjyYTuyPqaFHmS5HpieoEcmdjZTUPC52OhtFAYr+GcdggVvNvWsxxxw49A6kHmSW3BpovMYWB6UAoCdF5+ontbgMaBgvetqxYrJW0nh1Uyz7qiQ2fZiN68ahtIzgd6rO44lWcTUtZAeOLs+cVuuNF3rcbuVwerFUmqN7PZwt7FxulNtQKOX1chFrhaVubUQD0K8aRae6GXf+QJWEVmXH9aCViXwi6npUWZPAHeui1vqlvCqa6/f1bu/WswPOJ1FlEHhbxOIYSYEol8AnO1bOxX1Jjql4KwJfWsJtW2JbQ3Xc3f7izxDFWmV6opXcatGaClburk4UBmJnnShRwvTlpXQDDFeVTWPWphGje6s46DGmwJfalbVMoq7KoKmMl5Wuwbq8RUQnVomp9uJrc92a1Tu0W2RbMSAZKm0wwgQbH3e9b5sWW2LzubF2NbHuj1UNK4N6lEfb0E4BFrLIcaViAzsTsOWFJj2ey6KZtS85Zj3bsxJt7Q9Hnew1Z3EgqsNGmu3ivuXmEmIZ2PVyHQyxwFdz6hampdMXpkT0C0FXbLGlhGPH8e2Gi/T6vKv1NrhcT4W6P6TFrsazFTXqaDtePFLwPRJ1YdZI6wKP8UMXnM7AyzeJ7s94LfHCWMjcfmxXyG2QOrgs4DTb7Pq5RmLns3zLj93Cu62vZCHsEls2Z0p0wlOkaKztYT1ed2GrucfLLbLjyEltRSFGltUwJRgDoqFYrdvyjmt1863v6bTWp0xe0RzKRkPBrgKWEBCQ80MpFxzBg4xw+Suz47q1cWC0k3I+ODVdHrar6LKxtw6dqJsdOrPOCLJAqOGap/VlOGTpBlwdA9psy7VoikrHw7tSIskyxszhjMcCXvv2hkz2RtM2cxheWdhCul5OiqnjLGLAXXGxg4XWFTW7W2ZVw6NCvJLRTgwltV1tGDM9RgGXsv4sNqWW3qdXGvWd0zV1hmubB868WV+lhhMLtxByb25vBXqnwn4faeRxcUwynyA1XSPPaomtaU7QvBEoRLBqUTebdbDcNLo590QVqersdlvPcu540/eyWMB8JTZgmD7kwaWggk5YjcS63o9rrb5qZN0EcksFfjSjLTYUd35V3dalZkWotGDDaHktqz3r1pJC4oeSnRMEyc/VJj/WOyEKtpzpGqm4ncnjLk5ubCMoZiLHuBjXZMyWiyoWzxo5iJpApymDrYT2fIO3mV5yMW627lasjM2mVc3FlvVGcicvloOJ6SdTtfuV2bWHbotE8ajZRue02LbRkF2H+7fZRaILfYVW7YJiuR2mrfGjbY1rCYvPGyV3fSrlXQXdtETG9dTCPi4bI9/HDkywLEafXMXJiLbzw8Ml3B3ne30vFsbMl5iZqUlpNOY6fAY2+XmcL4WTpjDuKduUW1SKcTZPMla5bdDwYjnrYK/FCoh3XOU6DyO4liK6eOOtEdAVsLW1XgVRtpOUjePy7C09rcGqj7Sq7lJQMmY+d6GcRTiQgcmkZuBYgVBtLi7Yp4qrQDZ7fX45iG13TQc/vRY3T1JYmdCxNTJWBSxR6dGCd3osezTTJ1sm78XOX409Oj9eRAwjF0Focex6OM7hGazOdiS8XYw0Te9hHIYPu2IgT/h+H8gG582sKo2ZZdpfKA0XVmntDEe+nThXF9NgODXjuMa0IVp1LRNRK1279lzrnPmqzHalzBV4KJz5KEZVo755J/KYhcfUmPfZjJ+VeXkVkmPOXXxsfmgvHoV6C0OX1WuMWrPjMOJDZvjCZXmV3W6oAfmQfrT3D8lFLdnYiPHCpc7ZauG2Rqm2poomubuhKsRWYjYIZFwoHGIQW1oQ+C3YA2FaSWCXPjndjNnWQUt7rY/MbevK2AXDM9qHIzOqTEHsDyKbsIWWyLe0bF1cKdsFioo3AY8ENp7XXQ2cZMSrPTo3JPQa3XTCzdbeebj4c9ZdKjczoA71eNikpWkGkcKGRAWieIVK612LyeerWW4KKVjxq4MUUxvVz+EjQzs9L+SkhV1AWAsnTiiSAZXts5qwwcnc00u3571lrOkqckrTcTTFLLuzWCWczFZsONxSqDXTSFfZjviAc5aqdJ5XsbE4F7Z5UDh5RV6ZwdthJ06mLDK5mnq8CP0D2yKCfOHpI7xBl1Jpt6ojRFqLVbmCL9JDubAwUBMMiquWcEk1IKauMm2chsBlkgo7n1xbmd3Qco0XOqdf2o4S1qZkprlOxKUFr5vg2qgWd/I5YuXJqMF1uZYYmouw5KWxS708WDs+QBYccklkDNReJmovjRrCWI0l0nhKimUcwJ0qEcbS5pckMnpJfMnF7BAsDWebnVGCtnSjURBSTuTCYcn92ofxLYYLSHMUy1i1tICOQ5W2C2l59ILSpNFZaxJXSvfPoV34GbW4sIuNXvp7zLeCWjbzarm+Xjao1CI1f7owAqcsa1RCxwyjACkeLtuBb9ZRvyp4RaXEAy3PfO2IoMnyVOWxU+PwDvRnTN+UK5I1kkOWr3Oqigl9u5l31m6pdF7YOGGOOyUyUJ1cpVjhuLfZynaWASvMmk7gA2c8qWrsHgtqtz7vJGRzahyMinmnHqUoMhPG8PlAx3bmXq02e3lVdqnq5YbTHBJh0QOGpfnDsFtUSgbLF3VWeSwirLHLaZ4PFtajt2SRW0prBjNnpyfmMlyH0jltA+Da8HhlynAoAwCnKKMOydtHArmdAT7HAjNExLz4gYBJ7XF1bTKNLsY8O672bqZimiZvUN2tFeUq0NmxWutxSc2wuoWV1CuY8jyOp5ZauRV5tkLM7o3RWWXcuLGbch+1Gj8QdbnewOVeSYlxaxltgjCeeQ237gBwKHB8s91fBZzu1b5K88i5XpRayThiPQS3iOtjdmnQJLtf9nm+GdJ9a9+M9Bhyw6JitgGv+01iovg+He2Djwvr3XBYYvBVINqWLOzKXZ2XJkIgnNFZJKJq6bLj9CY4zhg8jjcDY6mFqAfHY4jrpuJIA27K0vbEGpqy9/m4UEsc746sSa4x4UJytnIV57lwGi41pjdMe7mK6Xg9+/YsdpbFTD4ahiIc6pQfac7D59WB1IJ06xeYd0nP1I1PCW22R5G+dzBUrsPTMVmRUZmB1sZ01JrVDJrqe+M4528zyt3m/DWQrG6k+Qs5myt0d77yuTIygWRjuhGCHvCAwVZo0V6pu3kUIPI6uV52WWRtY2Tp3jyTA2We4ARknFXtcR9lhQXHq/Xcsg+qPHhi2XIKuRx0bMPQ+VYOqnnGbLQSuVRozEVhOji6HW8QMZOcvkOclb45YcySYpZ6SaK9m8mzfm70O4WN2V06HmGMi0nnEuu5haopJvJEY1kG62jHQ0eYiSHbEpxFtwUht+c2iXru2m1ZYM2pavYktYy3AemmrJQ2B0BTw5LFZpW80Hty1eE8bVAJ2dCNn1BuXYoFNq+yg78SS6qjm0ogYyFEPNzuQBjJ/qp3dYL0WNG2lV4YTe9GREW836UgMJVrIoSF1fFBgXgjQ2a9hPO5UHkrF0WQFYbaekQLjsYyQxftWMzgBGfk6y3h911+nG3D7CiYpIO3+KlkyH5j7K4M4hLn4LRDaHYuhsWeNLbrkMIXxc3cSzY/mpiAHwucplAuJOia9ocm6PhlI0hqLSw7obtseruiHPm2aBbw7KbDJ4cfqpXaUjc4socZnYGd8pqezeXrIvGSRFxKjsLykUEpcu8stvJylXetre1sRtpki6W9O274Tod3FQvaREEQK4k5Icg8mBeqs+mVjPfTUVrF7kEQqhbfkcTmwNiolLjZafCuEVNZmLKXb+U40xB6yLblethjMqeYIT5fWWcyDLMxunHzCnQdV3I1k+Rr1/b0nK/tAVUQNiN9dxHqQwOYsB6Vzb5b6Uvs2l/RzLfTZTgwSkW6oSOI+JJZbClKWA7NARY3sAEvLvOFHIWHNsjhwNCCqB2XCDZbIfS2oaXBS08RHSYEfYnGaIn11ViPBjqnDyUiXrEs85Ya7RVbxxFxgdhW3UFeBGnOMHBDtedeK+Y7jqqZAbQz7A5bV8jeVUDdXzg1vKDxOFz2JkMfENoLW3Yjkp5apoZAxwx1NHHyRsT75UZlA9UdO5AvGeG7ORruO3FOhM6SKAyxC7wZH6iNsspAuIL+ayYyt9WM2Jan/WDOOps2WUICiR2NOzVIlGVXIVjv7NWVFfZltZ3D+fmGbtCjKsALztnZp8PJgIvKFex6gR/m8h5nVXGM4+7mjcfL4VwusTPdtBazTLRdn3Y8v7iBaqGH7ZraCFVsVrsOi051ONaZbvE7WiPYG0JubreAnHsYPxpVII5V6zMS29yqA2psvRUjGixigyKUoS0Hnyiq3O4zI6UwGgs5Od14mWuu1k63zMHgkNg5/YLpVYnST8qCbRfilYkCn7nB+7M8Q4KclExszutrUfWN9Tk/EkqK4u16PecPCt2gCDE7bgbiMt8lLTbAdZuJC5889xGvnccLSbiHG5lvFyy1xWfbPgG7fXQ05z2yb2iebhk/5q423szyvZ2VWz+A4cG9waEhkLizbLvCXRDsMr7SfaiuGZQwwquOmx55xnvnahWr2+ZapBXe72db2uhuobXM+V1gFCVR+34WntbCZpid29MF9TxzAQxfNhlXi4KgzyWt9DNZVhP+BOeOcT0sF8vA3Z2CkS8qou4XqxTfJfsZniUj5TWddG6qNvDg7eWqRYcdLcPmQEsHDWyEwrmXyI5xk7wdCCanZ2qH13t3v26ORwfnqWpIsnws5UxOreMwOKvtUF1wSud2FaY18nwxLOeuuexn9GY+F2dSd84Z9oyaiEIfZ12SCnXdxtRZxllcLFqWPsyzEnfAXugmitZZtLjDht5GRXSFdZ47wbqQii3mpTONd+Aq6bcbxs72PdX23E6xLDs+8ZiYnhWJOW/1Q6Z5inOrYFPcZpVHdiqycbF2dlyBIpDF8Jw58CCQZnnBMMzfXz6+TAfVz+Pm/9V75unU7//Z4ePjnPDtddT9qBlM+3zX9fl/Z96vH18qJwLGPQ5e66QNnkeT/+nY9dNfeaExSRoer3Snt2m35u3kvgEN7mR3lLktGDx8rfOkvR8Cf3yx23r6pYn66/Ow++W+2LSYTs7/uLjn2frXJv/6fCv2Mv1Ww/SOyHOjx4DpNnieSn98cQfgwsipv+IU+dWrimnVz3ck0wHu9JLk5ff/ABZi6Q0YJgAA -->
