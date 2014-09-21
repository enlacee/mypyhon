from os import path
print '============================================================'
print 'return verified path exists : ' , path.exists("/home/anb")
print 'return date of create :' , path.getatime("/home/anb")
print 'return date of modified :' , path.getmtime("/home/anb")
print '============================================================'
print 'path join : ' , path.join('home', 'pepe')
print 'path join : ' , path.join('/', 'home', 'anb')
print 'path join win : ' , path.join('c:','Users')  
print '============================================================'
