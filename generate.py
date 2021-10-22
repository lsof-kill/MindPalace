import qrcode
# import pillow

GATEWAY = '192.168.1.10'

class ticket:
    def __init__(self, name, ticket_no, mob):
        self.TOKEN = 'abcdefghijk'
        self.NAME = name
        self.TICKET = ticket_no
        self.MOB = mob
    def generate(self):
        URL = GATEWAY + "/signin.php?name="+self.NAME+"&ticket="+str(self.TICKET)+"&mob="+str(self.MOB)+"&token="+self.TOKEN
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(URL)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save('qrcode001.png')

test = ticket("vinayak",12345,1234567890)
test.generate()