import alert
import inputs
import price
import time


def main():
    url = inputs.getURL()
    userAgent = inputs.getUserAgent()
    userMail = inputs.getMail()
    while True:
        currentPrice = price.getCurrentPrice(url, userAgent)
        originalPrice = price.getOriginalPrice()
        if originalPrice == 0:
            price.setPrice(str(currentPrice))

        elif originalPrice > currentPrice:
            alert.sendAlert(userMail, originalPrice, currentPrice)
            price.setPrice(str(0.00))
            return
        time.sleep(30 * 60)


if __name__ == "__main__":
    main()
