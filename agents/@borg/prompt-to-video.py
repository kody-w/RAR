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
    "name": "@borg/prompt-to-video",
    "version": "1.0.0",
    "display_name": "PromptToVideo",
    "description": "Renders videos from structured scene descriptions using Remotion — title, content, quote, and list scenes with style presets.",
    "author": "RAPP Contributor",
    "tags": ["video", "remotion", "render", "mp4", "scenes", "presentation", "prompt-to-video"],
    "category": "productivity",
    "quality_tier": "community",
    "requires_env": [],
    "dependencies": ["@rapp/basic-agent"],
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