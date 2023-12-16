
from .orders.company_dao import CompanyDAO
from .orders.gps_dao import GpsDAO
from .orders.service_dao import ServiceDAO
from .orders.terminal_dao import TerminalDAO
from .orders.master_dao import MasterDAO
from .orders.service_record_dao import ServiceRecordDAO
from .orders.payment_dao import PaymentDAO
from .orders.service_master_prices_dao import ServiceMasterPriceDAO
from .orders.service_master_availability_dao import ServiceMasterAvailabilityDAO


company_dao = CompanyDAO()
gps_dao = GpsDAO()
service_dao = ServiceDAO()
terminal_dao = TerminalDAO()
master_dao = MasterDAO()
service_record_dao = ServiceRecordDAO()
payment_dao = PaymentDAO()
service_master_prices_dao = ServiceMasterPriceDAO()
service_master_availability_dao = ServiceMasterAvailabilityDAO()
