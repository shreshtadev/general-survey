# Copyright (c) 2023, shreshtadev and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class FamilyMember(WebsiteGenerator):
	def before_save(self): self.is_married = True if str(self.is_married).lower() == 'yes' else False
