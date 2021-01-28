from django.contrib import admin
from app.models import SocialUserSearch, SocialUserFound, GoogleSearchModel, InstantUsernameModel,\
    PhoneNumbersModel, CnicNumbersModel, NumberDetailModel, NetworkInformationModel, LocationGenderModel
# Register your models here.

admin.site.register(SocialUserSearch)
admin.site.register(SocialUserFound)
admin.site.register(GoogleSearchModel)
admin.site.register(InstantUsernameModel)
admin.site.register(PhoneNumbersModel)
admin.site.register(CnicNumbersModel)
admin.site.register(NumberDetailModel)
admin.site.register(NetworkInformationModel)
admin.site.register(LocationGenderModel)