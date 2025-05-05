import subprocess

scripts = [
    "funnel_analysis.py",
    "category_analysis.py",
    "view_vs_purchase.py",
    "analysis.py"
]

print("Running all analysis scripts...\n")

for script in scripts:
    print(f"Running {script}...")
    subprocess.run(["python", script])
    print(f"Finished {script}\n")

print("All scripts completed successfully!")
