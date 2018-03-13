clear
echo "
              .______    __    __   __      .______     ______   
              |   _  \  |  |  |  | |  |     |   _  \   /  __  \  
              |  |_)  | |  |  |  | |  |     |  |_)  | |  |  |  | 
              |   ___/  |  |  |  | |  |     |   ___/  |  |  |  | 
              |  |      |   --   | |   ----.|  |      |   --   | 
              | _|       \______/  |_______|| _|       \______/  
              
";

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/pulpo"
    BIN_DIR="$PREFIX/bin/"
    BASH_PATH="$PREFIX/bin/bash"
    TERMUX=true
    pkg install -y git python2
else
    if [[ "$(uname)" == 'Darwin' ]]; then
       INSTALL_DIR="/usr/local/pulpo"
       BIN_DIR="/usr/local/bin/"
       BASH_PATH="/bin/bash"
       TERMUX=false
       /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
       brew install python
    else
       INSTALL_DIR="/usr/share/doc/pulpo"
       BIN_DIR="/usr/bin/"
       BASH_PATH="/bin/bash"
       TERMUX=false
       apt-get install -y git python
    fi
fi

echo "[✔] Checking directories...";
if [ -d "$INSTALL_DIR" ]; then
    echo "[◉] A directory pulpo was found! Do you want to replace it? [Y/n]:" ;
    read mama
    if [ "$mama" = "y" ]; then
        if [ "$TERMUX" = true ]; then
            rm -rf "$INSTALL_DIR"
        else
            sudo rm -rf "$INSTALL_DIR"
        fi
    else
        echo "[✘] If you want to install you must remove previous installations [✘] ";
        echo "[✘] Installation failed! [✘] ";
        exit
    fi
fi
echo "[✔] Cleaning up old directories...";
if [ -d "$ETC_DIR/kutaygs" ]; then
    echo "$DIR_FOUND_TEXT"
    if [ "$TERMUX" = true ]; then
        rm -rf "$ETC_DIR/kutaygs"
    else
        sudo rm -rf "$ETC_DIR/kutaygs"
    fi
fi

echo "[✔] Installing ...";
echo "";
git clone https://github.com/kutaygs/pulpo "$INSTALL_DIR";
echo "#!$BASH_PATH
python $INSTALL_DIR/pulpo.py" '${1+"$@"}' > pulpo;
chmod +x pulpo;
if [ "$TERMUX" = true ]; then
    cp fsociety "$BIN_DIR"
else
    sudo cp pulpo "$BIN_DIR"
fi
rm pulpo;


if [ -d "$INSTALL_DIR" ] ;
then
    echo "";
    echo "[✔] Tool installed successfully! [✔]";
    echo "";
    echo "[✔]====================================================================[✔]";
    echo "[✔]      All is done!! You can execute tool by typing pulpo !       [✔]";
    echo "[✔]====================================================================[✔]";
    echo "";
else
    echo "[✘] Installation failed! [✘] ";
    exit
fi
