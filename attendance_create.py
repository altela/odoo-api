new_attendance = models.execute_kw(db, uid, password, 'hr.attendance', 'create', [{
    'employee_id': 1, # put the employee ID (integer)
    'check_in': datetime.strftime("%Y-%m-%d %H:%M:%S"), # put the date as string
  }]
)
