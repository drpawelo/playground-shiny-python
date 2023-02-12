import subprocess

commands_to_run = [
'pip3 install shinylive',
# 'shiny create .'
'shinylive export . docs',
'git add .',
'git commit -m "deploying to github"',
'git push']


# subprocess.run("shiny create myapp")

for command in commands_to_run:
	subprocess.run([command.split(" ")])


# shiny create myapp
# shiny static myapp docs
# git add .
# git commit -m "deploying to github"
# git push