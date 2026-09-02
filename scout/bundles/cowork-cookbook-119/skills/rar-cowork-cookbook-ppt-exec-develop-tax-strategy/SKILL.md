---
name: "rar-cowork-cookbook-ppt-exec-develop-tax-strategy"
description: "Generates an executive-ready PowerPoint deck on develop tax strategy status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_develop_tax_strategy", "rar_sha256": "0785f2583c19bb211f3227466184e8f4180a8a1f14f67219dab133ea2dd3f60f", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "ppt_exec_develop_tax_strategy_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/ppt-exec-develop-tax-strategy:e4ea253c712bc0b5255b07a8f569bec0ef9eeef547d7b521337f8885fcf89133", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/ppt_exec_develop_tax_strategy`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `ppt_exec_develop_tax_strategy_agent.py` is
retained temporarily as a byte-exact rollback backup.

When Scout can execute local files, resolve this skill directory and run:

```bash
python3 scripts/run_agent.py --preflight
echo '{}' | python3 scripts/run_agent.py
```

Pass the real JSON arguments instead of `{}`. The runner verifies the
`SKILL.md` and agent checksums, prefers the rollback backup while it exists,
and otherwise executes the exact vaulted agent bytes directly from the Grail
record. If preflight reports a host dependency that Scout cannot satisfy, use
the `brainstem_chat` MCP tool to run the canonical agent in the user's
Brainstem. Never paraphrase the factory or agent into a new implementation.

Develop tax strategy Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop tax strategy status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-tax-strategy
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_develop_tax_strategy_agent.py` and embedded as the fenced Python below (sha256 0785f2583c19bb21…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_develop_tax_strategy_agent.py` first:

```bash
python3 ppt_exec_develop_tax_strategy_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_develop_tax_strategy_agent.py   # or on stdin
python3 ppt_exec_develop_tax_strategy_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Develop tax strategy Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on develop tax strategy status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-develop-tax-strategy
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_develop_tax_strategy',
    "version": '2.0.0',
    "display_name": 'Develop tax strategy Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on develop tax strategy status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-develop-tax-strategy',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-develop-tax-strategy',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e1c9567716130a91',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/define-accounting-policies/develop-tax-strategy'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/ppt-exec-develop-tax-strategy', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.667, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class PptExecDevelopTaxStrategy(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecDevelopTaxStrategy'
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
    print(PptExecDevelopTaxStrategy().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8VaaZOjSJL9K2zuh+peZSW3gBwbs0UIAUIn6AC62rK4Qdy3oLf/+waSMqtqu3t2xmzNVmWVKSDCw/25+3OPIH97Mps6yMqn1yfVNVNIMOM4DNwSMlMH4rIuKyPwK4ss8B+ys7QuQ6ups7J6en5y3Mouw7wOsxRMF9zULc3arcBUyL26dlOHrfu5dE2nh3ZZ55a7LExryHHtCMpS8Lt14yyHavMKVfU40+/BF7NuqmewUpLHbu1CXVgHkB2YZV3dVKrNOApT/3N+k5VmYL0XoIp7NccJ1dPrL78+P4Xg+9Prb092bFbg1tMur3mg0Py+4sG8qo/1wMzYTH0wJO8BCim4zt3Sy8oE3HJcD3pc/VS5sfcM/cd/RJ1Z+tXPr19S6PH58jT+U5oUqgMXqjOzql0Hss3ctMI4rPsXiI07s6+g0q2bMgVWjNYCE17uM79JAlj8fXz2032RF9+tf/rylOUjqgDiL08/Q1kJ1iub8fvLKCX/6eeXeIT2p5+/yaka6+La9SgMaP3y9rh+iAUDvw0NvduqfwdS78603C9P3xk3fu56j3aCmU8vFwD8T3fBeZm1bmqmtvvTz38l1g6Au+Owqv8pub/cBQcgZoBND8V/fr6B/Cs0eRj0IfOvl82BW/8VS8Dw9+WeoQdQfyX7hv//EB2HKQj8d8T/VNyfTZj8HfrlL237RxOeIe/L09yNQYaVphW7r9Bvb+qO53755Hy7+enX34Ho/1WMmjWlfZPwlphp6LlV/fb2y6fqdvvTr798anIQa66ZvDVl/Gcy/wzX2zo/IPgY9dOPc8H6xzRKsy6FPiId+i3L/638/QU6mXHofLtfvULf58v4mUCjEe+L3iH4LmcqoOt3OP789DsghxRY09i3xyDL//3foXVol1mVeTWk2llTQ8DBdZi4o/KHIKygwyOpv6qytFq9JM5XCNwd0x1QhNnENSSUZhhDIB9Gj48WZB709T/tG31+th/0Ced5/TYS49uD+t4A9b29U9/XF+gQgDWzMvTD1Iwhhd3tINN3Ac2B1W5xUTXJ53ZcECgT3glH4aSRbKomdv8Gff2HK7zdhL3k/aj+lxT4wwROApTqJnlWmmUY95A58pPV1+5nwKiAQ8osji0TEPb4o8lfRkzOgZs+kLI/qN6F4swGWnshYOFn4Owqi1vAhyN+VRTGMeSEJQAnK/sbjwOMX0dhX79+tcwq+JLeCRiH7iWlgsGAD4Whz5/z0vXi0A/qL6lrBxn06bffP0H/Bf2jWTfh4xo7UAVuYIEgjqGlut1AICObBAyroDEcAN3cPPbb73cvjNqBYgaBPAq90L1NBtK+uX+04O6ad78Am0cV3fKx0o+4QV0AcIHCGqAFcrt6/pKOIjIwtOzCyn0H8T75Dv27o+/rjD6pHhgCP3llltzG3iJvdKadlc4LJHnQB1LAXODXsW5CQVaNhTd3U8dN7R7MNOtvLgRVFKpAvlRe/ww1FTB1lPzVAqJHcBJASmb9FVpzO1Dfshj8GAG6LQ9mZ2k4Ov4RqffbQEj5CcTY7F3EC7QBEVlCuVmaeVCalXsb55n3iAB17X0+EG5CqdtBYxF3Rx/dMvkWefM/axn491bj+yZjPjYZXxoMQQno/68xGXVmBUHhBfbAzyF+c1D0e4CNndRo7735Am0CBNqMe7Z8ax3eWeadf7+kcQicUvZ/u4/0bjF1H3PntKYEAaOwyk3+mN3lTW5Yg8gYXV2WYzSbX9J3on8GYAO/VCNngQSORjrIPhYcn75rGoAsHa+/FX3oHnSj9SCcobyx4tCGPNd1bpFfByPC704AYeKOOQYSwQ5+sAoC0kEIAPkj+CGAExSDG3QbkB8A0nuwfwwPx1YKaOE0NtAWJJD7Ap3HeAYxWUEWcF03jgEofLqJghIXYAxU/EC4Csz8rszY3T4UNEdfZAnw9vceeDz0HyHkfEs8INV0zBpg2QEngLy63j37oefDV0DZZEyC26Qf3f2wFfq+Iv1tTD6g4zfiBw35WMy/Awcwdpncow6U2agC6Z24jwACkXCr2y/30nuv7R+6vP6hpf/pX+v6b8X0+KPnXqGgrvPqFYbvBe+93r2AXIFBjIS5W4217/OYe58f2fUZZNfn9+z6Qegdo1foX1PsBxGPiH6F0BfkBRkfrULbHUP28QE4cJ9n+mdifPolVdxvDn5EwchpgGet/qO0vA8B9cUvXX8cfC811VihOlAUbwx3KxUfQfBIEcATqT/WxSr7LnVHm0aX3j32wcTgUTpyvDP2cb47bm/iUf3KfXpNmzh+fkrNxP1ftjUj0YIQBUCMGyGQLqAlqkP3dvXRHo0XP27ibokEGMDJXsd8AkUNtLLP0EdX+gy97xNuu660ARulX8aOeFwSDAW/PsZ+7BAt9wlsyuo+H5W+b37GRuzRIP9RiTGNgMa2O5bt7CMvxxX/IAR88X23/KOQ7e2LGT/IAfD3yNSgAj9SugJ6OqBreoYAfCDVQPYAUmzAhD8uA9Yp3aIBxdcZzf2G3zezsrstv99gqO87yN+e3kli/H7vBO4hM244/6lWbcTzvcS+jVLNce6tobrBe2s/34Bp4VhKv3vkj33B2z38nl4BvbjPTyOIZQh66uG2UX66qwJs+Na4AgmAKD5XY2sAg+wBkkDBzkf9QXVzvltgvB06t/Hjl9c/63b/OuNfXcI1MRK3KRSzbMQiMZK0EMqkPXLKWK6NuB7juq5HEpRDgacojlMeTdOkZ3s0A66ABqMHE/OhAYyO2APdPwD+19rvp/tkUBowcgpmIxRYCyNp3EYZy8JQ1MMxjCKmU5QmXNojUBoxaRP1UMKbUhjKOKYFtAI2OQ7uTRFvlPfoAe8avb332+/euGf9GyDJJBz1xUzTpgEehMNQ5tR2ccTCbRfFUIfCXYRkcGA/QM15+pj68MjosLvRY6CC9g80X+24zm8PD4/BNyXASJGoJPb+4WDmZFpn2FKC1aSMJ9crXPkNec6WKywqRGmCimdbk9hk7g72Qj+W9MKK1LowicvKzs+Yo5ssnJWTrp2oLqa4apao6dRddOZ2fl6nDubEUy85RUVYrGYczsd2fOw7bKJvgiOul3GQD3ZY6hjNN73TBNZp2x9XHTqVmOWKmbTrlloes9lsUVz9KmGbhOAvg+XMnajm+dNkhaecgBGFd5byc+6QlSQ5Ib4Ji2OpBWkIRk9b8rCw46upZRrnegvf3g0F6qR5MdnheQ/rU6fFjQHmqR0q+3wczOSAsE5mESXWfFHkoREeURVPl+QgpwZ8Wfkrv5H0gz9F+Ia8nttNRTvEcZVIOcdmPLnR9GSdKph39gx7n6SrU17o7cHwtcVZteYznUakJpjrl2udnIqVyg9lLK8o0Sq2OnH20b4sAxdxmDg3Sb7T62PFF1FR5RLdCS4Kb+w86QJlbqVreWlEmlDT+/rEyfqZErMYYc7nnd/bRYdfl8VmlSwWzmKYG+dOY8LwZJ2E0uGj3UFt5nTJEwGJ5EcpsbySCoLTCc02mTcvs0iY+nQtUfq5EhDMZPvyRF2RqLjI1/0xnUwroEaDbguk8mwlOvihKjRX4uojnrbeFYpqNClnWxPrOkjbvZmnToNpZoteOSq1at9pUVoXtItKyT2jTV16iGwMLXjhJNSafomr8nK0ZO3cVfZqJ8OFHJw7IdmlTLK+9EvVkeW2CE+yZsODOK+IBd+wp0vOdelE05e9IJ5waVuhhyk/H+DKxUr5VBnHSZkby5V5MVNv0a/LZeZL533GyMdqyMPOmgydKRGwIOmT6W6JknkzHK7bvKc3PGXo8EWB+UspduUREZWpB89moXexcEKHu/PKH3ZKUx8pLZeZDdZvGZ4oz0rGcOp+qfVEWamH8Crm4nVyFPb6NRb5IhEHtWGmEbviwjMbcMFJdeaqgve5uD6Ki44V8otwTBadw+pRkRudziqV0CvLfo1E+tGrnGgmK/PckcwwlPWq0HLjItMEL0T2pUaprrbnBS20aSyKHZdGoXSkIzxYL3dLnj90A2MlzFxvOb6cha6BytrWoSPfa1L2DM+Vw2U1CXYTD2XtmbicKdSSPtfhAtb1dqMZ3pzluc3xYC4XZbxxI1xciUG7sVjNRA7S4izj8H4tMm5cGRN6NwkHjiz5glW7PCyoeZIo014+IPMd3eoHNU0TzFcZYOO6TS/oRlkctwY6TeJtHxY+moM8PfS7PiB9pQ4NkTP9KYD0eDyfwvYqOeYpktKs9EP8bG5oJJsVXK2iLDoVU3TDHkLD7tFDfD0rSxgZXMY9BvmF6Rl3s1xuJG63bg1W6rM+K7mV4yD40OxWrhEchuuwsfzZHkSqlRSH08Rez4iL7CxX1VbvnWFIa7sbhOGwH6r9xMEGc6+FmtoTfFIfBBp2TqujVSfFZrfkkI0LRwguH1e9I6zSOXZ0jOOB2O8IzEGO1HKXtQtKbX1n5rjw9nKFiaSbUasJvTUuQ6NLetz7CVdbG5nd0MwUiaQuRjyDC1Gby0hLCTNZT0RdjBPjTJg8fVj0+5QifVfYY52c98WAeKuE8VqdieRArBtzdzIWbR6FQwYiz+d3lnw59xIKZ73Kswls2Nu1KiK5KnASFndoH1iljQqlZurKmVXRZUcAbzpa1p5UMjMs4Wx0pMJyGhctLAMwzpKxMq6iN1tQyP0oYuordfDlPlamw7I3DHEJOGxQ3Wg6OVho76YWzexEuziqUZs1bcxoUiRmEX8yS3yuHxk+cuTDfgbDubSwnCsuWtWaU/SASEUKZTaJpg3khGnDlQL35XUg97BsZt0ppGja0iOWLTp9emzzebK0J6gk9MeQOK2nzLUK6o0jrRFSTjKpYRX1aC0oZnswJhvxQBvbVFkJzfwQ4dIemVp8E6XUIWK1QQR+uPomM3f8FZkvVvKU408gVlJ9uhPE+pSKB6kQtSZf5hG7z7LrAd2cFrR5WkX7uS66/aZ30jJj/TiXWdheb1V2sAxrnVvOFFHMYEnksrVQ8VrdrZUdy67mQHuVTNN8Dddr6XxAxTyTO9vqgmAoMMMasPQwPSKFnbg7faOusF7APYtF11zvdWxnFDl3RfWc9xhfdPodxrL18phS0o42LrNwOlnKJmaFZtMpASZPTk4h7o6MvG7XyYVF8dLbCWtickmQcNLH5Wpv5ITPoOSJLvgzKtmsfjy2IWaj5VzQMp6tuJmKJWVjBSRZsLMNttl2O1SNpdBfCsLxFEcxs1hXtV2R+FkpLx0sLEA5XB57hXRIq8nX8kVfXmyMT9Ude5gfeoQMPbFgNLmwL9uddJrhwbYuyQPC1NsI380KexPaKBnQ4Rx2STQXoihor4SIgHrjbM8rW1i32BAy0VEtFpk1m+lYdYiUwnQJwe8E/dCgLjctJqwLI+Kxb+TTwdjAhyxZEuvZVi6BAZtlpdi6ZNDh6SAfikrmCSsmZ4Ni5T7WSIdKR6KQI5JmgnArj+XFzATBEHSwJaS5SIq8IvHnVKPq1UVfEHLoCJ09XwxXgdUHn06tiOIxdSjU6apqbDLVemTnwDucaq84sVoGseBZc2s9gaedMp9VB629XLILpfXz8sR4RdINbU7qq97Y5lVpOYmXGEZA8uouA0UGY7rtmp1Fob+I2/UK1IeZxdHWfKIvY7na49LCn6g07qbL4eDMRZC/IeGflpeFfEJra+J2dLDPVQ6DZT52kn1E4DXmHOWdpySMg6zKhCPFAy+QdlEn00mwcmZsL9AL/CoTMXbhfIcUzEpZdAeGXMSNyEWcuNqT03K7knaXtVDuD/tUlYwdFlHB7FCWdl4LjjEzGhaOh72b7lKBB7QbE4N1AjvthUoOqrAqInxtk/uW56wh7a8hh6p+ygbFnk+5AZPTAaeiqHB6Ic6WO02yKo9vVtxGXQaFbfhOqIUXEHKwwtoTKdVENA/cI6avBt1EDKxoFO0Ub88JuRIvjbWWQHpoF9iYH0FZjLndVlxpBkooHHAmWtrXy/ZwUbBt3q1OV4O4Om6TbYMpnG+kuRmntGNcc6bJeU7DljJ9ijQ0VZDenSBVIM39jY9dEIsbwqNUcvxxM9tPfF8xBnt9Ou4X/KzMBaUJMX+xvzT4VqmI5Ymb5gyaX7b7eE2VpzV+OTtbBRlmghg2RNhLlhYf1ONsHRyQ/QHhhNAhs1kGmgVEOy/6QNocTW8bmwqprDasLIkbqdjYRmxZi2tCdZOLm1ccI+u4YVOsImRGKXUSJ3ZYV1rb6ynqrz4eCMa8QaXWJAcrvcKTzPC4yOyoenvtjyeKtBcOmh0rRubn+bVYsrLo57iE5oh8MWElmcuGjZnVcbfWBzoPdunVyzRnLqxwq9+EhxJdImgWSvyalj2ZnFrJErdM8pRkU6YlfONSysaKiwFRaOqZ2oOtV4/pRa859T6Z0qnK+EuUmx6ZXmn8gwYaJ7LdyJqeAQ6aocJsv54DX9Ept13Gse6t9PC47vcXbXNazU95Q9abi1jO0pmxZwah5y4TeS866ylaWTqfg6LA4cKSaUVxIDZ81uXZxXYIkVFmxZRMnCZT93R2XVXT5kwhNetcKJh2baYdUsRzN7PzMabdrPdlQAAL8XJGh/h03WdE53oe6Hr7toX1M4FQV0qxXMLC1Pnew1F3ZZXHzKEqxCyLXU06xOK8cxoqWVK2Y3mNpoFeqdXPbttWnZ9FkjKd0nJ4Nh1VdVzQwWeo0KBqtxYl3t01YG9rybPptDMjMimvta/ISiRHueJOQdEv6bYTM37fdha7OS922hTpWOYkGtqEw491xU0kejrfr+BVYWsT8TiF66tVbd2guRA4Y53ixKL3Jge74+aPRDsjmnvyvMP9slvglbX3SsKe4YQFT+jLZoIsrBhkLJPiIBURYupOYQpvy14ItipV7NHa7LVu7q/3e1fJ6fPabxJQCDcyyevFpEsP+6BEJy1fgqYMpNjc9M9r14c7dsXCy/a0QITlGu6J3bw8oz2hGVsH7da+jJVdgWxdf4LbQha7rCluS4wmQXFZbaeqLkwXwSLmPUS7ttaRofnjLhMcPHPbHRxY6ICivG5sFlMmctiaaZpJJZNbZkmVayQOcyTjbR3dOQZ+xX2dD8QKSz2NVzBnvTfFCWpeqqmmqPikhsmrWal0vm1zFvWFcu27cds122awhnqBD/xBr10M3dlmOK/mZp8YCYG1LekkzVFBHVsS080kzIg+xBlNSD2JvEgAZp5yKKHCdXJyDfnDAuMIrIomIZNh9lVg+gE+Yfq8WvhzAo+XEyYEu2kn3tqlQk09Fnf8dov487TLsBmhIWvdda6qsGx1Jy53/Phqi21c1y/PEh4LGnGKHPjkw257iFRlECl/d/KtBBnOKE6XWuwDPki2kQrquVnh1WG1pZbrbSOG+RlOUC5o2hPFHxkYwJM6W8bHiYSqLO3SdBWmU25e4ztTPSxEwUYT3JxVeDGvmDkKdgBzkwp3dEjghlX62zpB+4Y6tZgAWmOR35ZpxsMJ4ZmEzejw0ZlsKrDtoQRFO6htMsGZ6+FwTXZ1uuf4EC+teV3Mmk26TwwBV87kBmEozTq1ShfPU6cqOcQ+nbO5u3JpiWYXM0SJmVm28falbUrsuhQnnB2HxFboXTEgALVUSVOg8CHsWm9PZYp1ZTdcgyPzmX3C6wSDG4PGMKpsgytlLxgK7FlJutm61BluVAU+YFeLRCvD0TGUqSvNTjZy30zP1q6Nl1cG9XbUKRwoz8tauFcVZ0iZK24bracu+kxP+13LLdb7uRYWtRC03W7QZNgQUJUMN1vMbOjlUJIwvBYQU4g6GXCStoPrKu9noeJXuOhVzVqHB5OiFDwcQLxSWJcxQkPPuNiqmb3sik6LsLOsx5Z6MLhZuzf3KLe+aoV19ps9hddGSDvO9ZBUVppt1D7I4OZKi2khiEY3Edm2meqJJw0eXBGzSmDLQKC1xJcHeJgVJ216wVdmPrWOg4snqu+5J+o8V1tjAC4usWm7ZC/UVtLKPZ5weOdMaZRVp8NsSAhqyDcT5hIh6ZHAiDOJ2etzvQOlqZX4GY52K45Y7XM70eukllvmmJnidEkzMQo6KuRKJc66mVHdwiSSyxnza27OKY6vcB1CuSzBMeoxMECPjiYt4lztHbwZBN4+lhFJVH6MuqK/QzkUZuO5vGfZp+en2/vap1cUIaf489N43P84tP+nz339IczfHmJwCps+P/3fHU7eDwrfX+TdjvBd03m9rf76T2r46/NTaYdAm/sxcRU3/uMw8n8cvH7+hyfB49T+/pZ5fNN4rd9fctSmfzulDlOnAYP7tyqLm9sZNUC3qca/L6neHq8Jnm7mJPn4zuFd/fEE9nb8/VZnb/dX4U/jX3+ML89cJwSLPy79x2H+85PTAyeFdvWGT8k3t8xHGx/vksYD2vFl0tPv/w2A2V2aMicAAA== -->
