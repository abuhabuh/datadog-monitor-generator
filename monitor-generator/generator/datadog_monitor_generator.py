"""DataDog monitor generator logic
"""

from datadog_monitor import DatadogMonitor, MonitorType
from flask_endpoint import FlaskEndpoint


def monitors_from_flask_endpoint(
        fe: FlaskEndpoint,
) -> list[DatadogMonitor]:
    """Generate a list of DatadogMonitor objects for a single flask endpoint.
    """

    endpoint: str = fe.get_endpoint()
    methods: list[str] = fe.get_methods()

    # todo: only doing 1 method right now
    method: str = methods[0]

    # todo: do latency and throughput monitors
    monitor = DatadogMonitor(
        endpoint_path=endpoint,
        method=method,
        monitor_type=MonitorType.ERROR_RATE,
        data_period='10m',
    )

    return [monitor]
