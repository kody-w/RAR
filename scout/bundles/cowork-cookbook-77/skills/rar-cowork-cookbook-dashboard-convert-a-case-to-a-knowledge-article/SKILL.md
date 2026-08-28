---
name: "rar-cowork-cookbook-dashboard-convert-a-case-to-a-knowledge-article"
description: "Produces a self-contained interactive HTML dashboard for convert a case to a knowledge article - opens in any browser, no D365 access needed by the viewer."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cowork-cookbook/dashboard_convert_a_case_to_a_knowledge_article", "rar_sha256": "87c22e2fb5b4795a2b938bf7a91c3e8245322bec077b0e795b41511c5d7040cc", "source_kind": "rar-agent", "source_commit": "e0fe3912cd3625549172a9da47aad088707fdeed", "version": "2.0.1", "author": "Sean Galliher and Cowork Cookbook contributors", "tags": ["industry_solution", "business_process", "prompt", "dashboard", "case_to_resolution", "intermediate", "integration", "dynamics_365_erp"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cowork-cookbook/dashboard_convert_a_case_to_a_knowledge_article`. The original RAPP
agent is preserved byte-for-byte in `dashboard_convert_a_case_to_a_knowledge_article_agent.py` and in the RCI capsule.

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

Convert a case to a knowledge article Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for convert a case to a knowledge article - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-convert-a-case-to-a-knowledge-article
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `dashboard_convert_a_case_to_a_knowledge_article_agent.py` and embedded as the fenced Python below (sha256 87c22e2fb5b4795a…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `dashboard_convert_a_case_to_a_knowledge_article_agent.py` first:

```bash
python3 dashboard_convert_a_case_to_a_knowledge_article_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 dashboard_convert_a_case_to_a_knowledge_article_agent.py   # or on stdin
python3 dashboard_convert_a_case_to_a_knowledge_article_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
Convert a case to a knowledge article Interactive HTML Dashboard — Produces a self-contained interactive HTML dashboard for convert a case to a knowledge article - opens in any browser, no D365 access needed by the viewer.

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a automate capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : Cowork Cookbook (Sean Galliher and Cowork Cookbook contributors)
  Upstream entry : https://coworkcookbook.com/recipes/dashboard-convert-a-case-to-a-knowledge-article
  Upstream author: Sean Galliher and Cowork Cookbook contributors
  Upstream version: 1.0.0
  Licence        : CC-BY-4.0

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cowork-cookbook/dashboard_convert_a_case_to_a_knowledge_article',
    "version": '2.0.1',
    "display_name": 'Convert a case to a knowledge article Interactive HTML Dashboard',
    "description": 'Produces a self-contained interactive HTML dashboard for convert a case to a knowledge article - opens in any browser, no D365 access needed by the viewer.',
    "author": 'Sean Galliher and Cowork Cookbook contributors',
    "tags": ['industry_solution', 'business_process', 'prompt', 'dashboard', 'case_to_resolution', 'intermediate', 'integration', 'dynamics_365_erp'],
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
        "upstream_slug": 'dashboard-convert-a-case-to-a-knowledge-article',
        "upstream_url": 'https://coworkcookbook.com/recipes/dashboard-convert-a-case-to-a-knowledge-article',
        "upstream_version": '1.0.0',
        "license": 'CC-BY-4.0',
        "license_verified": True,
        "details": {'license_note': 'Recipe content is CC BY 4.0 and code is MIT. RAR remains index-only: it stores normalized metadata and attribution, then generates its own callable method from that metadata without copying recipe prompts or bundles.', 'license_url': 'https://github.com/seangalliher/Coworkcookbook/blob/main/LICENSE', 'repository_url': 'https://github.com/seangalliher/Coworkcookbook', 'taxonomy_url': 'https://coworkcookbook.com/data/taxonomy.json'},
        "content_digest": '9fe5146008fd725a',
    },
    "industry_context": {'deprecated': False, 'difficulty': 'intermediate', 'last_verified_on': None, 'mutates_data': False, 'plugin': 'dynamics-365-erp', 'process_roots': ['case-to-resolution'], 'process_tags': ['case-to-resolution/manage-and-work-on-cases/convert-a-case-to-a-knowledge-article'], 'recipe_category': 'dashboard', 'recipe_type': 'prompt', 'upstream_path': 'case-to-resolution/dashboard-convert-a-case-to-a-knowledge-article', 'uses_skills': {'custom': [], 'ootb': ['PDF'], 'plugin': [{'action': 'data_find_entity_type', 'plugin': 'dynamics-365-erp'}, {'action': 'data_find_entities_sql', 'plugin': 'dynamics-365-erp'}]}, 'verification_status': 'draft'},
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


class DashboardConvertACaseToAKnowledgeArticle(BasicAgent):
    """Automate agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'DashboardConvertACaseToAKnowledgeArticle'
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
    print(DashboardConvertACaseToAKnowledgeArticle().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/816aZOjyJblX6GjP2RWKzOQWATks2c2ICEESEIICYQqyzJZnH0TO6qp/z6OpIisevVed1fPfBiFhQUI93uvn7uc6078+mI1dZCXL19eNGBliGAlSRiAErEyF1nkXV7G8E8e2/AXcfKsLkO7qfOyevn04oLKKcOiDvMMTt+Xuds4oEIspAKJ93kcbIUZcJEwq0FpOXXYAmR93G4Q16oCO7dKF/HycpTagrKG8xyrAkidw6s4y7sEuD5ArLIOnQQgn5G8AFkFhUHTBsQu864C5Scky5ElPicRy4G6KyQDwIUq7QGpA4C0IehA+QptBb2VFgmoXr78/MunlxBev3z59cVJrAp+9bJ8M2jxsIVdQEuOOSu/mcE+rICCEivz4YxigKhl8L4AJVxECr9ygYc87z6OCHxC/uM/4s4q/eqnL18z5Pn5+jL+HJrsbmCdW1UN7XWswrLDJKyHV4RNOmuokBLUTZnd4YSgZ/7rY+YPSXmB/H189vGh5NUH9cevLxCl0hpd8vXlJwSi+/WlbMbr11FK8fGn1ySHkHz86YecqrEj4NSjMGj167fn/VMsHPhjaOjdtf4dSn043wZfX363uPHzsHtcJ5z58hrlYfbxIbgo8xZkVuaAjz/9K7FOAJw4Cav6vyX354fgAFguXNPT8J8+3UH+BZk8F/Qu81+rLaBb/8pK4PA3dZ+QJ1D/SvYd/38QncDEqN4R/6fi/tmEyd+Rn//l2v6zCZ8Q7+vLEiQwBUvLTsAX5Ndv2p5f/PzB/fHlh19+g6L/SzFa3pTOXcK31MpCD1T1t28/f6juX3/45ecPTQFjDVjpt6ZM/pnMf4brXc8fEHyO+vjHuVD/KRurQ4a8Rzrya178W/nbK6JbSej++L76gvw+X8bPBBkX8ab0AcHvcqaCtv4Ox59efoO1IoOraZz7Y5jl//7vyDZ0yrzKvRrRnLypEejgOkzBaPwxCGGJqu65XQKIaxVCYJ/jYPyPHh4tzj3k+/9y7uUVFspHeUXfy+K3Z0n8Zn0bS+K3OodX7yXx27Mkfn9FjlBNXoZ+mFkJcmD3+6+Z5YOsHk0oSgALZHsvhjX4DMvS5/FiLKDf/6Kmb3ehr8Xw/U4L4aN2HRbiWLeqJgGv49qNAGTPlTqQSUAPnAbqS3IHGueFsPh+gphUeQJpoB5xquIwSRA3LCEoeTncZUMsv4zCvn//bkMjv2aPQosjD6qpUDjg3Rzk82e4Si8J/aD+mgEnyJEPv/72AfnfyH826y581LGHxf/pKWihpCk7yDZ+k8JhI8/Awmy5d0/9+tsTaygmg9wIEQu9EDwmw8iNgfsGvLZmP2PkHLEBBByCnRY5xDDzkbB+RUQPebcXKh0fjfU9yKsacQGkNxdkzshcFlzOO5JZXiMVDM/KGz4hzciQUOt3u7TuJqawBFj1d2S72EM2yZORP8snu8DJeRZC+N/D4vE9FFJ+qBDuTcQrshtjFSms0iqC0nrq8KyHXyCLvE2/k3MGuq/ZSKFghOqeOA944CCIjPN06efR55DdU1gl3OpN932MNXLe8c595deseiaFVY6ucCBJQKV+E7ojVfztGVJVkDeJe8cPWnon94cX3KdX7jG4+G/1EuI/NiTv/I98bbDpjED+P25mxmWygnDgBfbILxF+dzyYD/hHI0c3PTo62EvcLbqn2o/+4q06vRXpr1kSwlgqh789Rt6d9hzzKHxNCW04sAfkDYTyLvce0GOAluWYCtbX7I0NPsE130sf9CnMfpgdIw5vCsenb5YGELvx/kdncA8AiCUMGRi0SNHYCQwoDwJhW04MrSrHpHx6CUY3GBO0C0In+MOqECgdBhGUj0AjQphmkDHu0O1yuEyYj16Zpz+Gh2O/VTyc7iKw/wWviAHzaoytCiYzbJrGMRCFD3dRSAogxtDEd4SrwCoexowt89NAa/RFnsJw/70Hng9/ZMLdltF8KNVyrRpi2Y2F2gX9w7Pvdj59BY1Nx9y9T/qju59rRX5PW3/7mt1tfOcGWBKSkfF/Bw4Cwzqt7jV4rGgVrEopeAYQjIQ7ub8++PnRALzb8uVP+4SPf20rcWfc0x899wUJ6rqovqDogyXfSPIV1hMUxkhYgOoHYX5+pt1n6/OYdp/rHF69p93nZ9r9Qc0DtS/IXzP1DyKeMf4Fmb1OX6fjo03ogDGInx+IzOIzZ34mxqdfswP44fJnXIzFORnGDH9jqrchkK78Evjj4AdzVSPhdZBj76UaOuVr9h4Wz6SBTJD5I81W+e+S+U7Z0MkPH74zCnyU1VC3O7Z/Phg3SclofgVevmRNknx6yawU/LXN0UggMIYhLuPuCuYTbKzqENzv3pus8eaPW8d7psES4eZfxoT7hIwN8Sfkvbf9hLztNu5buayB262fx756VAmHwj/vY9/3pTZ4gTu9eijGNTy2UGM792yz/2zEmGfQ4nvhHcv2M3FHjX8SAi98H5R/FqLcL6zkWT2q2hopPqzfcr6CdrqwYfqEQC/CXITpBatmAyf8WQ3UU4JrA7nUHZf7A78fy8ofa/ntDkP92If++vJWRZ4+ePaccDhM18/VyKYojFioEN4/Ygs++7/tRp/iYBmE7Q+UR1MOhgHMs0mboBjSwmwGp22PspiZgwMaI0gcw2zgTCnKngI4wiZm5GzmkC41JaaOA+U9Avbb2EGEo4lg6gGcmWGOi88xkiSYGYVZjGsRlGW5U5qmppTnQqb4MTWGNfS57sc6R1DfG+MRn+fyf32x5wQcuSYqkX18FiijW3N8Y/fBeXKbe6YY0bmkHfKGyI7T7JSFYUdllaUcZpY9aL7jsnw1mDN2I3arw2Zr3YAa0PmBjDMy21DhIWlmsVLviIvULqiCYBhUcdnuwm2XhT6xT7lMXy5dqfuJI2fXWV9vSaHhlF0iXXbbSnFJ6XQF+l6yKoFuztltk2ULJgpO7Qm1yxs16fS5Ls+nhzzbnUJjShwT3XXIUEqczO9slWh0J9WWVMEMiRo4/iyMFIdaFe71Oj2RJqTZI0rRNNsKPDPUhkbyYdhGa6s1/GS2qQ56onBXd7+uMa+1K1LZVItjTYHzeqLSflPxXRUGHT6DmCX2xhLO82vtHvwCLPqb4l+8cAdDUihP7XInS7t+cFpXpOpedgQHI8Sdq2906eAT+1uSnX0lEbWmjJdYq278SjKSolYE8swW7lFj25W8SIYkTeOwcQKfol37eJ3o/dJGD9TJKsrY29K81Z1CUwTgMlfozaBsybSTzqpKT1R5LwqL+jRvnGp9ilP8vE0ynBQE/6zMxZ2/XVaVhGJ9dwXz2D9TZDjMpBqrMLXmtNXufJZnV/EkevXkptXGLOKUzVKeFcep6mGdWJkYa9e7Qz4LGTI/JwdJPweRrkwSxz7naTNLk0SyWHrP0zVPq7NhL5x0fJgGrn3TN8MsSW+EQ5tc3Dc5XlwTe0Zk4om0nem6ntRrkd5ezoWgR6h2i7bqzbbyIxfcgLUSpxQdtrtZmkfZBmXpa97wnVBvPdvyhM5M7d3xclIZHeTXPmEwZlV22RJfwkCdb3ttbdCRX5hDkCSi509MdAJTqsJ1fXXOJ+lwTk1lowRmZt0U9lAF3HzmHy8z9mwmPF10sqV3VyftZLPpNlfcEM87zHF67Hr20XWmULmHd1ltTnQz9dubjpor43h1PfS2ZNZiEzkMb2FlupDYtpLFfnaqruE0UlAJyKWuJUa9jAemloLK3Nlmn57jaCVER4Ug+MjYr2hpbwq6Eq02RMFBNkx8OurPK3dnDmHtZJpkJ1pj7vjFYs0bh4gxczNHLzcz5BdrbQiKauX01qldhGlQTC8SS6RuhGcCsdZp3TOOq11bMCYW27tdv1CGo64WnlBU/C2zI27KFLNTOFG5eQsmXjETz4LLrNCS8lKatptKuuIMTnrkLdg7nuEQ2SVCd65HUaFM4McE28dJUIBabKZDWmjdOlr0mVCLFmXwB9GnT5s9vV4d9b1a2O553ddz2GL62nYN922r48Lz8FbGw5kxJfFK5rYue+jFGW8QhB7J9HqSaAUuraLsuN1jKQkjNO+usnnrBlaxlco5tnP+ZGO5dA7lw5nc0SFtL07rVB74g5Q3HqdPjlJFBiUEpFvUN+M4j9hmnh+rbELFgZbwxUpHYTQEB7YM+43DOE2yoKW1FKsHR6RMrlTV2J5qRnkh2aW7LYiwIdlr3DhddbNDwzjlpKLhSeUXLi+VBOdtMVme2rtlvLgNqGzEN2tnV2h8TXR9QXc92lJYEV2BM+Gys3GZOiZ1yvZ4vHP3xWY3P8AH24T2ir0+WWVk5B4DwhgcNz0ePfxyOLS1azg36rie+ZmQicWSiYuDZawJGLomRduCft2q3sbRdmtfbCNlrmXUxAeCNh1yachn6/YcTk56nkvhmu3M4bgyAAXs7qCyWGBxbBDG+EJeoqI8IzxhzNU8XbCBVPolyqjzqzCLVJU9bdxlr7GadNWEaaKnBbufnavFanURbgtbOS2SQNhnlnaZanzGDl1hR1GDncWVuD5UtnXVsMSpq4pRQGS4fdGIl+FYUkybFZjTni9TVQv5WbHQE7wlptepFREGaZS3w3zF3khBrVAabdksAgcMu62qPW6oAdrPZEh/KJotAepNqnhAvT27cgkqXPr6bhOZGT6zBemyIHPekZ3z8pYIrnViZX2Y69u5P0g2Nffso6LQzdTd+NLZQU2t4vwypfIwn9o8MF3HdxenWsal22oXk2GSXIqWvKoBX+iyvk72B5pdnzTvurnF5nXToCZH7pNsK9bHuZOK88wJZAV4ekBs8kEfrGl4HlqBnq4kp2n1MmL7GWc10pXdnK+zYq5y6JqctipnVwe0kC9BInnHnWLy2ky4tNeOvqhGOpxoUEqneZWUk9smvfF4tevl054Xe01fkVaxDbU9BhuUHWUeXfUkajo2GRhmZfrb0lTiOgxTLCY0ZbYr6017HegjzoRCsPTLrlAv8+2e0U2dI0X+JOj7i5WWliqtawnn09n1pNA5CNYSbZl9uRND/qoFS2sp4IeDiBp0fk3P7Grl68op0diYNXkzX124vE9us0yY3/qLguciSxhz3fG3k/1lpluuVl2StXrbY0q8ahah1WxxzaXWVr0trwsRD3rf2sUsu+Yo27pFqtEuuKXQ8ur5sL1g26B1OJSazeRGGBZ6qVMn2zukU+a00fTSqASWZ27zOolPS5Uy/ClbC6RiVEMp7idra7kg5YvKSok3nW+PIBI1u98ddKVbmUKVTrf0RHfC2wUzJLy6qFV+yZf0YEuSIUtmFS5UXz+cHN5NeZ8VV1LMjMDj04Cy+Jrd71gPw1smOPm0Wy9vlWUAUKyW4vG4m2MtoTSza3GaTY3DFAzsZn9kdoNztv1DQMe1lXSbeNkeQRmnKwc9zKlpmrUmiSv7Uk9OBT6d4FtjKQx7SVdqqGU33aPLA82d1u3lFubmxQAdK8hL0VwVJHVSk9zquWmt++k2DxU+By1+paTj/Brxre8VkIalG6sq+UK9Wcw6FSpRxeREUJulqG83g0sMC9gHkjZJac1El+Idt8htObyIbXWasqLso00D+0HeuyrudlMWF78kdrrgCaK0aXpIdS12uSa7JcGqfbWI1WipzdRjGE+zDmIuHHflpYh4ll7gDUtt0pgWXGNrmFRlRwmWcrG5X2yFhtXZy1mW8zJj9/Z2ZqJqwSfVmS8WlKwFYLJeBjNGw2Fg1FYVr5usDtgo44oz4QXXM6/2XLHOi9wr9bDNy3BZzYZM06pY5PxJL4LrJayF5TkoZONK9pkeAprQ4d4gc/ujk074DRmJqrJQyHoC3Lm5y/fhkWViUFFmUmqLBO+jKwEagmT4U7EipJqx5lfr7K7I0M4kbWrb7VHZy9sb8NU2b2RaqmeB28vnLAjEpHQCjA+VE1XsZc5I09Nqa6SRZJuWlDPXbltyckm2uwbl7Ul8KOv5sqqN9ZGoHS8M8jAW52fOHvLrgl3zVyEHQFxVmaCLU3Mhutyt5zy21tN1UMQLTQ5OXe7kYUEOmV5b5zogcfoI9wN0LasZOFBRzjcYXglKLDmXjOsvzgVsc3cuzdU5oyxnRUWIGymlzihbdlpYNzhXmTW/NahwpwST1S07yZ0fdPxamsiJ068OhcvO/f66luogCohIcOPtwZkcOw74SnoG+Lr0cb2hyELlTdEyHXp2m1/V9mguM2D5VwwNN+bUslYdt3Qb9lgry2XDCImUWFO330/3kc7662Ndy+2F7fb8tW9jcOivFslThaJuDz7PsNaW02OCxURDimh7VQWZtgWXIQFWscP2UmIvZ1xc58o86nuj2RBruFNiKG7OyYcsDnZRPMGYbEo4Yq5WdLj1nWVA8NO68rPdNeP3861mK3WyHS6DObeOp8mSXeDnYdnRi+PQCXsh31znjaEeOAJui9kjWWoXoppLh43XqJPrGYtSh3VLZ+4Y7qTtJvz2sjZRAHcncN99dm6oYmmDzZAOb5ZRdWuVrt3kZgYIBeuctYK1C2cw6YVoFRRNMGmm5kWkAX17zjvMpTl6UBZy1E4aIz4yboQZW1wn2SqNHGl/ik5ZSxLqfGugR+8KttKEjo7Npt2R9HlT4q6LLthCETFKQ3t67l6MhXdKqgsTRswsLnpC3tjsrcA6yjstd761VCc77JiQ2K2IIzBb99h6j89hobrgM6Co3eQ6QVGx83yZ2ErUmWJUtJ8SSXPBjXUrT7C5xEwluHWdroiAnUsrxS+dc6Z2vtNtpnTO1w0/ZAy3kbY8W+rorZTNLXSvawAxqIMJRy6Fy64LFZWSMud8dJTBOjPNgb7RB7HFjQvGnA+EwLe2NV0dsZUqk17UbhVncEo+XU2DS2Fz+Gxh2V2/aIMhpmijprpMaztvCUjA7bHDMAGiEaUTBT+bFydUdBeLoX/O3dzYTykRTO1h0lknfx2iiXq2jzVt7A1MCDwH19Cb0PYtBbcC2j7mThgVzdlLvJCYVMHwzlupLn5BD1Ps1KCFoczZqvNdQR/MQZhVlDygWGKUODhsCXBVFGV9yc49SQ0YIKSQXe8pIyNpYeE5ZpN0q2hHLkVBzEC8zLWQ4amoRIdW24rrXRDNt5kd76Zqn0lT0tGCvc6to8gjiCok/XjNagJeebHra8IGQObZtXzjoM6BzAW29meAVw9D0d9Qg5kQDOAWQu7NWFdbGFxbYBNsQ/VhTKh8d+6kE2tP6G21XrIdtsnl3EbteEnOI4uHZQS9nBca9MSi3WD40cDXbuFWnUFoxQTEPCZhF4ozXQkbgCbcOAIWSIXS+37d7J0kxGeztXfBHWY73zX0YrWtqANjLJagw9gaKFyVmwK65vztLSSWPGXbnWXKjkVXuk9tVe7WgaV5cqtm1znz9VnzSN2cUUetLafGMYiuN5lUlE3WKHjYAZhmni9Kt0kp8u2BbCXTXJ+Wg7Af0sv6pvNRzqypLj15+okpcMdZJhtbwCgfbltrJj8Z3I6mZu1E6eyOnGUY6SoOic6n3K5l9xP8hs6l5c1fUaeUc6aX6qijvaykVqDKVBM0F4acYHJmEMx2yig4QFmq7Qht2SQMRymXCj3qS/oS9RyerNb+MgvzGmtTczJsRNVCrVvv786b7bL1ZaxkfI+7mpwpycemLIm55VLcga9TcrJcc0WfpQe7rXfKBlxs7mw6moQBaS7I3uGmdi5rLOdLzlqsuFSOaxOYSlBe/KF27eVAMi2YCZsZjmN7N6oOPrvK0dyrejdbXRfZsac9iXNO/R4cJnTnxBwsyudFZxppxw2TSF7KHCrV6nbK3mDeaWo+0TcWo/mMBkL3qmjRZn0IMuHYFyRZ10RDK/vLylllsI/coXLqM7e4w8+0IaI3DYc91iLAGUHHcHZ6FAmyPZQbAyg9xZu6N+TcdU+ttmSK3VCdjtfKnHS4wF9fbpUQzTjtIsShGSa7qMCmabfq4oIeguEQ7bzhFs2JTbZzgB81VNZXJtYTcBvNGqQ3wYhW9ln25dPLeJb9PJH+n76+Hg8G/5+dTz6OEt/eW90PpIHlfrnr+vI/tvCXTy+lE0L7Hie0VdL4zwPMfzif/fwXX36MwobH++Lx5Vtfv53y15Y//lfUS5i5TVWXw7cqT5r7gfGnF7upxv/LqL49D8Zf7ktOi/sp+5v+8fT9ubT76/23yfc3pSlwQ6sGz1v/eYINZw/Ql6FTfcPn5DdQFuPCn+9T4Hqx1+nr7OW3/wNjpatonSYAAA== -->
