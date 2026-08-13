# -*- coding: utf-8 -*-
import os, sys

tasks_info = [
    (1, "Działania na Potęgach", "Zamknięte", "1 pkt", "zadanie1.html"),
    (2, "Potęgi i Zapis Dziesiętny", "Zamknięte", "1 pkt", "zadanie2.html"),
    (3, "Działania na Logarytmach", "Zamknięte", "1 pkt", "zadanie3.html"),
    (4, "Obniżki Procentowe", "Zamknięte", "1 pkt", "zadanie4.html"),
    (5, "Pierwiastki Równania Kwadratowego", "Zamknięte", "1 pkt", "zadanie5.html"),
    (6, "Liczba Rozwiązań Równania Wymiernego", "Zamknięte", "1 pkt", "zadanie6.html"),
    (7, "Miejsca Zerowe z Wykresu", "Zamknięte", "1 pkt", "zadanie7.html"),
    (8, "Wierzchołek Paraboli", "Zamknięte", "1 pkt", "zadanie8.html"),
    (9, "Zbiór Wartości Funkcji Kwadratowej", "Zamknięte", "1 pkt", "zadanie9.html"),
    (10, "Wartość Najmniejsza w Przedziale", "Zamknięte", "1 pkt", "zadanie10.html"),
    (11, "Ciąg Geometryczny i Suma S4", "Zamknięte", "1 pkt", "zadanie11.html"),
    (12, "Ciąg Arytmetyczny i Suma S10", "Zamknięte", "1 pkt", "zadanie12.html"),
    (13, "Jedynka Trygonometryczna", "Zamknięte", "1 pkt", "zadanie13.html"),
    (14, "Kąt Wpisany w Okręgu", "Zamknięte", "1 pkt", "zadanie14.html"),
    (15, "Podobieństwo Trójkątów i Styczna", "Zamknięte", "1 pkt", "zadanie15.html"),
    (16, "Pole Rombu z Kątem Rozwartym", "Zamknięte", "1 pkt", "zadanie16.html"),
    (17, "Warunek Równoległości Prostych", "Zamknięte", "1 pkt", "zadanie17.html"),
    (18, "Prosta Prostopadła przez Punkt", "Zamknięte", "1 pkt", "zadanie18.html"),
    (19, "Symetria Środkowa Funkcji Liniowej", "Zamknięte", "1 pkt", "zadanie19.html"),
    (20, "Okrąg Wpisany w Kwadrat", "Zamknięte", "1 pkt", "zadanie20.html"),
    (21, "Przekątna Prostopadłościanu", "Zamknięte", "1 pkt", "zadanie21.html"),
    (22, "Pole Kuli i Stożka", "Zamknięte", "1 pkt", "zadanie22.html"),
    (23, "Mediana Zestawu Danych", "Zamknięte", "1 pkt", "zadanie23.html"),
    (24, "Kombinatoryka i Liczby 5-cyfrowe", "Zamknięte", "1 pkt", "zadanie24.html"),
    (25, "Prawdopodobieństwo Klasyczne", "Zamknięte", "1 pkt", "zadanie25.html"),
    (26, "Równanie Wielomianowe", "Otwarte", "2 pkt", "zadanie26.html"),
    (27, "Nierówność Kwadratowa", "Otwarte", "2 pkt", "zadanie27.html"),
    (28, "Dowód Algebraiczny", "Otwarte", "2 pkt", "zadanie28.html"),
    (29, "Dowód Geometryczny w Okręgu", "Otwarte", "2 pkt", "zadanie29.html"),
    (30, "Prawdopodobieństwo Dwukrotnego Losowania", "Otwarte", "2 pkt", "zadanie30.html"),
    (31, "Przekątna w Trapezie Prostokątnym", "Otwarte", "2 pkt", "zadanie31.html"),
    (32, "Ciąg Arytmetyczny - Badanie Wskaźników", "Otwarte", "4 pkt", "zadanie32.html"),
    (33, "Symetralna Odcinka i Punkt B", "Otwarte", "4 pkt", "zadanie33.html"),
    (34, "Stereometria Ostrosłupa Czworokątnego", "Otwarte", "5 pkt", "zadanie34.html"),
]

grid_items = []
for num, title, ttype, pts, link in tasks_info:
    badge_cls = "closed-badge" if ttype == "Zamknięte" else "open-badge"
    grid_items.append(f'''
        <a href="{link}" class="task-card-link">
            <div class="dash-card">
                <div class="dash-card-header">
                    <span class="dash-num">Zadanie {num}</span>
                    <span class="dash-pts">{pts}</span>
                </div>
                <div class="dash-card-title">{title}</div>
                <div class="dash-card-footer">
                    <span class="{badge_cls}">{ttype}</span>
                    <span class="arrow">Otwórz →</span>
                </div>
            </div>
        </a>''')

nav_links = []
for i in range(1, 35):
    nav_links.append(f'<a href="zadanie{i}.html" class="task-nav-link">Zadanie {i}</a>')

nav_html = '        <nav class="task-nav">\n' + '\n'.join(nav_links) + '\n        </nav>'

dashboard_html = f'''<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Matura z Matematyki Maj 2019 - Kompletne Rozwiązania Zadań (1-34)</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;600;700;800&display=swap" rel="stylesheet">
    
    <style>
        :root {{
            --bg-primary: #0b0f19;
            --bg-card: #151c2c;
            --bg-card-hover: #1e293b;
            --accent-primary: #6366f1;
            --accent-secondary: #a855f7;
            --accent-glow: rgba(99, 102, 241, 0.25);
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border-color: rgba(255, 255, 255, 0.08);
            --correct-green: #10b981;
            --font-heading: 'Outfit', sans-serif;
            --font-body: 'Inter', sans-serif;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: var(--bg-primary);
            color: var(--text-main);
            font-family: var(--font-body);
            line-height: 1.6;
            min-height: 100vh;
            padding: 2rem 1rem;
            background-image: 
                radial-gradient(circle at 15% 15%, rgba(99, 102, 241, 0.12) 0%, transparent 40%),
                radial-gradient(circle at 85% 85%, rgba(168, 85, 247, 0.12) 0%, transparent 40%);
            background-attachment: fixed;
        }}

        .container {{
            max-width: 1100px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 2rem;
        }}

        .task-nav {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 0.4rem;
            margin-bottom: -0.5rem;
            background: rgba(15, 23, 42, 0.6);
            padding: 1rem;
            border-radius: 16px;
            border: 1px solid var(--border-color);
        }}

        .task-nav-link {{
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border-color);
            color: var(--text-muted);
            padding: 0.4rem 0.8rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.85rem;
            transition: all 0.25s ease;
        }}

        .task-nav-link:hover {{
            color: white;
            background: rgba(99, 102, 241, 0.2);
            border-color: var(--accent-primary);
        }}

        header {{
            text-align: center;
            padding: 2.5rem 1.5rem;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.12), rgba(168, 85, 247, 0.12));
            border: 1px solid var(--border-color);
            border-radius: 24px;
            backdrop-filter: blur(12px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }}

        .badge {{
            display: inline-block;
            padding: 0.4rem 1.2rem;
            background: linear-gradient(90deg, var(--accent-primary), var(--accent-secondary));
            color: white;
            font-weight: 700;
            font-size: 0.85rem;
            border-radius: 50px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 1rem;
            box-shadow: 0 4px 12px var(--accent-glow);
        }}

        h1 {{
            font-family: var(--font-heading);
            font-size: 2.6rem;
            font-weight: 800;
            background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.75rem;
        }}

        header p {{
            color: var(--text-muted);
            font-size: 1.15rem;
            max-width: 700px;
            margin: 0 auto;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1.25rem;
        }}

        .stat-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 18px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
        }}

        .stat-val {{
            font-family: var(--font-heading);
            font-size: 2.2rem;
            font-weight: 800;
            color: var(--accent-primary);
            margin-bottom: 0.25rem;
        }}

        .stat-lbl {{
            color: var(--text-muted);
            font-size: 0.95rem;
            font-weight: 500;
        }}

        .section-title {{
            font-family: var(--font-heading);
            font-size: 1.6rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 1.25rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}

        .dashboard-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
            gap: 1.25rem;
        }}

        .task-card-link {{
            text-decoration: none;
            color: inherit;
        }}

        .dash-card {{
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 18px;
            padding: 1.35rem;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            height: 100%;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
        }}

        .dash-card:hover {{
            background-color: var(--bg-card-hover);
            border-color: var(--accent-primary);
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(99, 102, 241, 0.2);
        }}

        .dash-card-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .dash-num {{
            font-family: var(--font-heading);
            font-weight: 700;
            font-size: 1.1rem;
            color: white;
        }}

        .dash-pts {{
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid var(--border-color);
            padding: 0.25rem 0.65rem;
            border-radius: 50px;
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--accent-secondary);
        }}

        .dash-card-title {{
            font-size: 1.05rem;
            font-weight: 600;
            color: var(--text-main);
            flex: 1;
            line-height: 1.4;
        }}

        .dash-card-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 0.5rem;
            padding-top: 0.75rem;
            border-top: 1px solid var(--border-color);
            font-size: 0.85rem;
        }}

        .closed-badge {{
            color: #60a5fa;
            font-weight: 600;
        }}

        .open-badge {{
            color: #f472b6;
            font-weight: 600;
        }}

        .arrow {{
            color: var(--accent-primary);
            font-weight: 700;
            transition: transform 0.2s ease;
        }}

        .dash-card:hover .arrow {{
            transform: translateX(4px);
        }}

        footer {{
            text-align: center;
            color: var(--text-muted);
            font-size: 0.9rem;
            padding: 2rem 0;
            border-top: 1px solid var(--border-color);
            margin-top: 2rem;
        }}

        /* Universal Responsive CSS */
        html, body {{
            overflow-x: hidden !important;
            width: 100% !important;
            -webkit-text-size-adjust: 100%;
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 0.75rem 0.5rem !important;
            }}

            h1 {{
                font-size: 1.8rem !important;
            }}

            .dashboard-grid {{
                grid-template-columns: 1fr !important;
                gap: 1rem !important;
            }}

            .task-nav {{
                max-height: 140px !important;
                overflow-y: auto !important;
                -webkit-overflow-scrolling: touch;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Navigation -->
{nav_html}

        <!-- Header -->
        <header>
            <span class="badge">Egzamin Maturalny • Maj 2019</span>
            <h1>Matematyka - Poziom Podstawowy</h1>
            <p>Interaktywny portal rozwiązań wszystkich 34 zadań z arkusza CKE. Każde zadanie zawiera podgląd treści, wariantowe metody rozwiązań, pułapki maturalne oraz kalkulator.</p>
        </header>

        <!-- Stats Bar -->
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-val">34</div>
                <div class="stat-lbl">Wszystkie Zadania w Arkuszu</div>
            </div>
            <div class="stat-card">
                <div class="stat-val">50 pkt</div>
                <div class="stat-lbl">Maksymalna Liczba Punktów</div>
            </div>
            <div class="stat-card">
                <div class="stat-val">25</div>
                <div class="stat-lbl">Zadania Zamknięte (1 pkt)</div>
            </div>
            <div class="stat-card">
                <div class="stat-val">9</div>
                <div class="stat-lbl">Zadania Otwarte (2-5 pkt)</div>
            </div>
        </div>

        <!-- Task Grid Section -->
        <div>
            <div class="section-title">
                <span>📚</span> Katalog Wszystkich Zadań (1 – 34)
            </div>

            <div class="dashboard-grid">
{'\n'.join(grid_items)}
            </div>
        </div>

        <!-- Footer -->
        <footer>
            Wygenerowano dla przygotowania do Matura z Matematyki • Wszelkie prawa zastrzeżone
        </footer>
    </div>
</body>
</html>'''

with open("d:/matura/index.html", "w", encoding="utf-8") as f:
    f.write(dashboard_html)

print("Main Dashboard d:/matura/index.html generated successfully!")
