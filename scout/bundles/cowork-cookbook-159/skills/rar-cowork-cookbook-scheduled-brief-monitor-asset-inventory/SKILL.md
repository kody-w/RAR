---
name: "rar-cowork-cookbook-scheduled-brief-monitor-asset-inventory"
description: "Schedulable morning-brief email summarizing monitor asset inventory for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_monitor_asset_inventory", "rar_sha256": "efed03c2a467f10a1207527ea480ebfb44633d25ab7693a9be439b1449cca6f1", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_monitor_asset_inventory`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_monitor_asset_inventory_agent.py` and in the RCI capsule.

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

Monitor asset inventory Scheduled Email Brief — Schedulable morning-brief email summarizing monitor asset inventory for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-asset-inventory
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_monitor_asset_inventory_agent.py` and embedded as the fenced Python below (sha256 efed03c2a467f10a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_monitor_asset_inventory_agent.py` first:

```bash
python3 scheduled_brief_monitor_asset_inventory_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_monitor_asset_inventory_agent.py   # or on stdin
python3 scheduled_brief_monitor_asset_inventory_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor asset inventory Scheduled Email Brief — Schedulable morning-brief email summarizing monitor asset inventory for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-monitor-asset-inventory
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_monitor_asset_inventory',
    "version": '2.0.0',
    "display_name": 'Monitor asset inventory Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing monitor asset inventory for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-monitor-asset-inventory',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-monitor-asset-inventory',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'b91b6bb99e310167',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-06-01', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/monitor-asset-inventory'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/scheduled-brief-monitor-asset-inventory', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 1.0, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefMonitorAssetInventory(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefMonitorAssetInventory'
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
    print(ScheduledBriefMonitorAssetInventory().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjxpb2X9HUfOj20F0IsYm+cSMGLWwSm4QAye1os4PYN7H49X9/E0lVbV9fz1xPTMSoqqKAzDz7ec7JRL+8WG0T5tXLl5ejZ2Uz1kqSKPSqmZW5s3Xe5VUM/uWxDf5mTp41VWS3TV7VL59eXK92qqhoojybljuh57aJZSfeLM2rLMqCz3YVef7MS60omdVtmlpVNILnYDyLAJGZVddeM4uym5eB22Hmg2dN6M0qry7yrI4mWnmXedXfZoBZFGSeO2vyWdVmMxfQHGZgfud5cTK8Anm83kqLxKtfvvz406eXCFy/fPnlxUkAl+/yee5qEkp8SEBPAvBv/AGNxMoCMLkYgFEycF94FRAqBY9coMnz7mPtJf6n2X/8R9xZVVD/8OVrNnt+vr5MPwcg4KRHk1t1A2R2rMKyoyRqhtcZnXTWUAMVm7bK6pk1q4FNs+D1sfI7pbyY/X0a+/hg8hp4zcevLzkQwZos/vXlh0n7ry/AGOD6daJSfPzhNck7r/r4w3c6dWtfPaeZiAGpX789759kwcTvUyP/zvXvgOrDt7b39eU3yk2fh9yTnmDly+s1j7KPD8JFlQM7Wpnjffzhz8gCHzhxEtXNv0T3xwfh0LNcoNNT8B8+3Y380wx6KvRO88/ZFsCtf0UTMP2N3afZ01B/Rvtu/38gnUSZV79b/J+S+2cLoL/PfvxT3f6rBZ9m/teXjZdENxAdIGm+zH75dlS26x8/uN8ffvjpV0D6vyVzzNvKuVP4llpZ5Ht18+3bjx/q++MPP/34oS1ArHlW+q2tkn9G85/Z9c7ndxZ8zvr4+7WA/ymLM5Dzs/dIn/2SF/9W/fo6060kcr8/r7/Mfpsv0weaTUq8MX2Y4Dc5UwNZf2PHH15+BTCRAW1a5z4Msvzf/30mRk6V17nfzI5O3jYT2jRR6k3Ca2FUz8DvA6OAXR8Q9ZgH4n/y8CRx7s9+/k/njp6fnSd6wvUbAH27w+K3Jwh+u4Pgt3cQ/Pl1pgHyeRUFUWYlswOtKF8zKwCjE+sCYKNX3QCo2EPjfQZw9Hm6ACA6+/lf5PDtTuy1GH6+o3z0wKrDmp9wqgbrXyddjdDLnpo5oDB4vee0gE+SO0AoPwI4+2nC6Ty5AZyb7FLHUZLM3KgCRpjAfKINbPdlIvbzzz/bVh1+zR7Ais4elaOGwYR3cWafPwPt/CQKwuZr5jlhPvvwy68fZv9v9l+tuhOfeChAzadngITCUZZmINPaFEwDTgNuBjBy98wvvz5tDMiA2jIDfoz8yHssBpEae+6bwY8c/XmBEzPbA4YGRk6LvGqmChY1rzPen73LC5hOQxOeh3ndgHJVeJnrZc4AqFpAnXdLZnkzq0E41v7wadbW3p3rz3Zl3UVMQcpbzc8zca2A6pEnb+VumgQWA4cC87+Hw+M5IFJ9qGerNxKvM2mKzVlhVVYRVtaTh289/DLV3edyQNyaZV73NZuqpTeZ6p4oD/OAScAyztOlnyefgxYAVPHMrd943+dYU43T7rWu+prVzySwqskVDigKgGnQRu5UGv72DKk6zNvEvdvPe9T8pxfcp1fuMSj+SZ/wXstn23tvcS/ps6/tYo5gs//jRmSSm2bZw5alte1mtpW0w/lhz6l9muz+6LhAM/BkA3Lne4PwBi9vKPs1SyIQHNXwt8fMuxeecx7I1VZAmAN9uNMHIQDsOdG9R+gUcVU1xbb1NXuD80/A6XfsAk4C6Rw/dHljOI2+SRqCnJ3uv5f2u0crd0puEIWzorUTECG+57m25cRAqmrKsqcnQLh6U8Z1YeSEv9NqBqgDMwP6MyBEBPIGWPduOikHagLP+FWefp8eTQ0TkMJtHSAt6E+915kBEmXyQA2yE3Q90xxghQ93UrPUAzYGIr5buA6t4iHM1NI+BbQmX+QpiN/feuA5+D2077JM4gOqlms1wJbdhLiu1z88+y7n01dA2HRKxvui37v7qevst3Xnb1+zu4zvIA9y/BG/340zA7mV1ndQnSCqBjCTeu9x+qjOr48C+6jg77J8+UMf//Gvtfr3knn6vee+zMKmKeovMPwoc29V7hUABAxiJCq8+nvFe+Tf52e2fb5n2+f3bPsd+Ye1vsz+moi/I/GM7S8z5HX+Op+G9pHjTcH7/ACLrD+vzp+xafRrdvC+u/oZDxPKgqy2h/eS8zYF1J2g8oJp8qME1VPl6kCxvGMucMbX7D0cnskCID0LpnpZ579J4nvtBc59+O69NIChrAG83alvC7xpY5NM4tfey5esTZJPL5mVev/yhmYqAiBsgUmmzRBIIdAMNZF3v3tvjKab3+/m7skFUMHNv0w59mk2NbGfZu/96KfZ2w7hvvPKWrBF+nHqhSeWYCr49z73fatoey9gY9YMxST+Y9sztWDP1viPQkypBSR2vKmw5++5OnH8AxFwEQRe9Uci8v3CSp6AUTfWVKaj5i3N34L008ybrDYhOQDKFiz4IxvAp/LKFtRDd1L3u/2+q5U/dPn1bobmsXf85eUNOJ4+ePaJYDrI0M/1VBFhEKyAIbh/hBUY+592kE8yAPFA6wLogBLrzlFnYWEE6SNzC1nMSXxBeha2nHu2b2MYgaLuArdskqBQi7I9DKVsBMMox7EIHwH0HjH6bar+0STawrKcpUMimEuRFuF46NxGHQ9ZIC6JenOcQv3l0sOAld6XxgAun/o+9JuM+d7MTnZ5qv3Li01gYCaH1Tz9+KxhSrdgjLT7kIPMOdRffFg1j83BbXZpxHRmq49ylXPWxhjQg0fzpCA4x0t7benBpJgY54Q1N6yUxdGvJHKNCyd/z2jJ9iQ5xOJ6rUmZhLOUMKKdkC8lQm+19SJurBxs44fqeBsIhoCGyqlstTUjK3IR3ibqRi/3PoxiJyQ6WBa3HZtjsr/6Y8I4+okqFg0uI3DAKbVJWFBfKWk5Pzb2Tt9Z89RsrVRXTtf42FbSYMr2ecgXyD7G9rGZ76kDUVXnHleE3pWzPQF5ZjVAUFw4N/NKLYvmfKOtahRUqaVvFylpNGI4O3mJ8pe1rpkuPcJbO2sKHXQDOhrPd6AtGNFrP4ZGLMpat1tL6c1ii93yxl0FcmewodgbEslgSL7qN47RxILs7hXdWhjntOCiyiobaaeWmqnVVJexc7bVnGPVJihxs7p1OYxiYKVWMvJOswxatzHaUKwEc3fCE1cdLt0gxZvimIRVZWALr6g9Yq3QrHdmyI5ZSWtJsG7ry3opUrwII5V5oRxNbZgzpiyW47BP9OZcMQppDbzd2LFVrdEVLSHCcuBJRqvZOUSofdWQwhAXVyKNDe3CQWOMzS2jQAwpqNgOVpz1iTkGOCpejmImkSsCIAk6FrLrSxi+Xe1Wulai3L4yLezqjsm8a9H5/OxmcViOIhpRTq2cje15Ubr4Wbxqys4a2sWl9Ih8f0wrTWTKLuujK7UIopEpDEbfYwtcuzFmtkeOdXhQnPORhS/Xa8qrjtnWp0uZNbJ5hUh3ZR5JpklBojBYK0qLC2TiwwVV+UN+bBJmvMT5sp23DlTJnq/fxLbiTTcrdyYm0yzHcZ2zX5obaMst6XUDzy9pJCs6fObRPXTx/ZGDuN5J9oh2O4cYnQ4QxbShsyhRU19sT8HRO6Qnopa2R78W+sb0MHVMsm0uG9xxdWaUKO2qAVsMIhpm8a6NN7fs1KpDu49v2ppvk7rmDq1qkRu9u+SuIMXRIbYuO76HhIUaF9uLVLpX4RyVqa6PeuqstKN8SQkq2bQM4sXmeEVHTIA9octIQdlCRzfIjp6nlZ5/rU5prUQMGbYe3iSnkJrHGE6IO6d2t/JBIWmY5ASt4PHTTl35Zc7TI8mSab9QkDRq9yofjotI05njvJAvi53VhDaykPItcxw3MKyKHOrqKk6xaMlw4q2FEFvfsYWszs+ITjFHU6f7UxWyEuY7UtAc/biFQ1ZAL7ikKH4B5W1RtjeOvhAbp2N2MbqQRAFG51Xpn5OrfqnpW+hXpLnr0LIxVqVdKnyzs7PSZOICEflBXcghTm1NRvD2OlO6rXEUFDm99a7rktiVUVDkGhgkH0OWf1zRscag+lYmOsJPT16tCiGs9SNnB6HfERZ/QDLqhJ01gjvZUlXz9oZzoDly0uVEMzg3RusTVo5bZ0cynNzP2dMyq6DWGM0K6XsqT5NCjsuR0Bh3EA6HtbAIbLldr+VlUYuS1GmEsHdzifRvdJm1x3659OELi8CeWgTEfnCY1SndRQAIFm5x2rlKxXqhSC+puJXhoOfiQc6CQ4XoJ3S1jPQ9SmwvvVglhX8dWIzZyPvlGKPiVjHhhZyeaeaSYxJc4rvzjdpWWy5lDXXF03NKJfFlIO+OMc2MICFBpaePaiH1bM0fpRpZEuRKRoPjktY7TfTLQyonK4MekQuxyyqZcmRzfWqT3WLkbwk/L3BMbpcyM8dEUUr3agEtiShLkaWsNw53Cxfx4Zyal3UbkctlS/bE0it3Bi1k7KlpQZkbqvp4jT1KtMwLx23JLROl1FrRere3EBCMwUKUjuqBPfo3rIOPvaTAlOP7Vdc5igK39KY3oF0b7EWZWiLcapfre/paaMfYO/L7kgg94qZblwV6IHf+HoME67jR/C1HC8VOaCF5rY3QWVkqsrrjLo26xKUjL64WXV6Ul3jJyCq+vu2cdcVXEKWu4qY89zFRnOHQUhawqEgagZzXqlw3JLGyhkQ0oRVkDuNAegmGVVRUMqeDYHX+EbvEPVmmF9/x7LliFXtsni8MJCd4Z87pndfV5Nq+uRdGtStXu8rYKA8pyty2zO4iGIbBbuYH2DItsgkOOwdFKknTxhSp+W5cqBqN+wIbZLJZ6OBe0veZv0Od0VGXe+0iQCbcOdfewCDRLoptV+elmFAgAT1gHsBfDhheisWbnIXlng3ibr3riqy9WtJNFOdexAYyZeseVIA6p0ZbHtaY+swp66HYCCHiCsjhNjonNi4SGSoJtrROgSySNEprjrZXd/soPYaxsbjYYwfhZ2ld75I5nVd4uUg6u1YDzKKZZdjx+uj3Ko75akrMC4KOhI14XmWhfKW3exHW19YuSPBiGyZXlWXP9abSNnQbwP2Ci/sNud81NmW4t0OYKa67Bd2iFNA1YVwW/IobW6EQhXSN43vcvVwpjCO2Wm4aZnnIeuE6kPlwOlIDoumR7LF0mF6Jlbw5Z42O9KGSCtJ42FPhQjdKTqAR+mIbgdxneqhXMn11feqiUzfZS26Yejx1p07x5yjMREjPexSkZBd5ty7Gba6hK1whU3mVCNmpaQz9xFwVNMs5FII8GbltyAjD2UXTyeR2IXcH6by/ntnB2xztq8tDjYkMtr+BYMOmze3gaqSBkNIm3ziphO3PG9m8aeaGF3bSVqVrilmOuIzpTtWfOYhHWe0clgDecME0Ecqdp8E80cxSK8Pz2TpmLnvaEmyVMTqvIml4OnhVaYpcTwY5u9MM3ow73mWcACHKwLDxvnQslwqS3VYd2KWE7pq+DK7Ha+huUe1wNjChxcZLFS4KOhzmKy8dL9lqZQqBPmwvhMMzxGVVwaXm8UfXtRtRosW0Rml7wPHqCIraRtykgrcWG3oh0nZfDjhvq8dWFIVTS3seax+Wg77ND5Wmrd09rdUHC1EY7XCLMyFu1CYyRr5bq2J/jfg4uHaSXO87ltjM2WNMXhCJUE56Qm+VRbGvu1I3EQO6bAPcqbOtHgsEtbjJkJZqBV04O1FtiY27I0ETK4w2zY5LV9ssF1qZElaNOwTCSG2KEmnN+6A/u1atRHssK7OgfblsqcTxjqkZ2vhFvUEtmwvt/iDBziUWDtwgOnh7lEsTChx7d4gLlbQ6ZM0BzNlcuqMla3u0ymXBWBhdn8rSerORb6W55NQxljr3QImVaQyqblAlqq+OPEvpDESPugzVqhizbqk1q1zMTPZcjsVSNksBJ/huiNQDniRyZUAUHpAun/Rlll/PBgPph1I4plFviKEWiZ2530hIRIQik122w+XizWUaha9brx89a75NzNTPEqRd3haCy8TnuuG5LTU6Fq+KgiojFX7I4N7ONdA9GiRhdoa45HuYcJV8t6AvtI8uTv3A4AlE1Kx2StLV1kPrMoqcU3UrlUK6FVBB4SG0N3m+2nVHmF4qeLyGK6sXVy3RJdI8hsqOdqCWWtc4D9Ess1jEnl7aFmKwea3KAbZfBVYcbXqPnp+rSjo3tHgSF/t4wGtLaxyTEJgSay16i9E8qGW1uHNBhMlUQJ+6smTWmenv8wZTQyS66EHMsMwBy66IkBOicBgcNVPKtUHCTeJuFU6K9xTbRusztB6Cfi9DPVyx7Ek/nGWdgKyxCkoCPiEnIYbbfOtcliVqDZoKW8uKTrSRovs2i30fJahybYdYi19vYN/KJfNqtJYw14ztPrDIccC0VdNwu0GiUNbVt6HooZtpb6rJhE4earm9pjbHcDSxLC+9NEKo77Bem7GVjOdRINZFHonoEatS9sT4sNTqy0vMHy7DxhDMhmyVnd9eoU3Yd6pH7mF8i4GN6uYMtqbheI2obU32ebohY/K8kCASNwcUSRKMFMfVWNUQz7RqhqPciuDac7uc3J5xZQYThOMvVSXXjXVG2fBUl8Rt04A9r3Ij+kY8mZaK0YeqQjhUXEfu4YIZznyIByzn0jqSTL8TtvOTcdU2APrSub4ag2ajcApt46weeTHaXolNl/rIJcM736akqjFXBM5uDbQ6tagcxpSyC8/GADa8klbgx5O/Fj0kpQ/jbtBE+ZZf2RvfYJCK5sSOaoNWU30is0D9kIPSbvndjQw32E1G2p2whk0Q/4XNnGjiBPXxCh5uVUszAJz2B+taI8yFX/rREud63LouUfNSAgDw8c6qrTHPb7WYBNuqDjwNnZvZmapxKGcvJXd2vXaxBXVRr3egrRob3xug2zVHS4Ln98oeFtQVwnlWpMiQgcprK6L31LzF/cPx1hs3JuHUpl/z6Pl48/bzPWNp1GKE5XhQz9x6Hd6yokWuzrbaD75iiuex7w4Ykukcl6oY0+/npe1tQpUVqu44CtORd+EgHaaNx9r1VYRXYYW4sSh5FrkM7Y49yZEqNw8QtcdCSuybzjlkxirdEStB3duokATLON0im9AwfDxUc7uVTuc083vJvXAq2lmwjxoBuZTmdn3YoantjlIc9Ic+bfRaDkiwsebWoAWJJYzzeB7Gitg9DG08l210RdZpR6zWiOHUpHOlbxRLs7eMX8gS51/DjrXmzgFxqRJeQEf8ujDT+jZ6tCMx+QKJYYlz7FWmzHMnoiw/J28nsXLC2ELZVQ96qXErX10sj7tNd8q9OPPdcoOie5SN6M2uhwMS7CvHa53hkHfItq151kU4d88uB3bUW2OpbtSqgZPOZK7k2fXjJFgYc/sGwM5FKAw+UuzSYz1usXSBEQ9y30D6UjTNs++DnSzJHIrARTWyH6gIXaEm3+PI5jb3YDCOY1cOVrBdAzMe1BJsvM6Ga5rv8oBRrrpJ7S8ZLNS+UG7Kll0hjkO5S8Yc/UhZ2ilt0ccTV0KQcPMz5bTdsE3otsqp91xmaUgo09yY+naVmOVuXtCmIVxLlnZEcQ+6rT7ovDhQGchiRUWk1bHuGL9oaMEL0Y4YEwwnOdnqdX5OH+erOYqfIa1HN+phDinLFAB2DPfQcu7EqwtGkyF22pvnLeYfkk1CQ3p62shrcXDxOGeUxkMCsO100LyxtLYYNsvL5YDACIX3FHagPL/cYZVMJtgeN5rDaAqF184pvU/1m2vPuVQh17owBjaz9IcWdDnz2KjbjalXi5wuK3ivtj7lkLWDXPpQhulzvvZkMEjx4mE7X5x4xrSJNOSWh1NVinG6nMOBzRqO7yTNyIFoIAOcJKV95SvAjii65cmuoGn67y+fXqbj6ech8199pTwd+P2vnTs+jgjfXj3dD5g9y/1y5/XlL0v206eXyomAXI+T1jppg+eB5D+cs37+F99bTESGxzvb6X1Z37wd0DdWMH0J6SXK3LZugAx1nrT3A99PL3ZbT9+FqL89D7Zf7iqmxXRK/g8qgSeWcz9t/tbk39wI1Lzae5m+sjC9C/LcyGreboPnOfSnF3cAnouc+htK4N+8qpjUfr4Qmc5tpzciL7/+f9IttTv2JQAA -->
