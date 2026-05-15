# Run this once in your terminal inside the repo folder
import re, subprocess

code = open("premium_platform.py").read()

new_func = open("sidebar_redesign.py").read()
start = new_func.index("# ── START PASTE") 
end   = new_func.index("# ── END PASTE ──") + len("# ── END PASTE ──")
paste = "\n" + "\n".join(
    l for l in new_func[start:end].split("\n")
    if not l.startswith("# ── START") and not l.startswith("# ── END")
)

# Replace old render_sidebar
rs_start = code.index("\ndef render_sidebar():")
rs_end   = code.index("\nPAGE_CINEMA")          # keeps PAGE_CINEMA intact
new_code = code[:rs_start] + paste + code[rs_end:]

open("premium_platform.py", "w").write(new_code)
print("✅ File updated")

subprocess.run(["git", "add", "premium_platform.py"], check=True)
subprocess.run(["git", "commit", "-m", 
    "Redesign sidebar: categories, search, scrollable, theme-aware"], check=True)
subprocess.run(["git", "push", "origin", "main"], check=True)
print("🚀 Pushed to GitHub!")
