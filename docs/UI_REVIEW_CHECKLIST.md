# UI review checklist (pre-merge / demo)

Use this for a **final pass** before a release candidate or public demo. Complements [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md).

## Themes

- [ ] **Light** — body text, hints (`configure-hint`), nav, tables: readable without squinting; focus rings visible on buttons/inputs.
- [ ] **Dark** — same flows; no illegible `--muted` on `--surface`; charts/cards not “muddy.”

## Flows (in order)

1. [ ] **Landing** — hero, next steps, quick start, feedback/Knowledge blocks: no broken layout at ~1280px and ~390px width.
2. [ ] **Configure** — expand **Agent prompts · runtime surfaces**; confirm SVG diagram renders; save/clear paths still make sense.
3. [ ] **Workbench** — select or create a thread; send a short message; expand **Run trace** — row labels show **Sova Agent** (not raw `assistant`) for model spans; trace panel has bordered container.
4. [ ] **Run history** — open a completed run if available; feedback controls visible.
5. [ ] **Action dashboard** (optional) — card list and filters usable in both themes.

## Language

- [ ] Switch **EN / KR** on landing; spot-check Workbench + Configure headings for truncation.

## Follow-ups

Record non-blocking issues in the project tracker; only ship blockers before the milestone you care about.
