import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lawyer_project.settings')
django.setup()

from lawyer.models import Service, LawyerProfile, Review, Article, HeroSlide, CompanyInfo
from datetime import date

print("Zapolnenie bazy dannykh...")

# 1. Company Info
company_info, created = CompanyInfo.objects.get_or_create(
    pk=1,
    defaults={
        'company_name': 'PRAVOZASHITNIK',
        'slogan': 'Vasha zashita - nasha professiya',
        'description': 'Yuridicheskaya kompaniya PRAVOZASHITNIK predostavlyaet polny spektr yuridicheskikh uslug dlya fizicheskikh lits i organizatsiy.',
        'phone': '+7 (999) 123-45-67',
        'email': 'info@pravozashitnik.ru',
        'address': 'g. Moskva, ul. Primernaya, d. 1, ofis 100',
    }
)
print(f"Company info: {'created' if created else 'exists'}")

# 2. Services
services_data = [
    ('Grazhdanskoe pravo', 'grazhdanskoe-pravo', 'Zashita grazhdanskikh prav', 1),
    ('Semeynoe pravo', 'semejnoe-pravo', 'Razvod, razdel imushestva', 2),
    ('Korporativnoe pravo', 'korporativnoe-pravo', 'Soprovojdenie biznesa', 3),
    ('Nalogovoe pravo', 'nalogovoe-pravo', 'Nalogovye spory', 4),
    ('Trudovoe pravo', 'trudovoe-pravo', 'Zashita trudovykh prav', 5),
    ('Nedvizhimost', 'nedvizhimost', 'Sdelki s nedvizhimostyu', 6),
]

for name, slug, desc, order in services_data:
    service, created = Service.objects.get_or_create(
        slug=slug,
        defaults={
            'name': name,
            'icon': '⚖',
            'short_description': desc,
            'description': desc,
            'order': order,
        }
    )
    print(f"Service {name}: {'created' if created else 'exists'}")

# 3. Lawyers
lawyers_data = [
    ('Ivanov Ivan', 'Vedushiy yurist', 'Spetsialist s 15-letnim stazhem', '15 let praktiki', 1),
    ('Petrova Anna', 'Yurist po semeynym delam', 'Ekspert v oblasti semeynogo prava', '10 let praktiki', 2),
    ('Sidorov Petr', 'Starshiy yurist', 'Spetsializiruetsya na nalogovykh sporakh', '12 let praktiki', 3),
]

for full_name, position, bio, exp, order in lawyers_data:
    lawyer, created = LawyerProfile.objects.get_or_create(
        full_name=full_name,
        defaults={
            'position': position,
            'bio': bio,
            'experience_text': exp,
            'order': order,
        }
    )
    print(f"Lawyer {full_name}: {'created' if created else 'exists'}")

# 4. Reviews
reviews_data = [
    ('Aleksey Smirnov', 'OOO Stroy-Invest', 'Obrashalsya po rekomendatsii. Otlichnaya rabota!', 'Dekabr 2024', 1),
    ('Maria Kuznetsova', '', 'Spasibo Anne za pomosh v razvode!', 'Noyabr 2024', 2),
    ('Dmitriy Vasilev', 'IP Vasilev', 'Pomog li s nalogovoy proverko y!', 'Yanvar 2025', 3),
]

for name, company, text, date_text, order in reviews_data:
    review, created = Review.objects.get_or_create(
        client_name=name,
        defaults={
            'client_company': company,
            'text': text,
            'date': date_text,
            'order': order,
        }
    )
    print(f"Review from {name}: {'created' if created else 'exists'}")

# 5. Articles
articles_data = [
    ('Dogovor kupli-prodazhi', 'dogovor-kupli-prodazhi', 'Kak oformit dogovor', date(2025, 1, 10), 145),
    ('Razdel imushestva', 'razdel-imushestva', 'Chto nuzhno znat pri razvode', date(2025, 1, 5), 289),
    ('Prava rabotnika', 'prava-rabotnika', 'Zashita prav pri uvolnenii', date(2024, 12, 28), 412),
]

for title, slug, excerpt, pub_date, views in articles_data:
    article, created = Article.objects.get_or_create(
        slug=slug,
        defaults={
            'title': title,
            'excerpt': excerpt,
            'content': excerpt + '. Polny tekst stati...',
            'published_date': pub_date,
            'views': views,
        }
    )
    print(f"Article {title}: {'created' if created else 'exists'}")

# 6. Hero Slides
slides_data = [
    ('Professionalnaya yuridicheskaya pomosh', 'Bolee 15 let uspeshnoy praktiki', 'Zapisatsya', '#contact', 1),
    ('Zashita vashikh prav - nasha missiya', 'Individualny podkhod k kazhdomu klientu', 'Uznat bolshe', '#services', 2),
]

for title, subtitle, btn_text, btn_link, order in slides_data:
    slide, created = HeroSlide.objects.get_or_create(
        title=title,
        defaults={
            'subtitle': subtitle,
            'button_text': btn_text,
            'button_link': btn_link,
            'order': order,
        }
    )
    print(f"Slide {title}: {'created' if created else 'exists'}")

print("\n" + "="*50)
print("Baza dannykh zapolnena!")
print(f"Services: {Service.objects.count()}")
print(f"Lawyers: {LawyerProfile.objects.count()}")
print(f"Reviews: {Review.objects.count()}")
print(f"Articles: {Article.objects.count()}")
print(f"Slides: {HeroSlide.objects.count()}")
print("\nAdmin login:")
print("URL: http://127.0.0.1:8000/admin/")
print("Username: admin")
print("Password: admin123")
print("="*50)


