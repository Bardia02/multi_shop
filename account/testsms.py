import ghasedakpack


sms=ghasedakpack.Ghasedak("4fbaf42afdf8f35b6279b118b949e34d9a3acef5c54cf121bff6935633dafe3b")

sms.verification({'receptor': '09231534', 'type': '1', 'template': 'randcode', 'param1': '1235'})
