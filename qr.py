import qrcode

img = qrcode.make("https://docs.google.com/forms/d/e/1FAIpQLScVorX6GYT2MEpFLmLqItZKUJY78Djf8ZE_DQLdnR5lPXVKfg/viewform?usp=sf_link")

img.save("ACMSpeaker1.png")
img.show()