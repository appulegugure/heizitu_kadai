UPDATE users
SET username = %(editname)s, age = %(editage)s
WHERE username = %(name)s
;