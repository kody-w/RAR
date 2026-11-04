---
name: "rar-cat-agent-skills-route-map-visualizer"
description: "Visualize routes and locations on a map. Accepts pre-ordered stops with coordinates from upstream connectors (Azure Maps, Bing Maps, Dataverse, CRM) plus optional road geometry, leg distances, and durations. Produces PNG, interactive HTML (Leaflet/OSM), GeoJSON, KML, deep links, and QR codes. Fully offline Python engine \u2014 road geometry rendered directly when provided, or OSRM used browser-side as\u2026"
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@cat-agent-skills/route_map_visualizer", "rar_sha256": "2f00ce5f28aaef338a2dcf9c25b34c562518cbee5d91d999961a8254e22a5115", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "3.0.2", "author": "Nazish Qasim", "tags": ["maps", "routing", "visualization", "openstreetmap", "python", "leaflet", "geojson", "kml"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@cat-agent-skills/route_map_visualizer`. The original RAPP
agent is preserved byte-for-byte in `route_map_visualizer_agent.py` and in the RCI capsule.

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

Route Map Visualizer — Visualize routes and locations on a map. Accepts pre-ordered stops with coordinates from upstream connectors (Azure Maps, Bing Maps, Dataverse, CRM) plus optional road geometry, leg distances, and durations. Produces PNG, interactive HTML (Leaflet/OSM), GeoJSON, KML, deep links, and QR codes. Fully offline Python engine — road geometry rendered directly when provided, or OSRM used browser-side as…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#route-map-visualizer
  Upstream author: Nazish Qasim
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

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
      "description": "What to apply this capability to.",
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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `route_map_visualizer_agent.py` and embedded as the fenced Python below (sha256 2f00ce5f28aaef33…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `route_map_visualizer_agent.py` first:

```bash
python3 route_map_visualizer_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 route_map_visualizer_agent.py   # or on stdin
python3 route_map_visualizer_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@cat-agent-skills/route_map_visualizer_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/route_map_visualizer_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@cat-agent-skills/route_map_visualizer/
# ───────────────────────────────────────────────────────────────────────────────────────────────
"""
Route Map Visualizer — Visualize routes and locations on a map. Accepts pre-ordered stops with coordinates from upstream connectors (Azure Maps, Bing Maps, Dataverse, CRM) plus optional road geometry, leg distances, and durations. Produces PNG, interactive HTML (Leaflet/OSM), GeoJSON, KML, deep links, and QR codes. Fully offline Python engine — road geometry rendered directly when provided, or OSRM used browser-side as…

AGGREGATED ENTRY. The content authority for this capability is the upstream
library; this file is the structured RAR container for it. It carries a
manifest, a version locked to upstream, a content hash, a provenance record and
a public feedback thread — none of which the upstream entry has on its own.

Nothing from upstream is reproduced here. What runs below is RAR's own method
for this shape of work — a general capability — generated from the metadata
we index. The upstream library remains the authority for its own instructions;
this agent is callable on its own terms and links home for the source.

  Source library : CAT Agent Skills (microsoft)
  Upstream entry : https://microsoft.github.io/cat-agent-skills/#route-map-visualizer
  Upstream author: Nazish Qasim
  Upstream version: 1.0.0
  Licence        : unverified (unverified — indexed, never republished)

Regenerated automatically by scripts/generate_aggregated_agents.py whenever the
upstream record changes, so this file and its source cannot silently diverge.
"""

__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": '@cat-agent-skills/route_map_visualizer',
    "version": '3.0.2',
    "display_name": 'Route Map Visualizer',
    "description": 'Visualize routes and locations on a map. Accepts pre-ordered stops with coordinates from upstream connectors (Azure Maps, Bing Maps, Dataverse, CRM) plus optional road geometry, leg distances, and durations. Produces PNG, interactive HTML (Leaflet/OSM), GeoJSON, KML, deep links, and QR codes. Fully offline Python engine — road geometry rendered directly when provided, or OSRM used browser-side as…',
    "author": 'Nazish Qasim',
    "tags": ['maps', 'routing', 'visualization', 'openstreetmap', 'python', 'leaflet', 'geojson', 'kml'],
    "category": 'devtools',
    "quality_tier": "frontier",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent"],
    # Provenance. `content_digest` fingerprints the upstream record; when it
    # moves, this file is regenerated. `--check` fails the build on drift.
    "source": {
        "aggregated": True,
        "source_id": 'cat-agent-skills',
        "source_name": 'CAT Agent Skills',
        "source_url": 'https://microsoft.github.io/cat-agent-skills/',
        "upstream_slug": 'route-map-visualizer',
        "upstream_url": 'https://microsoft.github.io/cat-agent-skills/#route-map-visualizer',
        "upstream_version": '1.0.0',
        "license": 'unverified',
        "license_verified": False,
        "content_digest": 'f6e86f5cfd0f8994',
    },
    # The platforms the upstream entry targets. First-class and queryable, not
    # buried in prose: this is what lets the registry answer "what can I launch
    # into Copilot Studio / Cowork / Scout", which is the whole reason an
    # agent.py container beats a bare skill entry for cross-platform reach.
    "platforms": ['Copilot Studio'],
}


try:
    from agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    class BasicAgent:
        def __init__(self, name, metadata):
            self.name = name
            self.metadata = metadata


# The toasted capability, generated by @kody-w/skill_toaster_agent. A licensed
# recipe entry carries the upstream recipe verbatim (with attribution) in
# _SPEC["recipe"]; a metadata-only entry carries RAR's own method for that shape
# of work. See the module docstring for which this is.
_SPEC = {'archetype': 'general', 'checks': ['The outcome is independently verifiable.', 'Assumptions are written down.', 'The result was checked against the original goal.'], 'confidence': 0.0, 'deliverable': 'A completed pass with the goal, the method, the result, and the assumptions it rests on.', 'operations': ['run', 'plan', 'checklist', 'describe'], 'params': {'subject': 'What to apply this capability to.'}, 'refined_by': 'rules', 'signals': [], 'steps': ['State the goal as an outcome someone else could verify without you.', 'List what you have and what is missing before starting.', 'Do the smallest version end to end, so unknowns surface while they are cheap.', 'Check the result against the goal as stated, not against what turned out to be convenient.', 'Record what would have to be true for this to be wrong.'], 'subject_label': 'task', 'verb': 'Run'}


class RouteMapVisualizer(BasicAgent):
    """Run agent, toasted from an aggregated upstream entry."""

    def __init__(self):
        self.name = 'RouteMapVisualizer'
        self.metadata = {
            "name": self.name,
            "display_name": __manifest__["display_name"],
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {'operation': {'description': 'What to do: run, plan, checklist, describe.', 'enum': ['run', 'plan', 'checklist', 'describe'], 'type': 'string'}, 'subject': {'description': 'What to apply this capability to.', 'type': 'string'}},
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

    # ── recipe entries: the upstream recipe, verbatim, deterministic ─────

    def _recipe_context(self, kwargs):
        extras = []
        subject = self._subject(kwargs)
        if subject:
            extras.append(f"subject: {subject}")
        for key in _SPEC["params"]:
            value = str(kwargs.get(key) or "").strip()
            if value:
                extras.append(f"{key}: {value}")
        return extras

    def _recipe_prompt(self, kwargs):
        r = _SPEC["recipe"]
        lines = [r["prompt"]]
        extras = self._recipe_context(kwargs)
        if extras:
            lines += ["", "Context supplied by the caller:"] + [f"- {e}" for e in extras]
        return lines

    def _recipe_attribution(self):
        src = __manifest__["source"]
        r = _SPEC["recipe"]
        who = ", ".join(r.get("authors") or []) or __manifest__["author"]
        return [
            f"Recipe: {__manifest__['display_name']} — by {who}, {src['source_name']} "
            f"({src['license']}). Source: {src['upstream_url']}",
        ]

    def _perform_recipe(self, op, kwargs):
        r = _SPEC["recipe"]
        ref = _SPEC.get("refinement") or {}
        if op == "prompt":
            return "\n".join(self._recipe_prompt(kwargs) + [""] + self._recipe_attribution())
        if op == "plan":
            lines = [f"Steps for {__manifest__['display_name']} on {r['platform']}:"]
            lines += [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "checklist":
            lines = ["Before you run it:"] + [f"  [ ] {p}" for p in r["prerequisites"]]
            if r.get("expected_output"):
                lines += ["", "Done when:", f"  [ ] {r['expected_output']}"]
            return "\n".join(lines + [""] + self._recipe_attribution())
        if op == "describe":
            lines = self._provenance()
            if ref.get("when_to_use"):
                lines += ["", f"When to use: {ref['when_to_use']}"]
            if ref.get("example_request"):
                lines += [f"Ask for it like: {ref['example_request']}"]
            if ref.get("inputs"):
                lines += ["", "It will ask you for:"] + [f"  - {i['name']}: {i['description']}" for i in ref["inputs"]]
            if r.get("business_value"):
                lines += ["", f"Why it matters: {r['business_value']}"]
            return "\n".join(lines)
        if op == "run":
            lines = [f"{__manifest__['display_name']} — run on {r['platform']}", ""]
            if r.get("what_it_does"):
                lines += [r["what_it_does"], ""]
            lines += [f"Prompt (paste into {r['platform']}):", ""] + self._recipe_prompt(kwargs) + [""]
            lines += ["Procedure:"] + [f"  {i}. {s}" for i, s in enumerate(r["steps"], 1)] + [""]
            lines += ["Acceptance checks:"] + [f"  [ ] {c}" for c in _SPEC["checks"]] + [""]
            lines += [f"Deliverable: {_SPEC['deliverable']}", ""]
            if r.get("tenant_caveat"):
                lines += [f"Verified upstream: {r['tenant_caveat']}", ""]
            return "\n".join(lines + self._recipe_attribution())
        return (
            f"Unknown operation {op!r}. Valid operations: "
            + ", ".join(_SPEC["operations"])
        )

    # ── entry point ─────────────────────────────────────────────────────

    def perform(self, **kwargs):
        """Run the toasted capability. Always returns a string."""
        op = str(kwargs.get("operation") or "run").strip().lower()
        subject = self._subject(kwargs)

        if _SPEC.get("recipe"):
            return self._perform_recipe(op, kwargs)

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
    print(RouteMapVisualizer().perform(operation="run"))
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1:H4sIAAAAAAAC/+16WZOjSLbmX2GiHyrrkhnsW7a12QBikRAIgSSEKtuq2EHsmyRUt/77OFJEZFXfqp47ZvMwD0OmZQLufvz4Wb7vOK5fX7xxSOvu5euL4d2zPoW2Xp+VL59fwqgPuqwZsroCjYesH70iu0dQV49D1ENeFUJFHXhzew/VFeRBpde8QnwQRM3QQ00Xfam7MOqiEOqHuumhazakUFCDl1nlzSLiri6hsemHLvJK0FJVUTDUXQ994u9jF0G61/SfISGrkrfbhTd4l6jro8+QaOk/Qk0xgqkfKnoFUMwLoSSqy2jops9QESVQmPWDVwURGDvrG47dU99XyOzqcAQNkGkon6GsGqLOC4bsEkHqTl9Dn9aRFxfRgGxs/cfPkBLVK3tjfIY0ff0ZCqOogYqsyt/Ebi2gPDDXKySPRTFBdRyD1ggyJ2DZCoqqZH76NuIoRv5RS6iLqqeJwqwDiweDr2lUAePVlyyMws9Q3UEb29KhsQed/K6+9lH3pQdtkNfPEnEauCq6eWVTRP3L15/++fklA/cvX399CQqvB69erNlhwIAfLuzAkMKrEtDWPFQEz03UxXVXgldhFENvT5/6qIg/Q//xH/nV65L+x6/fKujt+vYy/7HGChrSCBpqrx+AgoHXeH5WZMMEAqG4elMPVjiMHYgQD0RBB1z5+hz5XVLdQP+Y2z49J3lNouHTt5caqPDw1beXH2cjfHvpxvn+dZbSfPrxtaivUffpx+9y+tE/AxPOwoDWrz+/Pb+JBR2/d81i6GfblMS3uYDlsyYCwn+3vvl6qv4m7s0kPz87f6qbz9CfS57X8w+g7zN/fCD3z8UCG4CRL6/nOqs+vc0B3B5Vc8B++vGvxAZpFOQFiOv/ltyfnoLTyANh9unNJCCgZxf8E4Lf1vYh86+nbUDA/J+sBHR/n+7DUH8l++HZfxE9J1D/4cs/FfdnA+B/QD/95dr+3YDPUPztZREVAAE6zy+ir9CvjxD56Yfw+8sf/vkbEP2/FWPXYxc8JPxcelUWR/3w888//dA/Xv/wz59+eMe8n8eu+DOZf2bXxzx/sOBbr09/HAvm31d5VV8r6COHoF/r5n90v71CB5D/4ff3/Vfo95k4XzA0L+J90qcJfpeNPdD1d3b88eU3gDcVWM0YPJoBfvztb5CeBV3d1/EA2QEAHwg4eMjKaFZ+l2Y9BP7OqNFFM5hnwLBv/UD8zx6eNa5j6Jf/Cdjli5dE1fClz7Oi6JEH9wCjNj9fPsDsl1doB4TVXQZgFtCAxZvmt+oxbJ4I8BCAzMuMntMQfQE5/GW+AZAP/fJn4n5+jHxtpl8e2J49Ac4SlzO49WMRvc7LcGaUfiodeADib1EARD0IsYDirJgZB0xcF4BQhnnJjwW8oXwNgH+WDczydRb2yy+/+F6ffqueaExAT+IFyx2rD3WgL1/AUgCxJOnwDRBlWkM//PrbD9B/Qv9u1EP4PIcJuODN6EDDmcwgkERjCboBfwAPAoR4GP3X394MCsRUUQcBF2VxFj0Hz6QXhe/WtVX+C07RkB8BqwKLlk3dDTNbZ8MrtIyhD33BpHPTTAJp3Q+AQJuZ96pgAlI9sJwPS1b1APUg0voYMDjgvMesv/id91CxBNnsDb9AumgCyqkL8M+s5qMTGFxXGTD/h++f74GQ7oceEt5FvELGHHZQ43Vek3be2xyx9/QLoJr34UC4B1XR9Vs1M2o0m+qRA0/zgE7AMsGbS7/MPgdVQAkSPuzf53708WZi3D0IsvtW9W/x7XWzKwKA92DSZMzCGfX//hZSfVqPRfiwH9B0lvTmhfDNK48YfPD6XBlB35n9vcr4/+Xa/6vl2uw5XlEsSeF30gKSjJ3lPiMKWHSYI+9ZkIMaCgJp9USP73XVO3a+++FbVWQgPbrp78+ejzh86/OE5XHW1+Kth3yQBCBIZrmPHJ1zruvm7Pa+Ve9cBawEPYAZGAOEDEj4Oc/eJ5xb3zVNAWrNz9/rlkdMd+FsZ5CHUDP6BciROIpC3wtyoFU348ybbUHCRjPmXNMsSP+wKuCE2dxA/hyqGYhPwGePoDdqsEwQYX8MxmyuM5tnjIRQClz0CjkAKuZ06QE+gWJx7gOs8MNDFATcmdZAxQ8L96nXPJWpu/xdQe8tg4vfO+Ct7XtuP1SZtQdCvRDE/LfqOvNLGN2ejv1Q881VQNdyRqPHoD96+22p0O859e/fqoeKH5QGQK6Yy5Hf2QYCCVG+Zfkc6QBny+gtfkAgPCqP12fx8KxOPnT5Con8DuKfgP5gWehT+c7fD6rf/9EpX6F0GJr+K4J8dHtNAFaM/mtWI/+Fsv/2AKAvAGy+fCfZP4h9WuAr9Pv95x86vAXjVwh7RV/RuWmdBdEcbW/XV2isPhDy0+/u33z18MWcntUD+kGozHHZp1H4KKis6LszgTJ1CVBntvEESoYPVn3vAqg16aJk7vxk2X4m5xkGHrKBub9VHw5/ywbAWlUyo1pf/y5LH+UFcN/TOx/sB5qqGVnCuepMotd5szYvt49evlYAsD6/VF4Z/dW+bqY1EIfAYvMWEKQEqNyGLHo8fVRx88Mft/ePZAFZHtZf55z5DM0V92foo3ieUfS5nZn1iaoR7BR/mgv3eUrQFfz30ffj24EfvYDt6DA1s7bP3d9cL77V8X+thNc0xfRfgG+o56n/RRoQ10XtCNA4nBX6vsLvE9fP2X57KDo8N7m/vrzn6puV3spO0B0kxZd+ZmEERBuYEDw//Qza/nsF6dsggCigOAKj8BhFg4iKcdbzopggWA8Pg5gLcMonyICicQpjAz+KqJDDQg5cNOaxOEVGOO5RGEYBec8Q+XmuL7JZkRmkwPq/gCiLvjeDV+HbCp4az+b5qH/nlb4t5NcXnyZBT5Xsl/zzEhEY82hi7d/SI3ymY/d65pZDuqsbNaL91nTP48WRscOUw2WtCq5UZNtMkgRcpt3T4YSy1gpOF5Rb0cd4s855XhD3VBnQOUrUqFwfQ/N4wY9r5l5t93GmIAi8xeCbWTX4Kb/ax22xi4/LTtCHIs9b4UirYe6ReVOesvO0c7vLRj/u6C1w9ErC5Pyi7noKO1G3/CJSU7IhYFaA1/J+vE/7uhC1mihqn7b1HWqt0rBRezfTHd06nS+eT6VHFnUzsdNvvkM4dt6mZ/uOypslLPZ2peXXyTSyJWmtzi6Zra7VtjdKFaXK9aT3lcaRiCSjuUNhPScfuOAiXOVGP3qlsqTLeJGHHmNwq8CMkco6icQC025yJfVDP9x4icEPWeVnMaY0+0qZMCG4RD6uJFrPEg3WJ9ghw8Z9ZpvaSgQlRbrYaihmt1nc7+n1kRyxTIoS7KRe44xjcqqON5vexbZSpe/vGrEImXVzTm6O7oyUCRu8w3LJtmEUlT6f4KiibhodxYImU/UWqRjhyO13RXNS77vDWScmh14YZu7RVWmKOqDSZS4jsCssB+3sFo5kceilQvKVwbY3vGPkLNYotT/X1aG+Saf2fFSnXkywRYmKO3NoliajxxOviFSFjXjfS6Jc+RMTZUm5Hi9uutXxXSdmhnk7wBK/g+/2Bq9XK3lsTdJK7lSvRtYJ6+jB2Ox0oXfroNEtsygl3LvJvbH1N0exrWLavWwZdjcJR6q5iZTqpY6U3NsFzPH0neDMTJpS9I7vaAK532IDIe59MZHFAQQE14GbywWpwKoQ4ZY702mhnpN9lfiowvPYteYrybP8FS+nB60at1q23e7RzL0Mxln0yUQypWnKpW1/8Enr5ClGPkrKEsvLJaV3ll41GH3IjNhy41WTa0h885xse8vrRdbQweXWrpYZfgv3UpuK+Z5ns+G0pi1rRPlDtSzIZNdU6ME+Y1U8ypZzRG1nGnWbh9c9d9yI5mQcFCHXbgOMxPHBXsiIFqwKTSeKO+uAnOu5AqmjtUEjKlnDl2NNyWtln6KZzQTlGgl5pnCvZVNR+ybI5Hh9lj2eqfTDZXt0fKVYnpdVj3griXR2LnzAzy5Yp0mOmXPUN/G5JC/Xw8phezmprxrnrG7peYuEwwUZD1TDwnF155j40uH4wbwx5tFnGVY68+K1kSQ8Wy8kJKtvG1T0+pE/pnuHtOUVnXZsHdsXJsJz8SYrjAXjmXXQr7V70+1TnZFYwtZ8KWydpaCNS5kXw73WKld2tagnS7uKXL8MUr/fubKIbTPXwTG1ppzIw3kC2aNqcasokQZrEsP8uEXMCXU8S1k2J/+6rKdxPKz5s7Kzz0mTX1w/yZ0u3vDMZne2FT85G4K18f21KbLYvdqkZNoKN24jptNdt5S14V/tTGSXzVKInOyWlyXXLGoScSWVPwwJzpXdgq4OriNhUxg4bXrk0fNyx/tCFgrj7ZwQmCtgSw/tl+41woZ2t5PZDsNOGh6xVwwlZMEiF4eBYeqFmNUnSsQ1Ng+ilvW3mnGmPFAOkEbEbbe7LB43drldeZ2g+OvinkQbYVopErq0GdKlieVhcaVie9g48VJOaNL1m9WS2jVxmaolwoBq84wvMUb3NirJkzzrniSS18SQERROG9wozoY4xa5Vi1CcWDmTR07MtWn524LcqIpanqzVUpwQ3M/O60Wl2KcrTyxuZThJ6gjCHN5FEi1st0qN3ZdgZ0BThNmbzrj1l3x9CrPA2dDSudgu2NWw3xeb6JBno+eLI9Y0K9MJaNt1Nheuk9bRaaf4ksM3saGsGm0xKUdnie2sbG80C8WRlLvC2zSRgMS4+nf6ElQ8LJOIPOyDiqsc1LpYW9ZxQW3Y6K5AIb4e3QNRv226NN5YOHkImO1gipVuHlXsqCc+pSgjkReDB18xdVMMp3HHIpzNsnpnnJzON2iroNrTgcS9QNvfwnPJR4iVrHk/3xrZ3iy89Ip5qYBu4clCbHfhcpqZ6JxYYnKrmBtdOeJnmsNbe1GG/epqC8cxbK1VJ7MnZMlip71z5CT4dA6IzLaMOE5gkuXGo15e7CIV7jgY3tkh5shuvnImUXX06jLGe22lo3Ke5wEWESjGbRcU1tj1NiYMzBfIypbvdwPf9nqRHLRWHuvC2flLEun7k3kWNnhi38kBOxCYRZW9bq7E05IY63WtS+Vwl5xTs5CK7fWe851CbALmym8Ow70Yj5glShTOHbQgZvTdgFTDYluvLkTCblaH3Ym4+lylgd1TeSmE3mD3e67ou8GYLACEdr6+JCM8saTB2DjLq0PkUK29B7BRijC2tntYinaOUp5guXVouhEwfaV0lIiU3XG6IWpGnFN2iJG4O5qELvp04640l+8WTo2nl/BGqlveg/NlcFsWC7faW00r0k1cHNZDJsjbDrvJJL3aH/hkZyWRwdWXs3TmfDI3ljZMeJd0v11wq2E5cazanhyWPCyvd22N5WQ0cI3JZqvV3pfGnZBX4+mc8NYGbLmypasWCCNkgUvdcTexVHI16nepbCPY5XiMWKLGwpiypZQZgy+rQ1mfQU1BYHbp+pLljEdt7XCKxnh4qi4JNYuEu7yrekK+UseLkLbLk2zmU52atCVXyRTHe3Rvd9cF2W53O0S8XnokO+1bvl3rpRd3XOJcAFHk/c0i4LBWXHPYT8eAL23/cNtdORleX/CztlWN7VKpjmS0wPYrvd2UBcUVV/1Y1lmw6MuoJLf7QTgt6Nsl9qTdriVQ+rIWKqk9CndV4sOlzQpsFzrduuXX0Xm70H2WhxVEyrXh7i1vmpwdDslNzoTVupTx2KyKOx12NRKhVkFkBZyXQe1EKDcW96A/uNLyaNxE1epNgT/ui9a7H0krsCjBcEix16xW3Z2XPAljS8NFReHAY/BV25xSW3WW445wlvUhMTV1sSySc5yBkoEghb3hbtsO4LPdwnzRYO3RIbUJl2rAAwnTp6i33MCp6LGUd7dBuktyga59VM8D9khs1SvPqug+EsTtwaJLfrs84OPupLdKazm1eGZPe0k2s4TZ3tsjpWETK0tpLIp1jQxneLWcqnObKIIYBGOP5up0j0jUSeoqzeA9qF7lLsmYKtngVzOUingy9FtrkxIVTA6xVtjUifrssFEUrAAd1hUpNbZkbJyNiGdCn1yY0Bqc/BotlGl5kJK9k6rtrb7vNbV0xvqkH9a6QaM8xSaspR2tVAqPWKTyQdUyeMlaCJYLy3qxGA+tVoFSFvNF36yDujXhdF31Qros6KYbczYXEWmnrZvVoHlbJ08kOT7qtb1ur+gY492gXDxlbaNZg5faKdjD+hG9ExN8bbd3kadOYavsXSlht0qv7lRpa9yTi2dfAV/jS+/u5LJdHda7Mc69cIFs8FY7pAixFNY7JslY/aq4tl3SdlySjHSimdPJvHoRFoSrcIopLqlwQuhlF1dXKEHhCXrad7DuKbB7oVVOi0CFKGWpRjpilw/8xoyM63Fh7mp6kgwzQfdOogdYKBfbpg8Ol6jcX1yBqQ9U7ztCI6GBmnK1flE2bjRgIqE1TNs7Bs5uwrA9n+oDjgt4HBYeUbbrzVUPT+HtViqVHNHWNu6C7RJ3+4CC2T5WWYqH9yGusKPSIVFzLyofX7en8SjBjT3udEuyEZld8Op+Mi4odS0txz+Tui7WwdAvjM2aV8+t2ap8ZKuNRJi70/WyX+vIXhgSj74p03DhEnnnXpqrvN5md/akbKhUqUadYNqj5bQnVEaYOJQv4bQwKzkI067zk6prLZ/cBgeWv6P6mDKwJyJxhd8DzY3yJGuR66oT79MGbPOOp8wptOGKD7y2uAucuJLOdClz8c3emuQlbdf73gnbAwpQREOLqydF3L3XnYQXWHSvMcG9MhS2vpErOQtre+/ELTIdVzf/WBjCraiM2zaxtm2LHEZkhBG7u7k3r6dGaaOxjOY1khpoDMl5Sq5rh4i/TaUScxbh9/XRrVCcodpVc77BazyP1KI1uZye9ghWIbiiS5Ni7ydb6nmw1VxQFEySMD105l3B3QyUxkwXhG64rMRhXOudSgyXxZUxtDY8MBU/xbp3Y6Q7Dke3EblKOJLsSQnp6TZHpDtrFegA9r9jkK0wCWOFzU2/Mv3lplMnRbenfVorwWZCh5GvZOOgn1e7wGe9Gi94cnNieS7UFsKZ7+zV+Vart7wim0H2yCG9LWrl3tB8j+z0Ft4ze5KBncWNgxGQRYLpLvZkKWlOKB6IbvSX9+w6slaT9KjY9/mmaZLtPlKdXbh3TK7cFsdDg/Y2Yd7WBEeSbNpr+HWPxmrQnMYlHVTeRsmK8oS0d2en1zQynnlUy5a1dRxZmvEo4uT6Ke2fhmDgXKPsbVFSYrI7m4J0UPTzrlPoc3dFevvcE4vG5IrjcWT0pjuqXIo6hakzE+kz9/YUoUqK41l32fkbRHQKP3eUGo2DuyrjON+hEcNXd7EWl1mxJnQcDxRB5mErZUs7PvWCOylVQQDGStsD4xpXTvdHdIORiZqaPgwnqGpiZyce8qk7BVjHWuPxEHG7VAnh9cJcUCEOiqzm4gmc7y1NWvCQkeaVUDfijl4clbUfDgYbe+YlRCjmcllq42URo+o29GwmrpfFPR8aQzA2QnNuvUucVBVR+Zg17FN3sNDuKAl8W7OMf2EUIzqqrL2gT3tf0yT8qjFnU29HRKTkS7lMDielVeTCzKNW5hxG7mw3bTdTdRocbk2bJBlL4gnnE9ZzSa/gZM3Q4OJeS+7x2DhTKbH7COzgopAg+yumT5Y/1jUhruFtYYUZyoykIKtTw+36o3TjKKxFcbTEaep+3jDCvij2Q1mE7n2NeCMCKqs+rDTZ53WOutElWd8Wtnhfu0za0fXK7K/ceRGUFqh7BlM7w0I05fDFMgaHOsRaVpv3oR6ZyzrjccPcnrb+YHtogWtSb3gado8NXK/X1GU52kN/O1z2dMziwR6rBZpbL7R9fKOOG3ewXWyLuyg99K5q3C8iDnDVCiVzUQQMIfhVXXThrqzt7IpZCe6rmoMsIsZfdUwrbqrBcPsdEqL6XjbXLuZfTeZIpJVN2Abs2uh0dAp3X/U5syWZHL+WoaKV/rQx8LDLC4LUKxQJTHZYAfBE6dRYbqbzhB1R/IBbgCzDy4JJMUvemIh9Gg7cnVN3iicb7hndRgd+V8yfGNRy1cBHZ6A4pD0igo+HTcS2aDhePDSj1MU2VwWaGU8HVr2tD+XJ6GiTCLuwH5CDwVFeooNS8oATTk6syeJIEXV0P+OpJftRrjtusdF0gMziYrU/R9ZEyqthqljU5w7lwTrdYEldeQN8zv2gNiL8QoGyh8FjUj0UWcIJPPB1USvDenQQnQv2O3SsSWHAz64seGq23Cqhi5wSjd42bHXKmTjqmJCXzjUGap46TEtidb2tl0O6PcUplx46i0YsTOnAxmKIQOGsAMwB5LoPb24k0CnKxGt4A1d+aiNIg+SEexmH/pLSzJWAlVoHNQQihosNolMB3DGUcLB0XgmkQUHIkxrEOpxscmfBjFx1xE+rTbP2CCWU72BvZhCVe+okGI6X/d0/ekfvfh8XDCgI+gthEuTQwtWEX+/1GSmTobuxQSDFl9v5ytWleuFOKtgXX+PMMHBlA+PsVubkXmN38Abbrdwl3xoXyjDIEufpJakVY1IvUYJb+wnRE+EeZz1OFlc1fT72XaWVmZ8vvLpVY6SuJslaeF1Aw6TL3OutzCA35+qTsU+EYO/M+YutS3SASNVq6NIjdVGyoB7z+o5FDFayONqVsSWA7eEogQ1bc0AX/iLBypQgDCTqACVtYlOq1W5co4fDmcyuNCiHNlRwaxDbQVz2dqJlecfv9QH2ZQOlTNRX3NUxjZcYz/P/ePn8Mp9SvJ01/NtfSsxfoP+vfex+frN+P098nDJEXvj1MdfXf6/GPz+/dEEGlHh+ue+BM94+h//rd/svf3YoNQ+Znr8ymM83b8P7ecvgJfNP615A937+uA/GzocPn1/exz6PHD7Pxw/zuV0UDaDrfDLy/uu64nk8De6SqD73j3d5Wcwavx1uAUWJV/QVf/ntfwEqFfdjkikAAA== -->
