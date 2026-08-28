---
name: "rar-cowork-cookbook-blueprint-period-close-readiness"
description: "Paste this period-close workflow blueprint into Cowork and it assesses whether the period is ready to close \u2014 unposted work, subledger-to-GL differences, and FX exposure."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/blueprint_period_close_readiness", "rar_sha256": "6c6066dccbfebbfcdb06bc6185bcdb2c78d7b1e7a2c49735259e06c4a69350f6", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt_blueprint", "blueprint", "record_to_report", "advanced", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/blueprint_period_close_readiness`. The original RAPP
agent is preserved byte-for-byte in `blueprint_period_close_readiness_agent.py` and in the RCI capsule.

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

Period Close Readiness Blueprint — Paste this period-close workflow blueprint into Cowork and it assesses whether the period is ready to close — unposted work, subledger-to-GL differences, and FX exposure.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-period-close-readiness
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
    "constraints": {
      "description": "Optional. Hard constraints \u2014 budget, platform, deadline, compliance.",
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
      "description": "What is being designed.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `blueprint_period_close_readiness_agent.py` and embedded as the fenced Python below (sha256 6c6066dccbfebbfc…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `blueprint_period_close_readiness_agent.py` first:

```bash
python3 blueprint_period_close_readiness_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 blueprint_period_close_readiness_agent.py   # or on stdin
python3 blueprint_period_close_readiness_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Period Close Readiness Blueprint — Paste this period-close workflow blueprint into Cowork and it assesses whether the period is ready to close — unposted work, subledger-to-GL differences, and FX exposure.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a design capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/blueprint-period-close-readiness
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/blueprint_period_close_readiness',
    "version": '2.0.1',
    "display_name": 'Period Close Readiness Blueprint',
    "description": 'Paste this period-close workflow blueprint into Cowork and it assesses whether the period is ready to close — unposted work, subledger-to-GL differences, and FX exposure.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt_blueprint', 'blueprint', 'record_to_report', 'advanced', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'blueprint-period-close-readiness',
        "upstream_url": 'https://coworkcookbook.com/recipes/blueprint-period-close-readiness',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '667474295c4ede3e',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/close-financial-periods', 'record-to-report/record-financial-transactions'], 'recipe_category': 'blueprint', 'recipe_type': 'prompt+blueprint', 'upstream_path': 'record-to-report/blueprint-period-close-readiness', 'uses_skills': {'custom': [], 'ootb': ['Excel', 'Email'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'design', 'checks': ['Constraints are written down and the design respects them.', 'At least two options were genuinely considered.', 'The trade-off accepted is stated explicitly.', 'The riskiest assumption has a cheap test attached.'], 'confidence': 0.529, 'deliverable': 'A design record: constraints, options considered, the choice, the trade-off accepted, and the first thing to de-risk.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'constraints': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'subject': 'What is being designed.'}, 'refined_by': 'rules', 'signals': ['tag:blueprint', 'word:blueprint', 'kind:blueprint'], 'steps': ['Write the constraints down first. A design produced before the constraints are known is a preference.', 'State the success condition in terms someone else could measure without you present.', 'Produce at least two genuinely different approaches; a single option is a decision already made, not a design.', 'Compare them against the constraints, and name what each one gives up. Every design gives something up.', 'Choose, and record why the rejected options were rejected — that record is what survives the next reorganisation.', 'Identify the riskiest assumption and the cheapest way to test it before committing.'], 'subject_label': 'thing being designed', 'verb': 'Design'}


class BlueprintPeriodCloseReadiness(BasicAgent):
    """Design agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'BlueprintPeriodCloseReadiness'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'constraints': {'description': 'Optional. Hard constraints — budget, platform, deadline, compliance.', 'type': 'string'}, 'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What is being designed.', 'type': 'string'}},
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
    print(BlueprintPeriodCloseReadiness().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/9V6Z5PiWJb2X2FzP1T1qipBHtXERCxGBoEMkhCgro5qee89/fZ/f6+AzKre7d6ZidgvSzqE7j3+PM+RlL+9mG0T5NXLlxfVNbMZayZJGLjVzMyc2Sbv8yoGf/LYAj8zO8+aKrTaJq/ql08vjlvbVVg0YZ6B7bJZN+6sCcJ6VrhVmDuf7SSv3dkkwkvyfmYlrVtUYdbMwE/+JnzSEzYzs67d6XvWB24z6Qe/nnJmQGLlms44A7seMr+2yALGZm1W5ECpc9fxaVa3VuI6vlt9bvLP7GHmhJ7nVm5mu/Wnux7mMnMHsKWt3FdgvzuYaZG49cuXn3/59BKC9y9ffnuxE2AL8Gf9Zq58t2IzKVaAGWEGDAW7EzPzwbJiBOHLwDEw1surFHzkuN7sefSxdhPv0+w//iPuzcqvf/ryNZs9X19fpi+lze6uNrl598Q2C9MKk7AZX2erpDfHyfemrbJ6Zs5qEP3Mf33s/C4pL2Z/n859fCh59d3m49eXHJhgTrn5+vLTLK+Avqqd3r9OUoqPP72CnLjVx5++ywHxi1y7mYQBq1+/PY+fYsHC70tD767170Dqowos9+vLD85Nr4fdk59g58trlIfZx4fgoso7NzNBYj7+9Fdi7cC14ySsm39K7s8PwQHID/DpafhPn+5B/mUGPR16l/nXaguQ1n/FE7D8Td2n2TNQfyX7Hv//IjqZyuk94n8q7s82QH+f/fyXvv1PGz7NvK8vWzcJO1AdoF2+zH77psr05ucPzvcPP/zyOxD9D8WoeVvZdwnfUjMLPbduvn37+UN9//jDLz9/aAtQa66Zfmur5M9k/llc73r+EMHnqo9/3Av0n7I4y/ts9l7ps9/y4t+q319nupmEzvfP6y+zH/tlekGzyYk3pY8Q/NAzNbD1hzj+9PI7AIgMeNPa99Ogy//932dCaFd5nXvNTLXztpmBBDdh6k7GaxMOgu+ptysXxLUOQWCf60D9TxmeLM692a//ad+h8LP9xNn5O1J+eyDgtzvqfave0OfX15kG5OZV6IeZmcyUlSx/zUzfnbAVwG/l1m7VATSxxsb9DHDo8/QGwO7s138k+ttdymsx/vpA5gc6KZvdhEx1m7ivk3fnwM2evtiANNzBtVugIMltYI0XJhPgAiPypHsyQh2HSQIAuQJu59V4lw2i9WUS9uuvv1pmHXzNHlCKzh6sUs/BgndzZp8/A7e8JPSD5mvm2kE++/Db7x9m/2/2P+26C590AHJ6ywWwkFclcQZ6q03BMpAmkFjg/z0Xv/3+DC4QkwEaApkLvdB9bAa1GbvOW6RVbvUZwYmZ5YIIg+imRV41AJ8Bnb3Odt7s3V6gdDo1IXgA+GrmuIWbOYCXAKMFJnDnPZJZ3sxqUIC1N36atbV71/qrVZl3E1PQ5Gbz60zYyIAv8mTiw+rJH2BznoUg/O918PgcCKk+1LP1m4jXmThV46wwK7MIKvOpwzMfeQE88bYdCDdnmdt/zSZmdKdQ3VvjER6wCETGfqb085RzMB6kAAec+k33fY05sZp2Z7fqa1Y/y96splTYgAaAUr8NnYkM/vYsqTrI28S5x+85CDyz4Dyzcq/BBy3P7rw8eyfm2Tttvw0J/8fmksm1FcsqNLvS6O2MFjXl+gj5NH1NqXkMbGBCmIG6ezj2fWp4w5w36P2aJSGon2r822PlPVHPNQ84A0odgCDKXT6oEuDjJPdexFNRVtVU/ubX7A3jgc2zO6CBPIKOBx0xBeBN4XT2zdIAtPV0/J3v70mvnMlrUKizAkQGFJHnuo5l2jGwagroWxhBRbtTU/ZBaAd/8GoGpIPCAfJnwIgQtBbggXvoxBy4CXrQq/L0+/J7poAVTmsDa0Ea3dfZGfTSVE81aOCpDMAaEIUPd1GzFCQ7Bya+R7gOzOJhzFQcTwNN0Mp16Gc/xv956nvt3y2ZjAcyTcdsQCT7CYsdd3jk9d3KZ6aAqenUrfdNf0z209PZj1T0t6/Z3cJ3+AcgkEws/kNoZqD50vpeaxOG1QCHUvdZPqAO7oT9+uDcB6m/2/Llv10EfPzXrhPuLHr6Y96+zIKmKeov8/mD+d6I7xUgyBxUSFi49XcS/Pxj235+Z6o/yH2E6cvsX7PtDyKeJf1lBr8uXhfTqUNoT036NgSAUGw+r6+fsens10xxv+cYqM9TgI5T6EfAuu9k9LYEMJJfuf60+EFO9cRpAFOyOxqDLHzN3uvg2SMA7DN/gog6/6F3H7hUP5P2ThrgVNYA3c40w/n3y5tkMr92X75kbZJ8esnM1P0nLmsmYgCVCoIxXQyBngHRb0L3fgRiB0wEtdncD/94/Sfd35jJ64wzJ+u/r33rCasFIAjgA0y5zXRx9Am0j+lMA9+niTuKJJwgYjK9GYvJ1sf1zjR7vQ9m/13vvY8BADn5l6md7+LB7/d5eNLyuEK5X/NlLbhE+3maxSdnwVLw533t+0Wt5b788idmPEfzvzAinKBkAp8HKrjOn7gChFRu2QLWdCYzvvv1XV3+0PH73bzmcU3528sbejyz8pwfwXLQpp/riTfnoHCBQnD8KDFw7l+eLJ/7AdqByQYIIGxiQRCObVuea1me7VgLwrIJeIlb4D1ik0uHtGCXNBEbo0gUR3DKXRA2ZhIUii88Ash7FOq3aTgIJ5vcheeiFIzYDkogOI5RMImYlGNipGk6i+WSXJCeAwjh+9YYgOXT0YdjUxTfh9wpIE9/f3uxCAys5LB6t3q8NnNKNxH0YCkBT+GwJ+x86EQH/Mht3GKxb5txV9XtphguBx6tx5QJjuN6p8VKuKMHnw1bNbngITcEXarIVD+2haTHh54aRs1kCDcrCChrV1fBZw/wKdBMXqIhUXd5dTwp2ZhUA7+HT5c2rJnDnFqWDbY/I4VyyM56qwgyhhhe2u4JRC+b9KDEktTRrsvquSbQJXPYmbBObSTEhM+tfmTYsRMUjIn8BY+uDrWr3cp2RKUtHayg64apm1NxrvUt3dw8zRDHgzISp1JfXysJYrZZh2vlwbueglPJ7VApixCy4wKE6qpwj3ID1l2SLcFg0VGMYvy0X9VleeGbTXJrB3F30faGiV+k8JS1NBqX5N46prhYiqdDXxjkGiP7Upf002Ljh3lrn3fhoV62qYXQ5LFIy2VzlDfzdbvxFwzvRpF9W5yaWF3muaXrQSMUrAmtSzK/JBS3R892SSQXR+7cM9PqGzM4bHo9HXdBdHKwbSnn582oq8F17HJDMGgfuSDXkbd7lWqsoS1deSU5oUL2zFpcJfOmSQUxPqzmyJjo/tloBLVGxd5LDky8ltwTwWFeCB9Oumowx4bJfFuE18vbjmTX3mIxmv5QwTcejZMVFrOBygtVqTsmLGmwtzcCKa4bY83vjBt7DNVbZvatYeQNRsg3S3UdZzWsFgKJ31SHIC9bsnVqZL2A0IiO61hHjIDKiKuKOechGAO9tmj7vM+kqoSvKYaOi+N+nhLlbm+PtCucPHbBpI4zeiwqUT1DDRRd8dr2tqUN0NKRL6l25AQ6firUrBYuEdS5UJHq4cU44xk/2oOF3aguWiHpINP+ktDlczpaVCXe0kQxUOlSWfJRk/thtHLbkyNpELzAn6/WekUqgnsOlxzlB51cxAOURuQKaxO1MVB2gdiBGi8T9FrRmhjii0tTammoqiV8DvT4aNdXsU6l5U7UeBhD1hHMRR6+2C+TJt1fhY2p5TmBHThXn6+HpEjU82ZI+CsuiWLYYIKwWm3DfR7leL4IbcB9yl7hru4OwTbpNdyzqqvBqU0jvq2JA8FH9r6EhC7TobQ5i6ax0CQwTZM7pLQF7yp065QfFsJ12cqEa/JNVheOvp73cr5uqTDJtHp+u/Wa0RzzVowzQh5Mh/JwtQoH5IIt1sxwCY21Y8SwEcceQ0drVzcckTke1Cuncix0iPgRiRQ2EBeoTtkpfU78o3g7zVe31OmP3MZbsGelDJwINsYjCdqJE7sqrhfLSHe1qFXsRkk2nXagI1wrSLbhPJ3f98IGFIUv+J3m6GAeho8miNehOIrJwdi6MWZRo7vH1hFTytJCln0Vqy4xdl5ImcEzXKRul9qhKFQaCx3PIHh6h873Gb7C1L26Ydz55chTZXSLFVoZXeRoLjGhcS/qzbQEm1+Mybg/YKxJJNqAigqhHYOSXuw7ddhmIK6FsnULAzsExyu/lAf4ZCZ8C1n5Dl9gx/lFtchB1kdP3e120okxGDXX0B2LoycE8ca9pYedSW2xq2xl5Dy1lhf8CI0ksRJ69HzZby52U2OIeN55543tumUsuyq/Dq9GNV4uURoUu3Jp+K6dhCK0EPJWXl62N/zoro5aG135dX9Db/icu+w43XGGqtO1mDiT7IlVlOt1G255zeJX4bw/bODdYl3jbOL3dK7a7G6zh7eLrQV3+2yoIqg49/1C8JGqso19cCVFfNuUAX9TAlvg7E18bJNU3QeNmjYu0WdZFHXi+crsGoSNz6uDNUKcPqKZUHLgmCe0atQ8+TZSbnco+iNwFxbXMIVTA68QicfWY01lkb3Z5KqUaqDhlshxD5FRKZFXYavYQZahKETIIrcl55jIETHdnfllzoVifxKx7iA145lbH1a8Ux7jIFJk45zrR/VY+leiYsQVQiBiERYHfc3UdHi2wrVWGBU7lnHQm7FzdPQoVrVBNHyy0TCJONmiE0hLZqmvAw2JWH19dGKdp5epsCQBeC63yd5pt/1Wjnn1oEueV12b7QCbc2KVHPzWOLsJod1IWdGNE4Npg3WYhwuuxMdbKl5WCgRvxKKO2gtulDuqVjAZNlcbqCCNPQWnxcFtIOG6jVRLcOyzcLUUJh2lkHQHNc+gVchaUiHrTgURnNbpyMrpNV9jaFzN47Q2ystmnkJYigXYOfWVZUyC1h4Gewjx9loSZXw6YzpvFhsyrglqC/kre+cwdpJ2qShrRyNR9uLOK6Slfrw0uWYsVvFwq8ZCB31K8/EqbHOz3fs9WtLR6Pt5xZe4WYaFddxjhVBcTslx1Ox4rWTmwQst37ioCVYlO8O4MOZyLjvIHtcatu3CslLWzXCqbIiHeH278/d8RrRLVM6dFFaleBcGKLvCl6qekVXmhLizXyV4wUS7VSIIkINWGi+KWzlrmi0A3mt36aIepdrDmUgasWANY9OE89g586qISujZX6wawSCRs08Z8LIYBcWNRWVfkMf8JhJCst/VVX9CkcNZW5/ThWmzNtcozDrQU168KYcmgNO1nhfXMIwUolB9og4Lp4/ZHOIFFsEo69wVW37DKLnoZvP59ZISfI/UhJ/j9CFr+B2ZHUDXn/pEKzUkrOQTXi3Hk+x5KIogydIXRD8muGxN1tuY3DnCmnY6u8AXQysz26Sdd1uLt6qcuqoUq5XWBkGNzgvMazbQESEEbrO1gYSVucu3xlXQMqvBSvwS9vJCCa/psL0cB25hthcGshd8Die+Z7ZBGKOwLqV2Pc9iWbMX0qppTSnOxSYUYsdYWU0zxAmjzAETihp2EU7tVTNsQ1jmPrEx9geHZdd4HTN+vPPUmhZ3hUJ6+sbAkm53onQhoDUbHvdnRRBMHbuGDN1vXIHbRw4bi/4RpvLzmmGi1HTNWuaWMrIb2LEwVvh2oRfGLuRyRtjNs0N1gjlJI/z5Rhso6HjRxUJTznSsHo82bg7H0DLGsRSXZnwyXT3D6wvHZsdzFckQqEy2FJqNgdAtKayN3UaC2Y2j7ckSue6rs3HC57zaOPDep0/LSt7u2mQlwmc7FKtebcq9tnfGsdZoeWhMVWnB6BsWOhNoaZdtVUzKaUyIY1g/Ews2WoGOHxa7vbXJICa+1hWq8kUbn3zOGNuRBPR6FI+rZrU6VDnG7IrVgSm4HbxPGTNCK9g+NqyVofi6gAtZoh1aNXGWnFN9wDAQ7zia3yOWGZjr29UQnM3RQilN0Qx4yDwBTqEKBuyQnvULzPnttY32pcH682ua1qIAw44Ip6DGnbigtvq1gvnSDi/iEMNRGwlgLrvSxFJDC0PcjyxxbnaJcqPqHar0+5O8NQd8Je3mm/2hauzsIK82Si51OXQqja4SMR906UG0FMRzV7inlvbc1yqYaC9HdoNvWB3Bh4Q2aFMzNlUS+BoRtPRGJdnKams37vImoeW1YiJS3o9iOi/5rKVI/BznypqdL+g9g6s+x6+kEoWt07WpbkGNBZzSBJc9I9XG/trwfe1BtzFoUrnY3srVBr0QgnY4Iok1iscgWrNXnRvpRbeSi82GcpBD2ke3Db1nSSGzDtRiDZF8bppVx1y2MVIkXbXRMXdoezQciW16aMP8cG0h2NfXGBNiWNQUY3GtRlnFuHLJJWoX70l261i6ppA17HBjZ0my0i6qyjLnPdw5xdZ1eA9N+j1lUjXZlYclwUloh15zScysSyDXxjbwxkVntLxRLEoOXshsB6Z5Mc2OIrYOFw0qaCINO82Az7fzg12dRSfVLdo6FaFvS0UapPtylzqcKBfQ2sMb9Xhy8WPN1b7GWjJsmFs/Oun5YYsFY75d2VdUQfq2Wubq3B8rkSEJkZRuVY0om/bIDQjXWWt04fgyCkmKRYpzaH66zPfrTq04DUrmc2YLObzsQksBvVHKNYqlRSzNzzGMFBzs5vnycLweo+2I30ZxzeIpFi+va4j3F9zWU1crmg5wSUIPwhFfeb57GlCzpvsLs5vXoxxlnUWJhyaTELxl1ol+VlpHUzCEFrp8qxB7ArokZB9xgjBsXOOs8kGyFD0hZJrWLpdsu0XmJdURODtfL8UhObEUGIXm3s5a4wgMg2lpiS9D/HAlkhWOpvuNNx4pZ7HeFkEt8Esw0OpxQbjh0mEh3A2WmX4p51DtFQtzN8RiMip0vQIz8nY05xuM4JpMXnCaoOSdSjn1+rrm4Hq/JIWh8dxxLlL5rSQQ/+yiRBhFpVwTkChBx4hbrzUfR0j0wIeHaKkB2NyGTFAOMeQnxdkeOBKOoGVDzFfSdnXTBI2CGKy4mrpNXfo+wiIr3rqXWJDlfQAAv85peIky9DUFpHFIXd4h0tsW7zm18UeXzpwAcWAolWFM4LYBQl9bnzoJg2meiUNr0q1cHH1J2At8NOIFWiQ+dtqwkLY+nWW8PTYn2KDCwJXLCtsNGY/iFBlaYKiH2oG52UNDSrbqMRx76jPU3dZZgteNLTIatykpyoA4G4wCcA8m/sZuOkuECETIj5hys7erDAoi8hL5FstuuxtV2biP3XaYBc+l5eJCVzJzlebKtmU3PWn6TsTXYqan+AHlq7QD0JJSIGycRCky4I9Tt+A7ZoUw7gpe96pDnfO1d65sc7cSKm7JulFNSOzocQOxRfg6hUp8riJ95p3JXLGGlbhpUQDFwgVtOt1bLiHTclD02HltSc2jcMEsW8kjz5irrufaPtAheMlsT/MBXH/1OqsRMeJwF5A6zl6DKZPL5oTnz6ERoeKAFiF0yTQd70KeysWrLOHSHZ/3jEig1GDbXtZdg1EoM5Q2xRx2Fu6FnePEAocS7SRt1RNXEtCe4yBMV+ihDTkFdS6aD0i3Hqx12elJTnY26kZaD6uD0DVLzuGKHO4hnzxTlh+t4DNUGtINWZiEVbpJjSbomSLP1467OKaG+AfxHFyJnGyH5S0rz/K1d7nIh0Yz7VaQl9vkerna6H3kHaIjg3frAN5XS61K8VJJF0Lv4HFOy4mLmsXKxkGWK8mMDrKGSgIY/jo7qX2LIrtj0qfO/NBfFoMZWTRfuC02j6GbgHbNuL2RVLSnh17sNeZGoWtx2BVWPIeSIy3DWzwrAcK0Ri8LhHHdor20GAR22SguzbIpwW4Yv4CWh16H4kIgwnHbiuRiL5EVNEhHsnJYQpIuZ97RboSIBh5Wp+f9cbV6+fQy3YN+3kn+px8lT3fy/tduKD7u/b09T7rfygUKv9x1ffnnTfrl00tlh8Cgx03TOmn95y3G/3LL9PM/eg4x7R4fT2enx15D83bDvTH96V+LXsLMaeumGr/VedLeb9p+egHU/jAIuGI/b7xXeVo0397VTat+eP94KPCtyb89niaDj0ynm2Iw3SkFa1z/eSf504szghSFdv0NJfBvblVM3j4fbwAnkdfFK/zy+/8HGWaWDPolAAA= -->
