import geoip2.database
import sys

if(len(sys.argv)==1):
    exit(1)

ip = sys.argv[1]
reader = geoip2.database.Reader("./network_analysis/GeoLite2-City.mmdb")
rec = reader.city(ip)

def main():
    print(ip)
    print("Region: " + rec.continent.name)
    print("Country: " + rec.country.name)
    print("Subdivision: "+ rec.subdivisions.most_specific.name)
    print("City: " + rec.city.name)
    print("Postcode: " + rec.postal.code)

if(__name__ == "__main__"):
    main()

