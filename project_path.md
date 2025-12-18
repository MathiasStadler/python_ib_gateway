# project_path
<!-- KtF-->
## python version
<!-- KtF-->
```bash <!-- markdownlint-disable-line code-block-style -->
python3 --version
Python 3.13.5
```
<!-- ktf -->
## Download gateway from here [![alt text][1]](https://interactivebrokers.github.io/cpwebapi/quickstart)
<!-- ktf-->
- unzip e.g. on linux/debian
<!-- ktf-->
```bash <!-- markdownlint-disable-line code-block-style -->
unzip clientportal.gw.zip 
```
<!-- ktf-->
- move to /home/$USER folder
<!-- ktf-->
```bash <!-- markdownlint-disable-line code-block-style -->
mv /home/$USER/Download/clientportal.gw /home/$USER
```
<!-- ktf -->
## start gateway local in a separate shell
<!-- ktf-->
```bash <!-- markdownlint-disable-line code-block-style -->
cd ~/clientportal.gw
./bin/run.sh root/conf.yaml
#Open https://localhost:5000 to login
# JavaScript is/must be enable
# You should see follow message => Client login succeeds
```

## create venv
<!-- ktf -->
install venv — Creation of virtual environments [![alt text][1]](https://docs.python.org/3/library/venv.html))
<!-- ktf -->
```bash
python3 -m venv .venv
```
<!-- ktf -->
## enter into .venv
<!-- ktf -->
```bash
source .venv/bin/activate
```
<!-- ktf -->
## list installed packages
<!-- ktf -->
```bash
pip list
```
<!-- ktf -->
## exit/leave .venv
<!-- ktf -->
```bash
deactivate
```
<!-- ktf -->
## follow the instructions from web page
<!-- KtF-->
```bash <!-- markdownlint-disable-line code-block-style -->
pip install 
pip install 
```
<!-- ktf -->
## dummy code block
<!-- ktf -->
```bash <!-- markdownlint-disable-line code-block-style -->
# place holder
```
<!-- ktf -->
For further steps, see Project path [![alt text][1]](project_path.md)
<!-- download the link sign -->
<!-- mkdir -p img && curl --create-dirs --output-dir img -O  "https://raw.githubusercontent.com/MathiasStadler/link_symbol_svg/refs/heads/main/link_symbol.svg"-->
<!-- Link sign - Don't Found a better way :-( - You know a better method? - send me a email -->
[1]: ./img/link_symbol.svg
<!-- KtF-->