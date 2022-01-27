import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AS15uHeS4leWaNy0s8ziTFx3BpH9dT8544cn7XEpGEATntV6-cxy0RRjrNTSfzD9ng7abeo7CwdxZuTY"
        self.client_secret = "EKx_wpwwiVbvoNOvKO3CfZnGrUD88wVKWsZ8nJg_ZyIuHFKx9WXFrbU1HjXw8ucC2hlXfDtWEMI_7LP0"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
