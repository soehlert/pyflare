#! /usr/bin/python
import json
import os
import requests


class Cloudflare:
    def __init__(self, email, key):
        self.endpoint = "https://api.cloudflare.com/client/v4"
        self.headers = {
            "X-Auth-Email": email,
            "X-Auth-Key": key,
            "Content-Type": "application/json",
        }

    def getmyip(self):
        """ Get public IP """
        pub_ip = requests.get("https://api.ipify.org/")
        return pub_ip.text

    def user(self):
        """ Get the user """
        user = requests.get(self.endpoint + "/user", headers=self.headers)
        return user.json()

    def zones(self, zone):
        """ Get the zones """
        payload = {"name": zone}
        zones = requests.get(
            self.endpoint + "/zones", headers=self.headers, params=payload
        )
        return zones.json()

    def dns_records(self, zone_id, record):
        """ Get the dns records for the zones """
        payload = {"name": record}
        records = requests.get(
            self.endpoint + "/zones/" + zone_id + "/dns_records",
            headers=self.headers,
            params=payload,
        )
        return records.json()

    def update_record(self, zone_id, record_id, record, ip_address):
        """ Update the record to use the new public IP """
        payload = {"type": "A", "name": record, "content": ip_address}
        record = requests.put(
            self.endpoint + "/zones/" + zone_id + "/dns_records/" + record_id,
            headers=self.headers,
            data=json.dumps(payload),
        )
        return record.json()

    def __call__(self, zone, record):
        """ If public IP has changed, call update_record method """
        zone_id = cf.zones(zone)["result"][0]["id"]
        record_id = cf.dns_records(zone_id, record)["result"][0]["id"]
        ip_address = cf.getmyip()
        if ip_address != cf.dns_records(zone_id, record)["result"][0]["content"]:
            return cf.update_record(zone_id, record_id, record, ip_address)
        else:
            return


if __name__ == "__main__":
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    try:
        with open(os.path.join(__location__, "config.json")) as json_data_file:
            config = json.load(json_data_file)
            email = config["email"]
            key = config["key"]
            zone = config["zone"]
            record = config["record"]
        cf = Cloudflare(email, key)
        print(cf(zone, record))
    except IOError:
        print("Unable to find config file.")
