from instagram import Instagram

i = Instagram()
i.login()
receiver_id = "340282366841710300949128212650830839244"
i.send_message(receiver_id)

