---
name: "rar-cowork-cookbook-teams-update-define-notification-templates"
description: "Drafts a Teams channel post on define notification templates status with an interactive Adaptive Card for quick triage."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/teams_update_define_notification_templates", "rar_sha256": "e5665b7bc9bd947c9722eb48a52d705f3be268dbbe5b6c6d24d86a041e53f3f3", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "teams_update", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/teams_update_define_notification_templates`. The original RAPP
agent is preserved byte-for-byte in `teams_update_define_notification_templates_agent.py` and in the RCI capsule.

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

Define notification templates Teams Channel Update — Drafts a Teams channel post on define notification templates status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-notification-templates
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `teams_update_define_notification_templates_agent.py` and embedded as the fenced Python below (sha256 e5665b7bc9bd947c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `teams_update_define_notification_templates_agent.py` first:

```bash
python3 teams_update_define_notification_templates_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 teams_update_define_notification_templates_agent.py   # or on stdin
python3 teams_update_define_notification_templates_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define notification templates Teams Channel Update — Drafts a Teams channel post on define notification templates status with an interactive Adaptive Card for quick triage.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/teams-update-define-notification-templates
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/teams_update_define_notification_templates',
    "version": '2.0.0',
    "display_name": 'Define notification templates Teams Channel Update',
    "description": 'Drafts a Teams channel post on define notification templates status with an interactive Adaptive Card for quick triage.',
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
        "upstream_slug": 'teams-update-define-notification-templates',
        "upstream_url": 'https://coworkcookbook.com/recipes/teams-update-define-notification-templates',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b4f6d3c36cfa81a1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/manage-notifications-alerts/define-notification-templates'], 'recipe_category': 'teams-update', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/teams-update-define-notification-templates', 'uses_skills': {'custom': [], 'ootb': ['Communications', 'Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class TeamsUpdateDefineNotificationTemplates(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'TeamsUpdateDefineNotificationTemplates'
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
    print(TeamsUpdateDefineNotificationTemplates().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6d7OjSLbnV2Hv+6OqH1UXJ5CoiY5YkBBCCCGHkbo6qjGJEd4J09vffRNJ91b165nZmbcbsVwjTObx53dOJvr9xWrqICtfvrwcgZUiohXHYQBKxEpdZJ61WRnBjyyy4R/iZGldhnZTZ2X18unFBZVThnkdZimcvigtr64QCzkBK6kQJ7DSFMRInlU1kqWIC7wwBUia1aEXOtY4CalBksdWDSqkqq26qZA2rAPIGQnTGpSWU4c3gHCuld9P5lbpIl5WIkUTOhECJbF88ArlAJ0F6YDq5csvv356CeH5y5ffX5zYquCtl7s4Wu5CPou7DNsfRDi9SQDJxFbqw/F5D+2RwusclJBbAm9B2ZHn1ccKxN4n5D//M2qt0q9++vI1RZ7H15fx59BAvQKA1JlV1cBFHCu37DAO6/4V4eLW6iukBHVTpqOpKqhE6r8+Zn6nlOXIz+Ozjw8mrz6oP359yaAId6G/vvyEQDN8fSmb8fx1pJJ//Ok1zlpQfvzpO52qsa/AqUdiUOrXb8/rJ1k48PvQ0Ltz/RlSfbjVBl9fflBuPB5yj3rCmS+v1yxMPz4I52V2A6mVOuDjT/+IrBMAJ4rDqv6X6P7yIBwAy4U6PQX/6dPdyL8i6FOhd5r/mC10b/rvaAKHv7H7hDwN9Y9o3+3/X0jHMMKqd4v/XXJ/bwL6M/LLP9Ttn034hHhfXxYghhlSWnYMviC/fzvuhPkvH9zvNz/8+gck/X8kc8ya0rlT+JZYaeiBqv727ZcP1f32h19/+dDkMNZgPn1ryvjv0fx7dr3z+ZMFn6M+/nku5K+lUZq1KfIe6cjvWf4/yj9eEd2KQ/f7/eoL8mO+jAeKjEq8MX2Y4IecqaCsP9jxp5c/IFKkUJvGuT+GWf4f/4EooVNmVebVyNHJmhqBDq7DBIzCn4KwQuDvmNslgHatQmjY5zgY/6OHR4kzD/ntfzp34PzsPIETq0cM+tbcQejbAwm//YiE396R8LdX5AQ5ZGXoh6kVIwdut/uaQqBL65F7XoIKlDeIK3Zfg88QkT6PJxAwkd/+dSbf7vRe8/63O8yHD8Q6zKURraomBq+jxkYA0qd+DsRk0AGngazizIFyeSEE3E/QElUWQ2yuR+tUURjHiBuW0BRZ2d9pQwt+GYn99ttvtlUFX9MHvFLIo3RUGBzwLg7y+TNU0ItDP6i/psAJMuTD7398QP4X8s9m3YmPPHYQ8J/+gRKuj+oWgfnWJHAYdB10NgSTu39+/+NpZkgmhbUOehNaCTwmw3iNgPtm8+OK+0zSDGIDaGto5yTPyhpiNhLWr4jkIe/yQqbjoxHVg7HkuSAHqQtSp4dULajOuyWhT5AKeqTy+k9IU4E719/s0rqLmMDEt+rfEGW+gzUki+G/Ucz7IDg5S6E34/eIeNyHRMoPFcK/kXhFtmOEIrlVWnlQWk8envXwC6wdb9MhcQtJQfs1HcsmGE11j5WHeeAgaBnn6dLPo89hD5BAbHCrN973MdZY6U73ild+TatnKljl6AoHlgbI1G9CdywQf3uGVBVkTeze7QclHSk9veA+vXKPwcU/7Roencb82Wk8ajzytSFxYoL8f2pHRqE5UTwIIncSFoiwPR3OD2OOzdNo9Ee/BfuB++R74nzvEd4Q5g1ov6ZxCCOj7P/2GHl3wXPMA7yaElrswB3u9KH/oTFHuvfwHMOtLMfAtr6mb4j+CdrkDl9QY5jLMNbHEHtjOD59kzSACTtef6/ud3dCtWEAwBBE8saOYXh4ALi2NdogKMcUe3oAxioY060NQif4k1YIpA5DAtIfXRFCN0HUv5sO9mbBmF1emSXfh4djzwSlcBsHSgu7U/CKGDBLxkipYGrCxmccA63w4U4KSQC0MRTx3cJVYOUPYcaG9imgNfoiS8ag+cEDz4ff4/ouyyg+pGrBEIO2bEfEdUH38Oy7nE9fQWGTMRPvk/7s7qeuyI+l529f07uM7yAPEzweq/YPxoGxWcIoHhF1xKcKYkwCngEEI+FeoF8fNfZRxN9l+fKXLv7jv9fo36um9mfPfUGCus6rLxj2qHRvhe4VogMGYyTMQfUoep8f9ejzI98+/5hvn9/z7U8cHgb7gvx7Uv6JxDO8vyDEK/6Kj482oQPG+H0e0Cjzz/z582R8+jU9gO/efobEiLJxD6vse8l5GwLrjl8Cfxz8KEHVWLlaWCzvmAv98TV9j4hnvozo44/1ssp+yON77YX+fbjvvTTAR2kNebtj9/ZY4cSj+BV4+ZI2cfzpJbUS8O+sbMY6AIMXWmVcGMFEgl1RHYL71XuHNF78eUV3TzGIDW72Zcy0T8jYzX5C3hvTT8jbUuG+CksbuFb6ZWyKR5ZwKPx4H/u+XLTBC1yk1X0+avBY/4y92LNH/qsQY4JBiR0w1vbsPWNHjn8hAk98H5R/JaLeT6z4CRsQ3sdKHdZvyV5BOV3Y93xCoA9hEsK8gnDZwAl/ZQP5lABiPsTdUd3v9vuuVvbQ5Y+7GerHIvL3lzf4ePrg2TDC4TBPP1djUcRgvEKG8PoRWfDZ/0Ur+aQEoQ82MJAUoBmGtqe2w9ouO5k67JQkgT2ZWTTpTnHao2xAMjPXtgFtMw7jkhN3xlj4hAA05cEfSO8Rqd/GHiAcpSMty5k5U2LislOLcQCF25QDCJJwpxTAaZbyZjMwgYZ6nxpB3Hyq/FBxtOd7Vzua5qn57y82M4EjV5NK4h7HHGN1a2pM7UNgsyUDzhcTk+xQYyy7XmZGa7gHPBUZfu33JzdLuaUbhWouR/miUoKp4W85ipR2iehdFJRVsF6bhAd3w5/tXCK2Q93TKQqASkh7fr1dWYU+rM31ibno6kXWt5uwIDan9UU+1kCeJsQkaa8zoosnmRN2+q7rSBQLcRCbS904bmbh7FjJ577i5yBxtQSPC7aQLYKoA6VfDmGt98XpqOOFk5cbfzWjo+Rc6LJj2EYIzAzyMuW6Va4xO2tOMXrZnQgU7LpdOhA9i80rs7we5LV/7mdCKTfbwtaIM0PpQbUljH1wpqmDgnXG2Vy6pFwIZL5VOkar3BZz2txU9Y0izNEiKqJGh1CdbohkFghCHLK6Lq9pQ1j2hljbUq/bCSj0antWsDI+5L1bKuu1dzYvKamuSpvZJAc3UrElY9BamSpCr8vxITxvdlvcb1wiVWOhXB/kM54mds8FFwdL+WxCyJTI4k6cnCWUo1frVRVGgtgIHTHEDlsP3C1ta70wLy7sBiwrbr04S/GVej0GhrwaQC8khmt0Yjksh5OY+9hFW4YFurDdrcQQCR1NTvuOPhrlukqxS1TR+E1hbnpUqhy20xhHsPZEJzRRtGa9FuRMUffMsTQnqLrk+zkLphU3LJieEuzAaZotjiYbvul5fZJYqnc5rcXzotlJ/HKTz1vnetr1x74iL0U9u4WLPg8np+N1H5g3cVcepQ106ZlYbK+bZDdbT2ggW6eb0PXB5IQa6pKec0eWWGyAxgZ+73VX0QoFUtfNc+fE6zaoTreeVYbdWRAtYXPRZoVcLunB0SiX1ogp4Rk3mYS1aaXq7a1zTiW59gLNzK7TiU21q5qe5d12WYASa+fLdEayWJKi65hWzSJruqFdw7hH12DuVlpThFXobaMobAhGt3BUlvakuThnQOmSyjmm4rlepT4zkfaXgqoW3KqIj81lTy4JTVNxZwhEYzPIcte7XBTLfoZzxwVYZ8Vln+H+bLlwTkoot/3+fFmGnaApRZhsFGY95SbJJqUaty1uawKd9BJu45uoDWS6EvbNZilg8M+Oi8ikD4SMXydpPNg7jSQ7h3eIA4XP1iU4xiuV2KE6Fmzl7TacLI8XcXecrROvN81lWd3yar4Sm6QNmWFtxetBDXanZmPvqTqTpLXtm1Qhrqbu8nDCiAxXsZ46lg5JBHvieOn5oxNgx/nULQp956ImDXr1aLrSMWMqVzBNDCe0ROtMs4wnc5TYNoY6qLfauuiYhjfzG3M9hjHJhfXUUC8TfI5ny5w25UNYYFLYmPa+3fCnQRGGvQkCerafxLQQNaVAOLWvY0xoXg9sxu4xVbaP9KFYCiUx7zNhqSvG2t7b2yvtaS06mcQcZta+UcW875OXs5sYWwG9DEuh7ucuNAlOJ6ZaVbSxL1grkz2N6FRtTeuk0ohuceywnXmxiIQ6NdSulnOHPfpDYU8ZOmNEYO79i04k7mqu4nPyxqTdiTwOIKKmu6CjF5OcxtDIW2DCaoFmfI/hoNrNw6uwsNV0Rjgryt85KeecQRgx65PEttqQJINYFbmsHdELt7XMTFXUU3WisEnkcKEJjPVxKLYpBL/VSTYst5rUHjnt7Y3L8f66WggZry0PjXaysX2wzVFO3EQXbcF3wXp+Lirb3RzrhGRtz1CLxUHhJn2y1PTzJcn3W2JXhbxAs22zEnP+KOXUsF0qECrXN1vQzvkUb8tQjK7XeLYs5yRbBKRzPUtTPHESLxTsBUVPm/SCeluT7vfHq1KfF3pNefikkOh6ZlHyQF22rbShJGa9TTwvLHnr5LK+NOW5QY521w2he/lyFplmr5Wop7PAnaVhPdPqxVVRWdZI+Q0nY+FhHtys3RpG0/5og8x0ytOOowzJOw/qelW3kckd62Uj0dacArbayH5QHOgr0fH7/IhPJeOKetxkSINK27KWzx8srYtzdt+q5dHTSUhyR/Y1fWH6aWNKKUdnq8vep86NQhjzzu3cFK9UBdV1YnOUmH0g5zV5tGK3XZnGtuipYh+fbZDq5/bM8gsuJGZywhLLWDzUrCJMTgdb9hzX2Wt2drssSdAcen277nanveVSXWl0zSa8HBPbXfGOsJEkQ3bzS2eSu82mmrobZ3DOjnQ6FljvTtJzG+Ua7W7S1KEnlVyG3gyXvdl66LxI6OZGecJxNdaONr+M9MVg5BaVzL2NttjnNys2m/myS7q1NWs2VxHjPDQ5qJyx0dv0sMXKNsaVxphuygLkhcxLq2rLBrvWInh9ph+iqmJO1wtYyddldslMtRWXnm4axfUU5OFWXoO1xjWZfFlhwyxbFaxyiFxJX9mqwm/O+YWLN5ltikqc7FOxqo77PZ369tEm44jHVJJ19qh8vBpYXNroOVxQp3oLmwh/hdXTjFmeowulTRKhDdzZciKeBewG0G7JiETQR/nsOGFVxomFmwbh+BynonAeAnNFVHtBSWknpgNg0NzmYOshLkq2siREAfXn6W4qFUa/5M4cGJY3dddMTTygLaHmpAW3Iwdsuq6XPjoVTK13nPgk7jlzX9PbmlEDwk41IjIOuKtxB3BdeXSPsldHuS6I3DwWkjrwFtpFWn8SzqUBWOaUgjOoqLi33cFid6pUHHAmxW81bpetKVroXiK3t2Ea5nNhFSz4vW9T+1Vbi4zuXKXJKpSIuW0F5sQ6MVtjMxtUK7Wsnuf1CperC8rERnIUGGtBrAxHsuNjKZlrfB6d+2keLdesLVNDk7Cwbum43XmNvrmubu154BR1j+UNvdbEwlL1RUMfuWMQMSfFaFbrTQQO55SOmMteTAtO4DKwCfjG2Fs3en3T9G1TF4nRbo6GHUEImemxzbbXZhXnqkzUQu/snXYQ043ZiUpB9+HFR/ENRdTzIIoqU0zCGTgGAF2ZBH/QD76Si5oL1N7oVF01LslG1Iwp7PpJYcK6/uyk9G7FNOzqEob+licvEAGqgxHrTtWDnNhcd6ngpkVBU1VDHZNdNWcDS/Ra36tXu6t844iKL73OUI6LS9NNi3A4XDdhRy5KVD9qeuK4GcOcTls9PElUf6wnheE52Kmohtn0sOPEgTRk2EtIPhOv1u3a1Yy13647kHnabssLpBYfhjkszsK6MarJavCvOKqZqekAj8huaCQ4RiTCIpoDyd2aJ4onV7fFAZ/hS3A70sRBM/gm1mu/QjkqisSes8pcJXyFCajLvmhS+jLRMlct1mspspyctVP9enUn1+kxdo5BuadEa8rosl3nTuuGUksHok4Nm9xUJp5gw440hhl3SzhqIBUqyXlFnG1mKAy7ZH6ws8KWyyPEpjn0S7TgtUVtoWcxQ+sWVIK5SYOwq2bdVZWzI5oeYPsqcksDUKazVLF5ejKuub+npEqyE90IgGKYqkqIFIppRjusYt9f79RW3gn4Ls7mWOQMSlJM6eWWJFHYuycJlRMzkeVJxzYOjEnHm3hxDLpW5H1hxp+1834QxGEJFLzQFGZ/HdRT2ROXhmC9LLIyhcr4Vcbzxi7q+NIundLny+AoLBfLq1deBkeVNvJMlrJhsxMVEG9NXZHFS2td6MORstmoR3lqRR4acslQ6Y5jJudmleo1cfNUifMty2Lcgc1FZpnNOK0aKIllzo5P2a0zda3ZwE7HbnWnpcIUELZ+468k28Cl2pX2t+YEa6hbTgW8t4hnt26o4NqEDK5TlpisGDXep6nV7vU1SjOWHBMr0acnyrb2fHd+BWFO7ajTqfVs7WrsavyyXy3kUorcfSXLbnqQFh3W2cqFkXknouPY9exru8MCX5mE1bylFga/M83G5sppVGZodfTyAbO2XOu5q9u8u9HEBt1bDeuNvSjp1gQxJ+IAdflWrWoqpq785doD2EVjHUpik3krG2fLI24Y7WEqpdcZylxQ0SToMLZlTAzdDnA3vN0E+NILySTRFil/nhH+oUHRuacstag9N7SpFNV61c1xqXdm3U66wuVDMuNs3tGu3UZiVJ694X1DOFNJO+PLxmzMaiqecMffXsT+sOdd80IP5k1WjvLp3Ey2sq3IWGaRnrKtUEMSKOdmX660hHWMMhD4cjja4gxotZCjFOWd9Vnp3KaYhJu56Rf+rKN4rL9db1wLm7EYrg8a8nppJyC8uiJKo8Esdb3i1lXeBT9n82mm7ibrVJLKWevUNx9Vuyk7MGleSc3kclBRrpr4diUzU+jGM9pXNZtPc+K0D2c3Id2tNm5vSbMpfVIcgZjP02nqhiSX7wLFLPC5JBJXYW9Ju/2UlGiwd0lihjv9Xlgtr4vZ7VDLIiOZVEKDxrqsiv1iQsf2ahdr5915Y/E7CrT2QrhNqsFMYSNpVxwK+KDUZDNYYDAFABYPXoN5NE0K5yZAs8XsaFkGix0am5QkadEmLX/y4/lMmcznuMNsFJC3t5KaM2VuJ3CFUbseLztrSl+0PKY3rUotp5FUdRoVYpcBP1Z9vVjbGy+WyZS9VpHF9Xsz24LzCZNEg04hyGYa2/C3JvHAeh6utvhWL/3dsOIaVD1UszOPrfhQYYvJvGKYTbtqr44VXvUA6raI/VokM5LG7auH500S9DlRNnnDZgfnEqQlZXDdajnZCjYBq8tOEX1JNtkNLqHXcFZ1/mW/085YkuNevZfVEwNusrtnY4qIFxN1dj5ZqTlfeAJfuDQ7ab05azvqTegHy/bIXaZOHYLqNntp6NuB8qihNHbyYufuwmG1mTZiOvWChDUtaXDxAPc9YnG1ywzMFG4YC+6Kmg5SN2zQjg4mUwrf7GfBmd27533Rcxq61V3CTWBmdTOxIiOgxAVD91NoBgsTsJbYcjMxWu90duZud2yXhRDrkkVz2rvAzd2QoIjytpzFi60+UXB60MLTZgUb5swhbwK/4H13vfcHByedxgHB6hIXaAKX4HmNkgwL1IYOlAm2tKLDWYxsykGnJcGl1cRbdHtzWZ+o0LspO4Wz4QrY2ZwC2+ZXC0YplGzFQGkv0SFdVFnEd2xBTojNAs+ZNVnRllK5K9HRd2reqMPNnxIoz8W94eJ5a85467pZrWNQ482eHfppxfa79fR2kzbXyvaTJZYEc7russzWsD7m5RWTzzqcvJJU2K0SdtvwdLtwJ8nigu5r+bQ4uUE3b/EpOAjzWa817oGWdiLFVhO04qYJqrYFuJE3CTRtNkmx9nI0VqxMhxHHcT///PLpZdygfm4z/zfeK4/7ff/Pth0fO4Rvr6DuW8zAcr/ceX357wj366eX0gmhaI/t1ipu/OeW5H/ZbP38r7/CGOn0j9e349uzrn7bq68tf/xi0kuYuk1Vl/23Koub+8bvpxe7qcYvR1TfnhvcL3dFk3zcLf9RMXhpuUmYhuP71W919u2x6Tzev7+aTIAbfr/0n/vRn17cHrowdKpvFEN/A2U+av58NzJu3o4vR17++N/N/sIFAiYAAA== -->
