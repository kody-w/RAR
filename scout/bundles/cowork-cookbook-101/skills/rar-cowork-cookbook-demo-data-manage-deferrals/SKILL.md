---
name: "rar-cowork-cookbook-demo-data-manage-deferrals"
description: "Generates and creates realistic demo records for manage deferrals in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_manage_deferrals", "rar_sha256": "24d564a8819a7274d42995a53504221781a1f65e1ceca2e744bda825dcea1be0", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "record_to_report", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_manage_deferrals`. The original RAPP
agent is preserved byte-for-byte in `demo_data_manage_deferrals_agent.py` and in the RCI capsule.

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

Manage deferrals Demo Data Generator — Generates and creates realistic demo records for manage deferrals in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-deferrals
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_manage_deferrals_agent.py` and embedded as the fenced Python below (sha256 24d564a8819a7274…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_manage_deferrals_agent.py` first:

```bash
python3 demo_data_manage_deferrals_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_manage_deferrals_agent.py   # or on stdin
python3 demo_data_manage_deferrals_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Manage deferrals Demo Data Generator — Generates and creates realistic demo records for manage deferrals in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-manage-deferrals
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_manage_deferrals',
    "version": '2.0.0',
    "display_name": 'Manage deferrals Demo Data Generator',
    "description": 'Generates and creates realistic demo records for manage deferrals in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'record_to_report', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-manage-deferrals',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-manage-deferrals',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '50cb6ea4a6e5c0d7',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['record-to-report'], 'process_tags': ['record-to-report/record-financial-transactions/manage-deferrals'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'record-to-report/demo-data-manage-deferrals', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:integration', 'tag:workflow'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class DemoDataManageDeferrals(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataManageDeferrals'
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
    print(DemoDataManageDeferrals().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjSLblX9HE+5BZT5khNrFkW5sNaAEhEAIkFlWWZbIvYt9Rvfrv40iKyKqurp5uszEbpWWEAPfr9567nOtO/PpitU2YVy9fXlTPymaslSRR6FUzK3Nnq7zPqyv4lV9t8H/m5FlTRXbb5FX98unF9WqnioomyjMwnfUyr7Iar75PdSrv/h38SqK6iZyZ66U5uHTyyq1nfl7NUiuzAg/c972qspJ6FmUza1aD2XY+zBovs7LmPrCprCiLsuAuuIiSvJnVDnhcRXn9CvTwBistEq9++fLzL59eIvD95cuvL05i1eDWyxqsu7YaS7wvt35bDcxLrCwAA4oRAJCB68KrwHIpuAV0mj2vPtZe4n+a/fd/X3urCuqfvnzNZs/P15fpn9Jmsyb0Zk1u1Y0HLLcKy46SqBlfZ3TSW+MEQtNWWT1ZB/DLgtfHzB+S8mL29+nZx8cir4HXfPz6khcToADdry8/zQAOX1+qdvr+OkkpPv70muS9V3386YecurVjz2kmYUDr12/P66dYMPDH0Mi/r/p3IPXhR9v7+vI746bPQ+/JTjDz5TXOo+zjQ3BR5d3kIMf7+NNfiXVCz7lOzv+35P78EBx6lgtseir+06c7yL/M5k+D3mX+9bIFcOt/YgkY/rbcp9kTqL+Sfcf/H0QnUQbi/A3xfyrun02Y/33281/a9q8mfJr5X0FQJ1EHosNOvC+zX7+px83q5w/uj5sffvkNiP6/ilHztnLuEr6BbIx8r26+ffv5Q32//eGXnz+0BYg1z0q/tVXyz2T+M1zv6/wBweeoj3+cC9Y/Z9cs77PZe6TPfs2L/1X99jrTQNlwf9yvv8x+ny/TZz6bjHhb9AHB73KmBrr+DsefXn4DpSED1rTO/THI8v/6r5kYOVVe534zU528bWbAwU2UepPypzACJam+53blAVzrCAD7HAfif/LwpHHuz77/b+deKT87z0q5mIrdNxdUnW+PKvftvcp9f52dgMS8ioIos5KZQh+PX6choNiB1YrKq72qA3XEHhvvM6hAn6cvU238/tdCv93nvxbj93uNjB4VSVntpmpUt4n3Olmkh1721N8Bpd4bPKcFopPcAXr4Eaign4CldZ50oJpN1tfXKElmbgSqNij54102QOjLJOz79++2VYdfs0f5RGcPLqgXYMC7OrPPn4FBfhIFYfM185wwn3349bcPs/+Z/atZd+HTGkdQwZ/4Aw15VTrMQD61KRg2sQUot5Z7x//X356wAjGAhWbAW5EfeY/JIB6vnvuGscrRn5ElPrM9gC3ANS3yqpnIJWpeZzt/9q4vWHR6NFXtMK8bwFOFl7le5oxAqgXMeUcymwgJBF3tj59mbe3dV/1uT6wFVExBYlvN95m4OgKOyBPwY1LzPghMzrMIwP8eAY/7QEj1oZ4xbyJeZ4cpAmeFVVlFWFnPNXzr4RfADW/TgXBrlnn912ziQW+C6p4OD3iCiaMnLr679PPkc0DqKQgnt35bO3jyuDs73Rmt+prVz1C3Ku/O4ECVcRa0kTsRwN+eIVWHeZu4d/yAppOkpxfcp1fuMSj+I+lP9Dyb+Hn2bCAmomsRCMZm/586iklNmmWVDUufNuvZ5nBSzAd8U/8zwfxomQDDP4RNqfKD9d9qxlvp/JolEYiFavzbY+Qd9OeYRzlqK4CRQit3+UAxAN8k9x6QU4BV1RTK1tfsrUZ/AlbdCxLwCcheEN1TUL0tOD190zQEKTpd/+DrJ2CT5SDoZkVrJwBK3/Nc23KuQKtqSqqnB0B0elOC9WHkhH+wagakgyAA8mdAiQikCajjd+gOOTATQOtXefpjeDQ5Dmjhtg7QFjSY3utMB3kxxUYNkhG0MtMYgMKHu6hZ6gGMgYrvCNehVTyUmXrSp4LW5Is8BYHxew88H/6I5Lsuk/pAqjVV0K9ZP9VU1xsenn3X8+kroGw65d590h/d/bR19nsy+dvX7K7jexkHKZ1MPPw7cED8VekjlKeKVIOqknrPAAKRcKfc1wdrPmj5XZcvf2rEP/5nvfqdB89/9NyXWdg0Rf1lsXhw1xt1vYJ6sAAxEhVefaexzxNenx+p9fk9tf4g8QHQl9l/ptUfRDzD+csMfoVeoemREIGMBCg8PwCE1WfG/IxNT79mivfDu88QmOpoMgLefCeVtyGAWYLKC6bBD5KpJ27qAR3eqyrA/2v2HgHP/ABFOwsmRqzz3+XtnV2BPx/uei/+4FHWgLXdqf8KvGlTkkzq197Ll6xNkk8vmZV6/3IzMpV2EJ0AhmnzAjIFNDJN5N2v3pua6eKPu657DoHkd/MvUyp9mk0N6KfZey/5afbW3d93SlkLtjc/T33stCQYCn69j33f0tneC9hINWMxqfzYskzt07Ot/bMSUwYBjR1vouv8PSWnFf8kBHwJAq/6sxDp/sVKnnWhbqyJfKPmLZtroKcLWplPM+A0kGWPet+CCX9eBqxTeWULWM6dzP2B3w+z8octv91haB77vl9f3urD0wfPHg8MB4n4uZ54bgECFCwIrh+hBJ79B93fcyaoZaAHAVMRzF3imEWSMGURCIG5GEJRS2uJLiEMQWCChC3Yx5ce7HiOhXgEhtmuRSJL1/Es2PYmTR6h+G2i8WjSBrEsh3QIGHMpwsIdD4Vs1PFgBHYJ1IOWFOqTpIcBYN6nXkEhfJr4MGnC770RnaB4Wvrri41jYCSH1Tv68VktKM0idMJWQpuqcM+8GIudHZ1Lwr648vba4XEhsSXD06NHKN5mT/C0o2qHE8dZbLzfweujHM5zhbrGMHq8RvtrgSARqUeB1gkZfyXcOcG1niNtz4aC0+dufi57YzVu4arviV1m7o/WBl721AY35G5rWQu/ugnzTWcqQecsL4V5WsTauD0Ip8OuX+eNWGq3fnkxGybZJ5ER31gGLht80AuVrCR0o2eHy5jxCaN543l9vrGmBWsr04sd3D/aLe5z9nzZ7fgWvS2XbUmkAnxZLa1iE/HlUDR4Zau1CxFnPSx10iyzumSy+b5jl3tzPJxObkyXF6tcojGFbgp12KS7HX/STFRvTzXe3fZR7upy0g51TlzIoVw1l8s1YDiJL/wVzEgOvkdlpSzVrVoSvVdYjdsp1oG53RzEWpQ45F0b7obJ6LaA8VByD3q92qsjNyasg0L0VXXSbnku9FWpGnaV6gga18cAUakddRVXdWB1hJmcjhcVM/oe3+4roPLlWrW9Ty2vECc2zS6+NEjjiRRyBiZG521rBXPpWKkrZGMzzTHNDxZlkU6R575+0DBEWTTnTU7tYWk31r5QJaegUlmJx+J6c7F1ARWHU5eNmrkghj5vTa7ItA5BveYYHQzJOK0I7zSObcSdTdaoFpYQ7JWbrcsnpoid1g6aCxpGiBZ2IdbrnoahErO/sQjbEbWmXW8Rfj565fYcO8UiFbOqP3fI6VDv9M1ij26wUBnbi1zeLE7cp/7CoSgddJotLnbHiyCIgkiQ7a1R0jCP5ORE38byXKR6VV7T2OKTrZ8Lx0N2hOagUVF9KZYQxx/yRaAoFa6r68Hsj/M1reKpgWLoQlHX+dgpc1chjMt+cMebu9NZuGLz2woW1S4pitoS+MjQD5FVu7swXiP8qT6mFUV0YqAvDiPv9Jt1myb8gHCoFJGMNNd5b7MO69zS546KJXZvBHLNjhqviv3V1P3avapctBkR5apsneFSGIl2KklM5DEstavblcU4hVR8aUcdg03bsuFhlKW1c62UjvXLK7rbo/Nw05tZ66sabfj8mYNsiLu4JdwPnTIuoDnGEsogn639QsD61bypupg3/RPMDrHbz1fYUKZx7kgiz+LegXYC69qvdLEb08siwkq9wuFD6S8yhjuxpUaL6rkJD1f1cm2cILVDgTJE3jKylgr8ZXpZ7ue+vzR3hgkZRnkVSdjdE/PQ7E56A8UknO3ourT0XoHc1i5y9UTuNoKxLAvGTDeeZksNElEalATskIQxz9yAt/eSku5PzuigV3luXf166za8GV/WxFLkhWSzauTF7mgpK6JSIRZfhFxiHAlrGYq3vo8tOXRPlz3S4ioc1yIPRWsblEHJGp21cFJCc4nparu095Jv26ayO45C1jgb4cTHktu5KzFFL5GdkbHD6nkXkBZHQjy7ZoVsFAd2ezsNtB3XQl8h6vmmVGzsLpQQdw8Z4aL1QmJIDd1JuxitZVN1NEbwWUQVaeKyHa4Ra5BFDDuUcm75o3OQ8Rt9YaI1vzW0ltUDlY6ECCQ9RQ62tO8V6YycEoz0h4MNheK+GlHpDJ/19naN1gdlt3MVRl7IrOVvu56b58utKVYwqmJL+hzs4r0mN5dcXqGKmyhRTfP9GrbOWstfZfOqwmeCjrTMbm2Z3u6gvjLEFcTJw6G89SkaZ02jbw77K5xArCMYo7XWCYQ7ZsIKPkuldLtVy7mfcUuy0xN6Ge5ZM70RHW5qPK+QqFdqfL1enf1VJGPUanGMuR4KcJzIEA6mczpeEltW9yMCKxbDjdQyZH+c2+tBXezZaoCtJalRrUwzBBMXKgZJZiEnsiyIVXJOLwf6FNkcwue9tqFkkgYaVpKR72kzPZ1gSTmHZDDfBJwxrl2+hkssk/m26FV0Xfc8PEiNxqKsRjuOf4Wrg3/GujY85EgxuAdbPPZ0S8ebRMCt3CiNMA6O0jrmB0zN2V0U8OZ60QbkHmNxCk3OiFG1ONRq3eBd4TVD5WRIb00boRNnlIQgWN4kkghY4XxBbhUzVMzGqilsrmKn8NTMa4mDCTdwR7UQbqKo+Qf1opc7q5X5ZUca3TbzTEwYDeRS6uw6akQDtCp1jTOHK5dk7bo4qAEdNrdqj+TSJdAipiH2lV4UINL6JStnQxm6y5O0wZhVuWGKgMJyntgx8pAPLnHeHeFmT0ICJuUmvosSceeEda+KkdQP1rDEb0HsJk1njxve2S8dbrg2LnyFuu0l3463Q1ytWVo5GcNpybcYoeVaQ2vcId2sBTLTDWvvG5pk9GWAraB2qQQHOut4wOb4WTbI29oyQ8fNrC3p60Zhqx1PQ5oKV0zXom2ca5HeOfHZjFc8ajeKPR4ZoyXlTXoYFIXYNLi7WR6VgB/OrlEzSgnL5Urz8Jz2eRdwYGOrDqagJr+MhnInF+Z1xxlBN7rsdlNjq6OGQKVQWyfPWDTsOWUtWjhIXU+ClqOe41QKQU69Pe0hemsclrCfS+ytyM6HraadD43IdRVSLkS061pEusxjDLOwHYJkBEnKHNc0S/xk6JZJCEc0UlqdwI1L2l0CLLNVlDhz1egy+O5q0yG8ROxTHrc7eb9Z23mMQJmFKb1Y9gt9j43CRtpGV5/HYc/YUkoWC1e2lQt6kxTRmBhCq4xXQ901pglbGqc4KzkqEqFbyZsKziunsNxbX6hRvsWXbtmkJTWoMBdc1vM9sdT71FLWx9AVZYhd36K0VI6VuEpSLA+GxbA62FfN2WEOslV2SlX28rq6QhmmEsvVSai8IhgtNwQeXySDOo8PGbtuXe0wjCZ+zXshCsKM2d72WyRsd8l8fbylzNIOxSPos5ToxJirNSHUXblOY3nJaXGd1dY5WVksMWztzapYZZjZ9wu6JEGbymVacZpn0qjmG5WQ4vq011hccPVrwVbXEHBlddO0WwUMS0Rpi/AQY5tRo57X2bBETqWux2uj3K6FJMi5ZXK7xfJhDuHyIirHFINTyHWFIoriTXRA+QwrU18/EseEwNIhpRsc55Uq2Q178xwMEsuHJYMtcwpnkCOB9FQNXfbnpCsPK9ty2m2N0Tgzj3P/sMmgiOEr3Yoa+LIQ8fTi9w4Fn5A5ylq8CikQgxhqdTlDRWD1mm2Ex+AAX2iHZiP8mJj0YueWmzK9QQ10PhZXJktAdA7HvbNvqNuFcTHP1ndORKVmdnG4QNuXh0SQw3RzU2GwfV6QayxZr52YTm4En0LDaXPxbp6wiA4mfRqPcWbfBMXYuLfEFEOeg4reCSDdTCQmStz9xXEgbLsRiwS19z1GDvFxzDfzlB9pJz/chGDspfLUgG0MkvMiK5LS3Nqihmg0XRVnVlihdsRdikMw9NGK6KBbJ8Urb93hQQnnQd3LvifHoW0aBTfnWWcztkwUn3HPys7xGDA8nG4wk2OCfR2vGRns89mw0ayVuVNqo0z6i9TCoVtt2Cpa5vSqp2PL6G35KMXFErf7rTjKQXbOO2xwcCY6zytmhWz36wFmR1tHjmwAb3jB25hbRNOObTYP8cFFRV+81oJ3qsoKP4fJ9qzFbdl518po2zyUpFBaYsAVkTcmcLNeo6uMXax2iw7Sa7ItyRKdExrBrQzYKR2CJo9EaeAUYhhzTBIwp6R0PGP6hjAdHt7K2GZz4Bpj1QKYzwieJke9cLmrQ1tOtBhz1ET3tuwLJuUHzbY9FSOc74JiPFhenilrZvApu+bxnj6cEX1jXGwO89udYxFjRIcuJC3pxdlT1tB61GDXY2gonDcryEHauIlMdO4nbk2UlL2SER/RmiVMu0kwr5OiY3xP6GwkWGjQ8phhFbEgY4aUK3pXxf7idlpwJxWxO9eZjzZh58m570ozJdFg7UM07ioc1rahBuEXrdFHwTAOyRFn2tES1yK62Ee784qGINwhmfh0GtdjcuhtxXKGuS3ikgvbfOG2S/9GD/LaUMB3d61g7c5VLXJ7kw6qOyKddyaXoE/KUuUaXS6+gm4PS3vErI6Zr8iW7sjjguIOhwFlTW27La+G24dkOx/barla3Ij4CIWxiu35zNrjR92lGoxd75Rdt4S2PUR4o9icMLxhbo1ANuyCXVAYhikklrfXDRWwZhB5VFy4FFeAtrv1a0oMtyhhAFyFfTWHExMR4cb3RrJb52i5DM6Gx6UxmnHO7Yje2i0072NTYfxoq9+Q47btY7dCRFbotpE1nvCNHmyJjYnaR1LzgtPOW++4VXNEa6NOwuicjHWW1Q0jxWuvzp0T15c62gsWInoUPRevFGhLa1Khhtt1c4vErTWk1C63Q+UCU+htwCnxmjnKSKxhmTunKW/bJNe0OqOcvU0ql/XGPdVooArMLa/DchtRHplp+7CVRztawhS3HDJXPkQGvMcZws/aNEJN27Ob7KipNxERt3kzPwt2J9FLMyYx2ehqsq8oXGdGFkdin69cAicvFHbd75wFj4gi5/f6sXbZVZ3Lh4VEbC7CFvTZFCQ4XBOLOknBDSTJQpLX0ni1MNRmbLj1tEVyi0/uzUXmWxUSKQ8vBAa0Nb2GS2hwvdEirWg+lMkMfnAB8TNbeq7Ei5JVllCQg+YBoXh4I5183TFiBmNaGGk3Z3InqIQLydhcZMeF5hckerksRkMK5t2KRUUkohfoglsX56O0QwvBbMYjIqXdoh1thMplC5ZRl3QTg5tjKU5sG8u3Ka5DDBQtd+FiPw/crta7kgW+Ksgc6xmXpQuy3BERIfrUIrS2sru7XgSYGhIjMHx4Phxl6kADat75GkqSorQO8kAS3GHkhE46ruaIz3qkbg5NOkc17qYhYONRrrOEjiGROOY0m+PixrFYZOATgjuUSqkxHU1cRcq2/M4+uboXc+d4Ewg7TvG1BX7kzivvFpJeojj6cPT4OYk5PV0jdBXiZ942d8tOSU7JYV40qoPQt3DUVNmca5W1Vk1q3xYezK1RgR6GjD2hhR2LBCZRviPzzjag9s6WnKfBfBgto/K4zc7BWk7Q44RCbgm/7MXeZsm9nLhIHiYNXuFRb4Xz0OkuB4w6LERm2Z2EwHNo1FNyyL0Kat5fDZOW64OIOnO6k0q5vpIycTOIE+apc32ZnaSVMrYke1Hx7AQZJK0qoFyT55ym6b+/fHqZTpSf58L/xqvd6bzu/9mx4eOE7+2d0P1I2LPcL/e1vvw7yvzy6aVyIqDK4zi0TtrgeYT4D4ehn//6HcI0b3y8IZ1eVw3N22F5YwXTH/O8RJnb1k01fqvzpL0fxH56sdt6+vuC+tvzwPnlbkhaPE6vn4pPx6z3Y/xvTf7t8R73ZXr9P72C8dzIarznZfA8FwZzR+CKyKm/ofjym1cVk4XPlxIT4NNbiZff/g+GzJ23LiUAAA== -->
