git checkout -b live-code
git rm dashbat/bar_graph.py
git rm dashbat/figures.py
mv dashbat/main_template.py dashbat/main.py

git add main.py
git rm dashbat/main_template.py
git commit -m 'Go live code'
