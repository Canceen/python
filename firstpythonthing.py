pT = "abc123"
pA = "abc123"

uN = "canceen"
uA = "canceen"

logAttempt = 3
logMax = 5

pizzatime = (pT == pA) and (logAttempt) <= (logMax) and (uN == uA)

a = f"hello {uN} its pizza time"
b = f"hello {uN} its not pizza time"

if (pizzatime) is True:print (a)
if (pizzatime) is False:print (b)
