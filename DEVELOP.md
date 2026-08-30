# Development Flow

Use one feature branch for one task. Do not work directly in `develop`.

## 1. Make a local copy

```bash
git clone git@github.com:OlexiiA/personal-assistant.git
cd personal-assistant
git switch develop
git pull origin develop
```

## 2. Create a feature branch

Start from the latest `develop` branch:

```bash
git switch develop
git pull origin develop
git switch -c feature/email-validation
```

Use a short branch name for your task, for example:

- `feature/contact-search`
- `feature/notes`
- `fix/birthday-list`

## 3. Run the program locally

```bash
uv run perso
```

Check your feature manually before you push it.

## 4. Commit and push

```bash
git status
git add .
git commit -m "feat: add email validation"
git push -u origin feature/email-validation
```

## 5. Create a pull request

With GitHub CLI:

```bash
gh pr create --base develop --fill
```

Or open the repository on GitHub and select **Compare & pull request**.
Set the base branch to `develop` and ask another developer to review the code.
