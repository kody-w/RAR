---
name: "rar-cowork-cookbook-dashboard-generate-ideas"
description: "Produces a self-contained interactive HTML dashboard for generate ideas - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_generate_ideas", "rar_sha256": "b22c1eb2de066f554b54a475d65f4603c1838384088cfec0a3a806bc9cbaac2e", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "dashboard_generate_ideas_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@cowork-cookbook/dashboard-generate-ideas:1edc002b3bd36cbe520e76ace5856db0db28869cebdf89facba08c04c644d420", "kind": "skill"}, "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "concept_to_market", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@cowork-cookbook/dashboard_generate_ideas`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `dashboard_generate_ideas_agent.py` is
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

Generate ideas Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for generate ideas - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-generate-ideas
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_generate_ideas_agent.py` and embedded as the fenced Python below (sha256 b22c1eb2de066f55…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_generate_ideas_agent.py` first:

```bash
python3 dashboard_generate_ideas_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_generate_ideas_agent.py   # or on stdin
python3 dashboard_generate_ideas_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Generate ideas Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for generate ideas - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-generate-ideas
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_generate_ideas',
    "version": '2.0.0',
    "display_name": 'Generate ideas Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for generate ideas - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'concept_to_market', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-generate-ideas',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-generate-ideas',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'e21d3c1aaaa3f321',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/research-and-develop-offerings/generate-ideas'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/dashboard-generate-ideas', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardGenerateIdeas(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardGenerateIdeas'
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
    print(DashboardGenerateIdeas().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/81aZ3Oj2Jr+K6z3Q8+s3CYn37pVKySEQCJIKICmp9xkEDkjzc5/34Mku7vv3Lmhaj+sXG0LOG963ngO/duT1TZhXj29PumelUGClSRR6FWQlbnQLO/zKgZ/8tgG/yAnz5oqstsmr+qn5yfXq50qKpoozwC5VuVu63g1ZEG1l/ifx8VWlHkuFGWNV1lOE3UetNzJa8i16tDOrcqF/LyCAi8DjxsPilzPqqHPUF54WQ2ogA4XyK7yvvaqZyjLoTlOkZDlACE1lHmeC3jbF6gJPaiLvN6rXoBS3mClReLVT6+//Pr8FIHvT6+/PTmJVYNbT/N3ycJDqDjKBGSJlQXgeXEBYGTguvAqoFsKbrmeDz2ufhoNe4b+67/i3qqC+ufXLxn0+Hx5Gn+2bXZTp8mtugHaOVZh2VESNZcXaJr01qWGKq9pq+yGEsAyC17ulN845QX01/HZT3chL4HX/PTlCWAC1AVIf3n6GQKgfXmq2vH7y8il+OnnlyQHAPz08zc+dWufPacZmQGtX94e1w+2YOG3pZF/k/pXwPXuU9v78vSdcePnrvdoJ6B8ejnnUfbTnXFR5Z2XWZnj/fTzn7F1Qs+Jk6hu/iW+v9wZh57lApseiv/8fAP5V2jyMOiD55+LLYBb/x1LwPJ3cc/QA6g/433D/29YJyDe6w/E/y67v0cw+Sv0y5/a9o8IniH/y9PcS0BmVZadeK/Qb2+6xs9++eR+u/np198B63/KRs/byrlxeEutLPK9unl7++VTfbv96ddfPrUFiDXPSt/aKvl7PP8erjc5PyD4WPXTj7RA/j6Ls7zPoI9Ih37Li/+ofn+BDlYSud/u16/Q9/kyfibQaMS70DsE3+VMDXT9Dsefn34HlSED1rTO7THI8v/8T0iOnCqvc7+BdCdvGwg4uIlSb1R+F0Y1tHsk9Vd9Ja7XL6n7FQJ3x3QHJcJqkwYSKitKIJAPo8dHC3If+vrfzq2Kgnp4r6LwR/V7e698b7fK9/UF2oVAXF5FQZRZCbSdahpkgUXNKOgWEnWbfu5GWbeyehO+nYljnanbxPsL9PXPmL/d+LwUl1HpLxnwwr02N15a5JVVRckFssaqZF8a7zMooqByVHmS2JYTQ+OvtngZkTiGXvbAxwHtwhs8pwWlO8kdoLAfgcL7DFxc5wmo9c2IWh1HSQK5UQUgyavLra8AZF9HZl+/frWBvl+ye9nFoXs/qWGw4ENh6PPnovL8JArC5kvmOWEOffrt90/Q/0D/iOrGfJShgcJ/wwmEbgJJuqpAIA/bFCwbewzwqOXe/PTb73cHjNoB5CCQPZEfeTdiwO2b00cL7l55dwmweVTRqx6SfsQN6kOACxQ1AC2Q0fXzl2xkkYOlVR/V3juId+I79O8+vssZfVI/MAR+8qs8va29xdvoTCev3BdI9KEPpIC5wK/N6NEwrxsQoqCpul7mjP3Sar65MMsbqAZZUvuXZ6itgakj5682YD2Ck4JSZDVfIXmmga6WJ+DXCNBNPKDOs2h0/CNI77cBk+oTiDHuncULpHgATaiwKqsIK6v2but86x4RoJu90wPmFujsPTT2bW/00S1/b5En/DgmiH87VHy0duhLiyEoAf1/GEhGxaeCsOWF6Y6fQ7yy25r3KBu1GY2+j19gQriJvqXMt6nhvcC8l94vWRIBz1SXv9xX+rfAuq+5l7O2Ajpsp1vo3drqxjdqQHiM/q6qMaStL9l7jX8G8ADn1GO5AlkcjzUh/xA4Pn3XNAQgjdff+j10j7wxI0BMQ0VrJ5ED+QCIW/g3YTUm18MdIFa8MdFANjjhD1ZBgDuIA8AfAkpEIGhBH7hBp4AkATPSPeI/lkfjFFXcvetCIIu8F+g4BjUIzBqyPTAKjWsACp9urKDUAxgDFT8QrkOruCszzrcPBa3RF3k6Ov47DzwevseE+y37AFfLtRqAZQ+cAJJruHv2Q8+Hr4Cy6ZgJN6If3f2wFfq+Gf1lzECg47fCD0bysY9/Bw4o21Va3yoR6LBxDXI89R4BBCLh1rJf7l333tY/dHn9w1D/078399/66P5Hz71CYdMU9SsM33vde6t7cfIUBjESFV79re19fsfy8y2/fuB3h+cV+vd0+oHFI5hfIfQFeUHGR+vI8cZofXwABLPPnPmZGJ9+ybbeN98+AmCsaaDOglR+by0fzdQKgsoLxsX3VlOPHaoHTfFW4W6t4sP/j+wABTQLxr5Y599l7WjT6M27sz4qMXiUjTXeHae3wBt3NMmofu09vWZtkjw/ZVbq/aOdzFhlQWgCFMaND0gTMAU1kXe7+piIxosft2+3BAKZ7+avYx6Bjgam12foYxB9ht63BrddVtaCvdEv4xA8igRLwZ+PtR97Q9t7Apuw5lKMGt/3O+Ps9ZiJ/6jEmD5A41s9HXvBIx9HiX9gAr4EgVf9kYl6+2Ilj6JQN9bYB0H7faRyDfR0wbT0DAGfgRQDWQOKYQsI/igGyKm8sgWd1x3N/YbfN7Pyuy2/32Bo7pvG357ei8P4/T4G3ONl3FD+sxFthPK9tb6NDK2R7DZI3ZC9DZtvwKpobKHfPQrGeeDtHnZPr6CieM9PI35VBCbo621P/HTXAqj/bUwFHEBt+FyPIwEMsgZwAo26GFWPQV37TsB4O3Jv68cvr38+2/5Nkr+inusgCGbjtotTju2RGOLRlOV4JENSro24NsYwFOt4tuszLLDLthDGQQiHIgiXwEadRr+l1kM4jI6IA7U/YP2X5+ynOx3oARhJAUIbwxzUszHXQyjKJ0nCJgmLoEmXIn2CQnAHZXDwQyAM4/ieg1i4xSCU7bBAR8vBvJHfY+K7K/P2Pl2/++Ce42+gGqbRqCoG6BiHRgmXpS3K8XDExh0PxVCXxj2EZHGfYTwC0H+QPvwwuulu7xiZYNgDg0g3yvnt4dcx2igCrFwStTi9f2Ywe7AojLa3oT2pKM88GbBoR3sqwQhjr1jrNqd2QnrWezlp93YwUy/bJdJs9iEZh/QxUKY4Jmqp4J/WzHVBrqLTym/MXGiInXk5TWw5NTTymnlCVEo5u1jtN51iyVK8tpuQPHqaVkm2EWQ4Szd7nJ7HeIluh8xWfB+mFp3Ll/ZVCgXBFRZiUxR1aV3QdbybEgbZ4rPQlUC1wJVkBX6mViXMGHytGOUQBKxpHaIryU6Ygy/I2BAdZwk/b7IibPZVb1FJy/HUMkdVo6IYddmQTEvX6q6hYY+OJmTE9td5IQJ5jHXyVjpenV0ASJzN5YQeDpyNzJeTbbUyL832xGh6EZdV5mlLebegxY25yVNlkbnWLOwdY831iYAu9K5KJdzgVxdUWqoyWl32M2xZzvbDdW3r2zLVF5eS6tvEbtzzxmIXV26jbfHCPaKrZXqaWadFkU57ozXPmgDrm/RUT7dtrK3b2a6YB/hiVu7PM9ScO6AmYNi1loPjkRWVXJ7VtQkrl4PMJlXoq0d9bW8tl1SGfYSUJKs6lbk5yn7TDsc2Fa5BtjCPVL6LCbgJVmZac9jEOqMVlw56m0WuZBzOB5VN3MrJDI06b/RNxOF6MT/ysns1Om07twaPbFdzBtOrDHfUZHGdszLRYBMalZhtSV4oE9/19tHFibgc6u7A7DXxcFaJuufUzopXwrDFkwTjyyY0GcNbEKgaqr2QKh3tuMd4G9MH38oLpHALP9KWdn/ohE1Xm0cetq48sd1eWsksrqu1Ih53E4dtDJm2Soqp5HNOXNrr/EpNJLkymQ1vizpZnpUijXuC3ab7ZOLUzEWGd5QyCSWGkGmTgMMtPA3OOBPKe2FOLYcr7GrVgWU1Td5FFC+hy85hktQo5pNjfllbnbUU98XswLTN4ayT8oYa6t2B64S1eRxWh3CCGp17ilco0W636TTzkbhQ1Q1CIloudSDGD1dhllfrBTrvrlsdDtppZSlxpMen06o3cZPOY4WXkjrMSvEUXfWuLJMD2QfZOTq1nbqtAnc5JAzhI5PZ5hokkne5VuF64VMyurTIyWbqaFdDKktCquOZRiupUq94mfKM7gxP+3yJHq6b+GDB68l1Ninybn44+ediCc83UhAP4UFZ7nTG1BWEsQNDNuPpLNPDEx0SdFlSB83DzFQRd/3ucML3s5g2DsxarbWTGaHXCFGXnaRfA7C1tVt+m0r1ouApoWLcoUqOy8m+jZXMavGiMSjfkSWUlKxZ1mCFWlIrn493yjzydRWVxTivJgnBsNauXkZqxq8Puepvk0Gfby8xLmeqxPtpkaGzgTX34ekMU2WxjPlzsoWJMN4s17keqzRtViky8U47nYrBTImF0TVGEuuAoIhgEn6xWKZbY88jCXHcpTvrcpnGmHNBDNe77gbM9JKlX5CrVXA9EowPGpjsZQK+HOLorO0Pcam4E28hcTF/JakTiIacCLQcAzFPS6qZJ5nednXgepPoPIFR2dp5K9paCiJLRwIPclFnhyaOcpXynJMYLvCVTxrq/kBHujHfqzUhHM3gsl2gtgv2NoEQkxp28P2x5jlXd9ea2PYw8TuzbuBNgGGuUZaXVLxucJ2T9JRXdW5ekbwO9yc1XEnt4M+t065XdUdYRtPhKB+Rxm7bqzl43DKfCQ1YI/GmxczQg22eBVWQr1x/3OShUJ4OhMijihXS2szyVNCtzA1S7o7Hzcls/O3GNXSKdC7nZjEv+BOOUlJ3RWjNsBlWlIRIl0Mpw/1+KHX9TIbsvnRNmu9Mnh9waiVfNP+6mpZ065m0zwUzideWqaMxiOfAPWPsBpZpgmWUMPvG48oDTuX2PphGGLfUkyJnCNHYhtP4Uh9mpxjhVlLXEKnP7ffFvJ8ZG6s+eQHRRCcF35OKzivqRCpJro5LCz3O6wUaE5I1YHueyrNjmVnnVbzyON1H06rcG1cvRfyF2TFIwU3qitYOiwWPX/d8OUsOCnoUOcNpkgFRmHVNNfolFeJgjhJsGuTaefAS7RSq2WpXtOzCYg0CdMCcwVlRnCdcal4OtJhTswtO9Bdv77XDeivVc76N2TzssortTz1z7NY9GKKaPrNMdIdO506om1hiRvtOCQOWVbCpHElChnZdZJ7naXxeIPxpbaZSYKk2cXErP43m+ZKKLONCzBE0lX2LVhvdCqiSi2zRiMOGSlOBWq4ceImcWdEMAjsUS4ErAtRar6ZU0m3564Hpeg9RNvtN6HOosJTEPcVx8WaxtU+mz/FuTazwYne61M3cnrX7BMmPosR11MUyohBZXLM1j6fmNBPOEahZPs9S9YFf2I6wiZVuptsKkmpNh0arLFB84ZoIHcJPtrWPWZG5zRCFVQIhXBmVMQy2hyaqy1f6QTvk6YkfiFW7iw1A6p2RTTg74VYT7nGtMhomqBO0MHZKV0pLCd7G0pzctGvJMCVhsRF8YhPwzJXeCgw2TdS9i8wws2HabdSfJD5o4/iyWQy7ayCyRqWL3SFUSHdi8YUsM7MJdYLdfmtHZ7ppHVCZ+oNc9VPUwc9HPYDpTepukMPhsFkghDdp6SrGvUlqe3lsqVxIB6xhDR07TJ0jiteF4uVFWNewL63IU1dcT0vUbCUEaShMJZF6c/HWwlTwvQZFYbMPFpdiiq3mbpNjA++spVojg9Yp+/kqOJzJFW4zpFoa/ImndWnKH8OetpDkGtlTZn8tZsd6b7arc9AygaeBsSTUy9Bjd/vsHEYsv7FQlD6slUNNGMS07gVZwgeLSSzOVkJFaRyUD6s4o4Zp4bSrWHTqvjtIij3VfTEwjovTakfPqe183SIZ6MQkZaxsIVvrRztYkDKzKHbsNaxAo3H2th1dDtxh35ay4vBdC/ZwC2Lm04q/OIrr/RARsajXurnWzBKeqFJ3kAd+4yPB0oRrN17NdKRGN7W6upqhLS60+eq4pMjTihK5AbdyEJFMXnLH1ZC78jWxpG1bWfp5cTl2yylGWLiA1MlEF+rZBCn5IRedmYo4sLa6uEeE69nkONjWtDSmaHBsJ25jzBU10cSyKzzu1GWg7jl9sTUz/1JQUoGz+SQO/UkZ+H11rCPzQhxrPVkQph6GMwmJZ5JKk+cVh5WRcljpWLYqZFc4KoIzd/vznlqk8FWX2Is5tOx05YH4pdRWEDeXMkRzEz821p6Twx2ysRFOiNyFyeXOnLXmNcXBnFXWXaYjsbyfkcmWLDgdDOiHxjSqY4eTGLozF9R+UC8JPg1U1hEDWRFo8yqtXSwhQKdZp9lpXiCzGKcoM+DSHe7Xx46bKSY7yUyyXLFXb9pSiHicNDNuj7XSdLUMCnx12APo5m5gBJfEYAuTP8OCrKn2jrwm4iw/U2bkdht6reILYgfCpRfhC0nEe7emfWwoty4w0p7wU2OabenptKVDmb52m2W3hutVY21sheeN1CRETKV0ONpmnLQOzLxRs7RAJSefbhpQZgWuN2eV2PeHvF7PCXtxDNIZby/6Qj7HFJ0iWB1Y9VqI5+72Upf+WuVqSl7jaD7dX9dgz7GN/PViAJuG3Yrnz2JQaCxhScrSliX6sOELcjszbLSuMHTmOjTJ7Ih5lV+otDkv+EPY6J0R0/am3UpqzS0tai800QRD0QYk46plYCun8RI+esutv7Bpt2yWoVz2B9WNvWUyNKwOO+vKWZKMejjirhUQR7b2eCrCkRl19LAqmluOXuru2ssqXj1fPEJuOfu0t2sbzHhqKHvt6lji0pm1I34jk0IhyLs63OQd3LBTxtwIpm1FqzrJYC0KNMUF08S0vSytXVdqcjCo7IpKOHjLin61kWilqmwTU2CYNGyVoo89GN3YxPbczfJkahVngtkc12msyTXUUXckS01gWBx8fpXPVgQOMwg8YEyT0LihlSXbIlx7MmJid7SRWVsuWdU8M8Zyk1FqX2HUia+K9JKx0+ykCNPoAF/ziGcCRVYzbWoiPRMwxdwRkONS9tOrej47x8g07PZQD8xxisaWYWcbxFsHi33Ucc71vM+cpsITTRUjoiDjk5juDcQld+6RaSbr3t9oa2btz2F4e9057iAstlsrI3FH9NddXZWTTder5BU0Q6SdecPkvGTRzLc9Lrjwuyvmco6i4kS63k+wau/QOrzedkMHe6rK++pqXfSayaWimHUmZfhbwuUwO6O1nbh1MZS2zculhN3TUTkrtoHX3RX3FKo1Fws8JHOWHHD52jB06Gq1jPEbgygPNRtN7FrGLTLiInoAm7d4EoAxwRmWLHaFeTyfXRbBdeirHUsvaMkmYtKpJJKWNru8x0Nbnw7MKmlAe2vOZzxfDHzXRJcki7pWq6et5wXVUcTDGcysVqqPga5gVBdJJM8ssSw3s7ypPBzv1iZTC5EmL1ROJlYmfmoCZj9bTnbcvtJoNpxWB3sf8rB2XVMz/Sz0Pn1uarSa475hi2TLYExmK15UpScEzFZzpsIyJ1Aplz/1aWtv4dBY+JrrcCjYU24xi8WIHdqLzoZquUFjuh0uzANfEM5V3wyq3TvSwlVKVqMdfLHWjiaLNlNJX3N1rbaJRRjuvDpX7oGOrzvc3TZHdjnbq6x3qddb8mAFDaHQ/bmf7pdbzrikgct0brTluUSEhx1SHjkK2/SMtt0OUoKiu4xdrGc8FuH9BY+m1tLtDtqsN7yjbU+kjDbWk5Jll0lvGFV63YBxi6SbdUgWS1awF10iDCjq2wZ6HJqLsS9KutjVk8k64/EDw9YbWmvYSQTDCph/pR2+docUZUVD4kItNjx+ZQaCtjgI7tL14bbWPUopF9eF1bZmS18qoktPsFDkQhAnHNV2UUHC7YLfIJYqqCYLo+Q+GfqrL6TMcdIvXcN3dwa3FUqs3XPahm4m06l1Fgl9EI+U6NAOwc7UnXigBCZMyrXP0iujOccynOQ5Z25Smc59naTiHSZrYLbAI6yoetnI6HSjBP3BFHeDb00rBZYp0C3RRadjueAKVrebr/uuEt3dujCQCgPTOXtatlMimoSki/unqQHDm1AL5IzdBF3XIulF3OmkO8CKCzaUsM3zVYc5lTZZBDORTg77LEdis25R42BcNyJqs4Toa217ihV55frzc7+kZqclw5DeXhBjyqfmgYRNsECBEX2RpPrOs3zLBkMFjsuxM0SCdoSz5bqU1S3McJnrXs3tvphOp399en66vZV9ekUREqWfn8ZD/cfR/L9ywBtco+LtwQGnUfb56f/uPPJ+Nvj+ku52TO9Z7utN+us/V+7X56fKiYAi96PgOmmDx9Hj35ywfv6z096R6nJ/eTy+Oxya93cXjRXcDqGjzG3rprq81XnS3o6gAZxtPf5nkfrt8QLg6WZEWtzeJrwLGo/Gc2BU0bw1+VtqVbE3Pr+90E09NwIqPC6Dx0E9IL4Av0RO/YZT5JtXFaOBj5dE41ns+Jbo6ff/Bc+ELtIIJwAA -->
