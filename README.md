# YTD

### A simple youtube CLI downloader
 
# Run & Build
If you want to run or build it please follow these steps:  
1. Install Python3
2. Run `git clone https://github.com/jasinco/YTD.git;cd YTD`
3. Create a python virtual enviroment(venv)
    * Linux&Unix Like:` python3 -m venv venv;source ./venv/bin/activate;pip install -r requirements.txt `
    * Windows:` python -m venv venv;./venv/script/activate;pip install -r requirements.txt `( if you are a powershell user, you need to execution policy first )
4. Run` python main.py --url [your url] [--cwd, --dmd]` or build(Recommand Pyinstaller)
  
#### The main.spec is for pyinstaller to pack, the executable file will be in the dist folder
