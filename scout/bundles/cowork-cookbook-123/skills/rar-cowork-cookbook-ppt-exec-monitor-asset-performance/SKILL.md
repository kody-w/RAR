---
name: "rar-cowork-cookbook-ppt-exec-monitor-asset-performance"
description: "Generates an executive-ready PowerPoint deck on monitor asset performance status, complete with charts and talking-point notes."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/ppt_exec_monitor_asset_performance", "rar_sha256": "c89f588de161f75220fe8e00d0ffac97853d77b140fb18e029ab83ebb5e6809f", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "ppt_exec", "acquire_to_dispose", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/ppt_exec_monitor_asset_performance`. The original RAPP
agent is preserved byte-for-byte in `ppt_exec_monitor_asset_performance_agent.py` and in the RCI capsule.

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

Monitor asset performance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor asset performance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-asset-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `ppt_exec_monitor_asset_performance_agent.py` and embedded as the fenced Python below (sha256 c89f588de161f752…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `ppt_exec_monitor_asset_performance_agent.py` first:

```bash
python3 ppt_exec_monitor_asset_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 ppt_exec_monitor_asset_performance_agent.py   # or on stdin
python3 ppt_exec_monitor_asset_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Monitor asset performance Executive PowerPoint Deck — Generates an executive-ready PowerPoint deck on monitor asset performance status, complete with charts and talking-point notes.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/ppt-exec-monitor-asset-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/ppt_exec_monitor_asset_performance',
    "version": '2.0.1',
    "display_name": 'Monitor asset performance Executive PowerPoint Deck',
    "description": 'Generates an executive-ready PowerPoint deck on monitor asset performance status, complete with charts and talking-point notes.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'ppt_exec', 'acquire_to_dispose', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'ppt-exec-monitor-asset-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/ppt-exec-monitor-asset-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '0deb4da2dc1a8e73',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['acquire-to-dispose'], 'process_tags': ['acquire-to-dispose/analyze-assets/monitor-asset-performance'], 'recipe_category': 'ppt-exec', 'recipe_type': 'prompt', 'upstream_path': 'acquire-to-dispose/ppt-exec-monitor-asset-performance', 'uses_skills': {'custom': [], 'ootb': ['PowerPoint', 'Excel'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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


class PptExecMonitorAssetPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PptExecMonitorAssetPerformance'
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
    print(PptExecMonitorAssetPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V6aZOjxpruX2FqPrQ9dBerWPqEIy6SEEgChACJxe1oswkQq1iFPP7vk0iq6vb4eM74xo24qg3IzHd53jWT+u3F7dq4rF8+v+ihW0CCm2VJHNaQWwTQohzKOgV/ytQDP5BfFm2deF1b1s3Lx5cgbPw6qdqkLMByISzC2m3DBiyFwmvod23Sh5/q0A1GSC2HsFbLpGihIPRTqCygvCwSQAhymyZsoSqsT2Wdu4UfQk3rtl3zEbDLqyxsQ2hI2hjyY7dum7tcrZulSRF9qu4EixIwfQXyhFd3WtC8fP75l48vCbh++fzbi58BDkA+tWp5IJX8YMtNXNVvTMHyzC0iMK8aAR4FuH+KBB4F4elNwB+aMDt9hP7jP9LBraPmx89fCuj5+fIyfWldAbVxCLWl27RhAPlu5XpJlrTjK8Rlgzs2UB22XV0AVYCmNdDj9bHyG6Wygn6axn54MHmNwvaHLy9lNeELwP7y8iMEgPvyUnfT9etEpfrhx9dsAvmHH7/RaTrvHPrtRAxI/fr1ef8kCyZ+m5qc7lx/AlQfZvXCLy/fKTd9HnJPeoKVL69ngP4PD8JVXfZhMeH4w49/RdaPgeGzpGn/V3R/fhCOgfcAnZ6C//jxDvIvEPxU6J3mX7OtgFn/jiZg+hu7j9ATqL+ifcf/v5HOkgKEwBvi/5TcP1sA/wT9/Je6/U8LPkKnLy/LMAOxVrteFn6Gfvuqq/zi5w/Bt4cffvkdkP6XZPSyq/07ha8gKJJT2LRfv/78obk//vDLzx+6Cvha6OZfuzr7ZzT/Ga53Pn9A8Dnrhz+uBfwPRVqUQwG9ezr0W1n9W/37K3R0syT49rz5DH0fL9MHhiYl3pg+IPguZhog63c4/vjyO8gQBdCm8+/DIMr//d8hOfHrsilPLaT7ZddCwMBtkoeT8EacNBD4nmK7DgGuTQKAfc4D/j9ZeJK4PEG//h//njg/+c/EiVRV+3VKiV+fSe/rPel9/S7p/foKGYByWSdRUrgZpHGq+qVwoxAkOMC1qsMmrHuQT7yxDT+BVZ+mCygpoF//NfGvdzqv1fjrPX0mjwylLdZTdmq6LHydNDTjsHjq47+n8BDKSh/Ic0pAYv0ING/KrAfZbUKjSZMsg4KkBqqX9XinDRD7PBH79ddfPbeJvxSPdEpAj1LRIGDCuzjQp09AsVOWRHH7pQj9uIQ+/Pb7B+g/of9p1Z34xEMFij7tASTc6DsFAvHV5WAaMBUwLkged3v89vsTXkAGFCkIWC85JeFjMfDPNAzesNZF7hM+oyAvBOABfPOqrFuQo6GkfYXWJ+hdXsB0GpqyeFw2U1mrwiIIC38EVF2gzjuSoD5BDXDC5jR+hLomvHP91avdu4g5CHS3/RWSFyqoGWUGfk1i3ieBxcCkAP53T3g8B0TqDw00fyPxCimTR0KVW7tVXLtPHif3YZepyD6XA+IuVITDl2Iqj+EE1T08HvBEUwlP/KdJP002n4ow8KGgeeMdPct8ABn3Cld/KZqn67v1ZAoflALANOqSYPK9fzxdqonLLgvu+AFJJ0pPKwRPq9x9UP7LpoB/6yi+7yWWUy/xpcNRjIT+P/cfk/ScIGi8wBn8EuIVQ7MfqE5d04T+o9ECjQAEOD0i6Ftz8JZa3jLslyJLgIvU4z8eM++2eM55ZK2uBtBpnHanDxwBoDrRvfvp5Hd1PXm4+6V4S+UfgenveQsoD4IaOP3ka28Mp9E3SWMQudP9t7J+t2sdTNoDX4SqzsuAn5zCMPBcAGcbTzC/WQI4bTjF3RAnfvwHrSBAHfgGoD9ZIAFwgnR/h04pgZogzE51mX+bnkzNEpAi6HwgLWhLw1fIBOEyuUwDYhR0PNMcgMKHOykoDwHGQMR3hJvYrR7CTJ3sU0B3skWZA2f53gLPwW8OfpdlEh9QdQO3BVgOU8oNwuvDsu9yPm0FhM2nkLwv+qO5n7pC39ecf3wp7jK+Z3kQ6dlUrr8DBwIRlj+8bkpUDUg2efh0IOAJ98r8+iiuj+r9LsvnP7XvP/y9Dv9eLg9/tNxnKG7bqvmMII8S91bhXkGsIMBHkipspmr3aQrAT88Q+3QPsU/fhdgfKD+A+gz9Pen+QOLp1p8h7BV9RachKfHDyW+fHwDG4tPc/kROo18KLfxm5acrTGk2G0F5fa85b1NA4YnqMJomP2pQM5WuAVTLe9IFdvhSvHvCM05AsiiiqWA25Xfxey++wK4Ps73XBjBUtIB3MLVrUThtZbJJ/CZ8+Vx0WfbxpXDz8H+zhZkKAHBWgMa08wGBAzBvk/B+994KTTd/3LrdQwrkgqD8PEXWR2hqW0H+e+tAP0Jve4L7NqvowKbo56n7nViCqeDP+9z3faEXvoBdWDtWk+SPjc7UdD2b4T8LMQUUkNgPp6JevkfoxPFPRMBFFIX1n4ns7hdu9kwTIJNPOTtp34K7AXIGoOH5CAHbgaADcQSw68CCP7MBfOrw0oFaGEzqfsPvm1rlQ5ff7zC0j93iby9v6eJpg2dnCKaDuPzUTNUQAX4KGIL7h0eBsf+LnvFJAaQ40LEAEj7DnmYME4QYhZ3oGY6jp5AJUTRAT6AVYGlmRgQ07WEkevIwMICzrscQoefNQopB2ROg9/DMr1PRTyapQkCCYDHcDwgKn81IFqNxlw1cknbdAGUYGqVPAagC35aCwhg8VX2oNuH43r5OkDw1/u3Fo0gwUySbNff4LBD26Hom4mmxBNcZfL0iTdTNzHIjEEZErGeYaPrWmsuXzs1f2Ye64dtxY2KKrxWdXM4uwi5RqQXSSHRWsKWZbpVsE94iXzgnm9sGD4ogKJzK3Zb5Gd1Xln7ZVNfaPsaZm1iXlh7kWG1oiVgLiXpanJytZRdU5mwz+8DyQZPBMHy02HQ8lJ0juLIjbSKpauc2QyA2MZO0eWZeb9StcH1FLRd+f6iSC8+H121+tiSsHvDr8lrEcWg12VXZMt1wXEaoWGK74ozSKtHiTOc1C6Ol4dBj4FnCmvtm2NootzIR2Wwt3ZsXO9u0W8VvyetRcdClyjjp0j8qFUfKeJkKhULB6Fmjk0O8j9K1EI0ou08c2C9mM5vN2KXfVIfcaRhFUEJsw+/kcjP3FzmanyWFKFtbT2L/0jFaV7L12V1a6y50KMNjrdYqCz3vVDPXL7e0uPEOSbg6f2vjfWLc0sYNnNQOu/mhMhcX3aTNpm16V1Y5OKB0+rZh4k1+XPmZoTr63mPHq+NieGHwqLQ3d0u2l5tktqrNNW4FtZedg2xzycpsboGdEHad2Ro+nG0lhrG4PdbWOdscd/gimqkstvdi1POp2r0y+E7bLTZrlxbPu6XGBkNYZVJL0gbtjcBLuZHDZJodRwqj+rVl0wEjNnArrsfGsRzBqhFXirbazTPtvXMwWT+Zm2OvaE1teIvr0DD1rKR4mnNtCmmvmLvfGe3x2B6NSp8ZiHAU68EcyXm+S6XFaWYA/O2TJZdHxy1QuegREDmmX9t4xYoDPsI34baDpVQ73LS13sSb2TFzMv2SYqycYi34ocdAK2hhQB2aVdszKYrM5hacYXjFIsvx7I/8VU+QiJF9o2bhvq9mWOQXdr9rWZpOyxF2wtyk3NHMAuG230gD5pbmdtzs6nWLWgKqjcezUJoGcghbpBgYLhbXWTRXgJzbA7ZYEbscmY+jNURm2mR7R5wxizSMDr1WLqiDs+XnPKqzVRyc0WSjC0GtrWzUwUTlgleXq5PNSfycYGkH88coOMEHRh7wbm356WxN8924u9JpTNFxTK9aan/dHeaGmCKqDGd1dIENf62dhoVsYt4CD6ITQ8DCbFwcE5TXKTVY2UHcw3x1ZpmDPShcJNbu5pgel3pJFt5mwAVQjYK9hI49h6i+Khqm1WxgJoSb8daSeKOZm8P+7FhmOzdGruF5KedLX+q32FlpGJhg1r0cqJIzjIx+OJ7OseNfOATbYsdev9BhkZ2qdhiKgU92K0wjugxtKqaeh4uxU4zUmJ1rzWuXVDPnFsNtNVcosUBXByuVdkfXSWbKOkWoI+JeJC26wuzK4uFEWC55ZH0299vieNzT50DvQoNyVoqi6zuHtucSHZMVUh8tgz7Hu/RgOpsgOptWHO4cpZbWW8sZXSFICnTAl6PA6CNpzQW8I5Hc62LB8BpC28y25rWUeQFGjPiwd64yOR8vdpeo3O64w/pFD4gqQuMqsFievIiN4BPcr+xTv+DEamMfdqSxso0d3qYFqW7nrK7zJE0SfqUl3ebkKwN9yJT5uVmOBOiblMUopexGYxGDWK4NN5BnlteJxRXhsSakjvsax5SCuoy4TGq+zxlxwIlGupT2PSW7Me9ycicIg784bNYLPhMo98I32A7Hs7rdbaS97q4y9xhpIG5WfXUp29a47Wh5jDn6fFgozCiN10NzdKxOQHyfZbbGpj50KbrsMzvsTbfY4VRQ2cctyHI1vemLCvd7a8ZoOq0d9Eo5twQsbxF+QCT0gpmuOpDCsL4ci8igYX2vzr3isiP2h3VSzenuECE3JF+qUq8iowsj8iAmLXNorbgOAEZKonMGzZ03xjYFjaIk7aNsZq2rhrIHHFkxIraWzvna4xJqflztF/QNI3cSQVxPxnyF6ld3P8yUkVfCfKg32y06AzvOilzGW18Y9kS6QLaaOXbRdbVPVGa1O1eRGK9u2GKb6AQqY+Ro9+2N2WTlhg6KipMozN9WC/0Qiby6ZbygaTNTyXPKbbXcly0lr+zdQl1fc26+E1pPz+h1qW/V2ge54OITNhbzeJyu9AseWzOhMPBTK69kMhk8zsJmyzl2Lkf5Mp5K4ZZe+ELAElonBRIh+Jst6kOqn3Icni8AiGeSqwpnW13IOFf9etYQZVhr9nqxGx2OZbeCcyUWaAhHOQ7qnntTFV6EO50ovESspHIpxKvGvOnXRvbyKNKHtSCFbsd1UpE0HE/YJM2xR+lw3nKp7WimqVuo2Y0z6hYZTt6qBmObFF8evQ3HI7WrSNnBm9tuoWV0sRf0ssxPuDryoXc05xoxTz2ZHMTdiDkziszpxODM4lx2Wc87ltbTxK5V+TRdweoez9eW5+DVKcUyCk+tMk6O+3Zpy5KZ5UGiTG3NVVjfFgFOo6YpYgjRtYtcuR4uZ69xiQrdp6zA9aujcLIXB3wfy4IPH+2l1dC1wAnr2e4QoAIMeoLumIzOhl93C2PGJ5IdpWLpV6qZDAidn6vlTOS1Nb8retqz8FEadgrYeI2KpXL2/LBYjHR3DZbzdlepFxBH27wrNnsWYRlYV/rrZfA3a6IFLsnddlfxSmrisrkx7p5gL47nqcTl0FkeFVhyeF5d5dYK26K9yb7in+fxfIW4Y4cq0Vwu95w/CAPdBA0N0m95wuZMe4xzvIwQvgxPxIUGlaS4CT0arFclV992F7OmT3vfrMh4bvLKeqz0I2wvzsWJ2LIGGbCil0l6Bx/XB2UbeRl+wdvzbKUNwnJt3Sxkg/E+6h78ZZXsLsF8ILYnc+1IGllGcwKP83YYd1x+nrPAVnNsdA14w4JmJWMblKhUecjR6DSCtOukt/PiUPAuTLYROgjduKja/ZHVT4JgXyxXuTjSNbxqh3IvJSZG4nocIuIyxli90+TVzdFTEYASzxOrjdPNfmR2zSjrHm3y1PFUXscwpdu9i+L9dltapo2C7ml2vBw8+FZIml/q+xkox6bdZSQxHjDSYrLhrC2WpYYuy9UM9y54tBObk6CI13ZvgWC9nXXQlacZwldpzOq3cNfN0OhqJtcNnbb6dvRgwh/3LeLv93wF8/ubQymadt0ejDjOd6i2SyNtQwTyar8/otey0k20rQ+rcnaLC47yebBhZdRZp/WCJrREubvNLmGxJmdkttRgvgSagB5O17iiLPFyEXAUNXDaVqarHbpNx71fLS6ehKPLxFzHMlP6fFfNjMux7byD16uzdhuPW7RKgkwEfaVb4vJ52ZHG0lvGLS3qRykXg0XVKQ6Wj24U96eSpqOMXGu12qKeqGpEGQ8ZcYgXBFEO20xYp1wJbzO/OmplsFbhsywcXKI3oiYgtZi+USeZl/ZXFw6PIVE6aeF1t02m8zbvkT6DSjytWmzrZkR4rnMiUUHCMG77Q0PP19RtYIReYihJ0bd0J/OW3VFWswThtK93uooudArX1R16rMJkuZin4t5eRYNi7DWyQxeRlDCsOV+XTlMI8Qh6dO8U3hLjOAQHXrqojW2vDyeN4mi8doOlwWVr7LqWfNsyB/+klqh+XlwSRiYieSMKdZ9tJEfnHUxfWGCvd9RyClZFa5+cDkuPvuSNcK6rGyXE2eoQLpOxd1PJSrpsrjCxsGIOqpKE6BFvFhKxLRYIXNL9KmeY7oJeLBg50CLI7fU2pBekKjVgj0REVkd2EulTwY4W59eWdv0NstqXKxRbNpYQotTqgFMSZphDsEqLYdtptW0HJHsjbHHE15hGB2IaDJ2TrDP/pufChjUismXMS+I3nHRQrCOP5ywj0q4odFePi3JSZKw+IbhiBs9GalsvRcpmzXgvi4Q2Do3HrkYYU0yzj0tDoXc4TEXClTsVe59G9VlCE4G9BCXFopkWY5Fhz7g1t6bbE4IZiGiMeNEHAZuBQhYf2y1LbL2c1TZlTIjlVt2i+cpOzKODe+vC94UDYpugOKarAilJaxnyi0L00lz2I3WQJJvY9Ks5Ic5k5EKJcZFjI1WcZHY1KJecrtALpc6HKz6YURcO1GonjezMuCXSsNBtc1zFWSueDrbbe0bAyPbycj0QJYIoiCYrtwwTbUdc0b6tci3bdnAkzcyZ6klrPBNqorTJWxNTt35ZcEO1VVcnIerWRc/k0gHGa98vdETS+muPhOohEbMVxjpiw13t1EAb+IChqqQHJQw7iTevMbwRz7zJRpJ5vPk3E2NpKSHw866uI65he2ylioeQvpAoPVvJAb/aLQqv9xmznqu4fxjtbnCFLC1QAOgNX1+73KIvN66IGn4uNK1KNEaT92V1w4LdSfBFugFbCLQBBW8xEDoVnQOi3+6vCi03nQPafExJxVskr9xrzpYFvWyImtkTak+UsuhrI73E9uIhLzxCJWVPbpbJQA7o9UjpS+3Sjo6tbuaxvB+OW4JBysMGE252WvRksmuKct5s4aZYLz2ZJVb4bV6flX5GjZZdkqOZ3Kh9kMNmkNWnrpRJz/I0JLLEsmf9OdjIdxrlsDBJ0NGejEdWuC7JnKAacQ/LimVE15uPRyQhUZIG/JLtpZ3bXuna4/aRtfTsIHCVa0fxhBTCW2KT5x1deK27XZUgYDLbPCczjPOuvhqLIKHtEr+v5xxNNfRZ4+fZGrka6MXURtwgYVWbXzcZgRkqZZiCRxnBIgjXc1LDWdzeJh3b4gShqjhMsEfGIby072WniJB4uCEhARKzSq1w+bQPzjWt4P0Qnz2ULT2F2IsOyw7hpmti2uHMk0WzKwR2TDmUz71JnxX6YvbWbRGuO2Z9uHJKuL2g1I5eIBv/uky9o5pvUdq50DdR7queQT3ngtB9gDGOorJRmczr4zADsbbrd2m323i0jye0Nm9rZFb2UdMcJes0RzTKVXzVlpelWW7JUvU3fWBHymoXE6WXy63hnXpP921kqW7c7d6X9V1dnvQKLs45r8YkozZ5Ww/liRRD0ue4Dt/3MV7q6BAP8PnYHc4zz1Fu7iLY+YmxFMfS40JD7DQUbJLHw8anw+qasVudHuGR6wlkvrDmDiEX85OhgLS9zzOKPl8NWpZCCi931qmZHYrd/LKwiczh6wvK+113PJmWEBHHnkhjBqZmRcQMFcbsThyy5w+hdMvIvZ0YlVjqXOGR3VyEtbTeyHzHoDCCb8sB8VHtJq4dxPOvFH1bliGyD6pmMTbRIuU47qefXj6+TIfQz6Pkv/HSeDrb+392xPg4DXx7rXQ/Rg7d4POd1+e/I9QvH19qPwEiPY5Sm6yLnseO/+0g9dO/fh0xrR8f72KnN2DX9u3cvXWj6b+JXpIi6Jq2Hr82ZdbdD3M/vnhdM/1nQ/P1eWj9clcsr6YT8DdFwKXr34+Qv7bl1yBpqrKZuCXF9FonDBK3fbuNnofLH1+CEdgIFL2vBDX7GtbVpOrzBQfQEH9FX7GX3/8LF+KYh7glAAA= -->
