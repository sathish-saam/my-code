
import datetime
from itertools import islice
import json
import xml.etree.ElementTree as ET
import logging
import re
import urllib2
import werkzeug.utils
import werkzeug.wrappers

import odoo
from odoo import http
from odoo import fields
from odoo.http import request
from odoo.osv.orm import browse_record
from odoo.addons.website.models.website import slug
from odoo.addons.web.controllers.main import WebClient, Binary, Home
import base64
logger = logging.getLogger(__name__)
import datetime

class Website(Home):
    @http.route(['/page/birthday/'], methods=['GET', 'POST'], type='http', auth="public", website=True)
    def birthday_list(self, **form_data):
        values = {}; birthday_list = []
	now = datetime.datetime.now()	
	current_date = now.strftime("%Y-%m-%d")
	print current_date, '================='
	for record in request.env['hr.employee'].sudo().search([('birthday', '=',current_date)]):
		#birthday_list.append({'name':record.name, 'image':record.image, 'job':record.job_id.name, 'department':record.department_id.name})
		birthday_list.append(record)
	if birthday_list:
		values = {'dob_list':birthday_list} 
        print values
	return request.render("website_birthday.birthday", values)
