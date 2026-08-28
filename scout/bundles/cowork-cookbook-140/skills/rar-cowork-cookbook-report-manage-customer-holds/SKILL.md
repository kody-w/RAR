---
name: "rar-cowork-cookbook-report-manage-customer-holds"
description: "Builds a structured summary report of manage customer holds activity with totals, trends, and breakdowns."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/report_manage_customer_holds", "rar_sha256": "8434b1775642a22be0025eba9550d115f088906e4a55cb14362d75ea5cd6ad2c", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "report", "order_to_cash", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/report_manage_customer_holds`. The original RAPP
agent is preserved byte-for-byte in `report_manage_customer_holds_agent.py` and in the RCI capsule.

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

Manage customer holds Summary Report — Builds a structured summary report of manage customer holds activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-customer-holds
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
    "audience": {
      "description": "Optional. Who reads it \u2014 this drives register, length and what can be assumed.",
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
      "description": "What to produce, and about what.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `report_manage_customer_holds_agent.py` and embedded as the fenced Python below (sha256 8434b1775642a22b…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `report_manage_customer_holds_agent.py` first:

```bash
python3 report_manage_customer_holds_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 report_manage_customer_holds_agent.py   # or on stdin
python3 report_manage_customer_holds_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage customer holds Summary Report — Builds a structured summary report of manage customer holds activity with totals, trends, and breakdowns.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a author capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/report-manage-customer-holds
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/report_manage_customer_holds',
    "version": '2.0.1',
    "display_name": 'Manage customer holds Summary Report',
    "description": 'Builds a structured summary report of manage customer holds activity with totals, trends, and breakdowns.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'report', 'order_to_cash', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'report-manage-customer-holds',
        "upstream_url": 'https://coworkcookbook.com/recipes/report-manage-customer-holds',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '077655d5f62ce28c',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['order-to-cash'], 'process_tags': ['order-to-cash/manage-credit-and-collections/manage-customer-holds'], 'recipe_category': 'report', 'recipe_type': 'prompt', 'upstream_path': 'order-to-cash/report-manage-customer-holds', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'author', 'checks': ['The claim is stated in the first paragraph, not withheld.', 'Every section maps to the claim.', 'Numbers are sourced and current.', 'The ask is explicit and actionable.'], 'confidence': 0.333, 'deliverable': 'A finished draft with a stated claim, an outline that serves it, and an explicit ask.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'audience': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'subject': 'What to produce, and about what.'}, 'refined_by': 'rules', 'signals': ['tag:report'], 'steps': ['Fix the reader and the decision. A document that does not change a decision does not need to exist.', 'State the single claim in one sentence before writing anything else. If it will not compress, the piece is not ready.', 'Outline to the claim: every section either supports it or is cut.', 'Draft at full length without editing, so structure problems surface before sentence problems.', 'Cut to the shortest version that still lands, then check each remaining paragraph earns its place.', 'Close with what the reader should do next, stated as an action rather than a summary.'], 'subject_label': 'document to produce', 'verb': 'Draft'}


class ReportManageCustomerHolds(BasicAgent):
    """Draft agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ReportManageCustomerHolds'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'audience': {'description': 'Optional. Who reads it — this drives register, length and what can be assumed.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to produce, and about what.', 'type': 'string'}},
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
    print(ReportManageCustomerHolds().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716abOi2Jb2X6FPf8isJvMIyKB540Y0IoIggwgCVlZkMQ8yySBgvfXf3416TmZ1V92+N6KjzeGo7L2GZ631rLXh/PbidG1c1i9fXg6BU0Cck2VJHNSQU/gQU/ZlfQY/yrML/kFeWbR14nZtWTcvn178oPHqpGqTsgDbV12S+Q3kQE1bd17b1YEPNV2eO/UI1UFV1i1UhlDuFE4UQF7XtGUO1MTlfZPXJtekHaE+aWOoLVsnaz5BbR0UPvg5meLWgXP2y75oXoHmYHDyKgualy8///LpJQHvX7789uJlTgO+etHu2qS7JuapiJ/0gJ2ZU0RgSTUCpwvwuQrqsKxz8JUfhNDz08cmyMJP0H/8x7l36qj56cvXAnq+vr5Mf7SugNo4AJY6TQv89JzKcZMMePAK0VnvjA1wGUBQPPFIiuj1sfO7pLKC/j5d+/hQ8hoF7cevLyUwwZkQ/fryE1TWQF/dTe9fJynVx59es7IP6o8/fZfTdG4aeO0kDFj9+u35+SkWLPy+NAnvWv8OpD5i5wZfX35wbno97J78BDtfXtMyKT4+BFd1eQ0Kp/CCjz/9lVgvDrxzljTtPyX354fgOHB84NPT8J8+3UH+BYKfDr3L/Gu1FQjrv+IJWP6m7hP0BOqvZN/x/y+is6QImnfE/1Tcn22A/w79/Je+/aMNn6Dw68s6yJIryA43C75Av307qCzz8wf/+5cffvkdiP4fxRzKrvbuEr6BYkzCoGm/ffv5Q3P/+sMvP3/oKpBrgZN/6+rsz2T+Ga53PX9A8Lnq4x/3Av1GcS5AHUPvmQ79Vlb/Vv/+Ch2dLPG/f998gX6sl+kFQ5MTb0ofEPxQMw2w9Qccf3r5HZBD8eCj6TKo8n//d0hKvLpsyrCFDl7ZtRAIcJvkwWS8HicNBP5OtV0HANcmAcA+14H8nyI8WQyI7Nf/9O7s+Nl7suPsQXLfHgz37Y3hvt0Z7tdXSAcyyzqJksLJII1W1a/TuqKd9FV10AT1FTCJO7bBZ8BBn6c3UFJAv/4jsd/uEl6r8dc7SSYPVtKY7cRITZcFr5NXZhwUTx88QPHBEHgdEJ6VHrAkTACPfgLeNmV2BYw2IdCckyyD/KQG7paAvifZAKUvk7Bff/3VdZr4a/Gg0Dn06AHNDCx4Nwf6/Bm4FGZJFLdfi8CLS+jDb79/gP4f9I923YVPOlTA488YAAuFgyJDoKa6HCwD4QEBBYRxj8Fvvz+BBWIK0E1AxJIwCR6bQU6eA/8N5QNPf8YIEnIDgC5ANp9QBbwMJe0rtA2hd3ufzWpi7rhsWsgPKtCGgsIbgVQHuPOOZFG2UAMSrwnHT1DXBHetv7q1czcxB8XttL9CEqOCPlFm4L/JzPsisLksEgD/ew48vgdC6g8NtHoT8QrJUxZClVM7VVw7Tx2h84gL6A9v24FwByqC/msxdcNggupeEg94wCKAjPcM6ecp5qCZg94M+uub7vsaZ+pm+r2r1V+L5pnuTj2FwgP0D5RGXeJPTeBvz5Rq4rLL/Dt+wNJJ0jMK/jMq9xyU/rTvH57zwaNjQ187DEFx6P9skpgMozlOYzlaZ9cQK+ua/QBsmnQmYB/D0SQPZM2jOL73+jemeCPMr0WWgOjX498eK+8wP9f84IpGa3f5IMbA7EnuPQWnlKrrKXmdr8UbMwOToTsNgSiAegX5PKXRm8Lp6pulMSjK6fP3Ln0PWe1PToM0g6rOzUAKhEHgu453BlbVUxk9MQf5GEyo9nHixX/wCgLSAfBAPgSMSEBhAOzu0MklcBNUUFiX+fflyTT7ACv8zgPWglEyeIVMUAlTNjSg/MAAM60BKHy4i4LyAGAMTHxHuImd6mHMNH0+DXSesfgR/+el75l7t2QyHsh0fKcFSPYTi/rB8Ijru5XPSAFT86nW7pv+GOynp9CPDeRvX4u7he/EDUo4m3rvD9BAoHTy5p5qEwM1IDHz4Jk+IA/ubfb10Skfrfjdli//beD++K/N5PfeZ/wxbl+guG2r5sts9uhXb+3qFdQ/aFleUgXNs3V9fpTU57eS+nwvqT/IfED0BfrX7PqDiGc6f4HQV+QVmS7tEi+Y8vX5AjAwn1f2Z3y6+rXQgu/xBerLHPDaBPsIeuV7G3lbAnpJVAfRtPjRVpqpG/WgAd55FETga/GeA8/6ADRdRFMPbMof6vbeT0FEHwF7p3twqWiBbn+auqJgOoxkk/lN8PKl6LLs00vh5MH/cAiZ6BxkKABiOraAWgEDTJsE909O5ycTGtP7Px6wlPsbJ5vKqZxa48Td76R5t9yvgVlT/UXJxOCfIGBtBHhwcqafanDq/y5wrgF8GviT9e1YTeY+DinTwPQ+Tf13C+5lDPjHL79M1fwJmibfT9D7EPsJejtW3A9pRQfOVT9PA/TkM1gKfryvfT8/usHLL39ixnOe/msjnhTzIHXHnVrR5OKf+ASk1cGlA73Pn+z57uB3veVD2e93O9vHifC3lzcWeUbpOf2B5aBcPzdT95uBJAYKwedHuoFr/9Jc+NwLGA/MJmDzAp/jLkpRBIljDoa5AYJgROA6S4JAfBQlQmSxWCJkgDsE4bkoPicxnyICh/B80vExD8h7JOy3qb0nkz0BEgbzJYp5PlhMEPgSpTBn6Ts45Tg+EEchVOiDpvB96xkQ5tPJh1MTgu8j6j1JH77+9uKSOFjJ482WfryY2fLokBjuyoML12QY6cVs615QLc9vTuwKAcpzvswy+qo4Yclie6zavXRy2eBmDNs0x1rboVXkEDZneJiv07NlBeO5gyNm7Q8OX4l8DIdjESz7DWtp+M5oiK1xcEzU744at5PKRQOLjZWQmWln+vFkcYm/hOGjsahvpnzgOP9ylC2OMASOtE8qiXkJfFQ8XUDh84XK3NR0k41Hmlq3xve3S5P25uCc8tU521Hq2NXrwebXyKKzqtHrUn/0w4SQ5hRCzBLJpFbmwYyPyoalBCxZivuWz6p405YiKpzGU6GQWgF7Vewd0ZU+BkaE3qT15jQjEkvxL9hJpIax0EivsbqSUSrZpszdMJ65XjrWMU1Lni7BR/+4siwmS/1jvr2y/bUBHlGWjWBdQpz50ypEg/y6ETe7zXajkGY2BilN38bricqU4ThWLuPqBzhiGa1wuyTaab6zsLoYaSw7oL1zr3D7nSjSfpghliTnLtt59a7RvUxqO+mMiygRjRdULbvjihuCHRVbOoNujaNEmBZ62/PDAI/b3cZoOARzaLTeULsxr/T8nJl6HxLLfKnemN7SD7bfmrR14DzhLFSIZ0lqrjmn7rpaupQt1KWyPcRXXzEtv1NWSzPAwhWpuqdofVxnEs9RarPIbgreugrvSWWz8/xjXba7ZIy9S0y3C7495ai+Op1Fb+H55tk+47trHg3YkVA8eWZ3S2k0xMWwsh00V4QcVbdzw1WdzHO6Hj7N0NscZfdNIV6b03pQApN10OZYdVqf8sUho+S0uC2i4kbGQhGzhQ4yqF0Q7GxNtnAsMCRLscSMS+HVhru2ZlW2tDTDGAZf8jceOc2GYB0d+WMw+G5mpJVMZKSAGbWNKqmIWexNOLHWBjn5iHJgC1NNmSif9WsaE7xGNRuYV9nIaup4v6dX7rIV9fSsKEueZEIczOeSkFz4ta200t7v+ZlmMNf9aYskp/MZz9beuov2ZwOxEjErt8k2vWA1S5bDgHcpnQ7+eNFpcibV1Ene44IeJQub2HJn70xt49hcDdJBacIeT0J5sbi5TuvVlcDBkhc5VGsGlsR14WJec3NsiW825gyGEa42lXkWN2G1SNYjr+TOEVuLV1JP1/SN81DNpZ0cYUS2HnKCinFKGJfSmT3gUWxHO87PzQOd1lV0wMszaubs0ZLng7dtE3puLnhTqS3hPMKB0FRGj2V7YWEtQP01JMssZQcjKawVesHA6zDdj9Ixs4KVIC24ckkZ2Jg4l04UbvqxmR1dOmWj0yY6EbyFcnRqhgey1fhQO+RhsgvaOgL1vmQMIxpTezVXR/7AhnkutavuajKbOZ9yuS0tGEk0z+yxo1begJBG4ceJzKp6JRjarrC6k9SXad9YErnLd3uM6M3zhijGazAz5xf8eqYMslu7zU3V53q+dk1zt1DbwJgjLqLLaZWjo1kk9GxtW0vdFqgNERp8zTc7qdg3s6s843t1oyA6urU3t1ZflIItYvPDXmmVxUmIK6q2NGprsGFsFLtTI5zlw0ZbJ+shy45XJXIiXI1dNRzWdixI852uKJkfXOfNUfKIKhn7I3FcuYRTbksaQMHw3n5Nyaxz7d1Alg13sNPCWBK8IDKswJ9igWgTjHCTNSY4fERjrF0nCVPVLFcDYti4kuFafNREq8P6zGCjtWL7JHQaTx57gop2jJgV1JreNbtya64N2CrUMhAcq7lxvh/e2gus6DLmFWv/ZKeu0s3SrhIkVcipbZmhzcGP9gZv1d5tu5y1JdN2BJGiCLfadrqWoUt4EWrVstDhIZANNSRcLtpmu23lAOY5yjixpquIVdDduK8aa8+3G0RMC4+Ym8ph1TYllnbGYenS2y462vpi7xjsqO6waqOzS3EhkASDgHMrmu86RoiobXNDTZbsCwCjz5+2J5vRQkUX2YNKtOuAB50Ly3hOd8gYwUpk7zWMrW6CYFGi8xMsGrxRatn6QKvEDSGRs+2LneiRRq2Y8+TYbluHi/3cDm/8oml33P7qnyjdMEk+bJw92WuAgilOuI3E4Wh16yVsU7MBE9VMctnaVlg2HjerjBe81LhqsbNc+Ants468q8MQj7mjvOWsel6hvc323RUlTgV3y+b6SYP7cu/XkrNSmVlbnyn2cKIHbz0f9vG11pKMGW/qFdTaKC7ENU2uRGNxymW/rBAAi9eSl+SwLOHdOS+k+Chu7VKr6oTf7hrZjLeDJEdRJx5H7uhX2yZa4xu/bE6GEvkblZfR6twMbpzuTGEEhX8tt6qmlQFMxfGyYvAMGejTio39q30ZfP4W60jMCjmSr+uS93iPkApjL84CrJT2mHAYgrivXcw+u4jZqobX4Swlzy5kZpz7Yjvn6D4C3FpzurQOYFJjLpylq5cAIaU0SIU9I1Ji4oclZYkbqltumGC/kPZuSxvXMe0iU9/U9uhrnrA9c3MjP6jOdVS0kS2L+b6/arBMhDByOtinchUi5KztNTdcU13g3tZ9H8iiTaPevDZ3HIpFMpm3l/FS6FWzWKrIXIOXTL8g+7PN0vvlqOipgfj7RGkNCi3lQLllJxtujxnIRrBdxexOQKWGw8wZdtnvlmKn4evNulkyJhzTpda2su7Nskt2pW9YvEjFjdTu8U5YeVcXI4TYOZMsYnORzPEFp58KsZXQdJstb8RGuBEITpCWsllJi+pq7LN0fzjVmuMdN4O66S/Ouer103ovkTqr34xNRpouIx8E4la1pLKXLVa7abokjfogX+wxhZ09Xm0DJLs4qw4X9sZySxM03eXpFj+hAl16COrlEnUTeWok6OLIn456iDg3UtB4jT+glkm7q9gNMynNXbG35YPBBHZlWvtjKBbqZpB2c3FIu80OZDinnS62q5/hjWRZ6f6MHGsk7vd9hjBL1L4RJ9ZeZQMJRjo6IdfLxboF3K8p6ChlgiVzGCUXyn5Ylew5TZGryNPMJYkakvG1ujEzzj8rblX3M3c9pzgPjxbWraDzgO3ogs9j9li2xtDrl8vGHDdeersd90M8SBZHRk1JlLCAp2eBsBGFRo2LOlsx816Psk1WYnCqrmlzn3DnJk2ic6mBw4+BeZl3wywlXeEnIXdT3xB5mKhMonfW1IFzC9kit1F7lTBTYWewhF/KVC4x0xOdfR7JTry1+Xw01WIn7o2RtVvLu+1a2WMrEWeStVILtz16SY92xaK2U7ZKEyjqNb+uQQZr7GVnbo991BYCtl/Rp2S2ZI/n87EPYGxGRCmLBx66jPDAZaJqsafKkfc01/fl9Vk6l7PdCWuGzKd07CIh7LxjcL/EuE1zlvnOcjpkG2JbQkkPa9kV1xov5kxy9iMiPxRy0ww2XavNinccRiOyYTwio3eIUUqllgmqNYGVhWt/7W6LSsjPSXwbj+Oq3RR9uMdhx+zNEDlsEna5wgf/gIHJGvPLIFDi9Xqxt30j4m+o54ZOGFMprNJ5jcdIrVuos9lb4rZkOjKKe7/NQ3rDCheUDzKuslMCy/2CD67H2qJkriVrtFj11pBT1qEdbxaqibNjFFppSlz8mTA3YTVNfWuXYRSlDM06wDqbiHWaAy2/TOc4oWcOX9fE1uditLnhNEU7vDLHlCYK+LbZgT7Qm4quFcjxtBtq3EIsvUQY4XJkqctCvawWvbp0S+DR2htvwcYyxuXS4ni7RGkevwa1x8ARJchUu2BF/LSo8d3ljPaiQwXj9dpVTCtZ6FVFiR2twT4Jcwu1j4wl5YfhglUVtg3YfdiHM7wKi1Lgif6QKNcM8L6KIe0CLxXLORuZc1iI3pKlS17pupWyDXczpkDWGwRL1tSGEq6Mu49kFbuqtI3MvMir4MtB09sB1lUnX87cUx7AhKnvNM+NDeEAy/xqaCRU2DR9vPVvKw+lxpTNz5gAxvLDSZsvroeC361UeUFTY+GDgfF2xTU3wKmUqDapousKssd31LUWB73jFPImb22JaZo4bwkfvXpuIDIjYh1G5wAO3UVUmvGyNXEKQ0HXmGXpDOZUtrmIu7mO2qvLbsunt+WurcNWwML5TdL3Xkeic9tOFtEOw8sbmDzRhSogGBnDVqcwW262V3Ay7Cw8uC7aAmOchF4Doh5D7cj3+a0LNHbn4azeCVYTbVhfXaneNZQviLVSRruf7YB5Q5fYNtedSjwmK1tJGNukGIB0LR2jTYtf1SCy2ENYX9OdxYee66w8xAe90b8m9p41bG+GlotAtXBvoPjZnouWyGLcwRiSqSc7wRJeOiZrFsxCQY6thzii9NtxFc/CRkC1Q6i79oGolrw2ntFlOF4wPtioPuwnZI7rtuIjKCnCp0Lz5VIdr67fD/ZNSgrGIVBwZvYYBEZ73rm5BH9q5+5KdffxsLzgmBDpY0Lxy7Upt8p1nV68GdcXGTLfATY4d/Qh6Ia64ziv5bmmxroQQ6zlpnb8k0Eh8wM45bbmaZVerBDpeQG7rqyS6hhV4npG1LtCBtNbBAZwiRFXi5RfdL7LW0xbhPwcJLd7kpd22c326m6ZXr1tjO+xFqO4YVg4ywI4hAodeZs5nbXyQd45FKvxMBiHuGtVdbZ2dYtIHk6A6nQ43S9hixobZGtprXaeH2bESK7yuda1cDqjeHeYsflMhKNli++suR4xabQxJbGMNurluAF1HzLLnsC01sDsWkNuPqwewVfsfOHkkcMcDNYhO7EoMPwIuuCQ8AdsJHG3v6gL80I0EtvirEHOHV9fyIed6FQNADVBiF6NZgOSJao65ml8SxGZklrLwPCTJ19NrKAwZG7yeuPNjVW+qTgZUzUv1ncUw/ezhhpcA8UNdfRTie9pwUpY2sIi8RbclESMYXDQVZy1frkZo30KNuHJPY+ksRSXNWcVpkZFiqqWJEwxzV6FZwly7jmLLGl9JjhrQUhdwl+hSottOrimN6ZFqcecZ+aJjW8qb1MajdsEIlarRLIXU1iwFN/3Zu2Jlm9wZ0TedtV5qd5StJGtqrI77FObDJthsfJ8I/YFtrpxc2Rtd7NZckqXnVEXPt7SBRpSkUqtsv1Smok0Tb98epnuET/v9P5TD2inu2v/azf5Hvfj3p7z3O+xBo7/5a7ryz9nzi+fXmovAcY8bmA2WRc9b/n9l9uXn//Rs4Fp5/h41jk9hhrat5vgrRNNv5zzkhQ+2FCP35oy6+43Tz+9uF0z/bZAM/1CiQd+vtydyavplvBDGXhT1j4wui2/eU4Tv0yP8afHKoGfOG3w/Bg97+J+evFHEIrEa77NSeJbUFeTd8/HDMAp7BV5RV9+///tnfao6iQAAA== -->
