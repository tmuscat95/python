import geoip2.database
import sys

reader = geoip2.database.Reader("./network_analysis/GeoLite2-City.mmdb")

def printGeoIP(ip):
    
     
        rec = reader.city(ip)
        print(ip)
        print("Region: " + rec.continent.name)
        print("Country: " + rec.country.name)
        try:
            print("Subdivision: "+ rec.subdivisions.most_specific.names['en'])
        except KeyError as err:
            pass
        try:    
            print("City: " + rec.city.name)
        except TypeError as err:
            pass
        try:
            print("Postcode: " + rec.postal.code + "\n")
        except TypeError as err:
            pass 
    
def main():
    if(len(sys.argv)==1):
        exit(1)

    ip = sys.argv[1]
    printGeoIP(ip)

if(__name__ == "__main__"):
    main()

