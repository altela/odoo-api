import xmlrpc.client
from endpoint import models
from establish import *
from datetime import datetime

new_attendance = models.execute_kw(db, uid, password, 'hr.attendance', 'create', [{
    'employee_id': 1, # put the employee ID (integer), you can first fetch the employee ID and put it here (but that's on different file)
    'check_in': datetime.strftime("%Y-%m-%d %H:%M:%S"), # put the date as string
  }]
)
