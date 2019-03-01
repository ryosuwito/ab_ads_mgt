from django.shortcuts import render
from django.views import View
from campaign_mgt.models import GpsType, StickerType

class AdvertisementIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/registration/ads.html')            
    def post(self, request, *args, **kwargs):
        return render(request, 'backend/registration/ads.html')

class AdvertisementAddView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/registration/ads.html')            
    def post(self, request, *args, **kwargs):
        return render(request, 'backend/registration/ads.html')

class ReportIndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'backend/registration/report.html')            
    def post(self, request, *args, **kwargs):
        return render(request, 'backend/main_dashboard.html')
