from odoo import models,fields
# import datetime

class Hotel(models.Model):
    _name='hotel.booking'
    _description='Booking'
    booking_id=fields.Char(string="Booking Id",required=True ,help='This is used to enter booking id')
    guest_name=fields.Char(string="Guest Name", help='It is used to enter guest name',index=True)
    guest_email=fields.Char(string="Guest Email",help="You can enter guest's email id" )
    check_in=fields.Datetime(string="Check in",help='It is used to enter check in time and date')
    check_out=fields.Datetime(string="Check out",help='It is used to enter check out time and date')
    # room_availability=fields.Boolean(string="Is room Available ?",help='This is need to be checked out if room not available')
    date_of_booking=fields.Date(string="Booking Date",default=fields.Date.today(),help='It is used to enter booking date')
    guest_info=fields.Text(string="Guest Info",help='It is used to enter guest info')
    per_day_cost=fields.Float(string="Per Day Cost",help='It is used to enter price for one night stay')
    type_of_rooms=fields.Selection(selection=[('king room','King Room'),('garden view room','Gardern View Room')],string="Types of Rooms",help='It is used select type of rooms to stay')
    description=fields.Html(string="Description",help='You have to enter any specific requirement of guest',size=4)
    active=fields.Boolean(string="Active",default=True)
    mode_of_payment=fields.Selection([('cash','Cash'),('credit/debit card','Credit/Debit Card'),('mobile payments','Mobile Payments'),('digital wallets','Digital Wallets')],string='Mode of Payments')
    taxes=fields.Float(string="Taxes",help='Depicts levied tax in bill')
    days_book_for=fields.Integer(string="Days book for",help='It used to specify no of days spent')
    password=fields.Char("Password",groups="hotel.group_hotel_staff")
    website=fields.Char("Website")
    guest_priority=fields.Selection([(str(ele),str(ele))for ele in range(5)],'Guest Priority')
    sign_in =fields.Float('Sign in')
    # days_book_for=check_in-check_out
    subtotal=fields.Float(string="Subtotal",help='it displays final amount',digits=(16,3))