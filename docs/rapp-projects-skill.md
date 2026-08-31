# RAPP Projects skill quickstart

`rar-kody-w-rapp-projects` is a local-first project punch clock and handoff
board for any AI runtime. It records project history as an append-only,
hash-linked RAPP/1 chain, derives current status and board views, verifies the
chain and its receipts, and can create a portable project-specific egg.

## Data boundary

The root is selected from an explicit `"root"`, then `RAPP_PROJECTS_ROOT`, then
the default `~/.rapp/projects-control/`. Use an absolute custom root to create
a separate authority:

```json
{"operation":"board","root":"/absolute/path/to/projects-control"}
```

The selected root is the complete storage boundary. The skill does not search
other project roots, silently merge divergent histories, or send, publish,
sign, pay, or delete external resources. It makes no network calls and never
writes project state beside the agent. Artifact entries are references and
receipts, not copied bodies. A `handoff` document is hashed and recorded as a
receipt; its body is not copied into project state. External receipt paths are
kept only in a private locator file inside the selected project. Chains,
derived views, and eggs contain an opaque `local-private://` token instead of
the machine path. Locator files are never exported; after import, those
external receipts remain explicitly unverifiable until rebound locally.

Each project lives at `<root>/<slug>/`. Its `chain.jsonl`, `rappid.json`, and
`head.json` carry the authority; boards, status pages, indexes, and eggs are
derived projections that can be rebuilt from verified history.

## RAPP/1 project lifecycle

1. `open` creates the project genesis frame.
2. Each runtime `punchin`s before non-trivial work.
3. Append `status` whenever progress, location, artifacts, blockers, or the
   next action changes.
4. Use `handoff` when responsibility moves to another runtime.
5. `punchout` with `done`, `blocked`, or `abandoned` and supporting receipts.
6. `verify` checks the complete chain. Historical frames are never edited;
   corrections are new frames.
7. Use `board` for the cross-project view or `inspect` for one project.
8. `export` creates `<root>/<project>/PROJECT.egg` only after successful
   verification and explicit owner approval.
9. `import` verifies the complete egg before creating or fast-forwarding a
   project. Stale, malformed, or divergent history is refused without mutation.

## Operations

Requests are JSON objects. Supply `operation`, or use `action` as a
compatibility alias. If both are present, `operation` wins; omitting both is an
error. Project slugs use lowercase letters, numbers, and single hyphens.

### `protocol`

```json
{"operation":"protocol"}
```

### `open`

```json
{"operation":"open","project":"example-project","title":"Example project","goal":"Ship a verified result","owner":"project-owner","origin":"initial brief"}
```

### `punchin`

```json
{"operation":"punchin","project":"example-project","agent":"claude-code","runtime":"claude-code","session_id":"optional-session","location":"/absolute/worktree","intent":"Implement the next slice","role":"builder","capabilities":["files","shell","tests"]}
```

### `status`

`next_action` is required; `pct` is an integer from 0 through 100.

```json
{"operation":"status","project":"example-project","agent":"github-copilot-cli","location":"/absolute/worktree","status":"testing","artifacts":["build/report.json"],"blockers":[],"next_action":"Run the acceptance gate","pct":80,"project_state":"active"}
```

### `handoff`

`doc` must name an existing file. The skill records its content-addressed
receipt without copying its body.

```json
{"operation":"handoff","project":"example-project","from_agent":"claude-code","to_agent":"github-copilot-cli","doc":"/absolute/path/HANDOFF.md","open_questions":["Does the release gate pass?"]}
```

### `punchout`

```json
{"operation":"punchout","project":"example-project","agent":"github-copilot-cli","outcome":"done","summary":"Acceptance gate passed","receipts":["build/report.json"],"blockers":[]}
```

### `verify`

```json
{"operation":"verify","project":"example-project"}
```

### `board`

```json
{"operation":"board"}
```

### `inspect`

```json
{"operation":"inspect","project":"example-project"}
```

### `export`

```json
{"operation":"export","root":"/absolute/path/to/projects-control","project":"example-project","owner_approved":true}
```

This operation refuses to write without `owner_approved: true`, refuses an
unverified project, and writes only the selected project's `PROJECT.egg`.
The optional `output` compatibility field is accepted only when it resolves to
that exact path; arbitrary output paths are refused.
The egg is `local-private`: sharing it requires owner approval. Approval is per
export; installing or invoking the skill is not approval. Its deterministic
`rapp/1-egg` payload contains verified project metadata and chain projections,
never artifact bodies.

### `import`

```json
{"operation":"import","root":"/absolute/path/to/projects-control","egg":"/absolute/path/to/PROJECT.egg"}
```

Import verifies the full egg before creating or fast-forwarding a destination.
A malformed, stale, or divergent egg creates no destination and changes no
existing chain.

## Result envelope

Success returns `status: "ok"` and the canonical `operation`. Verification also
returns `verification_frame_hash`:

```json
{"status":"ok","operation":"verify","project":"example-project","verdict":"pass","verification_frame_hash":"<64-hex>"}
```

Errors keep details under `error`; verification failures may also include a
protocol `step`:

```json
{"status":"error","operation":"verify","error":{"code":"chain-verification","message":"verification failed","step":"<protocol-step>"}}
```

An authoritative append remains a success if only its disposable view rebuild
fails. In that case the result includes `view_refresh.status: "error"` with a
sanitized error record, so callers do not retry and duplicate the committed
frame.

## Use from Claude, Copilot, or Scout

- **Claude Code:** install or reference the skill, then ask: “Use
  `rar-kody-w-rapp-projects` to punch in to `example-project` and record this
  work.” Supply the JSON payload when exact fields matter.
- **GitHub Copilot CLI:** place the complete generated skill directory under
  `~/.copilot/skills/`, invoke `rar-kody-w-rapp-projects`, and pass one of the
  JSON objects above.
- **Microsoft Scout:** import the generated workflow, select
  `rar-kody-w-rapp-projects`, run its verified `scripts/run_agent.py` preflight,
  and send the operation JSON on stdin. If local execution is unavailable,
  route the canonical agent through the configured Brainstem.

All runtimes use the same operation names and RAPP/1 history. `agent` and
`runtime` are declarations, not an allowlist.

## Stable sources

- Generated bundle: `<GENERATED_BUNDLE_RAW_URL>`
- Stable workflow skill:
  <https://raw.githubusercontent.com/kody-w/RAR/main/scout/workflows/rar-kody-w-rapp-projects/skills/rar-kody-w-rapp-projects/SKILL.md>
- Canonical agent:
  <https://raw.githubusercontent.com/kody-w/RAR/main/agents/@kody-w/rapp_projects_agent.py>

Prefer the stable workflow URL for Scout imports. Generated bundle placement
may change when the catalog is rebuilt; the canonical agent URL is the
single-file implementation authority.
