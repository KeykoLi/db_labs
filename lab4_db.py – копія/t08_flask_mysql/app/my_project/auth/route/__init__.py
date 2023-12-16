"""
2023
Nataliia.Parkhomchuk.IR.2022@lpnu.ua
© Nataliia Parkhomchuk
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.gps_route import gps_bp
    from .orders.company_route import company_bp
    from .orders.service_route import service_bp
    from .orders.terminal_route import terminal_bp
    from .orders.master_route import master_bp
    from .orders.service_record_route import service_record_bp
    from .orders.payment_route import payment_bp
    from .orders.service_master_price_route import price_bp
    from .orders.service_master_availability_router import availability_bp

    app.register_blueprint(company_bp)
    app.register_blueprint(gps_bp)
    app.register_blueprint(service_bp)
    app.register_blueprint(terminal_bp)
    app.register_blueprint(master_bp)
    app.register_blueprint(service_record_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(price_bp)
    app.register_blueprint(availability_bp)

