from .orders.company_controller import CompanyController
from .orders.gps_controller import GpsController
from .orders.service_controller import ServiceController
from .orders.terminal_controller import TerminalController
from .orders.master_controller import MasterController
from .orders.service_record_controller import ServiceRecordController
from .orders.payment_controller import PaymentController
from .orders.service_master_price_controller import ServiceMasterPriceController
from .orders.service_master_availability_controller import ServiceMasterAvailabilityController


company_controller = CompanyController()
gps_controller = GpsController()
service_controller = ServiceController()
terminal_controller = TerminalController()
master_controller = MasterController()
service_record_controller = ServiceRecordController()
payment_controller = PaymentController()
service_master_price_controller = ServiceMasterPriceController()
service_master_availability_controller = ServiceMasterAvailabilityController()