cd /root
curl -H 'Authorization: token 931d1f989c2aa0be087fd6fe655ab970a51d0539' -H 'Accept: application/vnd.github.v3.raw' -O -L https://raw.githubusercontent.com/dvas0004/CS-Install-Scripts/master/install_cybersift.sh > ./install_cybersift.sh

chmod +x ./install_cybersift.sh
./install_cybersift.sh

if [[ $? -ne 0 ]]; then
	echo "Script failed with $?"
fi
