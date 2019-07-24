from netmiko import ConnectHandler as conhan
from easysnmp import Session
from pymongo import MongoClient

snmp = Session(hostname='192.168.100.57', community='mantap', version=2)
change_conf = snmp.walk('1.3.6.1.4.1.9.9.43.1.1.1')

konek_db = MongoClient('mongodb+srv://kholid:Desemb3r@jawdat-qxiox.mongodb.net/test?retryWrites=true&w=majority')

db = konek_db.acclist
router1 = db.R1

old_valyu_kotor = router1.find_one()
old_valyu = old_valyu_kotor.get('R1')

for data in change_conf:
    new_valyu = data.value
    if new_valyu != old_valyu:
        konek = conhan(device_type='cisco_ios', host='192.168.100.57', username='jawdat', password='jawdat123')
        show = konek.send_command('show ip int br')
        print(show)
        update_db = new_valyu
        post = {"R1": update_db}
        posts = router1.insert_one(post).inserted_id

#Task :
# 1. bikin database buat nyimpen value last change nya (beres)
# 2. command buat auto run script
# 3. bikin tampilannya + connect API