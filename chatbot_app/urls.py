from django.urls import path
from chatbot_app.views import index, tickets, contact, privacy_policy, syarat_ketentuan, login, kereta, page1, page2, page3, tentang_kami

urlpatterns = [
    path('', index, name='index'),  # Keep existing
    path('', index, name='home'),   # Add alias for 'home'
    path('tickets/', tickets, name='tickets'),
    path('contact/', contact, name='contact'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('syarat-ketentuan/', syarat_ketentuan, name='syarat_ketentuan'),
    path('login/', login, name='login'),
    path('kereta/', kereta, name='kereta'),
    path('page1/', page1, name='page1'),
    path('page2/', page2, name='page2'),
    path('page3/', page3, name='page3'),
    path('tentang-kami/', tentang_kami, name='tentang_kami'),
]