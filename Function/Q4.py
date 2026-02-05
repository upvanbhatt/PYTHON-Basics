#WAF to convert USD to INR
def converter (USD_val):
    INR_val=USD_val*90.27
    print(USD_val, "USD=", INR_val,"INR")

converter(1)
converter(100)