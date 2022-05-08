import js
from pyodide import create_proxy

from datetime import datetime
now = datetime.now()
dt = now.strftime("%m/%d/%Y, %H:%M:%S")

def print_result(evt):
    name = js.txtName.value
    js.document.getElementById("lblOut").innerHTML = f"Hello <b>{name}</b>!!!"

print_result_proxy = create_proxy(print_result)
js.document.getElementById("btnClick").addEventListener ('click', print_result_proxy)

print(f"This is the current date and time, as computed by Python: {dt}")
for i in range(0,5):
    print(f"This is index: {i}")