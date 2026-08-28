---
name: "rar-cowork-cookbook-ppt-exec-define-agent-skill-sets"
description: "Generates an executive-ready PowerPoint deck on define agent skill sets status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_define_agent_skill_sets", "rar_sha256": "20ee37d1132e2e80d04422471d93fe78309a889cdec2a0b1ff4e22ef5a2ac766", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_define_agent_skill_sets`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_define_agent_skill_sets_agent.py` and in the RCI capsule.

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

Define agent skill sets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define agent skill sets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-agent-skill-sets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_define_agent_skill_sets_agent.py` and embedded as the fenced Python below (sha256 20ee37d1132e2e80…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_define_agent_skill_sets_agent.py` first:

```bash
python3 ppt_exec_define_agent_skill_sets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_define_agent_skill_sets_agent.py   # or on stdin
python3 ppt_exec_define_agent_skill_sets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Define agent skill sets Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on define agent skill sets status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-define-agent-skill-sets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_define_agent_skill_sets',
    "version": '2.0.1',
    "display_name": 'Define agent skill sets Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on define agent skill sets status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-define-agent-skill-sets',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-define-agent-skill-sets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'bcca733912a2e7cf',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/define-customer-and-employee-service-operations/define-agent-skill-sets'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/ppt-exec-define-agent-skill-sets', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.5, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecDefineAgentSkillSets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDefineAgentSkillSets'
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
    print(PptExecDefineAgentSkillSets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6eZPaSLbvV9Gt+4fdF7u0oAU8MREPgdAKAqEFaHe4taQW0L6Lfv3dXwqosvv29J2ZiBvxVGWDlJlnP79zMlW/vdhNHWbly5eXA7BThLfjOApBidiphyyzLiuv8CO7OvAf4mZpXUZOU2dl9fLpxQOVW0Z5HWUpXM6DFJR2DSq4FAE9cJs6asHnEtjegOyyDpS7LEprxAPuFclS+OlHKUDsAMCH1TWKY6QCdYVUtV031SfILMljUAOki+oQcUO7rKu7VLUdX6M0+JzfyaUZZPkKpQG9PS6oXr78/Munlwh+f/ny24sb2xV89LLLaw7KtLozXYw8DyPLA+QI18Z2GsBJ+QBNkcL7HJR+VibwEZQSed59rEDsf0L+67+unV0G1U9fvqbI8/r6Mv5oTYrUIUDqzK5q4CGundtOFEf18Ios4s4eKqQEdVOmUA+oZgmVeH2s/E4py5G/j2MfH0xeA1B//PqS5aNpoZ2/vvyEZCXkVzbj99eRSv7xp9d4tO/Hn77TqRrnAtx6JAalfv32vH+ShRO/T438O9e/Q6oPjzrg68sPyo3XQ+5RT7jy5fUCTf/xQTgvsxakduqCjz/9FVk3hD6Po6r+l+j+/CAcwsCBOj0F/+nT3ci/IJOnQu80/5ptDt3672gCp7+x+4Q8DfVXtO/2/2+kYxha1bvF/yG5f7Rg8nfk57/U7X9a8Anxv76sQAzTrLSdGHxBfvt22HHLnz943x9++OV3SPqfkjlkTeneKXxL7DTyQVV/+/bzh+r++MMvP39ochhrwE6+NWX8j2j+I7ve+fzBgs9ZH/+4FvI30muadSnyHunIb1n+H+Xvr4hpx5H3/Xn1BfkxX8ZrgoxKvDF9mOCHnKmgrD/Y8aeX3yE8pFCbxr0Pwyz/z/9ENpFbZlXm18jBzZoagQ6uowSMwuthVCHwd8ztEkC7VhE07HMejP/Rw6PEmY/8+n/cO2Z+dp+YieZ5/W1Ew28PvPt2x7tvd7z7NuLdr6+IDulmZRREqR0j2mK3+5o+UBHyzEtQgbKFaOIMNfgMcejz+AWJUuTXf0b68eA1H36942b0QCdtKY7IVDUxeB21s0KQPnVx35EbIHHmQmn8CCLqJ6h1lcUtRLbREg+s9qISqp2Vw502tNaXkdivv/7q2FX4NX1A6RR5VIgKhRPexUE+f4Zq+XEUhPXXFLhhhnz47fcPyP9F/qdVd+Ijjx1E9KcvoITSQd0iMLeaBE6DboKOhcBx98Vvvz+NC8nA2oRAz0V+BB6LYWxegfdm6YOw+ExQNOIAaGFo3STPyhriMxLVr4joI+/yQqbj0IjgYVaN1SwHqQdSd4BUbajOuyVhYUIqGICVP3xCmgrcuf7qlPZdxAQmuV3/imyWO1gvshj+N4p5nwQXZ2kEzf8eB4/nkEj5oULYNxKvyHaMRiS3SzsPS/vJw7cffoF14m05JG4jKei+pmNdBKOp7qnxME8wVu7Ifbr08+jzsfpCHPCqN97Bs7p7iH6vbuXXtHqGvV2OrnBhGYBMgybyxmLwt2dIVWHWxN7dflDSkdLTC97TK/cYXP1FL8C9tRE/NhCrsYH42hAYTiL/X5uOUfIFz2scv9C5FcJtde30sOjYKI0cHr0VbAAQGFaP7PneFLxByhuyfk3jCIZHOfztMfPuh+ecB1o1JTSbttDu9GEQQIuOdO8xOsZcWY7RbX9N3yD8E3T7Ha+g6jChYcCPcfbGcBx9kzSEWTvefy/nd5+W3qg9jEMkb5wYxogPgOfY0Jh1OBr5zQ8wYMGYc10YueEftEIgdRgXkP5o/wiaE8L83XTbDKoJU8wvs+T79GhskqAUXuNCaWEnCl4RC6bKGC4VzE/Y6YxzoBU+3EkhCYA2hiK+W7gK7fwhzNi8PgW0R19kCQyVHz3wHPwe3HdZRvEhVduza2jLbgRbD/QPz77L+fQVFDYZ0/G+6I/ufuqK/Fhr/vY1vcv4ju8wy+OxTP9gHARmV/KIuhGkKgg0CXgGEIyEe0V+fRTVR9V+l+XLnzr2j/9eU38vk8YfPfcFCes6r76g6KO0vVW2V5grKIyRKAfVWOU+j+n3+ZFgn+/6fb4n2Ocxwf5A92GmL8i/J9sfSDyD+guCv2Kv2DikRC4Yo/Z5QVMsP7Onz+Q4+jXVwHcfPwNhBNh4gGX1vdq8TYElJyhBME5+VJ9qLFodrJN3uIVe+Jq+x8EzSyBUpMFYKqvsh+y9l90RXh5+eqsKcCitIW9vbNICMO5e4lH8Crx8SZs4/vSS2gn4p7uWEfdhnEJTjDsdmDOw46kjcL97737Gmz9u1O7ZBGHAy76MSfUJGTtVCH1vTecn5G0bcN9WpQ3cB/08NrwjSzgVfrzPfd8FOuAF7rrqIR/Ffuxtxj7r2f/+WYgxl6DELhhrefaenCPHPxGBX4IAlH8mot6/2PETISCIj3Ad1W95XUE5PdjnfEKg42C+wRSCyNjABX9mA/mUoGhgCfRGdb/b77ta2UOX3+9mqB8bxN9e3pDi6YNnMwinw5T8XI1FEIVBChnC+0c4wbF/u018rofYBtsUSIDAAJgyHo5PCUCAGeZhJEkQJIN786kPmNkUm9uz2dyFhY+wMQf3fRIQBPApm7BdhqYhvUdQfhsrfTTKBDAfTOc44XpTmqAoco4zhD33bJKxbQ+bzRiM8T0I/9+XworoPRV9KDZa8b1jHQ3y1Pe3F4cm4UyBrMTF41qic9NmLMbRQmde0uB0PqKiExnFwfGcUpHOuGC5jrhIVuBWra9GUXHbQeLwrauFg815Ja+Gq/kiZSShbVLAC/I2zps4qPgywm9SQrkTb5LCMYPj9heJLnKXNq/LxrTwtUdHnR47sqkKTXuty0IeTJAQtdleTjaJzU03iieofz3OzFtc5JplGkqyv5h6TlsH2rFRUTbWUuW3HVMbZl3QSXbhHDHfWAerqU1COS9x5UBL+skyicLfmTXP9o3LW6QVYrP2Rk289Ha9eak+O56Lm59OST+6mTl74CmpLW41keu2Ux0P8UZuvINxsNzwdEb3Gx+PN7BAy/t6upW321522/p08/pC35n6hufUco0XptT7qaKSkakajnRyjF3fXaXOsrKhI4KLy+BGfMZE2aYMy7q66m0nSebZwQhKyEgC2HhS02ASbdduEU+TSJOvB4M+Y7OQB/iUTzhmbcgZFjP85XheTwifoALd2Rg40Xil4KvisKSmklRVZcPzLo6vcnW+uYR+GyoKlgz0oId54bCoFfl7l8bl9als8VqWq4osObvdHLcbVxDQTVBpfOc4ebEyq/psr7HZwVAu+yvhzSuO7efFfCcOgbel831QHtYQCxQZ060qLfyi9bfXgppPV7nudjtdVZy2mR98zm7cJlFwescr3lE59HNmu+lTtjr369B04l48OzmqiAeb2Wq7mAmAqR6jk2KGyiW40FjkTtfFRI7SPr7xE27mHg+Xaydsq8zi0PgSufuAbL39cIu3Rn/eUTcc926VYxOFat8sV1Q4ZtZoa2fDsTxtbK1KVgeDS6aFkaRySNWDfMXy2M+j9HRMyGaD0VjbLfTuuJptBHKvbnx5o2t7oUBn3Cafq21LoRP+pF7cuUnhbQ2us2Qq1rQsRzF+suvzZrAOBW7l5mVPkZetcXLWa4HfnBJKwTV6OvX102LVyubimht5Dq4e2w95uzF9qVsJxmGdeX1E9xppykzQdYtgSxaRdCEuh1WnbYcNra0XsT3TzA3rsfKpXSbHA891rr6lGOXiKtlk2aYxkV54QeK1DS2mq527P0iEdtVVXqjYadZdyZ7bTByWSpuiGNQ9YV8c0mbZhj3E6ZFBJbS3LJ7C3bnE0ULvobdjVpq9abU9tuL4nOsudqGvHZ1zXX1zYspllB/NvW4c2qWTNsIlL1ezQW/4XQQGI+dww05pmubaTTyJ+eRcoDHDnlOSnLpiqhZJdEPRQbN1+VTeOiuyTu1NieOKMa35tkBt2mKFg4afyt2q3tZ02O+SIIlB7JU0K+eoWKg1EXrWMgiOFB1ctqsbuazkPr5WMkWQ3aKc4RzK0cz5EKqScMTsyFxuKEZExWWiSdZZ3zulz030nr6tEz7dCcttvlgLk4nROpJyBl2XHiT2em3E+JLfNs3WPg+JoBfJcdtqVL+8ipSJg+YQZlh/202pA56k2sVJ6atBgCz1OpuZzcsq2e93Cy/BE5PnJhMWQ+mov1Ba7Bml1brhZUWQk82WQeOTuBuiCTvwm97HJf60Hijrpnc7nnXPchijxV7CFePIRNZx5TXneENcBmFIt2ZD7IuIRDXD3xHzbmm7AxlLqnUGbRrom+u6iC7746xIpWqCudj+1G32IRNwB2p/Kmc8ZkWFn1VaXAiLVXBlD5vI20JvrNWK6JSG5vyVMGN1K+Y5Qz7xor5bx2mkbpi8wxaLXDLEqX7b8bLHg7VLOnNqmAb5gj4XntnJtBlCB9AnSj9P1wkZJp7nO9tort7M3kslVpwN8d4+z6eTXXG9drNyKl2As9tfhSDL1J3VJuFtbgYy6qTJdtqduEjiyMMEHNMURXHysKMOAnFWBCKYcCa7ZGAhLqfxdbEguhNt9NtVkrhdoWnLPMYaD2eTwHHoXU7F3MXClkomWS7KyWfWuCTz4mAMOxjKoNnvpDypzxHT6yd1OFaex6oyOzH7iGWLZbYvuUmd+OfA93jnsD1eLun1lk5daRUUhImRmh+r62UCiEPErYYB9pXe3hiuO4aRydnRWTKyQ0d5NGwAuuiZzKnrhnXhEyOZR+uar2y1WKUhyS3dqDhdQ1RzLZRnYvaiRH204tu1I1oNvVWjCgXSkA8UXzRoq8XKuZpWCydIuvyUR7ke21eHnk4mV4JMSI3cJ4o3jwVK7gPp0EdUwV20GQVT5nZgEkw/smjXYuwgbdbmfG6EeObLM4HZL9v1BsctL88CMcRzYILSvVbdJhJ4sjqut3423WwSN5Olg4u7u9lxu51JYn7Eam24HWK208xKDkTARleD6faJfbud1WnceSIv2eWe9y5ZaOO64x4qUsdu7plb5KIsOfN+lk2T+TaMa/EsrIkNq5yKma4C0r7hoSQmiygujoO/IbxEK47sDrKcnTBpSZ0nneIRWU3hRr01ZtPDso5Q3LPyg3BLvcve3oPIxW+KAQoFkIO2dLpct1oO3+lFKA3qmlwWFRDjZBNvsy01Oy9U6mzZon4yUpXziCU41dZS2GiallfyqVDl3KjJw8pAuURhKt877nLBwGR7cch3LXoSCEbpcr7qtWFz3G1Pi6xZDeWl8rbSVM3XprdmE3wOgYRBqX5WOT63Wu1zwcpFlVrYk545LHRBT6oZfbTQmXZWWibD6OOZ3kFbB3M1nysO7B1nayLZccvV5VxMyGKvsZt9Z4g8qndTHh/L55lZTLQk0BWDTVfGUe8nzWA0xbJXOKHjs74gUie5VTojiDQQD3i4smHZLCh1cb7wR2e7F+bs2qGmOlhaR7nYTqZObpBEyazYbsVed2TZWCYbW5dkzzhGwJNncNXXZYgZvXBNpMlZTQxWwrB0n7vFQfSM2eDjwiXN3byh/a10bvbH622w4na65EmQXMnSqpIFvXIS3ygLWqzMMJWlZNV1tX/gZP5g9K4dKelZ5gRS8ww01vjyYHiXoif2iXSTIJIxZFM368mB0eJwwlrk5LRXVcLUJ6kqd9lSdtS06irNCOLwkJuAukn9+iw3rVcqLUYlQUvjPrOiMmrGHqkCv2yoaJv000ZIdrGciRXlOua1KFQfl6UcbHriUuaeODX7xaWluPkaY5h4HWsJ2p5EkiM8sQp8bRCJXIvcpaKTS7a7RluIphBhjCrmo0RsssiACbW+bdOlsF/z/ryvcCz3NzTn7EjTd7D5RtL6vd2UXMDj9JGIRVnkapOfkfpJsA4Le8WukytlLYrBopJlRRtxvAxMteBnom2CfK2bcVwDcoP6UiWH/GK6PjjkkVfiXOzUWridLyC5Ufq1TDfqhNOXQM+3jJE4B1AxkBiW7YtdfXVWqqZg9nVgrgk7hR2GHFsitsjmcnzqTS0pwnymu0vDZqiuszYzkUQpSrjCDkcq2vlNIaKzSRF0uzwbQcIKk+Om3YSNvFRw1A4dmi58L3OXDd2Ly/VRL1La5RdzFAiJmWr5eYgafC0smADNdVTi9/jaVdZriZwrLp0ObKacTnoYkDP2dD25N4731/SmK4zNsL/oql4OGc0cSSLSiuaWBAtTQ7flTqmXLq3uUipdGF2+ZL1Ia8OKnq1WOc5z+NWM08BQOSKtAIdujK04yzqlKppj2dWid1Uqnyxyau8fo0WpXwu5ubaXjt97S9FlTQarT7Q5MySVKhp/vWr2JZmoeLQBM2t6nF6E+SQghBo3L9acsFPz1s0dOQWdupow0qT0SGfqCuuZaqq9dwlIaw6FoLUrv9bknigvO9s9FJbHrzNCObJnYcanYjerAAm3sfaKZNZlsS3qAWw2cRbx+KbLQeTBiBLQdbFPs2ydreLCxKlmt0CtpC7bw226cgK/AWoLlqhDX1ctOpV2UwBSNsjm1Wrbnqf2IfVjxrCEC9xMoTKxnAU2Rk7UjsL2HsNPefomiDN05aPT+IwOC4s3T5Z/RdF+AVNCJ46tX01a0d6Zinkguqg8+wvV0ViN5P0INjKYkLKMUQZJVE5CgQyXe3uDcnmyPXHLVHCuoQhOfnDQ+okOxFWgDmd0jfmCuilxTJ54jBI4Ip4cG+0KVuGtFmvzNITGzmucW7IDxglg136LKbIiqmi2X/mbRQ2FX+W9NV1N5irKzrbzGONvEbtm3FO7oAhr6p+OM9SNvbg675d7hmaFKS2Chllp3cZ019EO9lv6sR00ZT8hStdlbPRmtXiLAlXl3GKpFJPdiU1EMW27+bYNAB8wW2YOGzS5Odozb8Pa/UI5mWfCKe0JGvcOpU2dGw9DCBSC626nu+mOp483ht3uF+sJHTu7gDySutJ77FVxSU6vJCGXaMOotNSt/PkUC3u2Oy0YBWNA2Cy5hALHIgIedl3Qm3N/7ilOZcGBDnT9VglakJKO591CaSpYrq8uZkbJH7skj/g1eoQtSckGGNh1FxYT6EDtpUxySnRK+WIQBLtlESgVp+n1Ldgr7C2rwkJYTlpXL4q42d+ciGJmWz2UaQAWR1qmesZPm9KMxGSmOypI4kSqzgrrzDP+5peTrk9vEgvU6bDcofaJ4XwYyF4yv1Ul206jfQXdKpgnUUZnM/80c9nTvvMnXiLeLCXY6GVznE17fWPN5niNyXslDip1yGwydVgHa4Dpx7eL7l08ollrCQ9aT19xXut18lzQuz0VYAsW+Ji/N+mTR3g8u4ZV9DI5C9oEX2TULqTm4logdN9aHpOQXDdwd85xM1E5MHN8Q0629DD1/Nlsej6j86PWgsaeo2HEsWgz8ZlDBk5sez6G9W09uzhHZqdFk63N856xnQJ0KHoPD3bAsc6133ZHlLqc+k5W504jTo9Y6bahOGgeuc+jxWm2PR8LplrNvBunarUxOZUadjOnUeP7ut9HNptJ0h6UJVkAnwlNzuPTreOC0Ia7NmadNzIxsaK6TttWvlAFqZ1O+VyoVxdMJHfZRshkjj9hRsMJFzMb1pru9PVAeLrjt87Bu05sP+qtxUw5bJTMd/NJqieLXUjOdhFEky7zr4J1UoOF1XASLMqLYzLjz5x5pC/Ta1+wcHbGdcNM5ofp+YJl8p6x3Jat5reVe3ZYbEJaVbeboLWRdLzZl50+7e0LxUm122TkcXJbTpvtZKko81S+oaG9iNSJZar0VuJLJej781zm4LZxMIZ06m+LXbV0/UvaCfLSEZYdDTBeutpnhVtIxKQk9yhnCbhwNYDtQy0HlSkbT93TzpknIQAqBzq9YMKNrTVhTcr7xeLl08t4Dv08Tf6X3xePJ3z/aweNjzPBt7dK96NkYHtf7ry+/Osi/fLppXQjKNDjMLWKm+B59PjfjlI//7N3EePq4fEKdnz51ddvh+61HYx/PfQSpV5T1eXwrcri5n6Y++nFaarxjxmqb89D65e7Ukk+noC/KTEejNsV+FZn3+4vzN/WRun4Rgd4kV2D523wPFz+9OIN0DuRW32b0tQ3UOajos+3G6P1X7FX/OX3/wchtOUJpiUAAA== -->
