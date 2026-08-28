---
name: "rar-cowork-cookbook-post-launch-readout-and-optimization"
description: "Close the [Product name] launch loop - what worked, what didn't, and what comes next - grounded in live launch data, not exported snapshots."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/post_launch_readout_and_optimization", "rar_sha256": "2014529f4b23606dc04e303068e6dc0ac3ada61aedbf504962090208f4534eef", "source_kind": "rar-agent", "source_commit": "2aac8c714d97a6ce30b3ce121d73e0593f88e4ed", "version": "2.0.0", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "other", "concept_to_market", "advanced", "integration", "fabric_iq"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/post_launch_readout_and_optimization`. The original RAPP
agent is preserved byte-for-byte in `post_launch_readout_and_optimization_agent.py` and in the RCI capsule.

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

Post-launch readout and optimization routing — Close the [Product name] launch loop - what worked, what didn't, and what comes next - grounded in live launch data, not exported snapshots.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/post-launch-readout-and-optimization
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `post_launch_readout_and_optimization_agent.py` and embedded as the fenced Python below (sha256 2014529f4b23606d…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `post_launch_readout_and_optimization_agent.py` first:

```bash
python3 post_launch_readout_and_optimization_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 post_launch_readout_and_optimization_agent.py   # or on stdin
python3 post_launch_readout_and_optimization_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Post-launch readout and optimization routing — Close the [Product name] launch loop - what worked, what didn't, and what comes next - grounded in live launch data, not exported snapshots.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/post-launch-readout-and-optimization
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/post_launch_readout_and_optimization',
    "version": '2.0.0',
    "display_name": 'Post-launch readout and optimization routing',
    "description": "Close the [Product name] launch loop - what worked, what didn't, and what comes next - grounded in live launch data, not exported snapshots.",
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'other', 'concept_to_market', 'advanced', 'integration', 'fabric_iq'],
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
        "upstream_slug": 'post-launch-readout-and-optimization',
        "upstream_url": 'https://coworkcookbook.com/recipes/post-launch-readout-and-optimization',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": 'd9b7da7b16292559',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'advanced', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'fabric-iq', 'process_roots': ['concept-to-market'], 'process_tags': ['concept-to-market/analyze-marketing-operations/evaluate-campaign-performance'], 'recipe_category': 'other', 'recipe_type': 'prompt', 'upstream_path': 'concept-to-market/post-launch-readout-and-optimization', 'uses_skills': {'custom': [], 'ootb': ['Word', 'Excel', 'PowerPoint', 'Email'], 'plugin': []}, 'verification_status': 'draft'},
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


class PostLaunchReadoutAndOptimization(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'PostLaunchReadoutAndOptimization'
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
    print(PostLaunchReadoutAndOptimization().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZebyLblX6HzfbDryU4Qs3xXrdWAhCQ0IRAgKNdyMc/zrOr67x1IyrTr1b2vb/XqDy0PKSDixBn3PhHk7y9m2wR59fLlRXbNDFqbSRIGbgWZmQNxeZ9XMfiRxxb4B9l51lSh1TZ5Vb98enHc2q7CognzDEznkrx2oSZwoV/EKndau4EyM3V/hRKzzewASvK8gD5DfWA20CTWdT49LpzQyT40n+4r3m/YeerWUOYODRjvV3mbOa4DhRmUhJ37Js4xG/MTlOUN5A5FXjVgRJ2ZRR3kTf0KlHMHMy0St3758suvn15C8P3ly+8vdmLW4NaLmNfN/i5Ick0nbxsmc07AkjS8mXd7Pr0kZuaDkcUI3DNdF27l5VUKbjmuBz2vPtZu4n2C/vM/496s/PqnL18z6Pn5+jL9kdrs7pMmN+tJR9ssTCtMwmZ8hZikN8caqtymrbIaMqEaeDfzXx8zv0sCfvt5evbxscir7zYfv77kQIW7rl9ffoLyCqxXtdP310lK8fGn1yTv3erjT9/l1K0VuSAsQBjQ+vXb8/opFgz8PjT07qv+DKQ+omy5X19+MG76PPSe7AQzX16jPMw+PgQXVd65mZnZ7sef/pVYO3DtOAnr5t+S+8tDcACCBWx6Kv7Tp7uTf4VmT4PeZf7rZQsQ1r9jCRj+ttwn6OmofyX77v//IjoJM5DLbx7/p+L+2YTZz9Av/9K2/27CJ8j7+rJ0p0qpTCtxv0C/f5PFFffLB+f7zQ+//gFE/x/FyHlb2XcJ31IzCz23br59++VDfb/94ddfPrQFyDXXTL+1VfLPZP4zv97X+ZMHn6M+/nkuWF/J4izvM+g906Hf8+J/VH+8QqqZhM73+/UX6Md6mT4zaDLibdGHC36omRro+oMff3r5A2BEBqwBsDU9BlX+H/8BHUK7yuvcayDZBhgBgQADiHAn5S9BWEPg71TblQv8WofAsc9xIP+nCE8a5x702/+07zj62X7iKFwA9Pn2wLFv1QN/vgH0+5b/gEC/vUIXIDuvQj/MzASSGFH8mpm+mzXTukXl1m7VAUSxxsb9DLDo8/RlQsnf/h3x3+6SXovxtzvuhg+UkrjthFB1m7ivk5Va4GZPm2xADu7g2i1YJMltoJEXAnj9BKyv86SbkB+oVcdhkgBEr4D5eTXeZQOvfZmE/fbbb5ZZB1+zB6Ri0IM9ahgMeFcH+vwZmOYloR80XzPXDnLow+9/fID+F/TfzboLn9YQAbw/YwI0FOTTEQI11qZgGAgXCDBwxz0mv//xdDAQkwG6AxEMvdB9TAY5CujpzdvyhvmMEiRkucDLwMPpRDcAp6GweYW2HvSuL1h0ejQheQBCADlu4QLqyuwRSDWBOe+enGirBnGovfET1D5p8zerMu8qpqDYzeY36MCJgDfyBPw3qXkfBCbnWQjc/54Lj/tASPWhhtg3Ea/QccpKqDArswgq87mGZz7iAvjibToQbgKy7b9mE0m6k6vuGfJwDxgEPGM/Q/p5ivnEzwAPnPpt7fsYc2K3y53lqq9Z/Ux/s5pCYQM6AIv6behMpPCPZ0oBrm4T5+4/oOkk6RkF5xmVew5OVP35SfrPbL6n1Y/ZDIEm4R6Sry2KzHHo/6deZLKBWa+l1Zq5rJbQ6niR9Idvp3ZqisGjAwMtAQQS7FFH39uEN5B5w9qvWRKCRKnGfzxG3iPyHPPAr7YC60uMdJcP0gH4dpJ7z9Yp+6pqynPza/YG6sBc6I5gwJGgtIE3pox7W3B6+qZpAOp3uv5O8PfoVs7kMJCRUNFaCcgWz3Udy7RjoNUUsrewgNR1p+rrgxB47UerICAdZAiQDwElQlBDAPjvrjvmwEwQWa/K0+/Dw6ltKu6hBdqCftV9hbQpXiBxalCpoPeZxgAvfLiLglIX+Bio+O7hOjCLhzJTi/tU0Jxikacgl3+MwPPh9zS/6zKpD6SaU/C/Zv0EvY47PCL7ruczVkDZdCrM+6Q/h/tpK/Qj+/zja3bX8R3tQb0nE3H/4BwI1Fla3xN1gqsaQE7qPhMIZMKdo18fNPvg8Xddvvylr//491r/O3Eqf47cFyhomqL+AsMPsnvjuldQQDDIkbBw6zvvPUv587OUP4PFPv9Yyn+S/XDVF+jv6fcnEc/E/gLNX5FXZHq0D213ytznB7iD+8zqn/Hp6ddMcr/H+ZkME9wmIyDad+55GwIIyK9cfxr84KJ6orAesOYdfEEkvmbvufCsFIDtmT8RZ53/UMF3EgaRfQTunSPAo6wBaztT6+a708YmmdSv3ZcvWZskn14mXPv3NjQTFYCEBf6YdkKgeEAz1ITu/eq9MZou/ryvu5cVwAMn/zJV1ydoamI/Qe/96CfobYdw33ZlLdgi/TL1wtOSYCj48T72fdNouS9gV9aMxaT7Y9sztWDP1vivSkxFBTS23Yne8/cqnVb8ixDwxffd6q9CTvcvZvKEiroxJ7IOm7cCr4GeDmh9PkEgeqDwQC0BiGzBhL8uA9ap3LIFrOhM5n7333ez8octf9zd0Dz2jr+/vEHGMwbPPhEMB7X5uZ54EQaZChYE14+cAs/+rzrIpwwAdKB7AUImGwl04eEWipEI6dgI7mIIhpC0O12YNgYUI+cmgG6PQPAFiSILBEVoDycw3HU9IO+Rnd+mBiCc9EJN06Ztao47C8okbSDOwmx3js4dCnMRYoF5NO3iwEXvU2OAkk9jH8ZNnnxvZienPG3+/cUicTByg9db5vHh4IVqwsTektj9DEPoQYCpft/44yjNz+mhVkdqHyuxypnFgQqTwtZD+UhpfBIZoeSkJ7TJyw3OJETctaQxXvZ1cThXJVXKjBqaWEHOMgcWr1tFMsVsaK6Xc2QkTWBoo9MjjcEm+3hQSRybaYDcksM+LGXiileO5wXXLLjyu/m6TqqCsOKbY+yVklDOtZSyl7W63pZW44585a2vZUPjFRyfQniz0GWCxsWDJZwvxbVQfYzkD3RhE8rumjcMVqbadZwXJ2mdlLlKqENj+vZOq7FjpewD8ngLcLirBtwTrRGPm4F2bwlxBV06kwmHRNTK/BxeLARVG8eqL2ftkNbZIckElfWQ5XGxjUxjPF4uXsSUjpamWIZlXCETitxvOfKY6JsNQTh1VhcyqRqWSUa1cjG5UzN32E0UmeN81SUyrw452UfcoKf+qK4sq4rMvabaI+akFXGdN2OuFKbhh/SoY4dx7kdiSl3OqeqXiWmPLW4cCK5AJTTZCXYv843WqwntMTaBylTPs0dmDldxo1tCxnYVmypNdYya0FwX6nAm+WzdJKo8zgQZNorsHKq6RghSmYuosdbLo49iN2UNCs5wlcR3jsZxlaHHoTFKilJNTUv05SB06TmQ12Ufzy4VIqN1FLM4ccGMUXJtZlxhh/0cGymC8nFLpxyEr6lOlMLRugprFfUafqsecCe1JUVuKVsa1UAmu0z1o/3qRPfiKa2NlJvrEt5LNHV2rRDbcyVBG3YBB2K2H851IIu2Lq9hI4ri7dm2MmVXzwOMKygY7Tz1ursBPN3fUPkWRWqm8+NRNXJ/e5VjrMR049QjxolWDQSj1oskoXY0xrdIdiUGjnM53B1YeL1B94lJIAXX7HuW1PEMowbMkzqNHZyymGM+TM/TK1Ih5bxPHVWlNL2RZeG6IxtNEsY+ng+2JW322sEMiC0v8f0q2FK7+Z73dheXM6/lTj610pkaYbw1ZRm3WGUe+aSEaMMO9oGRsSUoqZXHcbjJU2olx1KrjUd0W6XbajeWpV7f/N6UhhN8SZRTORPFTpul1VXUt3qCyezWjmPOLU6zs60x8mWV0JtiO6Azl3ASJWiQhBr3rULo5IZurTm8E+EC2Ttos9xswwy3mo1eJtE+scW2vPE7aXvCUc468VsEq9kwi5Sj6oQEu7G7fn/DlgMyV5HRVUTtWjBDkJVleUFD5pQv3W7sxjWZEqfsppV0Xe2Sdi4XiQG6aaLomCA0mEhPLN5SSmmDbTNCGU/FPNTmatnXy31QyNFQcOaNLB1eaxVZPZIXMc+OQaEt7UN8yHLXk4hB3tfzM8kdGGl9vsoL+nKrkmyF595ZNgR7e/PKDcEoMitYmhJi2Ezl1hm2lnVT4ewexbeajbYN7RSecFqvSOlKxHOUaRyXJ4ocae2wTFrnuj/5RDGw8Ra/AuS3HEzTqWyPopFQ1fMLAecY25R76roOMKnx/TEkzkGi93XorY48pS1KyjjheZJJXbO4GDk9umJLUPO9EA2UVI5b0U20VXguy5tNWeUO20kLUwjmVKkPlIDoVaBn+6DdqQAX60HjyZFk5/3ZkO0Mr7suOOCBcMAPt2xzaw5AL3EtpyhMFPjsqGlDJoulvwsPhVGEFGMWdHTaSeeaSbdo7bnFUj4XO2mdW2FJVegc6RZIGAfSLlcHtNJwVA38AiT5dYv3SOetEIbH6/O+O3KtEY3dUVGXwQ3b7H0uHo1kuMVKpWq5Zok30fZOSL2LDwthvui0C4032X4kt4LMqbZUklZH6+pMkMa5mx6FermMbS4kZLfxLkPUU4G9WNyoDSnlTCSICAKDNMtI/SRuMIqkdydR9FF2FRn81bgmmbkolz4AhGMoxUEme5yyL0Y2rgpnn10UXgaw3xG+tmrQYWnpq1WN8QeU1ar1aKbBaMbH80INFFlhj8ZuP1x4nvDGXZoKC9PP9bFg8TMpltjxeLwMkj47abU61EVcG9ZmoelaxzFDnDF54u2M1jjyTJXG6ZG4KiW22wHf8Tsn6rkLuYsrXYh3kmP1SbWwrNA5JvNsJLDdPO0G7DhIu5un9hQz1nxOJfmVlRP8SFP+ljoY9tCyu51x0txFp7imAJ8EtfArkj7e7F3X2Tl37XVaKnEZ09bdUNr6rMMS29gQNt7uwkCnTSKxW3Jpetha6Je1I8Xrq1NTpZ8wrGN2cLDTZqG6PeP02JGFcjXAJqDJtxa7X/eDGHGJfyi9tAvEYN+fzudcaYOQDHfykh1XK2N1TWgmjAbhxJ17ZrFbR/JGDmxG4OBSaJz1jS+3B+nQHQIfS3O52CkD0aDNBWFXsqsflkzotW0u7Zz50SvDSxzLO5UPDtxJ3ucX/rhku8xplsqxtjstv6joIt1u6fn5UqqZhpe05y0uAgk6m2Kzgtc5xjgHgmotnw+Ow5JBhI5bt8J+FknrC2KUqq2o7bZY8bPgcGoW0nXZ9El5YA434YTuMN2h1GDeN5Ih5Lhwjk/XdamtcP2wIkk3K8mcVGCJ3V7YC4PAV4CR7DWUqI6wosvYqweLZ0zcW9rmMtRn1nx/VXmVtW8qQR4bOKuQA35LM1cnpc1pPN12oMRWx546oEm8oPJUI4eFd6xidJY1NxHVWyGp6zXKUqeiX4+7NbMypxNqvFdUKfcZIz+waew4xa1fYxQDS2t8tFaiECqeEM7sK3GTZtFO4Zt1sZei+naYb5PhpFUoc5VXjZmryrUkkxtLe+SJGTM1XJBpsVGyhCx93crQ0rYWlFzHIjOuaR4DuYCeJUHqT+mW5MdgvB2xJVwqmWRwyy5ijzf/djLZXR5ve8TjGMeuUW/OdXFxWDTriheMVsHi5eyaiBS3pg1xLy0HNcrXuc+RrI0KO3q7bS6ust+uXUmOooNq5ysOn/fablyxjHiUBr7H7YSwg9KgZdRYRudlgeBhl8N0dVFXuuExkirKx7hIb/t8J5dLoqITTFeFzNpit0MazOqO0xAJpdNKnCHIqAxZe/JLarkQhtXYxOglRf1jtq6Y6gi62G5faIjdilWbdvJmrmoxVtjWZY618bHUcUnkklxCLzYNH+LwekR999iajHASJXbYHS6+lO4Q6bTyz3vMprvWOw2KsVNSIufzMy1iseVy17PSegtUj2LhIpJzpcMblxJII464MpNm2kYmi0Jm+LRsM87NeSNjzzlCs0nD3gzGCZuLbRnIiiGbc+oqx/GirGiJqwzHwoIlQg37QNve1njZ09z2JjvCms3P7eYgc81MEbbJbdkFqz6ryZtxZJSAv1BUaQ2anxekfNDbFZysz11pm9ihDxjS1tJ6xW2V2dFsFTQfQK/pG0Vyu13OtosPCbHnLmKCMzJzFPc+OTQKdm1vRHHm8K2B27P5/lTo3Ym1IpSIyDWpjznfmhq3Ca4IScCZ5DOzq4ODXk1H9TxvhGV/xA+l3BHbXtt2kb4FtGuShIoauu8EvmKxqL7rhJ4xw7JdljeOPd+MEwgL12zQgEhjFDRZ+VZDRGUAbW+/WrHY5chSoKp256sSEOfCszbYwK1TReeDs3Rmkx45m+5ivNhgk5TNV8tFg8pWepoZWTCQ142hGQmMIMdEoBp0nRUxv1KazWKGCnNsSZOozcU+xTML8lqPV3VlU3ZJLxdU183WCBfFbkfSDQZ2gVTnXsp0BaNJ711VEd03u24x2GpPLKhkvmYjC0XxaNYG57gkO7nlrQIzhWaOrq9gX7JMY3/fSgdLgxUrs3jXHDaoSeZ0hl2XusRTqaEMg8id9iE8R4ksD1FtI+JltTc6viEsqqXZnrfdjZPAMWcfCWtxRkjqki0ZUl+gQXjYYNIMNLWROHbZqazEHhHSRea5lL8eGC/bmhStERGFLfQl4rDKZYaSMxjnaF/N14B8bwsFvjXG9dq79dKYU66eJH3X9unsWoqhLjNkeN42RKAeCFYR98XKq2D/IuR2vU7Z2zrdFYeaLQSCIJbi9lIv+2SBWJKp3GbVijgtKKsoHJoQMWYY03kkUzS5jgAfzp2K5xh8fqpV4UQLw1zTWfFQCYd+nEWNSUtYhJsN26qU3QxHBs4XuXvCRzNyBgrc28IsgWJzL9+wGH0p9jodc9GF4hab7jDrcOaKG3Yj+OJNUeNoIIVb7G6SUrw5TprD5Bzu2HKoTj43O8ugC29HlhA9iXSWKJaRWZHmTjunKD0cOGbWVxcAmHN6sx/pU+RWhRbYK688uaeCGK/DAh59GxfKLSPCLkUseM7juDYpVmdnwW0z5dJx/mk/uD6I7gyLx62+2fGB1+UzPnNX5VnwxHOWL5tBAnUpZlvprB/kPRLq7oKV10J340a1Cx03t/kaj5ZabYiyd1ip/mJWUQR9OG2WswO+CGb5kpTNXCNgrrXQ7W4b3fie3zBpv2jyVdjb435rBn23x1Zk1VjxcbtqASJXpwMVLnHR0j392s7aYbu3DZs/oe6CF08KogH0p6t2Y9ssvF8ZfVp7Eg7YGO+WNos16ExqrcUMX87HHC9u9pKJOO8CmknfW6+jql/0J6u3jcTZE5REExjfiSed6ijm7F+XlulQWysCunTXBr+6mmtiDuZ0gQZySW3LyrevLsK7lYMLh5vFBJKD1PSaFLDhkh5XzEmNwP5IIpRsQ4gSshCM1ekC+AUrjdWOQ8QZ2LjqyzNWIZHfbjcobHlNPaMsbw4oALbnFLHjcRGnD7TY9HgSzcIjt6cF/Nw2sDGLaBERIhO32vYazYfbbN/Wtw3o3mGJWiS32SHcenSXbwA3wAtutd/ym2RzPF8lf+chYDtILc81HF58U9VtNcePFRyVXd42GW26rOluShG+8IsFDZtbX587BRWhh2uaenzljKTOWhv/Jnlws17NqW0/l1cncs3nUW/3+qn3z+rtfLni4rqS/LJFsb0V1DMUgd1ZikszhE7KnNXXsYR5TjLyoljz7uaCz0YSqzgU9h2px3NuAagiueXr+jb0fVjCK5JYO2ewURmkLL34OopSRzeRLuWC3yvO3D2La00xPKrFbw6uwR6dCngl4Nveg2fkhaiXFuGwSLesOxuvEc0Q8YXWa1yM8sN+t9iXIeEM25xSYIxnkuVCG3QSu80xGtkcSctd+gyPDkc+NEZ6e3AEZIXs+OxKjgw2k8BG4RC3oJcrr0tQD52pUNGxPFHxQBHYMnfgswPn5bFchjHDMD///PLpZTqQfh4r/61XydMp3/+zw8bHueDba6b7kTJY/8t9rS9/T61fP71UdgiUehys1knrP48g/8ux6ud/5wXFJGF8vKWd3ooNzdtJfGP6028bvYSZ09ZNNX6r86R9zrDaevq9h/rb8xD75W5cWkwn4nkTuNV0Sp4DQ4vmW5N/S80qdqdnptNN5k8HqCFYzK/eVPBMqwrtb2E5Wfd8xzG5fXrJ8fLH/wa6AHEM1iUAAA== -->
