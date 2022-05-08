from js import document

from datetime import datetime
now = datetime.now()
dt = now.strftime("%m/%d/%Y, %H:%M:%S")

document.getElementById("lblOut").innerHTML = "<b>Labeled Output</b>"

print(f"This is the current date and time, as computed by Python: {dt}")
for i in range(0,5):
    print(f"This is index: {i}")