

class ServiceAndTerminal:

    def __init__(self, service_type, address, company_id, gps_id, installation_date):
        self.service_type = service_type
        self.address = address
        self.company_id = company_id
        self.gps_id = gps_id
        self.installation_date = installation_date

    def to_dict(self):
        return {
            "service_type": self.service_type,
            "address": self.address,
            "company_id": self.company_id,
            "gps_id": self.gps_id,
            "installation_date": self.installation_date
        }