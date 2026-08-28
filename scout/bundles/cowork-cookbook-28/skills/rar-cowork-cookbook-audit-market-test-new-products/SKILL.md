---
name: "rar-cowork-cookbook-audit-market-test-new-products"
description: "Audits market test new products records for completeness and policy compliance against rule-based checks."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/audit_market_test_new_products", "rar_sha256": "ba3b8b713f073c7c11cc4b90580535e3b50494144203b008512d04b57cae805a", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "audit", "design_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/audit_market_test_new_products`. The original RAPP
agent is preserved byte-for-byte in `audit_market_test_new_products_agent.py` and in the RCI capsule.

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

Market test new products Completeness Audit — Audits market test new products records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-market-test-new-products
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `audit_market_test_new_products_agent.py` and embedded as the fenced Python below (sha256 ba3b8b713f073c7c…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `audit_market_test_new_products_agent.py` first:

```bash
python3 audit_market_test_new_products_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 audit_market_test_new_products_agent.py   # or on stdin
python3 audit_market_test_new_products_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Market test new products Completeness Audit — Audits market test new products records for completeness and policy compliance against rule-based checks.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a review capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/audit-market-test-new-products
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/audit_market_test_new_products',
    "version": '2.0.0',
    "display_name": 'Market test new products Completeness Audit',
    "description": 'Audits market test new products records for completeness and policy compliance against rule-based checks.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'audit', 'design_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'audit-market-test-new-products',
        "upstream_url": 'https://coworkcookbook.com/recipes/audit-market-test-new-products',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9e8c950c31127483',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['design-to-retire'], 'process_tags': ['design-to-retire/introduce-products/market-test-new-products'], 'recipe_category': 'audit', 'recipe_type': 'prompt', 'upstream_path': 'design-to-retire/audit-market-test-new-products', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'review', 'checks': ['Every finding cites a rule ID and an exact location.', "Coverage is stated as a fraction of the inventory, not as 'reviewed'.", 'Severity reflects consequence, and blocking items are listed first.', 'A clean result explicitly says what was checked and found compliant.'], 'confidence': 0.556, 'deliverable': 'A findings report: inventory, per-finding rule/location/severity/fix, coverage fraction, and a re-check delta.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'criteria': 'Optional. The standard to review against, if narrower than the default.', 'subject': 'What is being reviewed — a file path, URL, document or system.'}, 'refined_by': 'rules', 'signals': ['tag:audit', 'word:against', 'word:audit', 'word:compliance'], 'steps': ['Establish the standard first. Name the specific rule set being applied and its version; a review with an unstated bar is an opinion.', 'Inventory the artifact. Enumerate every reviewable unit (page, slide, endpoint, control) so coverage is measurable rather than asserted.', 'Assess each unit against the standard, recording rule ID, location and observed value — never a bare verdict.', 'Classify severity by consequence, not by how easy the fix is. Blocking, major, minor.', 'Propose a concrete remediation per finding, with the corrected value where one exists.', 'Re-check remediated units and report the delta, so the fix is evidenced rather than claimed.'], 'subject_label': 'artifact under review', 'verb': 'Review'}


class AuditMarketTestNewProducts(BasicAgent):
    """Review agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AuditMarketTestNewProducts'
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
    print(AuditMarketTestNewProducts().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/716adOjSJLmX9G+86GqRpkpbkS2tdmCBJIAgQ7uyrIs7vsQp6C2/vsGkt7MqumunmmztVUeEiLCw/1x98c9Av32ZndtVNZvn9+uvl0sdnaWxZFfL+zCW2zKoaxT8FamDvi3cMuirWOna8u6efvw5vmNW8dVG5cFmE53Xtw2i9yuU79dtH7TLgp/WFR16XUuuFH7bll7zSIoayAorzK/9Qu/aR4rVWUWu+Pz+9guXH9hh3ZcABl1l/kfHbvxvYUb+W7afAIr+3d7FtC8ff75lw9vMfj89vm3Nzezm+Zdk+NDDwWoIfnD6aUEmJrZRQjGVCOwugDXlV8DjXLwlecHi9fVj42fBR8W//mf6WDXYfPT5y/F4vX68jb/uXTFoo38RVvaTTurZle2E2dxO35a0Nlgj7O9bVcXwLxFA0Arwk/Pmd8lldXi7/O9H5+LfAr99scvbyVQwZ4h/fL20wJA9eWt7ubPn2Yp1Y8/fcrKwa9//Om7nKZzEt9tZ2FA609fX9cvsWDg96Fx8Fj170Dq03mO/+XtD8bNr6fes51g5tunpIyLH5+CgSt7v5i98+NPfyX24aMsbtr/kdyfn4Ij3/aATS/Ff/rwAPmXxfJl0DeZf71sBdz671gChr8v92HxAuqvZD/w/y+isxiE7jfE/6m4fzZh+ffFz39p27+a8GERfHnb+lncg+hwMv/z4rev1xO7+fkH7/uXP/zyOxD934q5ll3tPiR8ze0iDkCKfP368w/N4+sffvn5h64Csebb+deuzv6ZzH+G62OdPyH4GvXjn+eC9dUiLcqhWHyL9MVvZfW/6t8/LTQ7i73v3zefF3/Ml/m1XMxGvC/6hOAPOdMAXf+A409vvwN2ACxSg+Sfb4Ms/4//WBxjty6bMmgXV7fsZoop2jj3Z+WVKG4W4O+c27UPcG1iAOxrHIj/2cOzxmWw+PV/uw96/Oi+6HFlz7zz9UmAX2cC/AoI8Os7Af76aaEAqWUdh3FhZ4sLfTp9KezQL9p5xar2G7/uAZc4Y+t/BCz0cf6wiIvFr/9a8NeHjE/V+OuDSuMnM102h5mVGkCfn2bL9MgvXna4gOf9u+92QHxWukCXIAZk+gFY3JRZD1htRqFJ4yxbeDHgbcD340M2QOrzLOzXX38FlBx9KZ40ii6ehaBZgQHf1Fl8/AiMCrI4jNovhe9G5eKH337/YfF/Fv9q1kP4vMYJkPnLD0BD/ipLC5BXXQ6GARcBpwLSePjht99f0AIxBahcwGtxEPvPySAuU997x/m6pz8iOLFwfIAvwDavyroF3LyI20+LQ7D4pi9YdL41s3dUgirk+ZVfeH4BalQb2cCcb0gWZbtoQPA1wfhh0TX+Y9VfnfpRvfwcJLjd/ro4bk6gVpQZ+G9W8zEITC6LGMD/LQqe3wMh9Q/NgnkX8WkhzZG4qOzarqLafq0R2E+/gBrxPh0It+ei+6WYS6I/Q/VIiyc8YBBAxn259OPs87ngAg7wmve1H2PsuaIpj8pWfymaV8jbtf+o4UCVcRF2sTcXgr+9QqqJyi7zHvgBTWdJLy94L688YvD4V73B5o/9wKN8L750CARji/9vXcWsH73bXdgdrbDbBSspF/OJ29z1zPg+GyVQ4h+LPXLke9l/J4137vxSZDEIgnr823PkA+3XmCcfdTVY/EJfHvKBVgC3We4jEufIqus5hu0vxTtJfwDOfTAScAZIWxDWczS9Lzjffdc0Ark5X38v2C+cZlRAtC2qzgHILALf9xzbTYFW9ZxNL8xBWPpzZg1R7EZ/smoBpAPvA/kLoMTsGEDkD+ikEpgJEimoy/z78Hh20NNXQFvQVvqfFjpIiDkoGpCFoJeZxwAUfniIWuQ+wBio+A3hJrKrpzJzJ/pS0J65OQZh8Af8X7e+B/BDk1l5INP27BYgOcx06vn3p1+/afnyFBCaz9HxmPRnZ78sXfyxlvztS/HQ8BuDg0zO5jL8B2hAwNb5MxZnImoAmeT+K3xAHDwq7qdn0XxW5W+6fP6H5vvHf68/f5RB9c9++7yI2rZqPq9Wz9L1Xrk+gQxZgQiJK795VrGPz4T7OCfcR5BwH98T7k9SnyB9Xvx7mv1JxCugPy/gT9AnaL4lxq4/R+zrBYDYfGTMj9h890tx8b97GCxf5oDgZuBHUDa/1ZP3IaCohLUfzoOf9aWZy9IAKuGDUIEPvhTfouCVIYCvi3Auhk35h8x9FFbg06fLvvE+uFW0YG1vbsFCf96aZLP6jf/2ueiy7MNbYef+f7clmYkdBClAYt7FAKRBO9PG/uMKWARuxPb8+c/7Lfnxwc6ewdy0QEW7flDCKzleXPdh7mULQCfzvmGuXk+mB7sdu8vaWeV2rGYdn9uUuWX61k/946qP7AVreOXnOYk/LObe98PiWxv7YfG+sXjs04oO7Kx+nlvo2U4wFLx9G/ttC+n4b7/8EzVeHfVfKBHPBDJTztNc3/vODg+XVXYLSFC9iECl0n30DXOtbMZHTf1Hs8GCtX/rQHH0ZpW/Y/BdtfKpz+8PU9rntvG3t3d+eTnv1SKC4SCRPzZzeVyB4AYLgutnGIJ7/2bz+JoN2BC0L2C6Y6PO2iFhNIBI1CVdGHZdzKEgfA3hKO6jDg5hFAZjGAKhDgStcRjxIMzBSdf2wRAbyHuG8te5A4hnjRDbdtcuCWMeRdqE66OQg7o+jMAeifoQTqHBeu1jAJxvU1NApi8zn2bNGH7rY2c4Xtb+9uYQGBi5x5oD/XxtVpRmE7joXBhnSRJBySlUE45QETrbkNwN951pNbc0Oiguf4Vl+iraWetBtp7xpnqfGlhTBlZZxwq5D4iyamCWFBsn0qvz7g5Ty0LBV4JHkgqo8GS50zyjzK+ZwN70OEFF7WIZqpYPDTIaPHFQb9dQ8LKaa/LrahUI9VK7DqiOitkhHLmL1xTXVG9VY5B2Fp41SWnyuFik9mZ9RgxBv5ZCtJ9Sxo2tltMvnM+d7jfvVGSjG5ApJRk4vJzWS7sT9yiK2HE3yAeDTfvdDd1ZQhb6lObkGmO22JTKFrSV1sK0w8eyvW4czOEVXjUYyM/NrM7PIcpc5NAX9GG9NqroYp4yU7mauVE1hJsxmyZjXGxAek6ti325809NrW24iRN0S2I1rfKs/oJIcoKgvZRcPTgpazWBSxORxs0hOQnUZnfQ28iMtvsMZngoPrQ2qoiM2ujkidJSx5mK1OSFZjvq1jlkxiupySa5z3drQnXazLHqKm3GK7o7U8wk4MqAnClHyazT5m4LvNQre+a+qmn9XphMi8Fci+xE0SUkvroRkB0NVxQqsT7XJr8mmOau9o0J66Fx3R0ZckrLFdLsUztGg11CagicqOdOkExo1xFTbRTm/Vzhm8HsjRCCqvq+9TJzOeG8T8eo1Fu0J9y8jXNnq8zlEMQkTfvIBc36xp0LMxF3xjKX25ER7vVAEVmuGYcAT1Lc31TLgW+rzVBUjllAYqclQjOmg6auk3XfdRXvdbqlYQ2HtQcRmxo5WuINS69HblA3EIFLil9JdqDmsQzjMQEjqSAFltMMq8vtSm6ZDlHQldEvT+Z9LYwSM+jFaqCjYr12V1Oy2mJytJH2JAe3uZzhh2OQb6Pwol/SIrNEaVTD3Rq55vfSvW09dZXgtLI7mvpdaKOV1te+xe5gvIv23JbFK/4aehF8r060eqqQTG9CfmubeWsO2X2HJmcaG6Ww2WRWtBlY1KTKVMIYl0nvJJSt78ppTWa6hbGKPx2nohe8QU4wYSlrnSGLrqqFBrM7C4OAHYpNt5P6DC7DFDvvLEhBTpbFFiuGxtaXNd3U6sH077d7sApMKWidUTi2PTHs9qf6SmJVc6rGhL/2mAxv1d2Fv7iuNVEhVtMVT1Qcd1jdxWnF3DM8gOJLu222u+Nh61XqzmbYm6aGFclnEm/fmQOD13jP7j3dLUYa0jWV4anlKqHPQrTsa/ZwwfP16Nl00nqOuqmXlSxwpsreomSAa9IuVYUaWN7DVUgAg083Xant28lSxYErwV3x7C7XdVyrXL0pk3TY+KB9vfgwa9DWinI2LcuyPRv06RRGOF/uDxzp1NqI1miqYnF1OGtteWxwdizKW5qr5H4bCAS1aTmXT61cP6YpX22OmTYafQophc6d0dtV2pg0Ea/268yu2ZpJp/VwtHaQBKu5tz4dl9n5SnVMbunCbcd7CJP5+G5SYDqFTUdHz0gYQn0AIq4/Lz0Gu8LrTlptmAmqDs7QJhzkQiFxTIcRz1LJjznOxDRrRKhEYlJBOKoX3xa0mi3Fg7xtkwSlUoS9Fi6vcHJG+CcDzWyKTG63ZQedjo1yxsULU5uqaZ+Zu3SRCWXfY7RSV/f66AxQbFJbNaZjOUMxDjBzHXeTedHl3YFZwoKIsPFR8zlb32Pxcscfp3CIz2W0QWxrOISxpxd3vduRnttiIPZaQAkDY+2w1oxJWb7evSgFTpK7PkYIr8DXVFBU0gES5CbdJjWmLJVrwgurGBcbCrlEh925TI89up9W3nlfdnmKt2Fz5DZcEMfLWLyv/HgiqGC1YoxpRWLZ0RH29kVD5Mbo8w7esIxxOHiCuYsmxV0LZ4Up4bG3tHMWikZ2tMx8fzBkRhvoGnCArITlpbC0q4pJ15Osd8zI80hmJ047YTLhupIbyiVHAqiPG1XkBnpL9Mcp51rGqPVMPYZWIdqbwrQpuIvhbnJlzYsDTlnSYUDeG/hyJrUIH4trJMF2PkldkGnRsqpB+8DS9LgBzUrH8/w59vF96g1X0nQIpGbuCbO90RS2irFrrOTkcbnNKCuqrVuLRpW6zQ5Hs7Ud9WLmUO/1vjRJSDREvF/DPBp7CXPNEnbYXMSSYmiHMiKLaJdiBbnB7YL3dChfVfNOYKad4sK2MHfrxl+m51seR4wblcT6Zp4JdiMew03X5QdVk+Np6K3r2EeMqFLO4EHUgVaqhEoZPo2UiuWU5qy669P5fht5Yow4r2pFY2S3B0tIoY5Ft7tsVNcZuePMEROp5LBBi3BC4NrSis1quoh2GB+jxtxpFdtgqhfn0nngoolwI22M0iuDIpNUL0ODisl02pq52NaODPfOdZJjqxIKq8uvQwDAUy2uHNdwKR3Ec6URteqdrsTFhs29YFhElSbL4iIokLU5Xwyj5ov4WLHlZr/mQwkp4o4LUk48lnjJxfcaECmXhzrDyCkfpmmUJqobSQfqhnEE0ozZaVK46p6G6Alws76R1htP2k0h2FDQ1ZGgJdZdEuFygKPGTi+Wvm3PdVJeVks3qAWqp21JFyHyQqOQONmncMVAeuZbBCRLyj0kQN+kG6NJ3gM7xvaXq1Y4+1ofthuoMUNFJYpCIbfSxhBC2nSgTkcDNrowu6g39zF5PIzwNl1x+2HdGPguUG8mQdLQfYhz17aPrXZ2y6N5PZbbo3s1ifyY3lxmVLyVBRGUJKiE5R+CdbVsDoVTqQIJTS575SB8wwu8XoW2rNmIHobdfYM0qdrzyq1Y43yen+DzyRjSa1DSYahf81qBsTzMwlOlHuirSh0x6H5jPYbbEClLEnWjtZ5i3/V2Q3MIqdy5JcwuaU2gD2f9hHE3j5HhYAghFDkZjnG5B0QSXv16e0mOHiTiDAMaDh/mJUuS6r44oRPW+ZjB5qWw0fpDegtk81QvaSQfHX49cUjdbdnbztgm2xJ0I81I6usWOu7gRpGrzgJhLcXC3hj5LsVPFaZfcVeHOF+FtRvLg3ZaWfG8aKNn82ggkXjgAF5pufMapdWQgEO7fpXEanpcbpZS5x1QJXCQe2Ddj6MzJ0O65HAU2dKDfDHwacdltZZdInsVSZVwq1EsNYLBrHPDdQQK9jYSwxnbXV+vMC91AMtC5c5i5Pt576OnTLUj2msY+HC+xSCYshMHbW75driDLKcMysq4dWqIBEJMQSDbkhzYVRvW1LA7QZg/5LjjI1wx6Zs4TqCClg5bWS3JTeXx8cBTTZJG8EBf4ZXLZ5W6smPiHu+pK53p1XRhaRlODwm2FW4qkq+1o3GSbflaaWNiJgNipAJ73+VHYa/AbKIVvEtctw7PKtikxecDKIeh6GJTJoBQt7rJYmtjn7G1avjlmddlM7QrfeldB9E6w1JSXY4HY9iGGkfKvL0sHL6qrandcbLIxFoHKmDq6ufOcopT2CpjudVl275HJhoc7pnFimVC3/bGRtL2F5uNRkxg90qIKI5zJvebnE7xaHvCSZHjGPisrJJKWbJ+fKM2G+iib4OwnezLjXE49iLVc/hO1bE1U6IZsVuroAOQLSC9Rt2rO+Faas/KQq450XDTyxQLKmsDby/0UCLchdm0PckT7tTv0jPfERgdaArZhOJttFu6OGPnWlpyd8PkG1sAzXfUtAxk9SXPGZ4SB4aW1Gnkh5q81KbGgKOdrOdCKyDrovO87jgYHCt0MVMRNL/SDaPrk74GffQ4jGBj7dddnCCU4WxHonarwJtiuoOX9d0liIGEyaY3PTTXUFfSAsRJfWKEmyQwDNtmuFDIY5dqLwl8vFRdv1HEXsvv6Ol80PZn3smbm7uFqSCBG3JlBRGCH5mBwVDasyELyarktLVBw25462Z5uHUnUNfVTSP1RLlWRZBte80emMgqr0dikvdjitNT72+3yR5t99wyIjopo1ebrKwdvDrUCUMde5W86btNG/UZhHPtdk+S1CVYM54kNqIwGKu1GsAtbfJwTgSktk9hBzofWLPlDCxlKMS9Ti7E7k9WkXfFalRAXp8ITr1kRH9RtmbA8j1ytXbdYVWxWOymRUM5y5tyWp34VjwelzZjgLrqJnJ1vnnXY1KUJ3mIUe4y0M6RyiR9XVXDzuG2x6Q6TvYS7uxGb6VxpMhRJAjXhA+rvd/3y5XtYg00ClSX0qCeqLBzMBrUxbvsaF/ogF2ZuF4flrm5DeEl18I1MqmGoqS4SdpSMlL75fGGsivKXOFRuJQZD5vCqx5e4zHC8SUGoWSbnCYdMWMCNIaOy5gbBzAc11eTcKccB1nLiX3Lfc81ZV3SG/d+JPvi6LTrMIfWysq7+r1x1UnuhMiGbS4Hm6d4uQwdIc5iycmK5ZDoDQv47LLuFGkiSL7ja1wtTdpbQh7rjvxkqtJ2vWvFPVmfJeVg7wwLlJ32jha7bbgXWtT2oT10P5TE0s4Jbwl2KNQKnc7uTYy5g26vrWrtu/75tLELa6ljIn66wPpK216WtauMkV6cyu6+HpcUhMXduT87IiWJLXpHRw30dzWPJFlZWblF3GCVFOQelVL/eFXVQz1iTGNTitYEkdzVNi7eJqe956fDGUtJn9o41jR4MWQR45JG16vDsmyNfVtMl5YKDH2st6hucBIt20vUkXgIP+kbrTr5mpPeFUPmEFGPo9tej6x8V65buZT8LY3sO/oYkyW/xqB93+HN9UAfq/1q0omGTVsLVKX+6l2SFIUzjtD1k9V6dbQ7ATrKV54vn5JL04EODnfgprfEm9IbnResasYN8L64QzWZ72v0DukUQYmwTQG+6VIkl9agHXTv9X4vZ1QaT9CNDHplhR0HYiUu12THIn1lUc2RwWJyiBSpV3QfaiWw4a4sdEUfL5F2x6ILNGnTjQhJ92QXpZ6GOXNN2xhfrk7c5Wwru2Yr7HZkZZxUFPFEOJ9YEQ1WppxW1YYfRTFBMzqGjs6p3C5LgWWD9CBdscaWt2JG3KAkI0i/rWWjTdp7og2lXyrc0bkFatUVl5wWI8LfYt3NXm9xfFgPTCPQdSSoomeyFlqO5ditVB2X7X0FWRmb7vZx7Uy36zbN8Uw0paIzT0ktIn0+9irTJw5FlHRG6R7bjP3NsihnK1ZyhnkDNd2csL0tr7CDnHPllMS5NubR9Y7cyW0trgievp1Inr2noONosy16snHQP4U7e2yRumGu2i6N8dMG1C8LcgbuDl+rlAsL21r1yg7HoKog6tatexc7aim8DyDHO9NbyaIrmqb//vbhbT5GfZ1f/w+fQM9ng//Pjiifp4nvT7Aex8i+7X1+rPX5f6rQLx/eajcG6jyPYJusC19Hlv/lAPbjv37uMc8dnw9054ds9/b9gL+1w/lnSG9x4XVNW49fmzLrHgfAH96crpl/FtHMerng/e1hUF7NJ9+P5Z4n4HFYfG3Lr7XfxrX/Nv9iYX5s5Hux3b5fhq+zaDB+BC6J3eYrSuBf/bqaLXw9RJkPceenKG+//18VzGTK1iUAAA== -->
