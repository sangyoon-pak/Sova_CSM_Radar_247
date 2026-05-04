# Project TODO




- [x] after all update all the md files for the implemented architectures and flows.
  1. done — [ARCHITECTURE.md](docs/ARCHITECTURE.md) § **Configure tab: runtime diagram (UI)**; [PROMPTS.md](docs/PROMPTS.md) link; legacy diagram removed
  2. done — legacy § removed from ARCHITECTURE.md
- [x] we need 5 pseudo emails for the demo — see [docs/DEMO_INBOX_SEED_EMAILS.md](docs/DEMO_INBOX_SEED_EMAILS.md)


### Pre-distribution
- [x] Final UI round: light/dark **muted** contrast; Run trace panel (panel chrome, sans row labels); trace type **Sova Agent** / i18n tool labels (not raw `assistant`). Further polish can continue iteratively.
- [x] Example/vendor-specific script URLs neutralized (`docs.example.com`); README notes `.gitignore` for `data/` / `knowledge-base/`. Remaining **product defaults** (e.g. `config.py` vendor placeholder) are operator-configurable — review before public fork.
- [x] **Knowledge base** not in git: `data/`, `knowledge-base/` in `.gitignore`; README security line.
- [x] No secrets in tracked files (spot-check); use RELEASE_CHECKLIST before release.

**Manual review before merge:** follow [docs/UI_REVIEW_CHECKLIST.md](docs/UI_REVIEW_CHECKLIST.md) (themes; Landing → Configure → Workbench with Run trace → Run history).

### Distribution

- [ ] change the local project folder name to Sova_CSM_Radar_247 and do all the unit test, linter check and sanity check. 
- [ ] clean up all the db tables back to clean state. 
- [ ] **Host install** story: mac/linux/windows via venv + `run.py` (not container-first); `gog`/OAuth need a normal OS env (`docs/GMAIL_SETUP.md`)
- [ ] **Public docs UX**: canonical `docs/INSTALLATION.md`; README links; optional future docs site; landing links when published

### Post-distribution

- [ ] Landing links to **GitHub** guides once the repo is public
- [ ] Configure **gog** section links to the published GitHub doc page
- [ ] simple user-guide video that shows what it does. you can 


## Pointer

The former standalone file `docs/IMPLEMENTATION_TODO_STATUS.md` is merged here. See that path for a one-line redirect.
