
from odoo import fields, models

class pushnotifications(models.Model):
    _name = "wb.pushnotifications"
    _description = "This is push notification model"

    name = fields.Char(string = "Subject",required= True, placeholder="Subject...")
    sender = fields.Char(string="Sender")
    receiver = fields.Char(string="Receiver")
    content = fields.Text(string="Content")
