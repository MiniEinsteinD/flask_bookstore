# How to use (for Windows Subsystem for Linux Ubuntu, MacOS, or Linux environment)
 - idk just skip to step 5 if ur on a powershell/windows environment

Run the following:
1. Pull code, I use ssh, do accordingly based on whatever method you use
```
git clone git@github.com:1112zakaria/flask_bookstore.git
```
2. Goto cloned directory, its probably named flask_bookstore (?)
```
cd flask_bookstore
```
3. Create Python3 virtual environment directory
```
python3 -m venv .env
```
4. Activate Python3 virtual environment
```
source .env/bin/activate
```
5. Run Python flask server
```
python3 src/main/app.py
```
