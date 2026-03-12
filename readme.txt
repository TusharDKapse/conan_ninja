
install python
[Linux] sudo apt update
[Linux] sudo apt python3 python3-venv python3-pip
[Windows] install https://www.python.org/ftp/python/3.14.3/python-3.14.3-amd64.exe

Create a virtual enviornment
python -m venv conan-venv
 [Linux] source conan-venv/bin/activate
 [Windows-cmd] conan-venv/Scripts/activate.bat
 [Windows-PowerShell] conan-venv/Scripts/Activate.ps1

 python -m pip install conan

conan create . -s os=Linux -s arch=x86_64
conan create . -s os=Windows -s arch=x86_64
conan create . -s os=Linux -s arch=x86_64 --build=never #if cache has downloaded toolchain, then do not download


