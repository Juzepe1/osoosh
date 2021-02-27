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

size = 100
offset = 0
partners = models_v_9.execute_kw(db_v_9, uid_v_9, password_v_9,
    'res.partner', 'search_read',[[('active', '=', True)]],{'offset': 0, 'limit': size})

for i, partner in enumerate(partners):
    i = i+1
    print("Processing %s of %s [%s] %s"%(i, size, 100 * i/size, '%'))
    partner['image_1920'] = partner['image']
    partner['image_medium'] = partner['image_small']
    partner['company_id'] = False
    partner['country_id'] = 56
    partner['customer_rank'] = 1 if partner['customer'] else 0
    partner['supplier_rank'] = 1 if partner['supplier'] else 0
    partner['user_id'] = 1

    # print(partner['id'])
    del partner['commercial_partner_id']
    del partner['id']
    del partner['state_id']
    del partner['user_id']
    del partner['message_last_post']
    del partner['use_parent_address']
    del partner['notify_email']
    del partner['claim_count']
    del partner['birthdate']
    del partner['issue_count']
    del partner['phonecall_count']
    del partner['survey_ids']
    del partner['contracts_count']
    del partner['mails_to']
    del partner['supplier']
    del partner['customer']
    del partner['mails_from']
    del partner['survey_inputs']
    del partner['survey_input_lines']
    del partner['fax']
    del partner['website_wishlist']
    del partner['opt_out']
    del partner['payment_method_ids']
    del partner['survey_input_count']
    del partner['website_private']
    del partner['image_small']
    del partner['payment_method_count']
    del partner['email_score'] 
    del partner['issued_total']
    del partner['image']
    del partner['id_numbers']
    del partner['tracking_emails_count']
    del partner['phonecall_ids']
    del partner['tracking_email_ids']
    
    # continue
    
    id = models_v_14.execute_kw(db_v_14, uid_v_14, password_v_14, 'res.partner', 'create', [partner])
    print("Processed %s of %s [%s] %s"%(i, size, 100 * i/size, '%'))




