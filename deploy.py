import subprocess
import datetime

now_string = datetime.datetime.now().strftime("%y_%d_%m_%h_%m")

commands_to_run = [
# 'pip3 install shinylive',
# 'shiny create .'
"shinylive export . docs",
"git add .",
f"git commit -m 'deploying_to_github${now_string}'",
"git push",
f"echo https://drpawelo.github.io/playground-shiny-python/"]




# subprocess.run("shiny create myapp")

for command in commands_to_run:
	print(f"running: ${command}")
	subprocess.run(command.split(" "))


# shiny create myapp
# shiny static myapp docs
# git add .
# git commit -m "deploying to github"
# git push