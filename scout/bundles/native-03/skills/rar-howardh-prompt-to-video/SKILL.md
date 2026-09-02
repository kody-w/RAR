---
name: "rar-howardh-prompt-to-video"
description: "Renders videos from structured scene descriptions using Remotion \u2014 title, content, quote, and list scenes with style presets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/prompt_to_video_agent", "rar_sha256": "3bcdd845998ff84158cc2c2ab54fefcb54b0e3a6106fd4bfb8e59252b58694c6", "source_kind": "rar-agent", "source_commit": "fd516f31dfe3dc22441098daa43af4b5af84e047", "default_artifact": "skill", "canonical_format": "skill", "grail_record": true, "materializes": ["agent"], "backup_agent": "prompt_to_video_agent.py", "rollback_agent_retained": true, "rapp": {"schema": "rapp/1", "rappid": "rappid:@howardh/prompt-to-video:360e83c9863d8fdd6598a3cda1a1f53de2ff183cb600bfdbd4bcdf4ae2f0695a", "kind": "skill"}, "version": "1.1.0", "author": "RAPP Contributor", "tags": ["video", "remotion", "render", "mp4", "scenes", "presentation", "prompt_to_video"]}
---

## Microsoft Scout runtime

This Toasted `SKILL.md` is the default Grail projection of `@howardh/prompt_to_video_agent`. The
original RAPP agent is checksum-vaulted in the RCI capsule; `prompt_to_video_agent.py` is
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

PromptToVideo Agent — Renders videos from structured scene descriptions using Remotion.

Assimilated from:
- remotion-dev/remotion (React video framework — programmatic rendering)
- remotion-dev/template-prompt-to-video (story-to-video pipeline & timeline model)
- jhartquist/claude-remotion-kickstart (component patterns & composition factory)

The LLM breaks a user's prompt into scenes; this agent writes them into a
Remotion workspace and renders to MP4.  First run creates the workspace and
installs dependencies (~30s).  Subsequent renders reuse the workspace.

Scene types: title, content, quote, list
Style presets: bold (dark+red), minimal (light+blue), neon (dark+green), warm (dark+orange)

<!-- toaster:generated:begin -->

## Parameters

The typed contract this capability answers to (JSON Schema — the deterministic layer):

```json
{
  "properties": {
    "resolution": {
      "description": "Video resolution (default: 1080p)",
      "enum": [
        "1080p",
        "720p",
        "vertical",
        "square"
      ],
      "type": "string"
    },
    "scenes": {
      "description": "Ordered array of scene objects forming the video",
      "items": {
        "properties": {
          "accent_color": {
            "description": "Hex accent color",
            "type": "string"
          },
          "background_color": {
            "description": "Hex background color",
            "type": "string"
          },
          "duration_seconds": {
            "description": "Duration in seconds (default: 4 for title, 6 for others)",
            "type": "number"
          },
          "items": {
            "description": "Bullet items (for list scenes)",
            "items": {
              "type": "string"
            },
            "type": "array"
          },
          "subtitle": {
            "description": "Secondary text (subtitle/body/attribution)",
            "type": "string"
          },
          "text": {
            "description": "Primary text (title/heading/quote)",
            "type": "string"
          },
          "text_color": {
            "description": "Hex text color",
            "type": "string"
          },
          "type": {
            "description": "Scene layout type",
            "enum": [
              "title",
              "content",
              "quote",
              "list"
            ],
            "type": "string"
          }
        },
        "required": [
          "type",
          "text"
        ],
        "type": "object"
      },
      "type": "array"
    },
    "style": {
      "description": "Visual style preset (default: bold)",
      "enum": [
        "minimal",
        "bold",
        "neon",
        "warm"
      ],
      "type": "string"
    },
    "title": {
      "description": "Video title (used for filename and title scene)",
      "type": "string"
    }
  },
  "required": [
    "title",
    "scenes"
  ],
  "type": "object"
}
```

<!-- toaster:generated:end -->

<!-- toaster:generated:begin -->

## Run this — do not improvise

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prompt_to_video_agent.py` and embedded as the fenced Python below (sha256 3bcdd845998ff841…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prompt_to_video_agent.py` first:

```bash
python3 prompt_to_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prompt_to_video_agent.py   # or on stdin
python3 prompt_to_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
"""
PromptToVideo Agent — Renders videos from structured scene descriptions using Remotion.

Assimilated from:
- remotion-dev/remotion (React video framework — programmatic rendering)
- remotion-dev/template-prompt-to-video (story-to-video pipeline & timeline model)
- jhartquist/claude-remotion-kickstart (component patterns & composition factory)

The LLM breaks a user's prompt into scenes; this agent writes them into a
Remotion workspace and renders to MP4.  First run creates the workspace and
installs dependencies (~30s).  Subsequent renders reuse the workspace.

Scene types: title, content, quote, list
Style presets: bold (dark+red), minimal (light+blue), neon (dark+green), warm (dark+orange)
"""

# ═══════════════════════════════════════════════════════════════
# RAPP AGENT MANIFEST — Do not remove. Used by registry builder.
# ═══════════════════════════════════════════════════════════════
__manifest__ = {
    "schema": "rapp-agent/1.0",
    "name": "@howardh/prompt_to_video_agent",
    "version": "1.1.0",
    "display_name": "PromptToVideo",
    "description": "Renders videos from structured scene descriptions using Remotion — title, content, quote, and list scenes with style presets.",
    "author": "RAPP Contributor",
    "tags": ["video", "remotion", "render", "mp4", "scenes", "presentation", "prompt_to_video"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic_agent", "@howardh/markdown_to_slides_agent"],
}
# ═══════════════════════════════════════════════════════════════

import json
import os
import re
import subprocess

try:
    from openrappter.agents.basic_agent import BasicAgent
except ModuleNotFoundError:
    try:
        from basic_agent import BasicAgent
    except ModuleNotFoundError:
        from agents.basic_agent import BasicAgent

# ── Paths ────────────────────────────────────────────────────────────────────

_BRAINSTEM_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_WORKSPACE = os.path.join(_BRAINSTEM_DIR, ".brainstem_data", "remotion_workspace")
_VIDEOS_DIR = os.path.join(_BRAINSTEM_DIR, ".brainstem_data", "videos")
_WORKSPACE_VERSION = "2"

# ── Style & resolution presets ───────────────────────────────────────────────

_STYLES = {
    "bold": {
        "backgrounds": ["#1a1a2e", "#16213e", "#0f3460", "#533483", "#1a1a2e"],
        "text_color": "#ffffff",
        "accent_color": "#e94560",
    },
    "minimal": {
        "backgrounds": ["#ffffff", "#f8f9fa", "#e9ecef", "#dee2e6", "#f8f9fa"],
        "text_color": "#212529",
        "accent_color": "#0066cc",
    },
    "neon": {
        "backgrounds": ["#0a0a0a", "#0d0d1a", "#1a0a2e", "#0a1a2e", "#0d0d1a"],
        "text_color": "#ffffff",
        "accent_color": "#00ff88",
    },
    "warm": {
        "backgrounds": ["#2d1b00", "#3d2400", "#1a0f00", "#4a2d00", "#2d1b00"],
        "text_color": "#ffe4c4",
        "accent_color": "#ff6b35",
    },
}

_RESOLUTIONS = {
    "1080p": (1920, 1080),
    "720p": (1280, 720),
    "vertical": (1080, 1920),
    "square": (1080, 1080),
}

# ── Remotion project template files ──────────────────────────────────────────

_PACKAGE_JSON = """{
  "name": "brainstem-video",
  "private": true,
  "dependencies": {
    "@remotion/cli": "^4.0.0",
    "playwright": "^1.49.0",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "remotion": "^4.0.0"
  },
  "devDependencies": {
    "@types/react": "^18.3.3",
    "typescript": "^5.5.0"
  }
}"""

_TSCONFIG = """{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "jsx": "react-jsx",
    "strict": false,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "resolveJsonModule": true
  },
  "include": ["src"]
}"""

_INDEX_TS = """import {registerRoot} from 'remotion';
import {RemotionRoot} from './Root';
registerRoot(RemotionRoot);
"""

_ROOT_TSX = """import React from 'react';
import {Composition} from 'remotion';
import {Video} from './Video';
import {DemoVideo} from './DemoVideo';
import {timeline} from './data';

let demoCapture: any = null;
try { demoCapture = require('./demo_data').capture; } catch(e) {}

export const RemotionRoot: React.FC = () => {
  const totalFrames = timeline.scenes.reduce(
    (sum: number, s: any) => sum + s.durationFrames, 0
  );

  const demoFrames = demoCapture?.totalFrames || 300;
  const demoFps = demoCapture?.fps || 30;
  const demoW = demoCapture?.width || 1920;
  const demoH = demoCapture?.height || 1080;

  return (
    <>
      <Composition
        id="BrainstemVideo"
        component={Video}
        durationInFrames={totalFrames}
        fps={timeline.fps}
        width={timeline.width}
        height={timeline.height}
        defaultProps={{timeline}}
      />
      <Composition
        id="BrainstemDemo"
        component={DemoVideo}
        durationInFrames={demoFrames}
        fps={demoFps}
        width={demoW}
        height={demoH}
        defaultProps={{capture: demoCapture || {steps: [], viewport: {width: 1920, height: 1080}, fps: 30, width: 1920, height: 1080, totalFrames: 300, framesPerStep: 120, capturePrefix: ''}}}
      />
    </>
  );
};
"""

_VIDEO_TSX = r"""import React from 'react';
import {
  AbsoluteFill,
  Sequence,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  spring,
  Easing,
} from 'remotion';

/* ── Types ─────────────────────────────────────────────────────────────── */

interface Scene {
  type: 'title' | 'content' | 'quote' | 'list';
  text: string;
  subtitle?: string;
  items?: string[];
  durationFrames: number;
  backgroundColor: string;
  textColor: string;
  accentColor: string;
}

interface TimelineData {
  title: string;
  scenes: Scene[];
  fps: number;
  width: number;
  height: number;
}

/* ── Shared animation ──────────────────────────────────────────────────── */

const FadeIn: React.FC<{delay?: number; children: React.ReactNode}> = ({
  delay = 0,
  children,
}) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame - delay, [0, 15], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const y = interpolate(frame - delay, [0, 15], [30, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });
  return (
    <div style={{opacity, transform: `translateY(${y}px)`}}>{children}</div>
  );
};

const useExitOpacity = (durationFrames: number) => {
  const frame = useCurrentFrame();
  return interpolate(frame, [durationFrames - 15, durationFrames], [1, 0], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
};

/* ── Scene components ──────────────────────────────────────────────────── */

const TitleSlide: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const scale = spring({frame, fps, config: {damping: 100, stiffness: 200}});
  const subOp = interpolate(frame, [20, 40], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });
  const exitOp = useExitOpacity(scene.durationFrames);
  const lineW = interpolate(frame, [10, 40], [0, 200], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: scene.backgroundColor,
        justifyContent: 'center',
        alignItems: 'center',
        opacity: exitOp,
      }}
    >
      <div
        style={{
          transform: `scale(${scale})`,
          color: scene.textColor,
          fontSize: 80,
          fontWeight: 800,
          textAlign: 'center',
          padding: '0 100px',
          lineHeight: 1.2,
          fontFamily: 'Inter, Segoe UI, sans-serif',
        }}
      >
        {scene.text}
      </div>
      {scene.subtitle && (
        <div
          style={{
            opacity: subOp,
            color: scene.accentColor,
            fontSize: 36,
            marginTop: 30,
            fontFamily: 'Inter, Segoe UI, sans-serif',
            letterSpacing: 2,
          }}
        >
          {scene.subtitle}
        </div>
      )}
      <div
        style={{
          position: 'absolute',
          bottom: 100,
          width: lineW,
          height: 4,
          backgroundColor: scene.accentColor,
          borderRadius: 2,
        }}
      />
    </AbsoluteFill>
  );
};

const ContentSlide: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const exitOp = useExitOpacity(scene.durationFrames);
  const barH = interpolate(frame, [0, 20], [0, 200], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: scene.backgroundColor,
        justifyContent: 'center',
        padding: '0 140px',
        opacity: exitOp,
      }}
    >
      <FadeIn>
        <div
          style={{
            color: scene.accentColor,
            fontSize: 52,
            fontWeight: 700,
            marginBottom: 30,
            fontFamily: 'Inter, Segoe UI, sans-serif',
          }}
        >
          {scene.text}
        </div>
      </FadeIn>
      {scene.subtitle && (
        <FadeIn delay={10}>
          <div
            style={{
              color: scene.textColor,
              fontSize: 28,
              lineHeight: 1.6,
              fontFamily: 'Inter, Segoe UI, sans-serif',
              opacity: 0.9,
              maxWidth: 900,
            }}
          >
            {scene.subtitle}
          </div>
        </FadeIn>
      )}
      <div
        style={{
          position: 'absolute',
          left: 100,
          top: '30%',
          width: 6,
          height: barH,
          backgroundColor: scene.accentColor,
          borderRadius: 3,
        }}
      />
    </AbsoluteFill>
  );
};

const QuoteSlide: React.FC<{scene: Scene}> = ({scene}) => {
  const frame = useCurrentFrame();
  const exitOp = useExitOpacity(scene.durationFrames);
  const qOp = interpolate(frame, [0, 15], [0, 0.15], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: scene.backgroundColor,
        justifyContent: 'center',
        alignItems: 'center',
        opacity: exitOp,
      }}
    >
      <div
        style={{
          position: 'absolute',
          top: 150,
          left: 100,
          fontSize: 300,
          color: scene.accentColor,
          opacity: qOp,
          fontFamily: 'Georgia, serif',
          lineHeight: 1,
        }}
      >
        {'\u201C'}
      </div>
      <FadeIn>
        <div
          style={{
            color: scene.textColor,
            fontSize: 42,
            fontStyle: 'italic',
            textAlign: 'center',
            padding: '0 160px',
            lineHeight: 1.6,
            fontFamily: 'Georgia, Times New Roman, serif',
          }}
        >
          {scene.text}
        </div>
      </FadeIn>
      {scene.subtitle && (
        <FadeIn delay={15}>
          <div
            style={{
              color: scene.accentColor,
              fontSize: 24,
              marginTop: 40,
              fontFamily: 'Inter, Segoe UI, sans-serif',
            }}
          >
            {'\u2014'} {scene.subtitle}
          </div>
        </FadeIn>
      )}
    </AbsoluteFill>
  );
};

const ListSlide: React.FC<{scene: Scene}> = ({scene}) => {
  const exitOp = useExitOpacity(scene.durationFrames);
  const items = scene.items || [];

  return (
    <AbsoluteFill
      style={{
        backgroundColor: scene.backgroundColor,
        justifyContent: 'center',
        padding: '0 140px',
        opacity: exitOp,
      }}
    >
      <FadeIn>
        <div
          style={{
            color: scene.accentColor,
            fontSize: 48,
            fontWeight: 700,
            marginBottom: 50,
            fontFamily: 'Inter, Segoe UI, sans-serif',
          }}
        >
          {scene.text}
        </div>
      </FadeIn>
      {items.map((item, i) => (
        <FadeIn key={i} delay={15 + i * 12}>
          <div
            style={{
              color: scene.textColor,
              fontSize: 30,
              marginBottom: 22,
              display: 'flex',
              alignItems: 'center',
              fontFamily: 'Inter, Segoe UI, sans-serif',
            }}
          >
            <div
              style={{
                width: 12,
                height: 12,
                borderRadius: 6,
                backgroundColor: scene.accentColor,
                marginRight: 20,
                flexShrink: 0,
              }}
            />
            {item}
          </div>
        </FadeIn>
      ))}
    </AbsoluteFill>
  );
};

/* ── Main composition ──────────────────────────────────────────────────── */

export const Video: React.FC<{timeline: TimelineData}> = ({timeline}) => {
  let offset = 0;
  return (
    <AbsoluteFill>
      {timeline.scenes.map((scene, i) => {
        const from = offset;
        offset += scene.durationFrames;
        return (
          <Sequence key={i} from={from} durationInFrames={scene.durationFrames}>
            {scene.type === 'title' && <TitleSlide scene={scene} />}
            {scene.type === 'content' && <ContentSlide scene={scene} />}
            {scene.type === 'quote' && <QuoteSlide scene={scene} />}
            {scene.type === 'list' && <ListSlide scene={scene} />}
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
"""

_DEFAULT_DATA_TS = """export const timeline: any = {
  title: "Test",
  fps: 30,
  width: 1920,
  height: 1080,
  scenes: [
    {
      type: "title",
      text: "Hello World",
      subtitle: "Brainstem Video",
      durationFrames: 90,
      backgroundColor: "#1a1a2e",
      textColor: "#ffffff",
      accentColor: "#e94560",
    },
  ],
};
"""

_DEMO_VIDEO_STUB = """import React from 'react';
import {AbsoluteFill} from 'remotion';
export const DemoVideo: React.FC<{capture: any}> = () => (
  <AbsoluteFill style={{backgroundColor: '#000', justifyContent: 'center', alignItems: 'center'}}>
    <div style={{color: '#fff', fontSize: 40}}>No demo data loaded</div>
  </AbsoluteFill>
);
"""

# ── Helpers ──────────────────────────────────────────────────────────────

def _slugify(text):
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', text.lower()).strip('-')
    return slug[:60] or 'video'


def _node_available():
    for cmd in ('node', 'node.exe'):
        try:
            r = subprocess.run([cmd, '--version'], capture_output=True, timeout=10)
            if r.returncode == 0:
                return True
        except (FileNotFoundError, subprocess.TimeoutExpired):
            continue
    return False


def _run(cmd, cwd, timeout=300):
    """Run a shell command. Returns (ok, stdout, stderr)."""
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                           timeout=timeout, shell=True)
        return r.returncode == 0, r.stdout, r.stderr
    except subprocess.TimeoutExpired:
        return False, '', f'Command timed out after {timeout}s'
    except Exception as e:
        return False, '', str(e)


# ── Agent ────────────────────────────────────────────────────────────────

class PromptToVideoAgent(BasicAgent):
    def __init__(self):
        self.name = __manifest__["display_name"]
        self.metadata = {
            "name": self.name,
            "description": __manifest__["description"],
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Video title (used for filename and title scene)"
                    },
                    "scenes": {
                        "type": "array",
                        "description": "Ordered array of scene objects forming the video",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string",
                                    "enum": ["title", "content", "quote", "list"],
                                    "description": "Scene layout type"
                                },
                                "text": {
                                    "type": "string",
                                    "description": "Primary text (title/heading/quote)"
                                },
                                "subtitle": {
                                    "type": "string",
                                    "description": "Secondary text (subtitle/body/attribution)"
                                },
                                "items": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                    "description": "Bullet items (for list scenes)"
                                },
                                "duration_seconds": {
                                    "type": "number",
                                    "description": "Duration in seconds (default: 4 for title, 6 for others)"
                                },
                                "background_color": {
                                    "type": "string",
                                    "description": "Hex background color"
                                },
                                "text_color": {
                                    "type": "string",
                                    "description": "Hex text color"
                                },
                                "accent_color": {
                                    "type": "string",
                                    "description": "Hex accent color"
                                }
                            },
                            "required": ["type", "text"]
                        }
                    },
                    "style": {
                        "type": "string",
                        "enum": ["minimal", "bold", "neon", "warm"],
                        "description": "Visual style preset (default: bold)"
                    },
                    "resolution": {
                        "type": "string",
                        "enum": ["1080p", "720p", "vertical", "square"],
                        "description": "Video resolution (default: 1080p)"
                    }
                },
                "required": ["title", "scenes"]
            }
        }
        super().__init__(self.name, self.metadata)

    # ── Workspace management ─────────────────────────────────────────────

    def _workspace_version_path(self):
        return os.path.join(_WORKSPACE, ".workspace_version")

    def _workspace_current(self):
        vpath = self._workspace_version_path()
        if not os.path.isfile(vpath):
            return False
        try:
            with open(vpath, "r") as f:
                return f.read().strip() == _WORKSPACE_VERSION
        except OSError:
            return False

    def _ensure_workspace(self):
        """Create or update the Remotion workspace. Returns workspace path."""
        need_npm = not os.path.isdir(os.path.join(_WORKSPACE, "node_modules"))
        need_files = not self._workspace_current()

        if not need_npm and not need_files:
            return _WORKSPACE

        src_dir = os.path.join(_WORKSPACE, "src")
        os.makedirs(src_dir, exist_ok=True)

        if need_files:
            files = {
                "package.json": _PACKAGE_JSON,
                "tsconfig.json": _TSCONFIG,
                os.path.join("src", "index.ts"): _INDEX_TS,
                os.path.join("src", "Root.tsx"): _ROOT_TSX,
                os.path.join("src", "Video.tsx"): _VIDEO_TSX,
                os.path.join("src", "data.ts"): _DEFAULT_DATA_TS,
                os.path.join("src", "DemoVideo.tsx"): _DEMO_VIDEO_STUB,
            }
            for relpath, content in files.items():
                fpath = os.path.join(_WORKSPACE, relpath)
                os.makedirs(os.path.dirname(fpath), exist_ok=True)
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(content)
            with open(self._workspace_version_path(), "w") as f:
                f.write(_WORKSPACE_VERSION)

        if need_npm:
            ok, _out, err = _run("npm install --no-fund --no-audit",
                                 _WORKSPACE, timeout=120)
            if not ok:
                raise RuntimeError(f"npm install failed:\n{err[:600]}")

        return _WORKSPACE

    # ── Timeline builder ─────────────────────────────────────────────────

    def _build_timeline(self, title, scenes, style, resolution):
        preset = _STYLES.get(style, _STYLES["bold"])
        w, h = _RESOLUTIONS.get(resolution, _RESOLUTIONS["1080p"])
        fps = 30
        bgs = preset["backgrounds"]

        built = []
        for i, s in enumerate(scenes):
            stype = s.get("type", "content")
            default_dur = 4 if stype == "title" else 6
            dur_s = s.get("duration_seconds", default_dur)
            dur_frames = max(int(dur_s * fps), 30)

            built.append({
                "type": stype,
                "text": s.get("text", ""),
                "subtitle": s.get("subtitle", ""),
                "items": s.get("items", []),
                "durationFrames": dur_frames,
                "backgroundColor": s.get("background_color", bgs[i % len(bgs)]),
                "textColor": s.get("text_color", preset["text_color"]),
                "accentColor": s.get("accent_color", preset["accent_color"]),
            })

        return {"title": title, "fps": fps, "width": w, "height": h, "scenes": built}

    # ── Data writer ──────────────────────────────────────────────────────

    def _write_data(self, workspace, timeline):
        data_path = os.path.join(workspace, "src", "data.ts")
        json_str = json.dumps(timeline, indent=2, ensure_ascii=False)
        with open(data_path, "w", encoding="utf-8") as f:
            f.write(f"export const timeline: any = {json_str};\n")

    # ── Renderer ─────────────────────────────────────────────────────────

    def _render(self, workspace, slug):
        os.makedirs(_VIDEOS_DIR, exist_ok=True)
        out_path = os.path.join(_VIDEOS_DIR, f"{slug}.mp4")

        cmd = (
            f'npx remotion render src/index.ts BrainstemVideo '
            f'"{out_path}" --overwrite --log=error --port=9876'
        )
        ok, stdout, stderr = _run(cmd, workspace, timeout=300)
        if not ok:
            detail = (stderr or stdout)[-800:]
            raise RuntimeError(f"Render failed:\n{detail}")

        if not os.path.isfile(out_path):
            raise RuntimeError("Render command succeeded but output file not found.")

        return out_path

    # ── Main entry ───────────────────────────────────────────────────────

    def perform(self, title="Untitled", scenes=None, style="bold",
                resolution="1080p", **kwargs):
        if not _node_available():
            return (
                "Error: Node.js is required but not found on PATH. "
                "Install Node.js v18+ (https://nodejs.org) and try again."
            )

        if isinstance(scenes, str):
            try:
                scenes = json.loads(scenes)
            except json.JSONDecodeError:
                return "Error: 'scenes' must be a valid JSON array of scene objects."

        if not scenes or not isinstance(scenes, list):
            return "Error: At least one scene is required in the 'scenes' array."

        slug = _slugify(title)

        try:
            workspace = self._ensure_workspace()
        except RuntimeError as e:
            return f"Error setting up video workspace: {e}"

        timeline = self._build_timeline(title, scenes, style, resolution)
        self._write_data(workspace, timeline)

        total_frames = sum(s["durationFrames"] for s in timeline["scenes"])
        total_seconds = total_frames / timeline["fps"]

        try:
            out_path = self._render(workspace, slug)
        except RuntimeError as e:
            return str(e)

        return (
            f"RENDER_COMPLETE: Video rendered successfully!\n"
            f"VIDEO_URL: /videos/{slug}.mp4\n"
            f"Duration: {total_seconds:.1f}s ({total_frames} frames @ {timeline['fps']}fps)\n"
            f"Resolution: {timeline['width']}x{timeline['height']}\n"
            f"Scenes: {len(timeline['scenes'])}\n"
            f"Style: {style}\n\n"
            f"IMPORTANT: In your response, embed the video using exactly this markdown:\n"
            f"![video](/videos/{slug}.mp4)"
        )


if __name__ == "__main__":
    agent = PromptToVideoAgent()
    print(agent.perform())
```

<!-- toaster:generated:end -->

<!-- rci-capsule:v1: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 -->
