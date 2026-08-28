---
name: "rar-cowork-cookbook-demo-data-asses-worker-performance"
description: "Generates and creates realistic demo records for asses worker performance in a sandbox tenant for training and pilot scenarios."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/demo_data_asses_worker_performance", "rar_sha256": "4e799db82acf71817873208220ad89b886f26221ae395494c6aa5c52fec40d11", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "demo_data", "hire_to_retire", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/demo_data_asses_worker_performance`. The original RAPP
agent is preserved byte-for-byte in `demo_data_asses_worker_performance_agent.py` and in the RCI capsule.

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

Asses worker performance Demo Data Generator — Generates and creates realistic demo records for asses worker performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-asses-worker-performance
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `demo_data_asses_worker_performance_agent.py` and embedded as the fenced Python below (sha256 4e799db82acf7181…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `demo_data_asses_worker_performance_agent.py` first:

```bash
python3 demo_data_asses_worker_performance_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 demo_data_asses_worker_performance_agent.py   # or on stdin
python3 demo_data_asses_worker_performance_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Asses worker performance Demo Data Generator — Generates and creates realistic demo records for asses worker performance in a sandbox tenant for training and pilot scenarios.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/demo-data-asses-worker-performance
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/demo_data_asses_worker_performance',
    "version": '2.0.0',
    "display_name": 'Asses worker performance Demo Data Generator',
    "description": 'Generates and creates realistic demo records for asses worker performance in a sandbox tenant for training and pilot scenarios.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'demo_data', 'hire_to_retire', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'demo-data-asses-worker-performance',
        "upstream_url": 'https://coworkcookbook.com/recipes/demo-data-asses-worker-performance',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'a77e388bfc101ec1',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': True, 'plugin': 'dynamics-365-erp', 'process_roots': ['hire-to-retire'], 'process_tags': ['hire-to-retire/manage-performance-and-growth/asses-worker-performance'], 'recipe_category': 'demo-data', 'recipe_type': 'prompt', 'upstream_path': 'hire-to-retire/demo-data-asses-worker-performance', 'uses_skills': {'custom': [], 'ootb': ['Excel'], 'plugin': [{'action': 'data_create_entities', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DemoDataAssesWorkerPerformance(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DemoDataAssesWorkerPerformance'
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
    print(DemoDataAssesWorkerPerformance().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/8V66bLixpbuq9C7f5TdVG00I9UJR1wJgQaQACGEkMtR1jzPI3L73TsF7F3l9nGf9o0bcakBSZm5hm+NmeK3F7Ntgrx6+fxycs1sxplJEgZuNTMzZ7bK+7yKwVceW+DfzM6zpgqttsmr+uXji+PWdhUWTZhnYDnnZm5lNm59X2pX7v0afCVh3YT2zHHTHNzaeeXUMy8HHOoaTJg4AHaFW4FnqZnZ7izMZuasBlSsfJg1bmZmzX1BU5lhFmb+nUERJnkzq20wXIV5/QrkcQczLRK3fvn88y8fX0Jw/fL5txc7AYyAfCzgz5qNSU9sL3euh29MwfLEzHwwr7gBPDJw/xQJPHJc703AH2o38T7O/uM/4t6s/PrHz1+y2fPz5WX6o7TZrAncWZObdeMCIMzCtMIkbG6vMzrpzduESdNWWT0pCeDM/NfHym+U8mL20zT2w4PJq+82P3x5yYsJXwD2l5cfZwCOLy9VO12/TlSKH358TfLerX748RudurUi124mYkDq16/P+ydZMPHb1NC7c/0JUH2Y1XK/vHyn3PR5yD3pCVa+vEZ5mP3wIFxUeTfZyXZ/+PGvyNqBa8eTL/yv6P78IBy4pgN0egr+48c7yL/M5k+F3mn+NdsCmPXvaAKmv7H7OHsC9Ve07/j/N9JJmAGvfkP8n5L7ZwvmP81+/kvd/qcFH2feF+DbSdgB77AS9/Pst6+nw3r18wfn28MPv/wOSP9LMqe8rew7ha8gKELPrZuvX3/+UN8ff/jl5w9tAXzNNdOvbZX8M5r/DNc7nz8g+Jz1wx/XAv7nLM7yPpu9e/rst7z4t+r315kGsojz7Xn9efZ9vEyf+WxS4o3pA4LvYqYGsn6H448vv4MMkQFtWvs+DKL83/99JoV2lde518xOdt42M2DgJkzdSXg1COsZ+DvFduUCXOsQAPucB/x/svAkce7Nfv0/9j1xfrKfiXMx5b6vDkg+X+9J7+sj6X39Lun9+jpTAeW8Cv0wM5OZQh8OXzLTd0HuA1yLyq3dqgP5xLo17iew6tN0MaXKX/818a93Oq/F7dd76gwfGUpZCVN2qtvEfZ00vARu9tTHBpXAHVy7BSyS3AbyeCFIrB+B5nWedCC7TWjUcZgkMycESR1UhNudNkDs80Ts119/tcw6+JI90ik6e5SKegEmvIsz+/QJKOYloR80XzLXDvLZh99+/zD7z9n/tOpOfOJxAPo+7QEkFE97eQbiq03BNGAqYFyQPO72+O33J7yADChSM2C90Avdx2Lgn7HrvGF94ulPCE7MLBeAB/BNi7xqppoTNq8zwZu9ywuYTkNTFg/yugHlrXAzx83sG6BqAnXekcymOgWcsPZuH2dt7d65/mpNxQyImIJAN5tfZ9LqAGpGnoD/JjHvk8DiPAsB/O+e8HgOiFQf6hnzRuJ1Jk8eOSvMyiyCynzy8MyHXaZa+1wOiJuzzO2/ZFN5dCeo7uHxgMefSvhUqu8m/TTZHNT8FPiQU7/x9p9l3pmp9wpXfcnqp+ublXsv8ECU28xvQ2fyvX88XaoO8jZx7vgBSSdKTys4T6vcfZD+q55gqt6zqXzPnn3GVABbBIKx2f/nxuMuNscpa45W1+xsLavK9QHn1C5NsD86LNABPIhNofOtK3jLKW+p9UuWhMA3qts/HjPvRnjOeaSrtgKYKbRypw8EA0pMdO8OOjlcVU2ubX7J3nL4R6DVPWEBG4FoBt4+Odkbw2n0TdIAhOx0/62eP4GbNAdOOCtaKwGQeq7rWKYdA6mqKcielgDe6k4B1wehHfxBqxmgDpwC0J8BIUIQNiDP36GTc6AmgNar8vTb9HAyIJDCaW0gLehH3dfZBcTJ5Cs1CE7Q6kxzAAof7qRmqQswBiK+I1wHZvEQZmphnwKaky3yFDjI9xZ4Dn7z7Lssk/iAqjll1i9ZP3mH4w4Py77L+bQVEDadYvG+6I/mfuo6+77Y/ONLdpfxPb2DEE+mOv0dOMD/qvTh0lOGqkGWSd2nAwFPuJfk10dVfZTtd1k+/6lv/+Hvtfb3Onn+o+U+z4KmKerPi8Wjtr2VtleQHxbAR8LCre9l7tOE16d7iH16hNin70LsD5QfQH2e/T3p/kDi6dafZ/Ar9ApNQ7sQRCZA4/kBYKw+MddP2DT6JVPcb1Z+usKUX5MbqKvvxeZtCqg4fuX60+RH8amnmtWDMnnPtsAOX7J3T3jGCUjmmT9Vyjr/Ln7vVRfY9WG296IAhrIG8HamPs13pz1MMolfuy+fszZJPr5kZur+b/YuU+YHzgrQmLY8IHAA5k3o3u/ee6Dp5o97tntIgVzg5J+nyPo4m/rVj7P31vPj7G0zcN9fZS3YDf08tb0TSzAVfL3Pfd8QWu4L2H41t2KS/LHDmbqtZxf8ZyGmgAIS2+5UzfP3CJ04/okIuPB9t/ozkf39wkyeaaJuzKk2h81bcNdATgd0Oh9nwHYg6EAcAexasODPbACfyi1bUASdSd1v+H1TK3/o8vsdhuaxTfzt5S1dPG3wbAnBdBCXn+qpDC6AnwKG4P7hUWDs/6JZfFIAKQ60KoAE5i4pyrFIxLS9JUzCS3KJIhCJIJDpkJRFkoSHEAgCmy5K4RiF2YRp4jaOeK6NQQ4MA3oPz/w6VftwkgoxTZu0lzDmUEuTsF0UslDbhRHYWaIuhFOoR5IuBgB6XxqD/PhU9aHahON73zpB8tT4txeLwMBMHqsF+vFZLSjNXF6WlhJYVEW4V0NfCFZ4Lk3dRQOrMGD+YlsCnbLGWG/yc1Wv5Zu4hmVb8/fcWau4fcBSdLYU+a7NXI7fyonYJn7NVSE8iiluz515BsbO6/Uxkoha04xa1dPmlHC5nWbbyO5VUSGqSOEOxknfnPFLdU7MdLNbUGTajZvBEg+MJpaeP3qpbmpRrmxNqNIuuy1MF8J6sW15/dgWu9VxXbRonmzxcdW4Z1E74WPhkUdzM8Z9Ygm74BzUVhQbmYpTrh71lIuiw2VzI10exb0TSIG4Jqg0piQGAzeqmVSZsYc3hRXbwWqIyshYhFXfnoiaOUNo3t94w72hPFqIIQ4XRV6kGzrTNKTUNjdXt0TMFM5qvAmcwBUNxt4kpR0fhWEQdvilESOgMayZlr5VUvdolrdOtWI3igy8Mh0POAdnyqgCIZJkRGeM6juJGFNWLjSx2IlyRdBHcavXvryMT0aYIiaO1BSJRcIus+NLzzD6aaNTtS2Cgmez2NXZpKaqOkZMtb0H5xnE75tTcNkuKfO2Ti/OZeCqkRsKNscWRrwJc4S1HPlowiWeYOqJseEYPnlXlMOUNTrPoboTg3jMkxPXCvEtXlm7U3JZR9pl7olatOj4VYj7bupcFpZDQHMBtnFH2nWUXZ+Im6IZqYV4hrrlrmO7E+RoG107T917ulaOstIlmO86sn66brXgEE6KbIx0Z5Myf1C9dF8bC6w9aXGVYGEIQUvJPgXwQcDMy/5qWKcs3qWHhUPJileVYVV7rLEDrhnC2EVE7P64toqjE19x+aSpqpoaRUgYRQXHhN8gclHuWGrf7EiOJzc9yTLzNTuyt+h8XfXBbs73w3DoUGI+Tz1JDQlNhLvOs2FOhzIsgE4NpWyMiycn67DVSs2E3JOgX1T2mjvCENGI6LWHS7dYeuvoIiVkscc2kZsm2+G2QffpgrmhyX4vcEEn7S7l1cQ2Vn+l9zJ3do6xyZxEZS6mimAL1k7kDFob18bptt2a9ej3GRsa7UG0rcDhB43ERoi8wkuBEFCGG/a3XQZcOIuqtY4dYfEcYcl5tA5nBNmpeyI08vpwdDeXINtxlLdbjMvINveXVTSoRH1gKjhxbobFE6Y/rEtmLbRkaFZbg41CJ+Rl+yJwQ8PIwZYUW5Cd9mm5D1Ri8IgrAe822jndJpeNulDWOK6i2+bSq4cDugqtsW4kp9uuVQ5FEXhJrctw5FYEdfK7uDrPl/l5B8GVnS9gXPR3ZQlhuRTZowNHoScHmx2lryWeIzKSNeAG0sv+LK2ow3qt5K7HaMNJqGHQF1hRvTqM54hUd01MrLHY8ZSteBZGruTxtXITVwBD3vFyfmS7+UnqRxzLtUaga7HRPOgWEnJty1DYKkIVbkyiHsWIa53iegpNM9U1NxhDWTrcQJtph/yxiEK3u+GV7GYcehiEgsSPLhrDh2LUccn27XwpVVIriQ3GFh28iXQoTKlzdemcNmARYiEjyy6ar3kK8ZkbfXB7dhWPwspwuxoi2SHWuVNueETKOieNW2EJ1aNWemWV5nwVQsogDbMT1rv9SOo62jc1FrBcwfToiM8ptohD+XIxT4vsjMtJG+U+G6uC4Bn0JWN36gIyFXOfz0Oc0/yetmNfOJ2tovTNvoARSHT6U3xVGH9bInllGwJ7LtIwgJmE3S9t2ae3J30lQ+SonOkEqQ4rz927c/h6PNdeLftdf8myOi3QrtXPF+NmupCWZOjYLzs0GohcXPtxbJQof0HduXqKhHLuWCBjSz52Dq6QuclGb+zFvhbaOYQ7Aelv17sYx+fVuFxiQoKl7ECSmpSw/C2Yn51VuDMp8oJuBFqkfAUqYvMgr43kqqj7KjmHDsxkocUjYikmmyjFVrtc1uyOZpzBDlPQ4RZsQVEivSVjfW4ald7ve51U/WTOW0f1FruJZJydM3z2NZG6GG2heA5nKaIe3ZgB2/ruhYrkJqxXVhWXY+WY434pD/2ZSLZCadIR29LkBeMICmFMR9KwzFys4Li5GPqy7aBDCvA8H9vlTt9LUXUd1ZAJySEdGW0dcZyaStSSVA0lVeXNlUSqdLmJ93VfgvI8BDStlfI2PxN4j6boEiHPoOb4CzEZG8HvUNgwsgQVDdnlkbUuI7GYbuWdxyPFZuvnKUMIcdZWqiavOWkv7m42gW75k44wB/YIb01Miefa2k+ZvYmY7a3cZDco8bYGGZz3G0g59WvuhGKMzbCYxIWpHcboxa12EKlsAwbTGRLXNK2gSuFyljdGK2p04wtiRRhkjXpOCt2QWAir5YpJyKOWukEJ9yMnraq9kIpGnq19dRGPa5ja5ru5I5fXwLZBD0qiFz0e4CxtTbDJ1PwDbOkGsh3WYqsQkhJIOL677r2CxKgiZKEiYhLRIlIF8SBjezxuoHOSlQfmNihmv7K5NR8oSevLF1EclZ3jo63Il8U1DGMW6UXnUEnlxWbokjTVDULJ7a5Dou2Jl+ldmuqYy+40ekE05Ryy/Y2KnGkuY3B4XO+5eJOdk1pXzlYjgw1Ji87tzjOc/dxZhDHmYDkBlUuiO6IsaKdbVY9tc7lkoRJp1WVpWZxeD3ZUamh15XdmQ9+w/EprMgFZOurntLqNQbnZLlK28Uv8cuoPkFKuw4GtjgUPma2+mXvnBBuSlVNp/TpTT8m+lYJmJHmTaQRg3kQ/2urFL1i2JXypgK+duy+dYYvbZT4QhF1mHOWSYhlhUtAxzm20TUYo0r5NBcJQTNq4zq/XzU4eNCbqUqPUpIstXG2EUQSlqvIjW8ZpNC8aMhATqju7xmF/CyHfu2HF4noe2TWZbSzvJMXxZmUTua/1SkCEdn457o0QIrvclWwxxOD1ybidRV+RRkJCKoTgmbhRpVM6yo65KxRrrZM0n5kZw3E6th7UedifRzM5EHbOShET1VircoMGhE0uFro13GstJA3VGDKVkcQawrSS840bv1RGbNWNcMWfwZaAC5KSQGQbvtilTKO4NYzzotjuIsnJCUI/wbB0FJZz5aAAi+IWfjQ6nGPmjKPFp1xfKeEZq5jwzKqRzTB+FFL9Yt1o4xk5B8rYn+ohtttNja2XDFc1nkzPoZO8rTgtbcp+kTq63OUnr8SXrhXJ68LcIDFyI3a6ttleuVq7wJiKgcJwtGimmEe4SyugUU1WNeEm3TZw9uGazEMItKSnQOtaV+BQBa+vAyIgG87DjyYbFzl0lrnoGtFJPYCEts9dXESUbXpS4aImBNhj3XF+gUEU3g5RZo37U7WaJ7daSkQeKnq7PCuSeNxquyHcRi3ClNJJ2iNmBak9Jy0EfyQMPpcRn+87drnFTg6CI0izEo9JGvALXSqbFXktO4UqN11TFg0SsDt9K4CKdtpDyEHMVwuM7KQwXO43Muztk4rWTyp1svF8K+x3slrgulhUieoeB3rJ0krND3lOZgJvbmOj0vJNGKQ3O9WHhLBOPHLSypYtI9qi6UYct/Kw2l/nUOOv4g12VqVQXDS8GGGNUB31bSStl0FwzSGHxXLjUhSZJjIOZapLzipd7NjaSzzadO4goOtE13l0wwpbP3a32/n22HgE0a/xHlp6e5/ODTJBL9Ch80rbIi/RnNKt8UaUkOUtN3qPh2a9UVGDH5a20WkdQiwRZvDYRG/Qi7DfdBYfgF6YC/QT5ML2YamG2nlXXaX56F95AaMJnGsStcXbS0rP08FER7Oys47dckLoqNL2es0U3hsWg0mIhMBYPu4kjmux2IEoWmF5rGkfXfNzX63QJGfYkwZre5GFXKJbx1e4jajoiqJt4u087ZJF+Sgvt8gN802oX+yPKJo34wbNiD7LMXK/WDQwvOjpZaldTR32FljgZTm+tNB273lgm4WoSxfEgJNUOYOYOX6gR0jv/JagsNU1tbfQxYMEPT4e2QzEkxHpAV0MCJaf+JTHVrHpxWhIY6ydeoOdFWi0pZxVlzE3jINlI1nGBu9jzvK60y5SrrGgYSLxCE04YSNKqrO6hTe2I9YSOtJoFxQ05W4R4midut5jQWpmQBM1uCi36/dO0qDIZsGivG5YHGhz0rkfNlTEV20P2ayc+JIyN0PiSrmhYvIDbEadpbsmOm8W+DD0QXJUPFlc0pIirin3UDQ2W0KZ0XnSIAfwcqlHQbhradYKo/1IgZxOtrtjyeEu1gudRR2XUdHi3kCgt5t3FUuaPqBg60puVt5q2yb5+iiPvrLHEu+q+kpIrZ0bTCL6SVrzYsaSndJsOUJQ0RR3263Bm0cWw5NddgiO1911ZzIS6Dc97uSFTbI7rHXbxhkJi5hLbXSr0xw7n6l5uZmTe1ZVSal3mHnO1ifTvBALYW7dBEGI+rRnWD8NndRdBUfJ2dTy8eqhy5WjnZvbOiC9fedX+/UyPGAbQ64MtJ23YFtsGzK2v7nUhpdGn7yEPK42LU6zZCKlqy1F8e3GO59ACwZixsL3Vqfr0SFbBwOb4BIe+cv5dXCivIebFbOEqJrxW73XM5QD/eZubjbDslzSoa+zouk4AnxrCVbfz+cVKqZpS3pWc9ux5/3iErZ8boaLI0Kuo6uD0WeeEQHY/obsnFBZM4mwCFTIykQCOULUQdkPuwTaqAdCurAiJbbB0K1paLt0cXftD2SNoGRwQOY6pS1u6K5tXYdsmY4PsoBs+UvuQnINdrXdKoG7JQpHQTso5WV0IIx0O0W+UXDh2dh+XB48v+vGWmFbjVotveHSlW4g0gOZYz3jcHRBmuUytSQP6UJzc3SE2NjB1KjpPu9pc+FwpA6kbIHBgVp4G/oImT7sDEt+F3mHukTty4W83CAI0nvl5FGuIEnngJ0HgynZPMQxULJipVG8YjZGsftxp8Fyy+msBTfFnGpkJCqC+Q4G22RZGNuAGrNSOVz7Oa/m852ZdnTr2q5BIysGZPxshSDM3sKMs6GjsAiy7pXd8yLIpBF+aYJW5QsNEpEadwtjuZewmyuPjqVbNLpc9MzOr5eF7ne1APHIVj1R3gD2OOmmA5uFvY5a+3OW0SMjWYv9SkPNkDmjRReoq/MO3uFZ0fDArfqDRBg2O/YccbO5sB7cM8elBHPb+MV8AfcbCjqJMB/rtundDiHOwKi8dYKYXDSHnLKNAtkvfDlPwQZMCGOapn/66eXjy3To/Dw6/htvh6ezvP9nR4qP07+310j3Y2PXdD7feX3+O0L98vGlskMg0uPotAat8POY8b8dnH76168fpvW3x0vX6Y3X0LydszemP/1s6CXMnLZuqtvXOk/a++HtxxerraefMNRfn4fUL3fF0uJx4v1UBFwHYeV+bfKvlduAq5fp9wXTOxzXCc3m7dZ/niSDlTdgoNCuv6IE/tWtiknP59uM6fh1ep3x8vt/AR9GRCaeJQAA -->
