cd /root

#curl -H 'Authorization: token 931d1f989c2aa0be087fd6fe655ab970a51d0539' -H 'Accept: application/vnd.github.v3.raw' -O -L https://api.github.com/repos/dvas0004/CS-Install-Scripts/contents/install_cybersift.sh > ./install_cybersift.sh
wget https://csinstallscripts.blob.core.windows.net/install-scripts/install_cybersift.sh
chmod +x ./install_cybersift.sh
./install_cybersift.sh

if [[ $? -ne 0 ]]; then
	echo "Script Failed With Error: $?"
fi
