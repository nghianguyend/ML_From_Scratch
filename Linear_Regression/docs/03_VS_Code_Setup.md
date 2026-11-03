# A small Windows workspace for learning regression

Create files as you reach the relevant checkpoint. This is setup guidance, not a generated project. Commands below are for you to run; no packages or global settings have been changed.

## 1. Install and select Python

Install a currently supported Python 3 release from [python.org](https://www.python.org/downloads/windows/), [VS Code](https://code.visualstudio.com/), and [Git for Windows](https://git-scm.com/download/win). In VS Code, install Microsoft's **Python** extension; add Microsoft's **Jupyter** extension only if using notebooks. The official OpenAI **Codex** extension is optional for the teaching skills.

In a terminal, check `py --version` (or `python --version` if that is the command configured on your system). Open an empty folder such as `linear-regression-learning` in VS Code. Run subsequent commands from that folder, not from a system directory.

## 2. Create one project environment

In PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install numpy matplotlib pytest
```

If `py` is unavailable but `python` launches your intended interpreter, use `python -m venv .venv`. If PowerShell blocks activation, do not weaken system policy just for this exercise. Activation is optional: use the environment's interpreter directly:

```powershell
.\.venv\Scripts\python.exe -m pip install numpy matplotlib pytest
.\.venv\Scripts\python.exe your_script.py
```

Alternatively, in a Command Prompt terminal, activation is `.venv\Scripts\activate.bat`. To leave an activated environment, run `deactivate`.

Use **Python: Select Interpreter** in VS Code and select `.venv\Scripts\python.exe`. Check `python -c "import sys; print(sys.executable)"` in a newly opened terminal. The terminal and editor should point to the same environment. Prefer `python -m pip` over a bare `pip` command so the installer belongs to that interpreter.

Packages: NumPy for arrays; Matplotlib for plots; pytest for your later tests. Add `ipykernel` only for notebooks, `jupyterlab` only for a browser-based notebook interface, and `scikit-learn` only for an optional reference comparison. NumPy's `linalg.lstsq` is already sufficient for the main reference.

## 3. Choose the right working format

| Use | Good fit | Main risk |
|---|---|---|
| A `.py` file | Reusable functions, reproducible runs, debugging, tests | Mixing demonstrations with reusable functions |
| A `.ipynb` notebook | Derivations beside experiments and plots; short exploration | Hidden state from executing cells out of order |

Start with one scratch notebook **or** one script, not six notebooks. Move a function to a `.py` module once you understand it and want to reuse/test it. A notebook can later import those functions. You do not need both formats immediately.

Run a script with `python your_script.py` or VS Code's **Run Python File in Terminal** action. For a VS Code notebook, install `ipykernel` in your environment, create a notebook yourself, and select that environment as its kernel. Restart the kernel and run all cells in order before trusting the result. For a browser interface, install `jupyterlab` and run `python -m jupyterlab`.

## 4. Let the structure grow with your needs

| Path you may create | When it earns its place |
|---|---|
| `AGENTS.md` and `.agents/skills/` | When installing the supplied teaching ZIP |
| `notes.md` | Immediately, for derivations, decisions, and mistakes |
| `regression.py` | When writing reusable prediction/loss/gradient functions |
| `experiment.py` | When you need a repeatable training experiment |
| `exploration.ipynb` | Optional; when interactive plots help |
| `tests/test_regression.py` | Once the first function has a clear input/output contract |
| `figures/` | Once you want to keep plots |
| `requirements.txt` | When recording the environment for reproduction |

No `src/` package layout, configuration framework, or data pipeline is necessary yet. Keep generated caches and `.venv/` out of Git. Use simple names without spaces to make terminal commands easier.

## 5. Test deliberately, then automate

First calculate a tiny expected result by hand. Check a function against it and inspect its output shape. Later put such assertions in files named `test_*.py`, with functions named `test_*`, and run:

```powershell
python -m pytest -q
```

Use approximate comparisons for floating-point numbers (`pytest.approx` or `np.testing.assert_allclose`), exact comparisons for expected shapes, and deliberately wrong inputs to test your contract. Do not choose a tolerance merely because it makes a failing test pass. No test suite is supplied: choosing and writing your tests is part of the learning task.

## 6. Save milestones with Git

Initialize once with `git init`. Create your own `.gitignore` containing at least `.venv/`, `__pycache__/`, `.pytest_cache/`, and `.ipynb_checkpoints/`. Avoid committing private information or oversized generated outputs.

Before each milestone commit, use `git status` and `git diff`, then stage only the files you intend to save (for example `git add notes.md regression.py`) and commit with a descriptive message, such as `git commit -m "Derive and verify MSE gradient"`. These filenames are examples; do not stage nonexistent files. If Git asks for identity, configure it for this repository according to your preferences. A local Git commit is history, not an off-computer backup; a remote is optional and requires your own choice.

Keep one short note per checkpoint: what you derived, what failed, and how you verified the correction. Record package versions when reproduction matters; `python -m pip freeze` displays the environment's installed versions.

## Documentation checked on 2 November 2026

- [VS Code Python environments](https://code.visualstudio.com/docs/python/environments)
- [Python venv](https://docs.python.org/3/library/venv.html)
- [VS Code notebooks](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
- [pytest getting started](https://docs.pytest.org/en/stable/getting-started.html)
- Codex-specific installation and activation instructions are inside the teaching-skills ZIP.
