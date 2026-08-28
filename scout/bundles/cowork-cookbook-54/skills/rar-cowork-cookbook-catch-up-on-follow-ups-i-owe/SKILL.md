---
name: "rar-cowork-cookbook-catch-up-on-follow-ups-i-owe"
description: "Close the loop on every contact you met but never circled back to."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/catch_up_on_follow_ups_i_owe", "rar_sha256": "99c24877616770710a2460b244cd5ade6aa0d57c7cda1de7af5e7156dede9d2d", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "prospect_to_quote", "beginner", "integration", "dynamics_365_sales"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/catch_up_on_follow_ups_i_owe`. The original RAPP
agent is preserved byte-for-byte in `catch_up_on_follow_ups_i_owe_agent.py` and in the RCI capsule.

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

Catch up on follow-ups I owe — Close the loop on every contact you met but never circled back to.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/catch-up-on-follow-ups-i-owe
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `catch_up_on_follow_ups_i_owe_agent.py` and embedded as the fenced Python below (sha256 99c2487761677071…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `catch_up_on_follow_ups_i_owe_agent.py` first:

```bash
python3 catch_up_on_follow_ups_i_owe_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 catch_up_on_follow_ups_i_owe_agent.py   # or on stdin
python3 catch_up_on_follow_ups_i_owe_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Catch up on follow-ups I owe — Close the loop on every contact you met but never circled back to.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/catch-up-on-follow-ups-i-owe
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/catch_up_on_follow_ups_i_owe',
    "version": '2.0.1',
    "display_name": 'Catch up on follow-ups I owe',
    "description": 'Close the loop on every contact you met but never circled back to.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'prospect_to_quote', 'beginner', 'integration', 'dynamics_365_sales'],
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
        "upstream_slug": 'catch-up-on-follow-ups-i-owe',
        "upstream_url": 'https://coworkcookbook.com/recipes/catch-up-on-follow-ups-i-owe',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '010809eac7e6b811',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'beginner', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-sales', 'process_roots': ['prospect-to-quote'], 'process_tags': ['prospect-to-quote/manage-customer-relationships/maintain-contacts-and-accounts'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'prospect-to-quote/catch-up-on-follow-ups-i-owe', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Calendar Management'], 'plugin': []}, 'verification_status': 'draft'},
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


class CatchUpOnFollowUpsIOwe(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'CatchUpOnFollowUpsIOwe'
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
    print(CatchUpOnFollowUpsIOwe().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/616eZeiyLbvV+Hm/aOqr1WJTKJ11lnriSKoCAiiSFevbIZgkHke+vZ3v4FaWdW3z+l3znqPzKoUImLP+7d3BP72YtaVnxYvX15UYCYIZ0ZR4IMCMRMHWaVtWoTwTxpa8B9ip0lVBFZdpUX58unFAaVdBFkVpAlcvorSEiCVD5AoTTMkTRDQgKK/LzLtCunTGolBhcDlSDIOIXZQ2BFwEMu0Q6RKXyFJ0JlxFoHy5cvPv3x6CeDnly+/vdiRWZYjC7OyfS2Tkk0aRWmrZeVWagFcFpmJB8ezHqqSwPsMFG5axPCRA1zkefexBJH7Cfmv/wpbs/DKn758TZDn9fVl/FHq5C5/lZplBeWyzcy0giio+ldkGbVmXyIFqOoiKRETKaElEu/1sfI7Jaj538exjw8mrx6oPn59SaEI5minry8/IWkB+RX1+Pl1pJJ9/OkVagOKjz99p1PW1g1Aq0FiUOrXt+f9kyyc+H1q4N65/h1SfXjEAl9fflBuvB5yj3rClS+vtzRIPj4IZ0XagMRMbPDxp39G1vaBHUZBWf1LdH9+EPaB6UCdnoL/9Olu5F+QyVOhd5r/nG0G3frvaAKnf2P3CXka6p/Rvtv/f5GOggSU7xb/h+T+0YLJ35Gf/6luf7XgE+J+fVmDKIDJYFoR+IL89qbK7OrnD873hx9++R2S/r+SUdO6sO8U3mIzCVxQVm9vP38o748//PLzhzqDsQbM+K0uon9E8x/Z9c7nDxZ8zvr4x7WQv5aESdomyHukI7+l2X8Uv78iZzMKnO/Pyy/Ij/kyXhNkVOIb04cJfsiZEsr6gx1/evkdIkMCtant+zDM8v/8T+QQ2EVapm6FqHYKIQY6uApiMAp/8oMSgb9jbhcj8pQBNOxzHoz/0cOjxKmL/Pp/7DvmfbafmIfaI+a81dlbmry5d9iBN+Vb8AYz9tdX5ARppkXgBYkZIcpSlr8mpgeSauSXFaAERTMiXF+BzxCDPo8fkCBBfv0rsm93Cq9Z/+sdhYMHKimr7YhIZR2B11Griw+Spw42BG7QAbuuRvC1oSRuAEH0E9S2TKNmRGUoThkGUYQ4QQHVTSEwj7Shlb6MxH799VfLLP2vyQNCCeSB7CUKJ7yLg3z+DFVyo8Dzq68JsP0U+fDb7x+Q/0b+atWd+MhDhiD+9AGUcKdKIgJzqo7hNOge6FAIGHcf/Pb707CQTALrBPRY4AbgsRjGZAicb1ZW+eVnnJohFoDWhZaNs7SoIC4jQfWKbF3kXV7IdBwakdtPywpxQAYSByR2D6maUJ13SyZphZQw8Eq3/4TUz5L2q1WYdxFjmNxm9StyWMmwTqQR/G8U8z4JLk6TAJr/PQYezyGR4kOJMN9IvCLivf5lZmFmfmE+ebjmwy+wPnxbDombsFi2X5OxFILRVPeUeJgHToKWsZ8u/Tz6HFbbGOa/U37jfZ9jjtXsdK9qxdekfIa7WYyusNN7lfbqwBmLwN+eIVX6aR05d/tBSUdKTy84T6/cY/BekJH6Xu0fUfwZRjGyRWAUI19rfIqRyP97XzByWnKcwnLLE7tGWPGkXB8WGGmMlnr0MLBQQymKR7R/L97fUv8bAn5NogC6s+j/9ph5t9tzzgNV6gJyV5bKQ8ZgjMGR7j2mxhgpijEaza/JN6j9BN10xxWoHUxAGKBjXHxjOI5+k9SHWTbefy+7dx8UzpiOMG6QrLYi6FMXAOehv1+MefE0JgwwMOZI6wfQ8D9qhUDq0KqQ/mjiAEY6hOO76cQUqglTwi3S+Pv0YGxmoBRObUNpYccHXpELDO3RvSXMJ+jLcQ60woc7qdFHfgpFfLdw6ZvZQ5ixSXwKaI6+SGMYcT964Dn4PRjvsoziQ6qmY1bQlu0IjA7oHp59l/PpKyhsPKbPfdEf3f3UFfmxJvzta3KX8R2LYVZGYzn9wTgIzIa4vMPgCColBIYYPAMIRsK9cr4+it+jur7L8uVPnfHHf695vpcz7Y+e+4L4VZWVX1D0UYK+VaBXmNIojJEgA+WjGsEc+5wmn78n3OfgM0y4P9B8mOgL8u/J9QcSz4D+gmCv09fpOCQENhgj9nlBM6w+M9fP5Dj6NVHAd/8+g2AEw6iH5e+9MnybAsuDVwBvnPyoFOVYYFpY0+4QAD3wNXmPgWeGQORNvLGslekPmXsvkdCjD4e9IzgcSirI2xkbKQ+Mm4toFL8EL1+SOoo+vSRmDP5qUzHCMwxPaIVxDwJTBTYkVQDud+/NyXjzx33QPYlg9jvplzGXPiFjI/kJee8JPyHfuvT7hiep4Tbl57EfHVnCqfDP+9z3TZYFXuB+qOqzUeLH1mNsg57t6Z+FGFMISmyDseSm7zk5cvwTEfjB80DxZyLS/YMZPYGhrMyxgAbVt3QuoZwObEc+jYgO0wxmDgTEGi74MxvIpwB5DSuVM6r73X7f1Uofuvx+N0P12L/99vINIJ4+ePZqcDrMxM/lWKtQGJ+QIbx/RBIc+7e6uOdaCGewk4CLFwsbJ+c0PcNmND2lsamJk7OphZOk7VBwTzMzzalD0TZtOybmANp0KUBj1MwBDlg4uAPpPWLxbSzGwSgPmLqAWGC47RAznKLIBUbj5sIxSdo0nel8Dtm4DkT870tDiIVPJR9KjRZ8byhHYzx1/e3FmpFwJk+W2+XjWqGLszkjBEv0rUkxc5flbRFW3d6phMYpCgHkoJzhdjuNCF6ldcVeH2s13Krm1vdWt72Mgf1VnqpuGU46wpY2YpDUFupwh8u8ZG2eaYUKpda5lwaBlRDc0cIi5RBd+igIBWfYVfty5hyI4w2fk3O0dMWVafMHpWBW+1MlNoyO3eJLLq7bwdpDv/gXLrti/u6IdyfRMLb6/jKve5NTzvIuduQk6oC8jmjXZaOauE0mjWDFAs7Ju62nliJ5Hcw8iq88cynK3VoXwOF8ujjLAWUv1rGPTit65mzW+wpYGE2tzNpY8asN26WHStZwuehpcZvt2TJVuD3cp0Sn5XyDCddz7ApClJ3bnXUxDwc8qHYadcml1sxJLK9mspJKgJu1xEJ39LxQfSo+RpdgOpwlIEZyyQ+7AAu7yFhREp1y09u2UDbC+ZjH57qLtzhfoUl43R0kM2TxODqaqBXmV1pIVhM7xS6Lc45PCU691AzqHmKPIi3tWl9dS/b96izm5zAn1zPTm4hyoa77gbWicGG2oDwUGRnnxQzLE6lvqqrfNtU5M1aYJ68HOVH2oWifuoQpJ0d9vT34bpOsHAu1uiGVjpcscWrOKvSkWxWJVXlOg6XXRL+Z9L5f6JQyZ1SJVgcYIwERe70o21kxnIx8T/TzVpby/HRg8oHH+4QqN+e4tfGLDHJac64Fiots0WoNzmyqLX5Y7Hl27vsLW12aWO4ee0NvF4vqsrSufb6Q1smOPgiHgiyH6oQxysHfz3bSYe7lmbhxo+ZQF7XR3goUbhh17UILToYZrucRLsOXV5n07OtEy2IvFU4oedgNteO66wbdt9ckmglD3gB6x8vNRchuUl5Fhqvs4p3QLqz0YlK5fZHctBZT3091wcb8yTQpgDHd4ySAecVE9jSsjpJHUtMm3KEBJhjGjdO4uHVU0rc8AlWOq1A19izGtqpTZvWOULcqZ1vdRp1eN7yY41mNnRImMCWD61HqHDPTSZEM/aklu1MYmGbGRtdoYGT6GGiDF+wjl2ax7WyYcKwy4Sg60c72hlAVZsJjAW6SxyGlXKKbsMOKN5XjbYdeZj27uJqNeDbck8GRa6vHVfqYc9VukGIZZiK/VPPpKWVrjkCPB54G51SbL7cYTyt0qsZafFArctp7AX3Ou+hipTs2CiilYcjSDaUqk4zTjaYW3GRHpfpxOtN1hiQVE9ObGatCBMInVpdJ2u543YM+C8+ElZXq6bCHidnBkKTw7TyYOpYYzVJGWGa37XoqysOMP+xjQ9JMKqakLT3Hlui17yzhipoLBk3DqPX9+YAFG3pjn4fLlOuuPj/BZWtFemWBt8Ll6C+WYJMDUl3fmgPV3m40kwe12tuDoCqKRnWh4/TGZevSJ0NJhV5waxcV/aRDed0JNiFB1dfkkACOi09Lh18Abo6uy3XYlrNQiBNPJmVNZyA81vHtcs7OtCavvTZCAb2wlzTLK42qEqoYu2eGCWELcVrurnwXxpx+iNZ86Ssc2Kh2FU6HFZnJ/bqf5oU993y2c0NqMtlZfoiVi/iaVzTf01JS4Ju9rq0p2E5pTLCYrrSjuUq7db1lZGyTJ52OM2x+cC7rtV1TxGa7Cnes4XkLwrCUqjjOrv4ylzqf3U8y7uopabSPcqUdWM5oqcN2pXHBxqLKWxgz23nCXKQYvdoVaR53hSZNp6uiOoIiRCXmOEXVY64ljmieCmoG9KFDHY0NWn2lRbdbQTfObqfEXINJEV5TO4lhjo4UnA5rdHI8SiSd5BJ/3a4UO1j77XwC0KXcWhIaTNHT0M04s2Z1RcXneKY3t+V0d2WEUj2EgqXQw9ErVwodmb3ZZksuFrbX9MKLWsMwZb6Zm6433QWGWF7t2F9dGoc9ax6pQkG73XRtA1uyFaxmZ7DXPe+40yzcMyvV5YYzoQp0OZhiYOueSWy0lSLZxtoLpXO5KLTTzSNKf3/BbZU2aHqZu8nqMKWGQTgvWb3ig5kXpms04xVLR/srftZwm0732N7oOpvg1uRUq7u5smWFtdVk5sbTHFq38tNthUXHQ77fySaLod5qqYsy6XZ9Nuj0LlzMFUMhuVazeBxrDpI7hLhRQS+RBsZdBlRzufNqx2OeedqT/nITESBb89e1n7KMd5H6rhAuhtF6TEe4rigthUg4DAZPpuIlXoueGea5Osc4wQ88amIFgb6asMLGy7lsE7Bbfrou/LVxdZeNvTNXIn7B567giVttph3CVSf1Z1PfZzgbexvYI2ycLkmzpNGJHoXJrDAXgglPwrVl654xDPJaOWh23a35luI0UirCVp7H1xg1Fow7kGKmbnp8fr60lQEiwZ6Hp7NWtN3aKExKUtTt2aHkHcNudScnNqK9MAB5cfsLHpmlNElZJ1lwR1iMLsGhbg2QZ6tUqmY3di0Kk9TMxG5vp3S6CTrTPNw2QXDZMavzLgwOVeBrtn/YzswZP613lYDi/v60lpdmnehovBJa03Gy4WLU0rJbZd4yIhwRz2+EHVhnKOMZkzjVpyH+LaKC6G9Wd6AVnpVt70grFbbd3kKOl6QS80AoqcMEPTdR7SZi0BgemVyyBqendWhuBGXbLyfroZHijIuX3nnLDVpf5bHWNnxUuBe+73TOMP314XKiRF0ICDFf7c05k5Z7luFm53l2VWekbUXYNfKIan/L62Gp2TROWuFmv5hx2J6rnPnumOUXEhPEc2Py3gGGy4qlSRONALMWGVFSpkNSsDs7RFVjY/m91vGhqPCLXWGvhmy5xttip/K2oG4dGw/RgNcFlTpdsXqmDvay2SZ9tXcn18N1Bk7BzbEvc3J3CutqeZ6f5NNa0oSW1S5XUHOSoO0CMizVZa9tPQlTCoXdOBsflwre4K5hI0B/W8EeTxcrUW67yJ+ste1820oSDeKF5ISRJjjEgjdiLcdycWGq57xWMZIMUOaiT6KQmNlDe5lHy2aeLKYsfaGve70wJeGyxHFMvq6DBmOuje5KTauv3Wzde1tn3QtVSM4IYLKcwNKTs6xUDMBPQNo00yMDRMDVu72gcN3+ADW8eTjjtUoHSvckYXVW7DgVY8y2brgNViVL/rjbOCLf+FPfPeQHq7kq7klbyLuuU/K9T+26BmDi7riqejar2E2y6oeltxTN0BKOx/pIaLuzGFXmIjXU7Unec5iQ7y8C04u6JDTrxOpkX9sOHL0f7BXZqZXBMXV6EwXGxhYwlqLburmxPa9VizImd9ugImjOml9gbjg7XLIC15Q8oYbOTdJj60iismWO+Ubu1Dw65JIl6Ca3P7k47XHy/NrOqUxOVGzJz6XbWa9M7rzByeZiaF7McBNeXkNgGM7oFaQRkeZURfo9pW5xd9sGM2eOdl4rV0XF7qvZhdpPmYufthy+Mo9or8CqU9yuKdyBV7D/Mq5LbzYs7QMsqRtw8pdBd77wKr6P1odwOxXOJokl+hWNO5+Mgi5dbjSXN+W2Oa6lW2xQ5XIVG9ujkGs6ea3dZTtzFO9GMZsdld0UMZslvmzmbCjvDyt6n0eN6lJ1kilycZ3SUrWXCazbkrPZtk6La6dsrpZWYIWED0K4OhVLpa4oJbs2leHwjFT1RY3ipjTgJZac+sbP5tLsdiSvebY5hdY6ndcBWuiXjbtuwZmkwHpvCmorDgYw6I28lYkpuTc93rRV9eTE/S2dxjUhe1yt8LbhRGKHb9cdJms1LbqJcQyUYLuxhaAKjek5mTekHnPHZmmx4jk6EHg13VC5FNTkpj7SKrM4URi91SlXS90ZoHawH9PIUuSdpdLQ5qyw9fCCbXySLmm3L7xmy1SSfKtFxhGaK9daxdxWB4hw6MRn0XRzgC19gVIUGmSUKxB1DTQMddO1rDZGG+dJKjqsPNjdiaqBL055X6/CeKevqkiebYR+v1XWBCoEpNUuWZK2y93ttJ6sek7sre7odJOTPKt9smT7mjgUmyQtmULDnLridzOJXWZrc0UREN4pV2/2wFbOnTpscVhFmzTpA7qiLFpPcQ/ooY7z9KTAgzndp/ug7yRhMj9OeMvQz3PfneqdHFa3fGkNMntJwPw2syAeHofMFEorhlv2JJsN2NSCzQa/MMRaQGfdgrjtfN1ZLebMoVpuxGR9KibCrQS4jYq0EQgllxSVJ3DpIqos3O5KF+CLRmyJPCt1XVpHJ73g7ZPEUwRHu1ul2npFa9MObJUJQ5l0+ea0wYNONHYL1pKCRSDpiTzPgL8n1eWSkEqZD/USa4ITNqsTHrZqk2QJDqVzS1rYCF0FkzvIoHU5FQwFH4PdosMSfvDkzb47L3YC6SsONomIgTzwPD93OnpNHXktiDJLX9wqcGG6q8OyV11lTwciq7y5FvDUydcKmV74y+JsaR2Lyn0xW/W3SWvRiyrA8oFwdQvuy+f4PLFEEBSxMdUFYz0vcMzWwMwMB18ERwX1iFXZLOzd9GDpW/qydiu2c1bJXiLSNplcfOzW9eLtphDkjExEU2JzqUbBSWzoQNOLEpD18pBtUvzM66psC/UN62CLJi3E6YJQ1nu4TZ1V2P5yCmacp8wkwvOG5WGpGO60zGiA89dE8ZSjXF7R/SYElbaXbj1Aw9WNzpJsT7ft3NOvNLHaAlYsnLyb2y6HGnOGICCeXdxBHGi6aLdZLZLlYUFg8xl264NNB7uGK1g0TDZZ2ScQnVeWmoGWjnGuhr41mNpMnclNRn3M572SbnWbimi/b2ABVxRKoYKVeWBOoCAsIhkood/at3226LhbFhf1LJ8wdIuSU3E5ZUNS0LC5JsuLtgi427H1CT61G6Gc7DmaPhIBDbtfmkhTmqyDzfose2hqX248s2A8Z3f0lFjkEyHhUwU3Vo2Gh4fqaKGNoS5qx0/IcqPKK9a/Oc5Ml7UetP5c5pn5BYNlT6cYLF5DpL307Fy/eMIg8WKwL+ZqMa1yJVHi66Hv7RXfJ9d2pm12NK5VzHzRr+eOoZwXuEPZzly2G3EJm0KijGpuvhFs60qJO6yuer4G+mJTnHpAWz2EBo7c+CAij7Vlq/0F0xfZ0fQn3rwxRHKBkaVCNSfBA/aSAEqKO6Gghm1I6PNjKR50o142Un4sw/mRHvQZQwJv4QwCb9u327mZZf3sduvd+XLCihMjWKbL5fLvL59exqPk54Hwv/Rqdjyp+/92YPg42/v2Quh+HAxM58ud15d/TZxfPr0UdgCFeRyGQht7z+PD/3UU+vmvXiGMK/vHW87xfVVXfTsrr0xv/E7OS5A4dVkV/VuZRvX9IPbTi1WX4/cEyrfngfPLXZk4G0+v08oHxeNBmQG7eqvSt7xOq5GTBbxgfJP4Mr7Or4D3PBD+9OL00BOBXb4RM+qtNMevA0H1nq8joFb46/QVe/n9fwCjdLD6uyQAAA== -->
