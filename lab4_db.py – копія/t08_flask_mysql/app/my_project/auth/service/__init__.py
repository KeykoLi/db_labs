"""
2023
Nataliia.Parkhomchuk.IR.2022@lpnu.ua
© Nataliia Parkhomchuk
"""


from .orders.company_service import CompanyService
from .orders.gps_sevice import GpsService
from .orders.service_service import ServiceService
from .orders.terminal_service import TerminalService
from .orders.master_service import MasterService
from .orders.service_record_service import ServiceRecordService
from .orders.payment_service import PaymentService
from .orders.service_master_price_service import ServiceMasterPriceService
from .orders.service_master_availability_service import ServiceMasterAvailabilityService


company_service = CompanyService()
gps_service = GpsService()
service_service = ServiceService()
terminal_service = TerminalService()
master_service = MasterService()
service_record_service = ServiceRecordService()
payment_service = PaymentService()
service_master_price_service = ServiceMasterPriceService()
service_master_availability_service = ServiceMasterAvailabilityService()
