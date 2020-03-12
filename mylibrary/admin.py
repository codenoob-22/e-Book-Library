from django.contrib import admin
from mylibrary.models import MyLibrary
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(MyLibrary, SimpleHistoryAdmin)
