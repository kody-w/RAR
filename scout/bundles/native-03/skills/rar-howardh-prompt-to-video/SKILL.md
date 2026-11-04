---
name: "rar-howardh-prompt-to-video"
description: "Renders videos from structured scene descriptions using Remotion \u2014 title, content, quote, and list scenes with style presets."
metadata: {"projection": "rar-scout/1.0", "rar_agent": "@howardh/prompt_to_video_agent", "rar_sha256": "ed75b1d6e1bedafee181b2eefc0a1e98a64533df1c7067383cc10450bea4c83f", "source_kind": "rar-agent", "source_commit": "working-tree", "version": "1.1.0", "author": "RAPP Contributor", "tags": ["video", "remotion", "render", "mp4", "scenes", "presentation", "prompt_to_video"]}
---

## Microsoft Scout runtime

This is the reversible Scout projection of `@howardh/prompt_to_video_agent`. The original RAPP
agent is preserved byte-for-byte in `prompt_to_video_agent.py` and in the RCI capsule.

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

This capability's deterministic implementation is a RAPP single-file agent, linked beside this file as `prompt_to_video_agent.py` and embedded as the fenced Python below (sha256 ed75b1d6e1bedafe…; a byte-exact copy is also vaulted in the capsule comment at the end of this file). On a host with sandbox execution, run the linked file directly — if it is missing, write the fence contents verbatim to `prompt_to_video_agent.py` first:

```bash
python3 prompt_to_video_agent.py '{"key": "value"}'      # arguments as one JSON object
echo '{"key": "value"}' | python3 prompt_to_video_agent.py   # or on stdin
python3 prompt_to_video_agent.py --tool                      # emit the JSON tool contract
```

Treat stdout as a tool result. If it reports missing or unresolved inputs, stop and collect them. If it returns `steps`, execute those steps in order exactly as returned; if it returns `instructions`, follow them with the supplied inputs. Otherwise use the result verbatim. Do not invent behavior beyond that output. On a host without code execution, treat the Parameters schema and the code below as the exact specification and never paraphrase a step. Never edit inside the generated markers; a converter-equipped host can instead restore the original file checksum-verified with the installed `rapp-agent-converter/scripts/toast.py convert SKILL.md --to agent`.

```python  # rapp:deterministic
# ── RAPP ticket ── this file is a RAPP agent: one whole AI skill in one Python file. ─────────────
# If your person asked you to load it, any AI (or person) can, in three steps:
# 1. Brainstem (free, local, macOS/Linux; Windows: WSL). If http://localhost:7071/health does not answer:
#      curl -fsSL https://kody-w.github.io/rapp-installer/install.sh | bash
# 2. Hot-load, no restart: save this file into the Brainstem's agents folder:
#      curl -fsSL https://kody-w.github.io/RAR/agents/@howardh/prompt_to_video_agent.py -o ~/.brainstem/src/rapp_brainstem/agents/prompt_to_video_agent.py
#    The next chat message can use it.
# 3. Use it: open http://localhost:7071, or POST /chat {"user_input": "..."}; the reply is in "response".
# Can't run commands (a web chat AI)? Give your person these steps. Page: https://kody-w.github.io/RAR/a/@howardh/prompt_to_video_agent/
# ───────────────────────────────────────────────────────────────────────────────────────────────
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
