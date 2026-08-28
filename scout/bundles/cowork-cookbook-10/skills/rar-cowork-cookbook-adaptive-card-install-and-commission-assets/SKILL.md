---
name: "rar-cowork-cookbook-adaptive-card-install-and-commission-assets"
description: "Produces a reusable Adaptive Card JSON snapshot of install and commission assets status for embedding in dashboards, emails, or Teams."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/adaptive_card_install_and_commission_assets", "rar_sha256": "f672399588670c2420ad49a2d3df89b2dc12251c15103d389eafa3522d5c0509", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "adaptive_card", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/adaptive_card_install_and_commission_assets`. The original RAPP
agent is preserved byte-for-byte in `adaptive_card_install_and_commission_assets_agent.py` and in the RCI capsule.

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

Install and commission assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of install and commission assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-install-and-commission-assets
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `adaptive_card_install_and_commission_assets_agent.py` and embedded as the fenced Python below (sha256 f672399588670c24…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `adaptive_card_install_and_commission_assets_agent.py` first:

```bash
python3 adaptive_card_install_and_commission_assets_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 adaptive_card_install_and_commission_assets_agent.py   # or on stdin
python3 adaptive_card_install_and_commission_assets_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Install and commission assets Status Adaptive Card — Produces a reusable Adaptive Card JSON snapshot of install and commission assets status for embedding in dashboards, emails, or Teams.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/adaptive-card-install-and-commission-assets
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/adaptive_card_install_and_commission_assets',
    "version": '2.0.1',
    "display_name": 'Install and commission assets Status Adaptive Card',
    "description": 'Produces a reusable Adaptive Card JSON snapshot of install and commission assets status for embedding in dashboards, emails, or Teams.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'adaptive_card', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'adaptive-card-install-and-commission-assets',
        "upstream_url": 'https://coworkcookbook.com/recipes/adaptive-card-install-and-commission-assets',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'da5a866170a550e6',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/acquire-assets/install-and-commission-assets'], 'recipe_category': 'adaptive-card', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/adaptive-card-install-and-commission-assets', 'uses_skills': {'custom': [], 'ootb': ['Adaptive Cards'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class AdaptiveCardInstallAndCommissionAssets(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'AdaptiveCardInstallAndCommissionAssets'
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
    print(AdaptiveCardInstallAndCommissionAssets().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZfiyJLlX6GjP2RWKzMEWpCU77xzRiAQAgQCCS1U1snS4tr3BS3V9d/bBURkZdd7b6Z65sOQSyDksuWa2TVzJ357MZvaz8qXLy8yMNMJb8Zx4INyYqbOZJm1WRnBH1lkwX8TO0vrMrCaOiurl08vDqjsMsjrIEvh41KZOY0Nqok5KUFTmVYMJqxjwts3MFmapTPZysfDpErNvPKzepK5kyCtaqjvrsvOkiSoKihrYlYVqKsJvFc31cTNyglILOA4QerBRyaOWflWBgVWn+ANM4jhT7hGAWZSvUKzQGcmeQyqly8///LpJYDvX7789mLHUCw0882k0SLhoZ9NneW7dvauHIqJzdSD6/MewpPC6xyU0JQEfuQAd/K8+liB2P00+Y//iFqz9KqfvnxNJ8/X15fxz7lJJ7UPJnVmVjWAbpq5aQVxUPevEzZuzb6CaNVNmY64VRDd1Ht9PPldUpZP/j7e+/hQ8uqB+uPXlwyaYI7Yf335afT/60vZjO9fRyn5x59e46wF5cefvsupGisEdj0Kg1a/fnteP8XChd+XBu5d69+h1EeULfD15Q/Oja+H3aOf8MmX1zAL0o8PwXmZ3UBqpjb4+NM/E2v7wI7ioKr/j+T+/BDsA9OBPj0N/+nTHeRfJsjToXeZ/1xtDsP6VzyBy9/UfZo8gfpnsu/4/zfRcZDCknhD/B+K+0cPIH+f/PxPfftXD3yauF9fOBDDDC/HEvwy+e2bLK2WP39wvn/44Zffoej/rRg5a0r7LuFbYqaBC6r627efP1T3jz/88vOHJoe5BsvuW1PG/0jmP8L1rucHBJ+rPv74LNR/SaM0a9PJe6ZPfsvyfyt/f52oZhw43z+vvkz+WC/jC5mMTrwpfUDwh5qpoK1/wPGnl98hU0A2KBv7fhtW+b//+0QM7DKrMreeyHbW1BMY4DpIwGi84gfVBP4da7sEENcqGAnvsQ7m/xjh0WLIcr/+L/vOo5/tJ4+i5pODvtmQhL49WfAbZMFv31nw24MFf32dKFBFVgZekJrx5MxK0tfU9EBaj+rzElSgvEFisfoafIaU9Hl8M9Lkr39By7e7wNe8//XOxcGDs85LYeSrqonB6+iz5oP06aENWwXogN1AXXFmQ8PcAFLuJ4hFlcWQ8OsRnyoKILs7QQnByMr+Lhti+GUU9uuvv1qQyL+mD4LFJ49eUqFwwbs5k8+foYduHHh+/TUFtp9NPvz2+4fJf07+1VN34aMOCXr3jBC08N5+YMU1CVxW3ZsPpJN7hH77/YkzFJPC5gfjGbgBeDwMMzYCzhvo8ob9jJHziQUg2BDoJM/K+t6Z6teJ4E7e7YVKx1sjr/tZVU8ckIPUAandQ6kmdOcdyRR2wwqmZeX2nyZNBe5af7VK825iAkvfrH+diEsJdpEshv+NZt4XwYezNIDwv6fE43MopPxQTRZvIl4nhzFHJ7lZmrlfmk8drvmIC+web49D4eYkBe3XdGycYITqXjAPeOAiiIz9DOnnMeb3xg0DW73pvq8xx16n3Hte+TWtnsVglmMobNgcoFKvCZyxRfztmVJwKGhi544ftHSU9IyC84zKPQeFfzkyyI+R4cex42uDTWfE5P+P+WT0geX584pnlRU3WR2Us/HAdhyuxhg85jE4INwl3+vo+9DwRjlvzPs1jQOYKGX/t8fKe0Seax5s1pQQwDN7vsuH6QCxHeXes3XMvrIc89z8mr5R/CcI0J3PoKewtGHqjxn3pnC8+2apDx0dr7+3+3t0IZIQMJiRk7yxYpgtLgCOZdoRtKocK+4ZEJi6YES59QPb/8GrCZQOMwTKn0AjAog1bAN36A4ZdBPC7JZZ8n15MA5R+SO+zgROr+B1osGiGROngpUKJ6FxDUThw13UJAEQY2jiO8KVb+YPY8aB92mgOcYiS2Au/zECz5vf0/xuy2g+lAo5t4ZYtiMDO6B7RPbdzmesoLHJWJj3h34M99PXyR970d++pncb30kf1nt8T9/v4ExgnSXVPVFHuqog5STgmUAwE+4d+/XRdB9d/d2WL3+a8j/+tY3AvY1efozcl4lf13n1BUUfre+t873CKkJhjgQ5qN674OexP31+1tpnqO7z91r7/Ki1H1Q8EPsy+Wtm/iDimd9fJrPX6et0vLUPbDAm8PMFUVl+XhififHu1/QMvof7mRMj68Y9bLvvLehtCexDXgm8cfGjJVVjJ2th87xzMAzI1/Q9JZ4FAyk+9cb+WWV/KOR7Lx6Z5hGyt1YBb6U11O2M85wHxj1PPJpfgZcvaRPHn15SMwF/Za8z9gWYvRCVcasEKwnOSXUA7lfvM9N48eOW715jkByc7MtYap8m43z7afI+qn6avG0e7vuytIG7p5/HMXlUCZfCH+9r3/eTFniB27a6z0cPHjuicTp7Ts1/NmKsMGgxZPZqtOWtZEeNfxIC33geKP8s5Hh/Y8ZP3oBQjZ07qN+qvYJ2OnAOgox+G6sQFhbkywY+8Gc1UE8Jiga2SGd09zt+393KHr78foehfmwrf3t5449nDJ4jJFwOC/VzNTZJFOYrVAivH5kF7/3fDJdPUZD84EQDZblzCsMZhqTpOTW1MQKbmg7BmJiDOy7NWJhjzzCMnNkzcjbFHZxmgOmaOIlhDmlPySkD5T1S9aFqNA9MXYAzM8x28DlGkgQzozCTcUyCMk1nStPUlHId2B++PxpB5nz6/PBxBPR9zh2xebr+24s1J+DKDVEJ7OO1RBnVpPS91fk6M8xdIwvpbCufsobSYUuuj+uViuFG5ITIBYvwFTFnt0bkNwtt4e1l3pglVcyRbDpsORynmh0nLPHNXJcTWgm6xXEAtyuapmUdrVg5JKmkvm6NbWLagXhtDjUkZX3ll6qmr6+yVmJZMagLU73FVqBvzRyR0k1Ky+W0OM+yoj9lsTyLdT5ZFDfEvaUHGVsPmhPMCuN8Xab4TXZMp+bk+LKtjdxMjyrjBZck1StjzR7p1b5QJDoYoPjDYNjcaQ5Qq2JsbagGW9eJZB9jDHA7sDtg1ZrWk5iOSqGJC+sSO1YcN3V91rZ7Xq5EvODxPqtKr7biM4v36dnu0z3VLWew7YVRjC0WqXqeFeq+Q5p2FpD2XO21/Uy9ZGlsn6Bv5obbm/26vcXmNLHF+WxXp7thedaxNXZlQn+OIQHp55spmPGmSep7ab1pzWTvnRW/9I/OLD3Gq/1W3RkkFCg7gi1sBMWkhGZwytTscGrBn3Se3NYZu+RDAjsMsc3Ue1YKfVy75oe6C7S4yNvLBV9r+aVYH5DmKuu7Y2kHap6QmXJpXbpfditrUSNJ5pid09Pb3KiyUo0wGaVnvFqUN0cvhkvKgrRwjktHMInkVOyGZO457qDuZ3ikDTOa5hdRFCxxQY0P1ABOFTEsfde2ckTUOEAKATMw+6NoU/oQ7PxLY/F2fE2P5bwzEgLvEWMvJFQurvdt0i11FFtm/RoBvKJMcTIoeRfZZ5cqtiVRPPM3MgxsMV5LC7nDF3vToH26Q6jqWuwd9aI64dzaWm1Hu/VyJlYib672V82VYya68Ffn6KrqwXaKaTEv8mJeIkubvNroOpdvRoysexC0ri/rwfIwQ8vzmm+QEG17KZ32CJK4tLKfajd14SSpJ1s3a6rRa8XIHXVz1SwxiopaLVRzejxuDcziDKHQOz5zZGF1rYVbuJQPRq/3CespGgMCddjtiMZifTz1DvR+TcVrgzwS1rX3dZY/7cnzmtNUPtID9dAfeyFkt0kTaRyrn+Rkb1RlMfCLTtxsbjYVnwF3Q9pMzbBKzsJLvbKNmNaX22y9UbtA7ewunmtMH2xBG7hSEoCcybTE6fhBTVyu3tXbo0pTF5RECa4+h4keFYqe92pcUYi8I26ORdtsuCjzysCqXit6R2nPBBVgLe+Xwpw1lb015TimCbIcwbJIk6YhmFn55aJdArtEuiCnivS4WOTngsTcHjlV5VxkhPpUnBQexX3aPAixrRKEqu6rDRn3wfQ6Y25KcZs3cSbzF/OiHtvlNdvChqCvyrVWhwKpuhGs60M+X7NhmSzV7CCdECRb9k7n7Ituqx6JrYukaTGletNHts7tYLEHVZWYJaIt6SDZr6qyrqO1a6wQAl0vRL32+MrnuNS5Gk6oHVfzq6KuyH7hrC5WblxnQ75farWircH6Vi2JQ8HTuyHQlxrOEGhiVbGpUPnM2mDx/HAmLrjuo7oqDl57mld7oRFnOcEhCqxXHQm0DpJi6G4Rrj0pkSuhpC5I1CLCs7ZlOEcnT2c/vqXVyWQ4qpcST3HCKbIbMoy9TLnNoBVe6eccyTdYdryQ/TYdbHQTO+1uA1aL7fF6ANKGVsRSLbCwVrxduq2QqX08BYYoe3y0nfUeVZIHPN+1nWOEu9Y+VAtBjjeRdT0adYIPFqjxbqf6m4QlStOzQsWeFds2r7NzONzQpWcYMSqUpSROL8LVz6zLxe6oKVEGyygMYUkVAUYXLHZkkC3VD0eFa0MNc1xpQFCwicmTvF+0wqBWG52az2U5XBXIgUqv1CoiojUTMbvuukFJz9Ni/GZzzcm7xvIyc3uFRt3b4Cm9209NUWEcLw1q+lJznHhkGD1dbNm9FJxl/2ZKW+2qGrIFyvQiX2cqhq7pDXYagqtlb9ftCvqFpmFHS9yMPGxwIlhfq3lWLHlytZas1VqOpYH2TCNvuWR34gcWRwt2ts45tlgjmbVB+TjOPTzZ49m+sBjagA0GAGVnpVf0IhNEnZ/FiyMaXSSueN0piwRfzJzDrKDMy3KW1ABUi1Ah1luZk9sUxeTEvmK6Ryk+O6+6eCi7ddgs/WSKu4ZnHSPG3VsaAqvxuhgyUjg3UbGLY7Uze7GkPHSHXxRbmO4Ur0H6kI6Nk1De0jbCMTs4RymPlg4xU648v0yX5TLrYqNFDzJ5WZ3a02J9YWamWedecp5OaZ7SctU65ezW3vl5gPOHTKbjLjt4mqLi3HmLWq1/FRvN2pGFlVcFK2wqzvel1mQWCq12UVXNlfoKNpeQyzRDP7Z7oimGUj1XrSmGJyVu03Z3DQnTZqQc9raIWZ2nvnDrqWm09Q6rjKrzg2r2QpPpfbdTOEMH2HSY7o0N4tQF4Ven2GSQTsPpDtML3zTjq+oJvrlRZzt/jzbn5nCGOJIUJlY5JTPTYDfd3pbxVicif+5Mr8czyJEsgzpPa3bwz+msOG00PT/FV9/USHZ/tq4BftpqRW74bMOpBLpdq9hZWLBeYtTiAsF3WCxRpyhfXDzUVSS0ajCB7DAbiTNyu0vFiE39fWuZJ6BAEsxLA46caMUG9RJ3h5oi5rTKr29yE59ODrYETCamUXJI05yanpsrEcxnrr6Np0cKu9rnU5jPpNy1KvzS3sSZ6J2jvazjLsYJgswvfRbjpY48753d8RzZkBzMxQG6Jh7OjpQWRD4kubWqWtczKz5PXDnXt5lwPAbMybst+PyU9erc3nm6g4t9kOs3SztaGG4XUc/fhFLFStvcIku9WvjyAZlBQvWs8iSfLs4xn29ZPZemy1NtN4Uq2MUgKVus9zjR1NnsIrTTZic4F3qKFpJWyjAJHe7KHfsE88BynqOCOnBLOl1rSHTVCRHN8bOxr4IqFsgzHdnpmiJwf9Vfkr1/8Q/WtkUWIN6kly46ZNrJBgATu6MlymSW8xf7vLrwziG0lrTcnJhTdD1iqg7Cem3Yi2WdyJS4X6ukAvtNWqg9PWJmzc3ApaR8ukXYmxous4uUhCm9dhNLY4dGwDYbkqgNhh6uRnoOw2ZbAtFV17szMHpMCUvHVS5kGzgkJNzrYei9vurc44lHe6IwErpebVYZGaw2feILmwXYT7kiRjMe9NF8Z2hYsfWdAaQsYq9AGNIo5Z1vhcwzuDUj/HLmSMryYmt8WVrCAgXxvghW0VItQtPZ0lyx3dUksdPrRSkmbHLalbmpyfOtOheUws/P8zTeQu4lSY8C6N44c8dzsatwmET6Xrl61+R0HvhhHwZB3zstNVXsfCZGaa5cp7KCHFudjrItm6puyE9j2td2Dqfrs91C2pzk2TTyTjIsHTXk4eDYcIWXEHY100UcbgW6U6cPnevZMjuTUbwoDdghI8qcCnVxXJSepYtFvLDpUD00zBo/oBewmtPxwhOkBt8ep4QIewftiNQxSIZuvZ6XB8ZQjsja3p0rUdb5+ZnU13kZK+C0YDcca2Cs0apnxeOuM1McinZJngbyyElkn+9mCHOJzOw0zzo3Q3K/ia+MaHAwujTBN2vhtK9kkT6kmmfYt6z1lYDO6M251aY1ZAcygGN7zHOOP+sJk17p7uBM/RToJZhWq+GaHTa6Ks1SRRC8yDRNBvJfg5F+RLTTaKg8mtDpGjdbi7LntMRswgG5asXx3KHF1LKpjdWTmdZIybFHNnHfMBq9wJE5orNw5o/7hFNgMXo4LipGEe9cp3HVDJ+J+/xUb9p2JW1vVbna5BcFuTSuRlDRYk4tzYpJbjtWOJ/IKM9I0pVX8yWF4NM9fuYUdjCTik7LwVQ519l0m+UiWB3p0L0gLliX7K0A1Q6QW8S62oR94Bz2jFI7ClxKuLfkWoTDnJqc9WoUAnXTIetjXd5sbIprBLlOyQFFmaWEeAkZY3zKlBSyvVG4ycQbPJVuxSI/KpRzIS5OVGYLhM/mElvSerVqAppYrhJ7J2ooccohmLwkzcxrqPssscVIQd5oG2IV2fYFD1iCCxLQQeOHEG6muVsK+hXPHK4xVc+PC4/BT3xTX4WCPZYNTYZ4zG/XW9EFfLyOeHe6tm6J2qAbg8WNhrr6uYB2mTjMpvwgWzxtX5xVjuC4e1Fp3y42qDDVc9XLC2DgJ4bEO9wzRI8P0PSkW0rFrOWp6JT4Zovd6FnJWIgUDqwfn3TXPqOseN6uUCDFjs0N01S9uXZ38GcYdeHCYN+wGyoImiG0NIlO9m6hkc6qFW4Wcxq6OW7XNnDoMDku5XAxMHgDLPaUEg3eT5eCNgsjKQT+iovOAbPa1CVT5JEhHPdwlAEJdTm08g3d9ox9GqSLt+nCI36UdnkLa3u6NADD9vzW7WBTkFY+pLgFTXCcVl1vyz1CXDTHjRE35TqaF+AsTWzmp11/ZW5GCjdxkhB63rCwvHi5aDZ939o7jjNyryg3CJpty+YQnBL3hlvEsveRNkT2h/mhonDjdr7s7WtNSD1gVqlYerQWpKRSd8OC2u58MVrPKUncosdybyiMe4YDQuOg5gGh5fXq6Gag5Fi3DViHtrlrO+UQsdkOGheKYXiTGjdFiJrkqU1TetxuYRzqM4N5OE9lgz2ndilo5oDqYKgE8SBTtSYQoGyU+RHfs1gK2DXXJiU1Py0YwumMkJ17oO0QccgYU7DdTUbQl76cl2ktppsteWq6QxOdGIECZLhfBEiN4TjfSoMT31BjrlLMoLtst+TQDScxlH08nNDM6EoECMYNUgJ6qQ74TlF4qwn5cIArXMdU8NDDjBlFrxmkkUW7v1W8AeCEu7ocBU26bLTVrvLWUqjqznANUa1yF+Uh34Rbs2nMhmFL/tbxCJ9na++S7+e3W3i94tVhdTpYduv0881+2O+bs4bcHCNNMjKr2eQmmivTMsh2xXANTrAsHNX83SqxIn+oh3AqkOLBxTDh6hxuyEzfdzMcq7qwOmenOLPO7hWljullCQafdtcLG+tEZNvQrd2ylS24rbNb16JgS8K87JeomlzCoye2ThxlolQDHM4gduxel7PNXok32Xzg9lRBhQZFHBkXwFF0fXN29gHpEg/p+isk3v1KsokbJdlhDyiqXxJzntj6LmmcGss2d9pMoktP9pHCFZ1DxtSouCBviuUBm8XB1pu6cILK2ilu2KfqIOHhmb2J8T69AJnrYpQ/SsXaGayNoUo6pSdpWcHRCqUXebW2ZcfLWZb9+8unl/GE+nnO/D/5pnk88Pt/du74OCJ8+xbqfsgMTOfLXdeX/5F1v3x6Ke0A2vY4ca3ixnseSv6389bPf+FrjFFQ//hKd/wKravfzutr0xt/XeklSJ2mqsv+W5XFzf3w99OL1VTjr0xU356H3C93V5N8PDH/wbXx2r6fO3+rs29OUOVZBV7G32sYvxwCTmDWb5fe80T604vTwxgGdvUNn5PfQJmPjj+/HYH+Yq/T19nL7/8Fz3Yt7CUmAAA= -->
