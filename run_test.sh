cd /root

#curl -H 'Authorization: token 931d1f989c2aa0be087fd6fe655ab970a51d0539' -H 'Accept: application/vnd.github.v3.raw' -O -L https://api.github.com/repos/dvas0004/CS-Install-Scripts/contents/install_cybersift.sh > ./install_cybersift.sh
wget https://csinstallscripts.blob.core.windows.net/install-scripts/install_cybersift.sh
chmod +x ./install_cybersift.sh
./install_cybersift.sh

if [[ $? -ne 0 ]]; then
	echo "Script Failed With Error: $?"
fi

ss -a > ss.out

ELSTC=`cat ss.out | grep :9200 | grep java`
KBNA=`cat ss.out | grep :5601 | grep java`
NIFI=`cat ss.out | grep :9900 | grep java`
WEBUI=`cat ss.out | grep "127.0.0.1:80"`

if [[ -z $ELSTC ]]; then
	echo "Elasticsearch not running on port 9200"
else
	echo "Elasticsearch running on port 9200"
fi

if [[ -z $KBNA ]]; then
	echo "Kibana not running on port 5601"
else

./clear.sh
	echo "Kibana running on port 5601"
fi

if [[ -z $NIFI ]]; then
	echo "Apache NiFi not running on port 9900"
else
	echo "Apache NiFi running on port 9900"
fi

if [[ -z $WEBUI ]]; then
	echo "Web UI not running on port 80"
else 
	echo "Web UI running on port 80"
fi
