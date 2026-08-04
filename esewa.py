import qrcode
from PIL import Image
#step 1 : define payment details
merchant_id = "9810442281"
amount = 500
reference = "order123" #Transaction reference(could be  invoice / order ID)

#step 2: Construct esewa payment URI
payment_url = (
    f"https://esewa.com.np/#/home?"
    f"merchant_id = {merchant_id}"
    f"&amount={amount}"
    f"&reference = {reference}"
)
#Note: The format may vary depending on esewa's official API/QR spec

#Step 3 : Generate QR code
qr = qrcode.QRCode(
    version = 1,  #Controls size of QR(1 = SMALLEST)
    error_correction = qrcode.constants.ERROR_CORRECT_H, #High error correction
    box_size = 10, #Size of each box in pixels
    border = 4,
)
qr.add_data(payment_url)
qr.make(fit=True)

#Step 4: Create image
img = qr.make_image(fill_color = 'green', back_color = "white")

#Step 5: Save or show QR CODE
img.save('esewa_payment_qr.png')
img.show()

print("QR Code generated successfully!")