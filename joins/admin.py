from django.contrib import admin

from .models import Join

class JoinAdmin(admin.ModelAdmin):
    class Meta:
        model = Join
    # hello = 'test'
    # fields = ['email']
    list_display = ['email', 'friend', 'ref_id', 'ip_address', 'timestamp', 'updated']

admin.site.register(Join, JoinAdmin)