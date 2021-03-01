import xmlrpc.client


#v14
url_v_14 = 'http://odoov12ent.boxed.cz'
db_v_14 = 'boxed'
username_v_14 = 'admin@boxed.cz'
password_v_14 = '1Juzepe1'
port_v_14 = '8069'
common_v_14 = xmlrpc.client.ServerProxy('{}:{}/xmlrpc/2/common'.format(url_v_14, port_v_14))
uid_v_14 = common_v_14.authenticate(db_v_14, username_v_14, password_v_14, {})
models_v_14 = xmlrpc.client.ServerProxy('{}:{}/xmlrpc/2/object'.format(url_v_14, port_v_14))
print(uid_v_14)

#v9
url_v_9 = 'https://portal.boxed.cz'
db_v_9 = 'boxed'
username_v_9 = 'admin@boxed.cz'
password_v_9 = '1Juzepe1'
port_v_9 = '443'
common_v_9 = xmlrpc.client.ServerProxy('{}:{}/xmlrpc/2/common'.format(url_v_9, port_v_9))
uid_v_9 = common_v_9.authenticate(db_v_9, username_v_9, password_v_9, {})
models_v_9 = xmlrpc.client.ServerProxy('{}:{}/xmlrpc/2/object'.format(url_v_9, port_v_9))
print(uid_v_9)

done = 0
size = 1#1000 - done
offset = 0 + done
print('Offset:', offset)

leads = models_v_9.execute_kw(db_v_9, uid_v_9, password_v_9,
    'crm.lead', 'search_read',[[]],{'offset': offset, 'limit': size})

for i, lead in enumerate(leads):
    i = i+1

    lead['company_currency'] = 9

    if lead['partner_id']:
        partner_id = models_v_14.execute_kw(db_v_14, uid_v_14, password_v_14,
    'res.partner', 'search_read',[[('database_id_v9','=',lead['partner_id'][0])]],{'limit': size})
        lead['partner_id'] = partner_id[0]['id']
    
    if lead['company_id']:
        company_id = models_v_14.execute_kw(db_v_14, uid_v_14, password_v_14,
    'res.company', 'search_read',[[('name','=',lead['company_id'][1])]],{'limit': size})
        lead['company_id'] = company_id[0]['id']

    del lead['opt_out']
    del lead['reminder_event_id']
    del lead['date_action']
    del lead['next_activity_id']
    del lead['phonecall_ids']
    del lead['next_activity_3']
    del lead['title_action']
    del lead['next_activity_1']
    del lead['partner_address_name']
    del lead['phonecall_count']
    del lead['weighted_planned_revenue']
    del lead['message_last_post']
    del lead['survey_results']
    del lead['planned_revenue']
    del lead['last_activity_id']
    del lead['next_activity_2']
    del lead['partner_address_email']
    del lead['date_assign']
    del lead['date_action_next']
    del lead['fax']
    del lead['sale_number']
    del lead['reminder_alarm_ids']
    del lead['message_partner_ids']
    del lead['message_follower_ids']
    del lead['website_message_ids']
    # del lead['opt_out']
    # del lead['opt_out']
    # del lead['opt_out']
    # del lead['opt_out']
    # del lead['opt_out']
    # del lead['opt_out']
    # del lead['opt_out']
    # del lead['opt_out']
    # del lead['opt_out']
    # del lead['opt_out']

    print(lead)
    id = models_v_14.execute_kw(db_v_14, uid_v_14, password_v_14, 'crm.lead', 'create', [lead])

    print("Processed [%s] %s of %s [%s] %s"%(lead['id'], i, size, 100 * i/size, '%'))