---
name: "rar-cowork-cookbook-audit-plan-training-delivery"
description: "Audits plan training delivery records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_plan_training_delivery", "rar_sha256": "8db79ecd5f0f2da17e756f941c86fb5a74fefa709aeaeefdec817119c4f6c1c5", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "administer_to_operate", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_plan_training_delivery`. The original RAPP
agent is preserved byte-for-byte in `audit_plan_training_delivery_agent.py` and in the RCI capsule.

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

Plan training delivery Completeness Audit — Audits plan training delivery records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-training-delivery
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
    "criteria": {
      "description": "Optional. The standard to review against, if narrower than the default.",
      "type": "string"
    },
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
      "description": "What is being reviewed \u2014 a file path, URL, document or system.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_plan_training_delivery_agent.py` and embedded as the fenced Python below (sha256 8db79ecd5f0f2da1…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_plan_training_delivery_agent.py` first:

```bash
python3 audit_plan_training_delivery_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_plan_training_delivery_agent.py   # or on stdin
python3 audit_plan_training_delivery_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Plan training delivery Completeness Audit — Audits plan training delivery records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-plan-training-delivery
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_plan_training_delivery',
    "version": '2.0.1',
    "display_name": 'Plan training delivery Completeness Audit',
    "description": 'Audits plan training delivery records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'administer_to_operate', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-plan-training-delivery',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-plan-training-delivery',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '08f8d19104add6f3',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-04', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['administer-to-operate'], 'process_tags': ['administer-to-operate/train-users-and-increase-adoption/plan-training-delivery'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'administer-to-operate/audit-plan-training-delivery', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.5, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditPlanTrainingDelivery(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditPlanTrainingDelivery'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'criteria': {'description': 'Optional. The standard to review against, if narrower than the default.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being reviewed — a file path, URL, document or system.', 'type': 'string'}},
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
    print(AuditPlanTrainingDelivery().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716+ZPiSJLuv8Lm/lDVq6oECR1QY2P2JIHQhQRICImutmrdErrvo1//7y8EZFb1TvfsjNnaoyozEYrwcP/c/XOPEL+9mE0dZOXLlxfFNdPZzozjMHDLmZk6MzrrsjICf7LIAj8zO0vrMrSaOiurl08vjlvZZZjXYZaC6WTjhHU1y2MgpS7NMA1Tf+a4cdi65TArXTsrnWrmZSUQk+SxW7upW1X3dfIsDu3h8XloprY7M30goKpnZRO7ny2zcp2ZHbh2VL2Cdd3enARUL19+/uXTSwjev3z57cWOzap60+MAtFCfSmyeOoCZ4FMfDMkHYHIKrnO3BAol4CPH9WbPq4+VG3ufZv/1X1Fnln7105ev6ez5+voy/Ts1wMLAndWZWdWTZmZuWmEc1sPrjIw7c6iAuXVTpsC6WQUQS/3Xx8zvkrJ89vfp3sfHIq++W3/8+pIBFcwJz68vP80AUl9fymZ6/zpJyT/+9BpnnVt+/Om7nKqxbq5dT8KA1q/fntdPsWDg96Ghd1/170Dqw3OW+/XlB+Om10PvyU4w8+X1loXpx4fgvMxaN52c8/GnvxJ7d1EcVvW/JPfnh+DANR1g01Pxnz7dQf5lBj0Nepf518tOIffvWAKGvy33afYE6q9k3/H/b6LjEETuO+J/Ku7PJkB/n/38l7b9swmfZt7Xl2cUm1bsfpn99k05bOmfPzjfP/zwy+9A9P8oRsma0r5L+JaYaei5Vf3t288fqvvHH375+UOTg1hzzeRbU8Z/JvPPcL2v8wcEn6M+/nEuWP+cRmnWpbP3SJ/9luX/Uf7+OtPMOHS+f159mf2YL9MLmk1GvC36gOCHnKmArj/g+NPL74AcAImUjX2/DbL8P/9ztg/tMqsyr54pdtZMDJPWYeJOyqtBWM3A/ym3SxfgWoUA2Oc4EP+ThyeNM2/26/+x79z42X5y49ycaOceDN/e2O/bG/v9+jpTgcysDP0wNePZiTwcvqam76b1tF5eupVbtoBJrKF2PwMO+jy9mYXp7Nd/JvbbXcJrPvx6Z9HwwUonmpsYqQLM+TpZdQnc9GmDDajZ7V27AcLjzAaaeCHg0U/A2iqLW8BoEwJVFMbxzAkBZQOiH+6yAUpfJmG//vorYOPga/qg0OXsUQGqORjwrs7s82dgkheHflB/TV07yGYffvv9w+z/zv7ZrLvwaY0D4PGnD4CGvCJLM5BTTQKGAfcAhwLCuPvgt9+fwAIxKShZAJPQC93HZBCTkeu8oayw5GcEw2eWC9AFyCZ5VtZTgQrr1xnnzd71BYtOtybmDjJQgBw3d1PHTUF5qgMTmPOOZJrVswoEXuUNn2ZN5d5X/dUq74XLTUBym/Wvsz19AHUii8GvSc37IDA5S0MA/3sMPD4HQsoP1Yx6E/E6k6YonOVmaeZBaT7X8MyHX0B9eJsOhJuz1O2+plM1dCeo7inxgAcMAsjYT5d+nnw+1VqQ/071tvZ9jDlVM/Ve1cqvafUMd7N07+X7Xsf9JnSmIvC3Z0hVQdbEzh0/oOkk6ekF5+mVewwe/rwpoH9sBO51e/a1QRYwOvv/1ExMupG73Wm7I9XtZraV1JPxwGxqdSZsH90RKO33xe758b3cv5HFG2d+TeMQBEA5/O0x8o70c8yDh5oSLH4iT3f5QCuA2ST3HoVTVJXlFL/m1/SNnD8Bx96ZCDgCpCwI6SmS3hac7r5pGoC8nK6/F+onThMqINJmeWMBZGae6zqWaUdAq3LKpCfiICTdKau6ILSDP1g1A9IB6ED+DCgxuQUQ+B06KQNmAsd4ZZZ8Hx5O7Q/QwmlsoC3oJd3X2QUkwxQQFchA0MNMYwAKH+6iZokLMAYqviNcBWb+UGZqP58KmhMnh273I/7PW9+D967JpDyQaTpmDZDsJiJ13P7h13ctn54CQpMpOu6T/ujsp6WzH2vI376mdw3fuRtkcTyV3x+gmYHsSR6xOJFQBYgkcZ/hA+LgXmlfH8XyUY3fdfnyDx33x3+vKb+Xv/Mf/fZlFtR1Xn2Zzx8l661ivYIMmYMICXO3elSvz1O6fX5Lt89v6fYHmQ+Ivsz+Pb3+IOIZzl9m8OvidTHdEkPbneL1+QIw0J8p4zM63f2antzv/gXLZwmgtgn2AZTL90ryNgSUE790/Wnwo7JUU0HqQA28UynwwNf0PQae+QGYOvWnMlhlP+TtvaQCjz4c9s744FZag7WdCRvfnfYj8aR+5b58SZs4/vSSmon7P+xDJkYHEQqAmHYuIFdAD1OH7v0KGARuhOb0/o87LPn+xowfkVzVQEOzvPPBMzOeRPdpamBTwCXTZmEqWw+KB1scs4nrSeN6yCcVH3uTqU96b6L+cdV76oI1nOzLlMGf7qT8afbeu36ave0m7nuztAHbqZ+nvnmyEwwFf97Hvm8aLffllz9R49lG/4US4cQeE988zHWd79Rw91hu1oABzycRqJTZ94ZhKpLVcC+m/2g2WLB0iwZURWdS+TsG31XLHvr8fjelfuwVf3t5I5en8559IRgOsvhzNdXFOYhtsCC4fkQhuPdvdYzPuYAIQdcCJq8ci1i7toN5Cw9xTJhwCQz31ihsr3DPwkwC9YB3icXadE3X9RzXXsEEDK9t1MNt2MaAvEccf5sKfzjp4y48d7mGEdtZ4giGoWuYQMy1Y6KEaTqL1YpYEEAOgOZ9agR49Gnkw6gJwffmdQLjaetvLxaOgpEsWnHk40XP15qJo4TVBzpU4q5R3aBIVU5FeqqVRqujap2gVCCyl00l+dmSvO3Dk8TgQr5Joqt+6Y8UGqqYn+K6J488ec61BaFqjd8dzYu8kdKxPRPMkHF+xY7azgyFQpcd0VDCcwnvYL3ptxdI0HitOHdXbkWUJ8YLa3gN1VdoL3CoJ8QXO0aj00B0Z/vqkiPFnzAhkZ25icVxUgXMQPlCvL2YTlHl1I5XeLeY33YBd6Cg6z7VMOcwxmvXC89NSiAr6LY9i2tbCEbpWHJKVSw1F09KVoO10jofK5pIj4K63NRdYeEr/pxfBetoZnqu9MsbtNzlZ1xbopzkaKPGX3BILtfhKqH4+NxfNJxBLxnTXcCv3dGwEjeJ97VmKCSD3Wx0jFyr35wx3dX3TqlnELwWKlyvT1iyPvcRb7FXZkelgSvi5LnSjsXFvqHUbaCOlWCOLb8P9S6vk8op5160Ncn91ZARkpSiWzpYx4t+sCuftYdR9CSpCQol7lqYZ43DoVZyTWAxQ1nz+LU60bmXXNbRZsWd9squ0x0+k3bVxajpVc3rNdqZPXdeIiGI5sJOi7VPMPyl4a5XjscolTaHKNvXDo/GeIHAxkp29t2Csypfh/YDZF/hlX8bmBt5iZOVvcGioVH2TgWNikZjIQwbbqaJSX/LvYLYm5xjYacxrv010TVGd3Fob0cfRnM/yhtMlAMmrVfVSlwZrUZ169BFj5FEqOJuHti9g0eag5lnjLSX7XpYwFuoKYSqr+RsiRnyKAdGyAheTzGrfM+f9UtA8iXqS+BHLgEWxXW4QizsOHSFwVeIP7lU4RrN2WKVelA929NYsoc8kR0Ux2CZIYeLApXrOafkMu4gQr8djMbRdtfCWSmDcyk0ujVZkelV5lahe8boi0sEnZmbe7LZlZYnAqLv9tsoPWwje18oQN/BuupRvOHNgY7tNOfPGkHZZEdeTxi5H8NKuTYUctxyWyre9dGekijBqMOu6fecvu3qprku6bDalFAn5TGawcHmtFO4garCVWYYTSXJga5C3HDrIx1yTU7eNCtf9ZB1Zx39rIAlds6utvUcQ3C4Xqzc+SimEBSFzWaxdjYBm0kytAojwFW0urdDaBdKeWmEKLXbe3h8nYeooJQ4LyzMFc1ej1t8A3FIcdhn4jrszQWVMvU2X2DzSghRbFVlh4tzGcLbOCckho/3144oE7HSIT2+NWqR7hLUi2HRL+lskeVxgBDwuWi3JeYVgFzFqyJorcLmWIbUtK9xA8JH1DJzve3OlTItcS6jc1hS1nwYXKmLfGYDEQRFxrsc8+bHQT914fl0TJP1TdarOXXbhNttQIMcAq4YGRQR1hXaHxGV1qpLLmiyaMNM6chbciNQDqNnfqbe6NVoZSIjL/bHLi1XlTlqDQyNkCIdlIqy0W4lrQ9+j7epFF1hJKkPWyqVO3fVFrzKFC0u9RuUTReo2LZuv7YPUYH73WJfSbAkKLu6Ust+x9bRweMadxdSFBlpfHhRNx7cGMLe9JujVq27MzunhbBre8xY0fGS5PplSretWC8wO4DHCsKXfJI2p2uTt9QAkxqmU0uN3sRUzvYqRG9VSNqfYgNZ0dtIVrarBdG4psW3EcbUkrsVyfzobMyk7qNCgsKsdfxTqTUszflCFrObq7iNtO4qZVdOD4JguSnPdKSXG2pDUyV2okq3ZNKFHIXjyVGjVMdHRxYHxG7FLIqGQrTNfYhDczfbZrDQVsjosRKJGsEmcii1Hderq0GZTr/cENmedu1bjq3aQ7Rw5q6u4uF5UEbM8OSF0wcotzPmaYSguUPm/vagiZ2fN+31kp05U3LFVLPztdaAyN8utGNo6wUbrkiNt3T1NuJWKovtdl30hVINVnRUnL1/oTeEhIzLherT6y3KuyHUbVfx7oph5+s55jNfhxXstD8QhwMIpMxbI5Bjt71kZnsyWZEnfizErc7s1Iui2KvCXgZyYhMG0mheFK2YDo4izCqWJnPqWUvjC78sjvC1OLA7vTKMjtwdD3Vyapw8VF1CpXeoJ0oRK/O7LU/RGChLCVKdi+pYrssSwdkoyT1tc4BZhTL4fcwyO6MyvNpXHOTQk2QseSIsLxcaiPesAcjb8rDf3PCATzZXa9nG9qk7Qw6zC0QpMQwMFnltt8pU46xDraLxe4NNgjKuQTJszW5/tFBoNywLiYGy07inqWKf1MkqIFZ1d4wLNq1YOzcTmySDaqFL25YchMjrNUEZxkaAs86bj9hOoHMkBKF46nQFSw7lcAX7nZ6kY8DbuFjbqVU7mBI73IleNDZ/RHtYZpC5KdGDTt36o3gxRZHjKiKx4h05B01KrG0wWYCVlSK1ZbCCYkuF0/5KX0MfBaSj7HRpeQHUKm2vKaJljqMh+dw4uvEhuioXKN966Xqn+CizZngLY0TMLxyu9rBuYwwEv5VXu3NJsyZJ7HfpSYAZZrvtFyZ/ULlCt3lykJc3qoIPSLlcsMiCN49eYXtlaosMTyJOfRt94yK7uR2RimY6krtOy10BC6qG+DWjX463+WruDbE5J6/qiVusFWqZixKsKrRt4NDI6p4Jr87yiYDQ4Xpwrps6BrR7yddivi7oOeMGLarIWXvF4aijqIrsLkdh1P1UJixeGSTJd7kqvrGktAC9UdZ7B5FGAMeW/JZznX7QLYcRBsQCu7TOXJCBeowXWqAy+dVG0SbV1/EqPaYwE1Bk1RWyHhVZd7wIAyUqEZdlSZHMM+wgLgqOwY0LuugjQVsUCsvLi36+oyJydeIRX6NJrjAj91IYZTD3fdbHiqtbZb1N0L5wTHoKwjNBgfIlYqhiF1Hyfud1cyTDz5vYP3fMLWEshZOacRU69NyorcQ7Mcf10dgn5tCXFpqRsqE4jY5kxbCI0xzapTFJ1kwgDxFFHForRyWO8xP9ElPC9dBucv6mya1UH2mtFvNzuXJQuABN4KoXhko6ISOsGrDJaxGaDCGKK7QV61rCaU5yUzWec8adTbqozcWnOBVvtn9t+gY5+5zn2ZapFseFeKHX4nUfb4SNa9jm0r3Ifoz6q1MLtEyInGO35EKBQkNWDzAaXAAvgxa3OOV8oor7Sx1JczY4ZPKAMsHKm+tSIg7wMiYzjr/tN6VlB/ypRKn2yLoFR10cYxHMl+7ZbDsB0tg4huDi5AYMOtjQgCznzgXpTTBKIOjGwyO2o1pz6Yh7KO+84uxura7rKmZxq4a4WwjZkKXZRUUVPg/8obVZwhtFJT8J+liM2zNn8ItFsPVIbD8wi5bOnR4l2jArW+PEBjI3+GjGnY3TMFfzE2YJKJUrwvnILnfHRu3iJUuKl2jgd3ZfmvBY79UkS7epunG4w/xM7M+0JnluTlK1polej+y2Ykf1SrhEQNMCO/B54WRI7Cy3fm8FFLW+sq2/kSRsg97OfUnDDhI0krIb0UQuQa+2ZfLjsDoVFMozZb3e0Bu/AznW+tqtLzJ+f1Sux3YXd50VbduoEOe7w6k5UIG0XWQLXndyXDgXUMjsulKDhDHbJPXGUXpJ0xkO4pQuPks43O4ufZEUpc3tnVrSD9Fx7Sldap3ioSdFOsTO2z3fyLKGBbdz3YYn4hptEJhqhq7spKILpEgWdx1bMWUUd1mmDcWuD5LRgY5F6mDJzp07JImb51Kw1gPjXrLRIRvieKVs+bzRsS0LHfvC7GSjltPcXUQLjEzNxUn1FDd1nA2+ivF5gIro3iMafT5fZqW5xZfxvNk4O7AVXJZzW8PmkOquhX5ZiYfLYWV39NwuRgfNciZJqe2g9vwg7bLu4Aw00fWLUu5Sk4Ray3C9ZD5SKLQSSdhH9u0CSWTdgLmxa5SWu968OXtgfDscrDkpXZ11wg50e4OhuahtDcukWNlOVUixOcJ2WW8r73AyntPHMmaOy67CeWhtqjjee/pRIaLLznEAA46rayNYPtg3zrsTVLTUMb15LQ6W0rsjk0qMVyyR8VTxkczGJOOZEgLzskSWtp5faL9CeSJfUYh76PhQ5WS3QaiTa4wuUL6qThuLgiiMTK5SF8jHkk/3anmV0SuK8vJI9vubtD7F19hmW8MhSNG5bNtNibGC7QAPN7S1I8isr7oRSho9jKN2wHu8GaH1aouJK9G9eU03rjgD1NXTIvS5ueOAUOmwlpA4JN5GeptYocuuZai1N2HcpUlF4LgptdfkElSO4GNNvE5rr2yRyhW2phge8/PoJ1cybFUKgSA6IoiGOOBy4gf4uoCRExPlrYb6us5EUnlFtBzss2u9WQ3Xbk0aju2OsqenlXiah0m48Q9ZfhhRAYMYyha7fWCF29MOTUx+4YSH8pZC7MErOZGMVHivriEGzS1BjxwddMhoX5/WoRoPZbXR9iYlHeSMU7lku8zXV9Xp0jFkQKjHiwEiMUZxZViKD2s3zU89xBgXf35m+WtGqyXo5BYXrvRpcZdI5art9py7mctQMW7mS2MzDGbs9eJtDa8YTN3tj16oJRAUyoRJMLo07tRq3fMrtRoTEiLGPF7BYprtyMIgbrrns+Gy1PebNQxXAqSCbcfYIQRzRP3RrQ8WesguJb9cxNJ5iR5q/SQimwGiQ8/RDwYmXQ2CQU4km/g13p+dRpI6G994GTTgcIG0bNAGxjW4lZt9Zt7wEWat3jw0YsRmMi14bU2WKwp4eEsx3DwQ5ic/Qy1usFOfNZihEIp0vbEYxpkjQdyiJDwQnhLtuiMkE946MyTDxgkcxCptz5ELiR8S1tMxtN6vsaMAbSHmfBzXKuLBh42qCmujMMxRJNLKBXUZHjSirtYQJ8+J7kasRXyDeH41v143A6mHtxvJLDM6hWkOIcd0OaD4TU8v3G6LYNfQFZYsJM6xatgcz4lspmLYr1egFToWClSVriCPmnpYDIgEF71pHqwUy+bn7TJTXJ0xqOWpMJnqkG3WmYJyXW6YMaBs1KjK9AKvbSgdrZuG40TVLW2/1QQ4WJ08R8Ua8bxtRn+1j092BMsu5a5R7LwxuO0Y0JWe+KdxvuEKzcFVa8AKt9H352sRoTspR/B2IQgaUWDmrQJNJDoMm3KdUabfrpZmVHQ7HeJIndjj9ZXF6qohiTQYyaUHhxtVhG4C4QQw6bEEbdycXbTS6jHpr2uBYdR5JMQy0jgJXMm2dcs76UwT8jVcQj6nkgtk3HY8AvlnhdhqNB4OQiqxaN4jNwjECo9vD5hrCvu+PvOoNCfVxtpd8Eg4kuTLp5fpEPV5eP0vPXaeTgb/1w4oH2eJb4+u7kfIrul8ua/15V9T55dPL6UdAmUeh69V3PjP48r/dvT6+Z897phmDo8nuNOTtb5+O9evTX/6ytFLmDpNVYOFqyxu7ge/n16sppq+A1FNX5Oxwd+XuzFJPp143xeb/joJWGl6tvqtzr49Tpvdl+k7CtMDI9cJv1/6z4PoTy/OADwS2tW3JY59c8t8MvL5AAXYhrwuXuGX3/8fdgbP8sUlAAA= -->
