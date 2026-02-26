**DAY 1** 

**VERSION CONTROL**
- Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.

**Git**

- Git is a fast, scalable, distributed revision control system with an unusually rich command set that provides both high-level operations and full access to internals.
- 

**Git Commands**
- We divide Git into high level ("porcelain") commands and low level ("plumbing") commands.
- git init: Start a new repo
- git clone <url> : Clone an existing repo
- git add <file> : Add untracked file or unstaged changes
- git add . : Add all untracked files and unstaged changes
- git rm <file> : Delete file
- git rm --cached <file>: Tell Git to forget about a file without deleting it
- git reset: Unstage everything


**Commit Hygiene**
- Basically means: *don’t commit garbage.*
- One commit = one small logical change.
- Don’t mix “fixed login bug” + “changed navbar color” + “deleted random file” in one commit.
- Write commit messages that actually explain what you did.
- Bad: `updated`
- Better: `Fix validation bug in signup form`
- Think of commits like saving checkpoints in a game. If everything is messy, future you will have to give a lot of time for debugging.

---

**Branching**
- Branch = separate line of work.
- `main` (or master) = stable branch.
- When building a feature, we create a new branch like `feature-dashboard`.
- When done → merge it back into main.
- This avoids breaking production code (and avoids getting shouted at).

---

**Rebasing vs Merging**

- **Merging**
  - Combines two branches.
  - Keeps full history.
  - Creates a merge commit.
  - Safe and commonly used.

- **Rebasing**
  - Moves your branch on top of the latest main.
  - Makes history look cleaner.
  - But can mess things up if already pushed and others are using it.

In simple words:
- Merge = safe but slightly messy history.
- Rebase = clean history but handle carefully.

---

**Stash**
- Temporary storage for unfinished work.
- If you're in middle of something and suddenly need to switch branch:
  - `git stash`
- Later:
  - `git stash pop`
- A common everyday example can be: Hiding your messy room when guests come.

---

**Revert vs Reset**

- **Revert**
  - Creates a new commit that undoes a previous commit.
  - Safe for shared branches.
  - Does not delete history.

- **Reset**
  - Moves branch pointer backward.
  - Can delete commits.
  - Dangerous if already pushed.

So:
- Revert = safe undo.
- Reset = risky undo.

---

**Conflict Resolution**
- Happens when two people edit same file or same lines.
- Git doesn’t know whose version to keep.
- It shows conflict markers.
- We manually choose what to keep.
- Then add, commit again.


---

## Failure Modes (Common Git Problems)

**Messy History**
- Too many random commits.
- Hard to understand project timeline.
- Happens due to poor commit hygiene.

**Force Push Disasters**
- Someone rebases and force pushes.
- Other team members lose commits.
- Chaos.

**Wrong Branch Commits**
- You commit directly to main.
- Realise later.
- Regret instantly.

---


- Main rules I understood:
    - Make small clean commits.
    - Always work on branches.
    - Be careful with rebase and reset.
    - Don’t panic during conflicts.


**Best Practices in Git**
- Keeping commits clean
    - Make small, focused commits (one logical change per commit).
    - Write clear commit messages.
    - Avoid committing random debug code or commented junk.
    - Don’t commit secrets (.env files, API keys, passwords).
- Always Use Branches
    - Never work directly on main.
    - Keep main stable and production-ready.
    - Create diff branches for diff works. Eg one for fastapi query handling, one for retrieval etc
    - Useful when debugging
- Pull Before You Push
    - To make sure your local branch is updated.
    - Avoid unnecessary conflicts.
    - Avoid embarrassing push rejections.
- Understand Merge vs Rebase Before Using
    - Use merge when working in teams (safer).
    - Use rebase for cleaning up local commits before merging.
- Write Meaningful Commit Messages
    - A good pattern:
        -  'type': short description
        - Optional longer explanation
- Review Changes Before Committing
- Resolve Conflicts Carefully
    - Dont use git push --force casually



Sources - Git Documentation(https://git-scm.com/docs/git#_discussion), Pro Git book(https://git-scm.com/book/en/v2), ChatGPT(chatgpt.com),
