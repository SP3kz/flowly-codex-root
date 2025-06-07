# Auto-deploy script for pushing to GitHub
import os

os.system('git init')
os.system('git add .')
os.system('git commit -m "CI/CD Ready: Codex Init Anywhere"')
os.system('git branch -M main')
os.system('git remote add origin https://github.com/YOUR_USERNAME/flowly-codex-init-anywhere.git')
os.system('git push -u origin main')
