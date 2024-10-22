from django.contrib import admin
from .models import *
# Register your models here.
class showuser(admin.ModelAdmin):
    list_display = ['NAME', 'EMAIL', 'PASSWORD', 'DATE_JOINED']
class showUserProfile(admin.ModelAdmin):
    list_display = ['USER', 'DOB', 'ADDRESS', 'PHONE_NO']
class showCategory_Table(admin.ModelAdmin):
    list_display = ['Category_NAME']
class showEquipment(admin.ModelAdmin):
    list_display = ['USER', 'Equipment_type', 'TOOL_NAME', 'DESCRIPTION', 'AVAILABILITY', 'Price_Per_Day', 'Duration', 'Condition']
class showBooking(admin.ModelAdmin):
    list_display = ['user', 'Equipment', 'Total_price', 'Booking_from', 'Booking_To', 'Return_Date', 'Is_Confirmed', 'Payment_status', 'PICKUP_LOCATION', 'RETURN_LOCATION', 'DAMAGE_REPORT', 'LATE_RETURN_PENALTY']
class showPayment(admin.ModelAdmin):
    list_display = ['user', 'Booking', 'Booking_from', 'Booking_to', 'payment_mode', 'payment_status', 'Payment_date']
class showEquipmentMaintenance(admin.ModelAdmin):
    list_display = ['user', 'Equipment', 'Maintenance_type', 'Maintenance_date', 'cost']
class showFeedback(admin.ModelAdmin):
    list_display = ['user', 'Equipment', 'Rating', 'Comment', 'Review_date']
class showComplaint(admin.ModelAdmin):
        list_display = ['user', 'Equipment', 'Description', 'Date']
class showContactus(admin.ModelAdmin):
            list_display = ['Name', 'Email', 'Subject', 'Message', 'Passport_number']
admin.site.register(User, showuser)
admin.site.register(UserProfile, showUserProfile)
admin.site.register(CategoryTable, showCategory_Table)
admin.site.register(Equipment, showEquipment)
admin.site.register(Booking, showBooking)
admin.site.register(Payment, showPayment)
admin.site.register(EquipmentMaintenance, showEquipmentMaintenance)
admin.site.register(Feedback, showFeedback)
admin.site.register(Complaint, showComplaint)
admin.site.register(Contactus, showContactus)