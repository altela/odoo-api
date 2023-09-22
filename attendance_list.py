import xmlrpc.client
from endpoint import models
from establish import *
from datetime import datetime

# search attendance
active_attendance = models.execute_kw(db, uid, password, 'hr.attendance', 'search', [[['employee_id', '=', 1], ['check_out', '=', False]]]) # this will find attendance based on employee ID
print(active_attendance)

# write a check-out time on that attendance
models.execute_kw(db, uid, password, 'hr.attendance', 'write', [active_attendance[0], {'check_out': datetime.strftime("%Y-%m-%d %H:%M:%S")}])
