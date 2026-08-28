---
name: "rar-cowork-cookbook-scheduled-brief-analyze-rebates-and-incentives"
description: "Schedulable morning-brief email summarizing analyze rebates and incentives for the responsible owner; designed to run daily or weekly."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/scheduled_brief_analyze_rebates_and_incentives", "rar_sha256": "bb16855fb69acb605eda26dade218fb5766ec50a6deac8d460c10b52a86039db", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "scheduled_brief", "source_to_pay", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/scheduled_brief_analyze_rebates_and_incentives`. The original RAPP
agent is preserved byte-for-byte in `scheduled_brief_analyze_rebates_and_incentives_agent.py` and in the RCI capsule.

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

Analyze rebates and incentives Scheduled Email Brief — Schedulable morning-brief email summarizing analyze rebates and incentives for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-rebates-and-incentives
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `scheduled_brief_analyze_rebates_and_incentives_agent.py` and embedded as the fenced Python below (sha256 bb16855fb69acb60…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `scheduled_brief_analyze_rebates_and_incentives_agent.py` first:

```bash
python3 scheduled_brief_analyze_rebates_and_incentives_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 scheduled_brief_analyze_rebates_and_incentives_agent.py   # or on stdin
python3 scheduled_brief_analyze_rebates_and_incentives_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Analyze rebates and incentives Scheduled Email Brief — Schedulable morning-brief email summarizing analyze rebates and incentives for the responsible owner; designed to run daily or weekly.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/scheduled-brief-analyze-rebates-and-incentives
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/scheduled_brief_analyze_rebates_and_incentives',
    "version": '2.0.1',
    "display_name": 'Analyze rebates and incentives Scheduled Email Brief',
    "description": 'Schedulable morning-brief email summarizing analyze rebates and incentives for the responsible owner; designed to run daily or weekly.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'scheduled_brief', 'source_to_pay', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'scheduled-brief-analyze-rebates-and-incentives',
        "upstream_url": 'https://coworkcookbook.com/recipes/scheduled-brief-analyze-rebates-and-incentives',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '63a9d8859abbba8b',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': '2026-05-25', 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['source-to-pay'], 'process_tags': ['source-to-pay/analyze-procurement-and-sourcing/analyze-rebates-and-incentives'], 'recipe_category': 'scheduled-brief', 'recipe_type': 'prompt', 'upstream_path': 'source-to-pay/scheduled-brief-analyze-rebates-and-incentives', 'uses_skills': {'custom': [], 'ootb': ['Email', 'Communications'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'verified'},
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
_SPEC = {'archetype': 'automate', 'checks': ['Every step is idempotent and the whole run is safely retryable.', 'Failure behaviour is defined per step, and failures are loud.', 'A completion condition exists and is checked.', 'The first production run was reconciled against the manual process.'], 'confidence': 0.8, 'deliverable': 'A runnable automation with a defined trigger, per-step failure policy, an observable signal, and a reconciliation against the manual process.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'The process to automate.', 'trigger': 'Optional. What starts it — schedule, event or manual.'}, 'refined_by': 'rules', 'signals': ['tag:automation', 'tag:integration'], 'steps': ['Run the process manually once and write down every step, including the ones people do without noticing.', 'Identify the trigger and the completion condition. An automation with no defined end does not terminate, it accumulates.', 'Make each step idempotent, so a retry is safe and a partial run can be resumed rather than restarted.', 'Decide failure behaviour per step: retry, skip, or halt. Silent failure is the expensive one.', 'Add an observable signal — a log line, a status file, a notification — so a broken run is noticed without being looked for.', 'Run it alongside the manual process until they agree, then retire the manual path deliberately.'], 'subject_label': 'process to automate', 'verb': 'Automate'}


class ScheduledBriefAnalyzeRebatesAndIncentives(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'ScheduledBriefAnalyzeRebatesAndIncentives'
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
    print(ScheduledBriefAnalyzeRebatesAndIncentives().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZei2NbmX7Hj/ZBVr5nBICDkXXetRlBRmWQQpbJWFsNhkkkGEeqt/94HNSKqbt17u+vt/tBmxgqRw97Pnp69zzF+fXHaJiqql68vOnDyydpJ0zgC1cTJ/QlXdEV1hr+Kswt/Jl6RN1Xstk1R1S+fX3xQe1VcNnGRj497EfDb1HFTMMmKKo/z8ItbxSCYgMyJ00ndZplTxQP8HAp30n4Akwq4TgPqu7I490DexFd4GRTVpInG23VZ5HU8iiy6HFR/m0CdcZgDf9IUk6rNJz4U3U/g+g6Ac9q/Qljg5mRlCuqXrz/9/Pklhu9fvv764qVOXX/ABP5ixMY+gGgPHGzub95RQEmpk4fwkbKHHsrhdQkqCC2DH/nQrOfVDzVIg8+T//zPc+dUYf3j12/55Pn69jL+0yDM0ZqmcOoGIvec0nHjNG761wmbdk5fQ0ObtsqhHyY1dHAevj6e/JBUlJO/j/d+eCh5DUHzw7eXAkJwRvd/e/lx9MG3F+gS+P51lFL+8ONrWnSg+uHHDzl16ybAa0ZhEPXr9+f1Uyxc+LE0Du5a/w6lPgLtgm8vvzNufD1wj3bCJ19ekyLOf3gILqviCnIHevOHH/+VWBgJ75zGdfN/JPenh+AIOD606Qn8x893J/88mT4Nepf5r9WWMKx/xRK4/E3d58nTUf9K9t3//yA6jXOY028e/6fi/tkD079PfvqXtv27Bz5Pgm8vPEhhEldjNX6d/PpdV5fcT5/8jw8//fwbFP2/FaMXbeXdJXzPnDwOQN18//7Tp/r+8aeff/rUljDXgJN9b6v0n8n8Z3696/mDB5+rfvjjs1C/mZ9zWPmT90yf/FqU/6P67XVycNLY//i8/jr5fb2Mr+lkNOJN6cMFv6uZGmL9nR9/fPkNkkUOrWm9+21Y5f/xHxMp9qqiLoJmontF24yc08QZGMEbUVxP4P8HU0G/PojqsQ7m/xjhEXERTH75n96dSr94TypF6jca+n7nyO9PRvz+ZER47X//YMRfXicG1FJUcRjDhRONVdVvuRPC2yOCEhIlqK6QW9y+AV8gK30Z30BKnfzy1xR9v8t8Lftfnpx8t07jNiNr1VDM62i5FYH8aacHewa4Aa+F6tLCg9iCGHLv55G7i/QKWW/0Un2O03TixxV0SVH1d9nQk19HYb/88ovr1NG3/EGzs8mjqdQIXPAOZ/LlCzQySOMwar7lwIuKyadff/s0+a/Jv3vqLnzUoULuf8YJItzqijyBdddmcBkMIQw6JJV7nH797elqKAb2mwmMahzE4PEwzNsz8N/8rgvsF5ykJi6A/oa+zsqiasbmFjevk00weccLlY63RnaPirqBLawEuQ9yr4dSHWjOuyfzopnUMDnroP88aWtw1/qLWzl3iBkkAKf5ZSJxKuwlRfrWAsdF8OEij6H737Pi8TkUUn2qJ4s3Ea8TeczUSelUThlVzlNH4DziAnvI2+NQuDPJQfctHzsoGF11L5uHe+Ai6BnvGdIvY8zhdAAbfO7Xb7rva5yx4xn3zld9y+tnSTjVGAoPtgioNGxjf2wUf3umVB0Vberf/Qcec8AzCv4zKvccZP/9CPHe5ifL+/Rx7/aTby2OYsTk/49R5W7Feq0t16yx5CdL2dBOD++Oc9YYhcdoBgeFpxpYSR/Dwxv1vDHwtzyNYapU/d8eK+8xea55sFpbQTAaq93lw4SA3h3l3vN1zL+qGjPd+Za/Uf1nmAJ3XoMhg8V9ftjypnC8+4Y0ghU8Xn+0/Xt8K3/0F8zJSdm6KcyXAADfdbwzRFWNNfcMCExeMNZfF8Ve9AerJlA6zBEofwJBxLCKoHfvrpMLaCYMUFAV2cfyeBymIAq/9SBaOMiC14kFy2aMQA1rFU5E4xrohU93UZMMQB9DiO8eriOnfIAZZ98nQGeMRZHBDPh9BJ43PxL9jmWED6U6vtNAX3YjDfvg9ojsO85nrCDYbCzN+0N/DPfT1snve9LfvuV3jO/MDyv+kcYfzpnASsseeToSVg1JJwPvefro3K+P5vvo7u9Yvv5p4P/hr+0J7u3U/GPkvk6ipinrrwjyaIFvHfAV0gUCcyQuQf3RDR9l+OVZdF+eRQev/S8fRfcHLQ+nfZ38NaR/EPFM8a8T7BV9RcdbYgx1Qc88X9Ax3JfF6Qsx3v2Wa+Aj4s+0GKkXFrfbv/ehtyWwGYUVCMfFj75Uj+2sgx30TsQwJt/y96x41gzk+Twcm2hd/K6W78wDY/wI4Xu/gLfyBur2x9EuBOMOKB3h1+Dla96m6eeX3MnAX9z5jP0B5jB0zLh3gvUEp6YmBver9wlqvPjjHvBeaZAi/OLrWHCfJ+O0+3nyPrh+nrxtJe4btbyFe6mfxqF5VAmXwl/va983mC54gfu4pi9HIx77o3FWe87QfwYx1hlE7IGx5xfvhTtq/JMQ+CYMQfVnIcr9jZM+2aNunLGDx81bzb9l7OcJDCOsRVhekDVb+MCf1UA9Fbi0sFX6o7kf/vswq3jY8tvdDc1jk/nryxuLPGPwHCjhcliuX+qxWSIwZaFCeP1ILnjv/3LUfEqDLAiHGyjOdTGKJsnApRjHcymUBL6DUz7chOEYHbjknKKAR6IO5QPHo32CQj0MdUncoSl0xvgulPdI2O/jfBCPCAEagBmD4Z4/o3CSJBhsjjuM7xBzx/FRmp6j88CHjeLj0TOk0KfZDzNHn75PvaN7ntb/+uJSBFwpEPWGfbw4hDk4CDF3b5EwPaLTmx0g+6PeaEkjLS+H7tgeuvZyWma8R7YxzR5wziLPiS142rkFVpB6SxZszshpOz3P6nl91rw8V5bWAssXcWzUc2WokevtfIkv4lbTMxHZMzuMuxwSd8ulVb63HXenNUhM0U19QXa4KWYEfk79WGIule/GxwGZrlb22YrjmzSzyp5GafJwXKWi688tvQnoxSAJM/QsWqXmKql9aG00K2MHkLuDQRutu6XMqUjcipgSTVPB8noxTdrULUpG3aZeoOYp41vHFTVt1cg/HudTCklOVkWzFwk3eea8wwffNdsmn+/n+0PmQGPChooyBnXTq12mdi/3KWrVDYXQnVYlxzPN7UNHVLJKF7aMZ2I16TnLZOvOPCPW9upaBpQK6wSvG62y7dY+K1sLOziuGe2zdibMOCnQnHIx7Ka4dU0B1h6sNFpTYeINpgLSS9j6jdVGUrU97kwy9/ec3fXyeV/qWVRVFoFPyxrM2ID15liehyK3Y10du6z6isDbBSLVl7kMZ8a1YbUrGpHwkLy5B6c5IQJarZndfOWcL8NiphFqadixhnNVJW9JLJ4fbMuItsZsvijOV+3qVzxpKi1ap6u9UM5zI4z1dXs7i1FNtifV6rGe8Wy3JlV1Hdp8VzE7m/Q5Ginc09zrVo3f5EvSlt1zIrrqjJta/XXprwvQAq9u+DTRDm6NKb6JVQZWZhxWaESv0fO97cbodXEQCZzUg3WgCG1pc9n0tlg600xRTrdND3aYcdlZODnlSQyVXdGzcEe/zI9c18/KhAyOq8wPGyLaUebRD/cpNw/JBBYz/KF5PGCmS0yVjNLpc2DQRLSYIoqOrBYIp03D0kScW7esghAxpSpFRPlKzhGeaDWHObp4fuG3rNBq8+IoOymK+dFqs6xyG1uX/I3N3J52D0JKybZ22zVlhF7bRbJhrjvvotb88uRE3C1fkYll7QlLRK8Gt2nTuhY0xdZ0F+c1Tkmv53gfWVt5qS6C2XJeLrVFBXorLIu0tDB7WFmAX6Ne36SzXV7zFYOt0lKoBzPr7QjtDSBvzjPenee6NXUuVpCnZuHl6K4RCCNvXfuwCfytolDHrdIq6WyzY6YB7VLGdbMdBp10q6vRDfM1cr5l4ozqz7rW1QGuB9aKm/m+URjoXMd6+Wht66hdB1RqIzFxuVWUzG9sFRdVXbsYB2Gr8jNtq5hiur566mzwOytn2GsBVv7aMXhY+7vVCpMPGNka4t5Fe6Yka5nJtT5gmJ1epNvidgyEggoxrEpPLmbN5p4DzpgJzOvMmh3X1ULT7W0WzRp+oFZqj6LmpfJIj17qgJGDOKOo803ZBdeGOLem68kqs+w4jqUul7W3ARi6CU5SR7LRVs6bULre5GYROMN8J3lbesjRzMdZ2RoasHMaMd/uWj5tMXo/va0SYSlTq1xQeDFUw6nTUgdXng5+s0SZLboSXOM0L/ZSrF4VU7Cx0NTUcjuLyJYLoq3bLK4OM5tvp5xe+ei16wcR6T1p3Z5sY7qFY9vq1uY+ya2S6S0P9zPVtfUk3ig1KdslsXTwgy93wc4RmdVCyBOFdI7EfNUu9kOyl0hlUGczjEiP0o5rTHA+8R4mWdPepJeHRNpwOgumhV+0nmBvPVawY9ld3aiOO25NsGY6A2sOyHK+UtjOYNmI5Wv/MrRyqjnFkGpzvRCVhSSmvFmT4nomXlcsXobdfh6WhhGCbLZZbLP5ZitqontrAXYD1iLW/PLkb1az4/FG3sDxgE2RK7ez2LW6dpobhtAtsSyY9TVZp7iG3RRlFftKuio2U6Smo5rvVF6ITwpdcqpK6sgwICS5U4N+0GRSB6V/05EdKHoJMDQ6X4ibNbNIbkZ4Vk6idYhW+EG5YkNZxfgJOWpUjp93scwCQe/Zw8o758YwBSqSFsh1nxRNjPG+b7X1mnVPJouZHUCvkkcdU4Xy8zToi5VuYdKJ8k0l7aiM9zPjnCKyw0VUvpXqMFlouFHwgr3nOy806VW6aqebITLdzO0u3PEQg/K2LxPsUFM0cVYrBzMP2NauG3eg9rQwMxZa5OxkEVC7XbhmGFVikv18Z8O5bm+259JenrprrM71uWA33IHP+6a8XNTgyGDqdrO9NawinS+8Te4vvtY7qqiuqSwiUyLamJnu0tdZfUgWOjWtkqJcds3MASkVuCnDSZauhCRbhc7JznxVPijyQjgt5cUhoOQCp7uhpfa8xlD4hSE1w64jqTj0mRhoymmT91F6EA9DcmMIsjecFY2aRw297avT2riyQh0fQ7tb6cxy49c9PiunsBJ5K3VLtkhw21czvIhW+2UossvFuVonmYUKQduQjWGuBH2zR/kr5625/b5TSBc/aNuek1e7rEVVsOeRmljSvLhxp/5C9vYtjpS7WZuJSz86ZudEbqNlt9dBtSRXHerJZykUjC1A0qtyXSAhR3MiXhkyvhmmibYwcPvCA/sSVbdUXyFaqM4jU8CvTln5vCr1WhbP5nxtpp5ibGvWX9chwitVnJjSQmA7ChMZYDJiQITnbXhBWcRQaWt73JDzmQGaM1H2ueRFR0nIgzmc/aydr+OYfdh7Egd7Y4DMjFtf056iHM89Z4c+JdpMGrpDLuxdiV4jR526MbYKOXOaM3SDby7bM0zrNsEuLSus0WADa4sJGFra7o2zuyl42+EqFnGbQ39dhYBIPFuO1/nCV89lANslpm8H6yD7W7VfpdFyyUd9yGu2v68ijkNRJ95Vl2ZYeMq822Oc03IMtcCKLuaPlwu73Ssyl5jX6wqNVuYi8fy+ucrBJjA9sciuF4XLSXm2DiRPwTYE0EMR7V2JkMSbxLX7hNcz1o3O6+u0lIlwm+PDqTuKldyt6xY4XUoTN4MlYfLkIpAzQhAvXauvieU1WXEH8STMIh2tpEzbLR0ULfLEQLcqtXQuy8uFx9OeFCyxiJreDFNGookY4iUSw1ueqoCVDJUSt8PhYiElFUqelIF5TEpOemB6si+2trJCiQTSrqUwuNSbnVUc1lHUC/1+aA+BdXTWosPibnEhCLM/7LpLnybNETZiN7iAPrrMBdy3b2VH3KZsHJBrZmULSFSlphVE1ApZobNIsbwtUjjyTb2kUSewQDwnl3RaQHY6lzvTwWt5fyEHIwzaZZxce4ya84ndpLVkJTjJxvkRxeYLVCJ5TzB9RvSwhb5rZo1FFLsFN7vkarcOjtLisME7TmtkPNqejK3hBTcULNTV/iZTJ86i+11uVgGgO6s9cwRmHKNWjBFxczArY7q/UFo0rCkxj1rba4uAtXcHObPcpuK6zTpQ7SN9Pm31qzRVxeuJFNaiv1qeimYzX9KD54ihtNgrh4rUczaehfmGhdk0rDtLoje3K+WphUex7iaYoeatXxHplKrXmpleFktrVl/i2DuIQpui6xnOmDiyX2PNcmnlp8UxBnnXLVRKqofNaR0QVVZ1hOutG3EExBoe4VKKW84t0rQOGz3ruiPPnqTV4Uzsd4SVr6d2JGxsNBEi/TxLM3IurKZx5MAdR8gq+8W0DlTAtVOIkZXNnR4ZJZyRnNOcE9qC26GrvOgu6pIGkXw8hDtYr8uS1PSjC/cFdUiDZJOQbSscLvROlY7C4URTfduIJKOtWGtdXUS1Tavikgxp2vAgocto2CnEmT5Q5rYXomNO1b3lGw1ptVNa3eXtiTpa+cBSR22uEIQ/dAwQYqcahpO6wfEkOq2nSJLv4H5BtUO92TUmnqVL5xDVKIB1VRDseld4phJPB5I0MPSKRZg8q7lyZVN61h9IpriFkjoPykC3OTbzIfbDHMwZ/bxg2ZAoPEFsdXqtKZupFWWyErgmQVw18UKDbXgjFUqOVUrYgG5mOkLUDLWqRD4dWuQ6yOmTwCsMPfdld4jNoEGQqtSQbsVzbYcilyty85HFVGgqQN2mEuorcQEdrXAtH2xCK3aGeKvGJJGh2XE1mLOzlfDTSCHiGHUJ5HCyRMfcrJWZJJ2YRRA6FokbYMdf1N6eH/AgX8gVhiukL2zPJ85tr3plkmu+Q3osdbcCa2MMstN5wkiuy55rNVO3oxnDekcyT4SBwpbcccCXYiwgp2E/9W/4yrAH+dAxXSDPcWlhbBJsDsrsXGMmVw+M4OXMbqrQXLrR2ibNZGzp5wNJ7QbUFTJKuPlNe4F7DWaWHCJLXkhIiLtsfDUWJIto00M0S3Iq3NalH2FwmtRvHLfrqqQeFKyZ7y64kipVGbI1c5WqWCmGnk6Ga9oMYbYJAeKL7RE1K/pQ3YCGih6B2vVWKLdUmtXbDLGR86zY1kK4YGcD2k1vLQdMMsgvmefPiQ3hDV2SDGLNnXDuLF+FBSHtCM5lAo8sCXxmKcspjHdlKdd4aRLpmUHQYE5KuVHOll7bMeYCE2VCCE67o0wu5eXWrk5cHWo0wFv2pkv2IZOPpyATWM264LfYBWoF8R7WXldOIXxnthGaY9EeWmlK55W8iPkcDrymo2THGd6eNgvGtGdKvdeQeAbH88QnUY9qjelJZlBuBROdHPwkTGiq29X5aWrKhhsOnYcXxKyiRBHx9rwq245/CwqbLXRRa67KNHQofOCLy55ZzdOjMSCe0nhR6fC8TOQGOq15raVNw40I3RQ0uDEE4WFqMAlYLlYbmL2oc7RvuEEj6lbpxNRamVdqhW9ujNFGwpXY3yJ5MdTANa505q17fLDpBXIsrldeZA2h55GABkpzoosIUConCguSEgJCiXCvxqRB52WcKY/CUGWBx0SDowaFGtyWeoLkzMJyk2tgVHy/Mm6LWboSQj6PLtW0yGykn210h6aGKPSPgpRcuwvu0gbCmx3fcfucgXO5PKfJXZEUuLc5k7Kxp6kdcZ5dK8zakQ04LTbugQpPVpnkAssupbm6YdcF4S09S2g5XlIlcc+blAAWOWtTLdqBNiNIahnojLmpWW3JEIh+o9JEkRKe7APbhx3mGNyUTQfOC4fYCzGJLoCLnvbaIbi4Hr8u155yOhuY2F3cjX8QLjqKNVpPZ1D39oY1Qo54/WAgA7/XY72flhrfUoLlNTc3FyMlRf1ynh+IW3lGQtkHp93gHTe1i1Y7sZwJcd4YiFOsC/XiioIBIOWJpkfYaaio7LGKHflYcehWkjfYcgcXiKQWivPLWSzV5ZrAkKsg4HTvzcjZcgP5cUP2880QBwgcf5bAO+u7kGVfPr+M59fPU+j/5vfR41ng/7Mjycfp4ds3VfcjaOD4X++6vv53Af78+aXyYgjvcSRbp234PLL8hwPZL3/t245RVv/4+nf8su3WvB3rN044/o3TS5z7bd1U/fe6SNv7AfHnF7etxz+yqL8/D8Jf7gZn5Xiq/g8GfpyyNsX30hk9DbMCVBnwYwjneRk+j6w/v/g9jGTs1d9nFPkdVOVo+PMbFGgv/oq+Yi+//S8GqQqwVyYAAA== -->
