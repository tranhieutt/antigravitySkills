---
name: understand-html-dashboard
description: Analyze a codebase and generate a self-contained interactive HTML architecture dashboard. Works without Vite/npm — uses a Python HTTP server. Covers 4 tabs: Overview, Dependency Graph, Guided Tour, Issues. Use when the user asks to "open understand dashboard", "xem architecture map", "analyze codebase và tạo dashboard", or "understand-dashboard" fails due to missing Vite packages.
argument-hint: [project-path]
---

# /understand-html-dashboard

Generate and serve a fully interactive HTML architecture dashboard for any codebase — no npm/Vite required. Produces a dark-themed, GitHub-style dashboard with 4 tabs: Overview, Dependency Graph, Guided Tour, and Issues.

This skill is the **self-contained fallback** for `understand-dashboard` when the Vite app packages are not installed.

---

## Phase 0 — Pre-flight

1. **Determine project directory:**
   - If `$ARGUMENTS` contains a path → use it as `$PROJECT_ROOT`
   - Otherwise → use the current working directory

2. **Get git commit hash** (for cache invalidation):

   ```bash
   git -C "$PROJECT_ROOT" rev-parse HEAD
   ```

   Store as `$GIT_HASH` (first 7 chars for display).

3. **Check existing graph:**
   If `$PROJECT_ROOT/.understand-anything/knowledge-graph.json` exists AND `meta.json.gitCommitHash` matches current hash → graph is up to date, skip to Phase 3 (Dashboard Generation).

4. **Create output directory:**

   ```powershell
   New-Item -ItemType Directory -Force -Path "$PROJECT_ROOT/.understand-anything/intermediate"
   ```

   On Linux/macOS: `mkdir -p "$PROJECT_ROOT/.understand-anything/intermediate"`

---

## Phase 1 — Codebase Scan

Explore the project structure thoroughly using these tools in parallel:

1. `list_dir` on `$PROJECT_ROOT` (depth 2-3)
2. Read `README.md` (first 3000 chars) — store as `$README`
3. Read `package.json` / `pyproject.toml` / `Cargo.toml` / `go.mod` — store as `$MANIFEST`
4. `find_by_name` for all `.tsx`, `.ts`, `.py`, `.go`, `.rs` source files (exclude `node_modules`, `.git`, `dist`, `.next`)

**Collect per-file:**

- `filePath` (relative to project root)
- `sizeLines` (estimated from file size)
- `role` (route, lib, config, types, test, style)

**Detect:**

- Framework: Next.js (has `next.config.*`), React, Vue, Django, FastAPI, Go, Rust...
- Language(s): TypeScript/TSX, Python, Go, etc.
- Entry points: `app/page.tsx`, `src/main.ts`, `main.py`, `cmd/main.go`, etc.

**Gate:** If > 200 source files, inform user and suggest scoping with a subdirectory. Wait for confirmation before continuing.

---

## Phase 2 — Deep File Analysis

Read and analyze each source file (batch 5-10 files at a time for large projects):

For each file, extract:

```json
{
  "id": "file:<relative-path>",
  "name": "<filename>",
  "filePath": "<relative-path>",
  "type": "file",
  "summary": "<1-2 sentence description of what this file does>",
  "tags": ["<role>", "<framework-concept>"],
  "sizeLines": <number>,
  "exports": ["<exported function/class names>"],
  "imports": ["<imported local file paths>"]
}
```

Also extract **classes and interfaces** (type: `class`) and **key functions** (type: `function`) where significant.

**Concepts:** Create `concept:` nodes for architectural patterns (e.g., `concept:three-portals`, `concept:supabase-tables`, `concept:auth-layer`).

---

## Phase 3 — Build Knowledge Graph JSON

Assemble `knowledge-graph.json` with this schema:

```json
{
  "version": "1.0.0",
  "project": {
    "name": "<project name from README/manifest>",
    "languages": ["<languages>"],
    "frameworks": ["<frameworks>"],
    "description": "<1-2 sentence description>",
    "analyzedAt": "<ISO 8601 timestamp>",
    "gitCommitHash": "<full hash>"
  },
  "nodes": [<GraphNode objects>],
  "edges": [<GraphEdge objects>],
  "layers": [<ArchLayer objects>],
  "tour": [<TourStep objects>]
}
```

### Node schema

```json
{
  "id": "file:app/page.tsx",
  "name": "page.tsx",
  "filePath": "app/page.tsx",
  "type": "file | class | function | module | concept",
  "summary": "...",
  "tags": ["route", "admin", "use-client"],
  "sizeLines": 120
}
```

### Edge schema

```json
{
  "source": "file:app/admin/page.tsx",
  "target": "file:src/lib/supabase.ts",
  "type": "imports | exports | calls | depends_on | related | contains",
  "weight": 0.7,
  "label": "optional human-readable label"
}
```

### Layer schema (group nodes by architectural concern)

```json
{
  "id": "layer:routing-pages",
  "name": "📄 Pages & Routes",
  "description": "What belongs here",
  "nodeIds": ["file:app/page.tsx", "file:app/admin/page.tsx"]
}
```

### Tour step schema (8-10 progressive steps)

```json
{
  "order": 1,
  "title": "🏠 Entry Point",
  "description": "Detailed explanation for a newcomer...",
  "nodeIds": ["file:app/page.tsx"]
}
```

**Write to:** `$PROJECT_ROOT/.understand-anything/knowledge-graph.json`

**Write metadata to:** `$PROJECT_ROOT/.understand-anything/meta.json`:

```json
{
  "lastAnalyzedAt": "<ISO 8601>",
  "gitCommitHash": "<hash>",
  "version": "1.0.0",
  "analyzedFiles": <number>
}
```

---

## Phase 4 — Generate HTML Dashboard

Create `$PROJECT_ROOT/.understand-anything/dashboard.html` — a fully self-contained HTML file with inline CSS and JS. No external dependencies.

### Dashboard Structure

The HTML must include **4 tabs** via JavaScript tab switching:

#### 1. 📊 Overview Tab

- **Header:** Project name, description, git hash badge, analysis date
- **Stats Grid:** 4 cards — Files Analyzed, Graph Nodes, Edges, Arch Layers (colored numbers)
- **Architecture Cards:** 2x2 grid of `arch-card` divs, one per major layer or concern:
  - Each card has a list of clickable `node-item` rows with: icon emoji, `node-name`, `node-summary`, `node-tags` badges
  - Tag color classes: `tag-route` (green), `tag-lib` (blue), `tag-type` (purple), `tag-static` (red for problems), `tag-mobile` (orange)
  - Include a **"Gaps & Missing Pieces"** card with red border, listing missing auth, empty dirs, known bugs

#### 2. 🕸️ Dependency Graph Tab

- SVG diagram (viewBox `0 0 900 480`) showing:
  - **Rounded rect nodes** — color-coded by type (admin=green border, lib=blue, types=purple, student/broken=red, concept=yellow)
  - **Path edges** — blue solid for `import`, green dashed for `related/link`
  - **Labels** inside rects: emoji + filename + sublabel (role)
  - **Legend** bottom-left: color boxes with labels
- Layout: Entry point top-left → pages middle → lib/types bottom-right
- Include `<rect class="dep-node <type>">` and `<text class="dep-label">` elements
- Use `<path class="dep-edge import|related" d="M x1 y1 L x2 y2"/>` for connections

#### 3. 🗺️ Guided Tour Tab

- Vertical timeline with 8-10 steps
- Each step: numbered circle on left rail + title + description + `file-chip` spans
- Step 1 always starts at entry point
- Last step highlights the weakest module (needs improvement)
- Active step (first) has green circle, rest are grey

#### 4. ⚠️ Issues Tab

- List of `issue-card` divs with: icon emoji, title, description, severity badge
- Severity: `sev-high` (red), `sev-med` (yellow), `sev-low` (green)
- Common issues to detect and report:
  - No authentication / unprotected routes
  - Hardcoded data (hardcoded dates, names, numbers in UI)
  - Static pages that should be dynamic
  - Empty directories (`src/components/`, etc.)
  - FKs not saved (inconsistent between form and DB)
  - Teacher/user names hardcoded in JSX
  - Missing error boundaries

### Sidebar (persistent, left of main content)

- **Layers section** — clickable items with colored dot, layer name, count badge
- **Tech Stack section** — framework/language list with colored dots
- **Database Tables section** — list of detected tables/models
- **Key Portals/Modules** — top-level routes or modules

### Design System (inline CSS variables)

```css
:root {
  --bg: #0d1117;      /* GitHub dark background */
  --bg2: #161b22;     /* Cards and panels */
  --bg3: #1c2128;     /* Input/input backgrounds */
  --border: #30363d;  /* Borders */
  --text: #e6edf3;    /* Primary text */
  --muted: #7d8590;   /* Secondary text */
  --green: #3fb950;   /* Success/active/admin */
  --blue: #58a6ff;    /* Import edges/lib */
  --purple: #bc8cff;  /* Types/interfaces */
  --orange: #ffa657;  /* Teacher/mobile */
  --red: #f85149;     /* Error/missing/static-problems */
  --yellow: #e3b341;  /* Concepts/warnings */
}
```

Use `font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`.

### JavaScript

```javascript
function showTab(name) {
  ['overview','graph','tour','issues'].forEach(t => {
    document.getElementById('tab-' + t).style.display = t === name ? 'block' : 'none';
  });
  document.querySelectorAll('.tab').forEach((tab, i) => {
    tab.classList.toggle('active', ['overview','graph','tour','issues'][i] === name);
  });
}
function selectNode(el) {
  document.querySelectorAll('.node-item').forEach(n => n.classList.remove('selected'));
  el.classList.add('selected');
}
// Initialize
showTab('overview');
```

---

## Phase 5 — Serve & Open

Start a Python HTTP server to serve the dashboard:

**Windows (PowerShell):**

```powershell
Start-Process python -ArgumentList "-m http.server 8787 --directory `"$PROJECT_ROOT/.understand-anything`"" -WindowStyle Hidden
Start-Sleep 2
```

**Linux/macOS (bash):**

```bash
python3 -m http.server 8787 --directory "$PROJECT_ROOT/.understand-anything" &
sleep 2
```

Pick port 8787 by default. If busy, try 8788, 8789.

Report to the user:

```
✅ Dashboard generated at:
   http://localhost:8787/dashboard.html

📁 Files created:
   · $PROJECT_ROOT/.understand-anything/knowledge-graph.json
   · $PROJECT_ROOT/.understand-anything/meta.json
   · $PROJECT_ROOT/.understand-anything/dashboard.html

📊 Analysis summary:
   · <N> files analyzed
   · <M> graph nodes, <K> edges
   · <L> architectural layers
   · <I> issues detected (<H> high, <Med> medium, <Lo> low)
```

Use `browser_subagent` to open `http://localhost:8787/dashboard.html` and capture screenshots of all 4 tabs to show the user.

---

## Error Handling

- If `git rev-parse HEAD` fails (not a git repo) → use timestamp as cache key
- If Python is not available → use `npx serve` or `npx http-server` as fallback
- If a file cannot be read → skip it and note it in the Issues tab
- Always produce a partial graph — never fail silently
- If SVG node positions overlap → spread nodes more (increase spacing)

---

## Output File Structure

```
$PROJECT_ROOT/
└── .understand-anything/
    ├── knowledge-graph.json   ← Node/edge/layer/tour data (JSON)
    ├── meta.json              ← Cache metadata (gitHash, timestamp)
    └── dashboard.html         ← Self-contained interactive dashboard (HTML)
```

The `.understand-anything/` directory should be added to `.gitignore` unless the user explicitly wants to commit the graph.

---

## Notes

- This skill is **OS-agnostic**: adapts shell commands for Windows (PowerShell) or Linux/macOS (bash)
- The HTML dashboard is **fully offline** — zero CDN dependencies, all CSS/JS inline
- Re-running the skill on unchanged code (same git hash) → skips analysis, only regenerates dashboard HTML
- Use `--full` argument to force a complete re-analysis regardless of cache
- The knowledge-graph.json format is compatible with the official `understand-anything` Vite dashboard schema
