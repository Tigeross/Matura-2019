# -*- coding: utf-8 -*-
import os, sys, re

# General navigation bar for 34 tasks
def get_nav_html(active_num):
    nav_links = []
    for i in range(1, 35):
        active_cls = ' active' if i == active_num else ''
        nav_links.append(f'            <a href="zadanie{i}.html" class="task-nav-link{active_cls}">Zadanie {i}</a>')
    return '        <nav class="task-nav">\n' + '\n'.join(nav_links) + '\n        </nav>'

# Ultimate Mobile Responsive CSS
ULTIMATE_RESPONSIVE_CSS = """
        /* Complete Mobile & Universal Responsive System */
        html, body {
            overflow-x: hidden !important;
            width: 100% !important;
            -webkit-text-size-adjust: 100%;
        }

        img {
            max-width: 100% !important;
            height: auto !important;
            display: block;
            margin: 0 auto;
        }

        .container {
            width: 100% !important;
            box-sizing: border-box;
        }

        .card {
            word-wrap: break-word;
            overflow-wrap: break-word;
            box-sizing: border-box;
        }

        /* Mobile Adjustments for Tablets and Phones (< 768px) */
        @media (max-width: 768px) {
            body {
                padding: 0.75rem 0.5rem !important;
            }

            .container {
                gap: 1rem !important;
            }

            header {
                padding: 1.25rem 0.75rem !important;
                border-radius: 16px !important;
            }

            .badge {
                font-size: 0.75rem !important;
                padding: 0.25rem 0.75rem !important;
                letter-spacing: 0.5px !important;
            }

            h1 {
                font-size: 1.5rem !important;
                line-height: 1.3 !important;
            }

            header p {
                font-size: 0.9rem !important;
            }

            .card {
                padding: 1.15rem 0.85rem !important;
                border-radius: 16px !important;
            }

            .card-header {
                margin-bottom: 1rem !important;
                padding-bottom: 0.65rem !important;
                gap: 0.5rem !important;
            }

            .card-icon {
                width: 34px !important;
                height: 34px !important;
                font-size: 1.05rem !important;
                border-radius: 10px !important;
            }

            .card-title {
                font-size: 1.1rem !important;
            }

            .task-box {
                font-size: 1rem !important;
                padding: 1rem !important;
                border-radius: 0 10px 10px 0 !important;
            }

            .options-grid {
                grid-template-columns: 1fr !important;
                gap: 0.65rem !important;
            }

            .option-btn {
                padding: 0.85rem !important;
                font-size: 0.95rem !important;
                min-height: 48px !important; /* iOS Touch Target */
            }

            .option-letter {
                width: 28px !important;
                height: 28px !important;
                font-size: 0.9rem !important;
            }

            .task-nav {
                padding: 0.6rem 0.4rem !important;
                gap: 0.3rem !important;
                max-height: 140px !important;
                overflow-y: auto !important;
                -webkit-overflow-scrolling: touch;
            }

            .task-nav-link {
                padding: 0.3rem 0.6rem !important;
                font-size: 0.75rem !important;
            }

            .tabs-nav {
                gap: 0.3rem !important;
                padding-bottom: 0.4rem !important;
            }

            .tab-btn {
                padding: 0.45rem 0.75rem !important;
                font-size: 0.82rem !important;
            }

            .step-item {
                gap: 0.75rem !important;
                margin-bottom: 1.15rem !important;
            }

            .step-number {
                width: 28px !important;
                height: 28px !important;
                font-size: 0.85rem !important;
            }

            .step-title {
                font-size: 1rem !important;
            }

            .step-desc {
                font-size: 0.92rem !important;
            }

            .calc-form {
                grid-template-columns: 1fr !important;
                gap: 0.75rem !important;
            }

            .calc-form input, .calc-form select, .open-task-input input {
                font-size: 16px !important; /* Prevents auto-zoom on iOS Safari */
                padding: 0.65rem 0.75rem !important;
            }

            .calc-btn {
                padding: 0.75rem !important;
                font-size: 0.95rem !important;
            }

            .math-highlight, .formula-card {
                padding: 0.65rem 0.85rem !important;
                font-size: 0.92rem !important;
            }
        }

        /* Extra Small Screens (< 400px) */
        @media (max-width: 400px) {
            h1 {
                font-size: 1.3rem !important;
            }

            .task-box {
                font-size: 0.95rem !important;
            }

            .option-btn {
                font-size: 0.9rem !important;
            }
        }

        /* MathJax Overflow Handling for Small Screens */
        mjx-container[jax="SVG"][display="true"], mjx-container[jax="CHTML"][display="true"], .MathJax_Display {
            overflow-x: auto !important;
            overflow-y: hidden !important;
            max-width: 100% !important;
            padding: 0.25rem 0 !important;
            -webkit-overflow-scrolling: touch;
        }
"""

# Function to generate complete HTML page
def create_task_page(task_num, title, subtitle, task_text, image_filename, is_closed, options_dict, correct_opt_or_ans, solution_html, traps_html, formulas_html, calc_html, js_code):
    nav_code = get_nav_html(task_num)
    
    if is_closed:
        options_grid_items = []
        for opt_let, opt_val in options_dict.items():
            options_grid_items.append(f'''                <button class="option-btn" onclick="checkAnswer('{opt_let}')">
                    <span class="option-letter">{opt_let}</span>
                    <span>{opt_val}</span>
                </button>''')
        interactive_area = f'''            <div class="options-grid" id="optionsGrid">
{'\n'.join(options_grid_items)}
            </div>
            <div class="feedback-box" id="feedbackBox"></div>'''
    else:
        interactive_area = f'''            <div class="open-task-input" style="margin-top:1.5rem; background:rgba(255,255,255,0.02); padding:1.25rem; border-radius:14px; border:1px solid var(--border-color);">
                <label style="font-weight:600; display:block; margin-bottom:0.5rem; color:var(--text-muted);">Sprawdź swoją odpowiedź:</label>
                <div style="display:flex; gap:0.75rem; flex-wrap:wrap;">
                    <input type="text" id="userAnsInput" placeholder="Wpisz wynik (np. {correct_opt_or_ans})" style="flex:1; min-width:200px; background:rgba(255,255,255,0.05); border:1px solid var(--border-color); border-radius:10px; padding:0.75rem; color:white; font-size:1rem;">
                    <button onclick="checkOpenAnswer()" class="calc-btn" style="grid-column:auto; width:auto; padding:0.75rem 1.5rem;">Sprawdź Odpowiedź</button>
                </div>
            </div>
            <div class="feedback-box" id="feedbackBox"></div>'''

    html_content = f'''<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zadanie {task_num} - Rozwiązanie i Wyjaśnienie | Matura z Matematyki 2019</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@400;600;700;800&display=swap" rel="stylesheet">
    <!-- MathJax for LaTeX Rendering -->
    <script>
        MathJax = {{
            tex: {{
                inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
                displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
                processEscapes: true
            }},
            svg: {{
                fontCache: 'global'
            }}
        }};
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
    
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
            --correct-bg: rgba(16, 185, 129, 0.15);
            --wrong-red: #ef4444;
            --wrong-bg: rgba(239, 68, 68, 0.15);
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
            max-width: 950px;
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

        .task-nav-link.active {{
            background: linear-gradient(90deg, var(--accent-primary), var(--accent-secondary));
            color: white;
            border-color: transparent;
            box-shadow: 0 4px 12px var(--accent-glow);
        }}

        header {{
            text-align: center;
            padding: 2rem 1rem;
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(168, 85, 247, 0.1));
            border: 1px solid var(--border-color);
            border-radius: 24px;
            backdrop-filter: blur(12px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        }}

        .badge {{
            display: inline-block;
            padding: 0.35rem 1rem;
            background: linear-gradient(90deg, var(--accent-primary), var(--accent-secondary));
            color: white;
            font-weight: 600;
            font-size: 0.85rem;
            border-radius: 50px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 1rem;
            box-shadow: 0 4px 12px var(--accent-glow);
        }}

        h1 {{
            font-family: var(--font-heading);
            font-size: 2.2rem;
            font-weight: 800;
            background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
        }}

        header p {{
            color: var(--text-muted);
            font-size: 1.1rem;
        }}

        .card {{
            background-color: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 20px;
            padding: 2rem;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s ease, border-color 0.3s ease;
        }}

        .card:hover {{
            border-color: rgba(99, 102, 241, 0.4);
        }}

        .card-header {{
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 1.5rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 1rem;
        }}

        .card-icon {{
            width: 40px;
            height: 40px;
            border-radius: 12px;
            background: rgba(99, 102, 241, 0.15);
            color: var(--accent-primary);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.25rem;
            font-weight: 700;
        }}

        .card-title {{
            font-family: var(--font-heading);
            font-size: 1.4rem;
            font-weight: 700;
            color: var(--text-main);
        }}

        .task-box {{
            background-color: rgba(15, 23, 42, 0.6);
            border-left: 4px solid var(--accent-primary);
            padding: 1.5rem;
            border-radius: 0 12px 12px 0;
            margin-bottom: 1.5rem;
            font-size: 1.15rem;
        }}

        .task-image-preview {{
            margin-top: 1rem;
            margin-bottom: 1.5rem;
            text-align: center;
        }}

        .task-image-preview img {{
            max-width: 100%;
            border-radius: 12px;
            border: 1px solid var(--border-color);
            box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        }}

        .options-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 1.5rem;
        }}

        .option-btn {{
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 1.2rem;
            color: var(--text-main);
            font-size: 1.1rem;
            font-weight: 600;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 0.75rem;
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            text-align: left;
        }}

        .option-btn:hover {{
            background: rgba(99, 102, 241, 0.1);
            border-color: var(--accent-primary);
            transform: translateY(-2px);
        }}

        .option-letter {{
            width: 32px;
            height: 32px;
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.08);
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: var(--font-heading);
            font-weight: 700;
            flex-shrink: 0;
        }}

        .option-btn.correct {{
            background: var(--correct-bg) !important;
            border-color: var(--correct-green) !important;
            color: #34d399 !important;
        }}

        .option-btn.correct .option-letter {{
            background: var(--correct-green) !important;
            color: white !important;
        }}

        .option-btn.wrong {{
            background: var(--wrong-bg) !important;
            border-color: var(--wrong-red) !important;
            color: #f87171 !important;
        }}

        .option-btn.wrong .option-letter {{
            background: var(--wrong-red) !important;
            color: white !important;
        }}

        .feedback-box {{
            margin-top: 1.5rem;
            padding: 1.25rem;
            border-radius: 14px;
            display: none;
            font-size: 1.05rem;
            animation: fadeIn 0.3s ease;
        }}

        .feedback-box.active {{
            display: block;
        }}

        .feedback-box.correct {{
            background: var(--correct-bg);
            border: 1px solid var(--correct-green);
            color: #a7f3d0;
        }}

        .feedback-box.wrong {{
            background: var(--wrong-bg);
            border: 1px solid var(--wrong-red);
            color: #fecaca;
        }}

        .tabs-nav {{
            display: flex;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 0.5rem;
            overflow-x: auto;
        }}

        .tab-btn {{
            background: none;
            border: none;
            color: var(--text-muted);
            padding: 0.6rem 1.2rem;
            font-weight: 600;
            font-size: 0.95rem;
            cursor: pointer;
            border-radius: 8px;
            transition: all 0.2s ease;
            white-space: nowrap;
        }}

        .tab-btn:hover {{
            color: white;
            background: rgba(255, 255, 255, 0.05);
        }}

        .tab-btn.active {{
            color: white;
            background: var(--accent-primary);
        }}

        .tab-content {{
            display: none;
        }}

        .tab-content.active {{
            display: block;
            animation: fadeIn 0.3s ease;
        }}

        .step-item {{
            display: flex;
            gap: 1.25rem;
            margin-bottom: 1.5rem;
            position: relative;
        }}

        .step-number {{
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
            color: white;
            font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            box-shadow: 0 4px 10px var(--accent-glow);
        }}

        .step-body {{
            flex: 1;
        }}

        .step-title {{
            font-family: var(--font-heading);
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 0.35rem;
        }}

        .step-desc {{
            color: var(--text-muted);
            font-size: 1.02rem;
        }}

        .math-highlight {{
            background: rgba(99, 102, 241, 0.1);
            border-left: 3px solid var(--accent-primary);
            padding: 0.75rem 1rem;
            border-radius: 0 8px 8px 0;
            margin-top: 0.75rem;
            color: var(--text-main);
        }}

        .formulas-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 1rem;
        }}

        .formula-card {{
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 1.2rem;
        }}

        .formula-name {{
            font-family: var(--font-heading);
            font-weight: 700;
            color: var(--accent-primary);
            margin-bottom: 0.5rem;
            font-size: 1.05rem;
        }}

        .calc-form {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-bottom: 1.5rem;
        }}

        .input-group {{
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }}

        .input-group label {{
            font-weight: 600;
            font-size: 0.9rem;
            color: var(--text-muted);
        }}

        .input-group input, .input-group select {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 0.75rem 1rem;
            color: white;
            font-size: 1rem;
            outline: none;
            transition: border-color 0.2s ease;
        }}

        .input-group input:focus, .input-group select:focus {{
            border-color: var(--accent-primary);
        }}

        .calc-btn {{
            grid-column: 1 / -1;
            background: linear-gradient(90deg, var(--accent-primary), var(--accent-secondary));
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.85rem;
            font-weight: 700;
            font-size: 1rem;
            cursor: pointer;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            box-shadow: 0 4px 15px var(--accent-glow);
        }}

        .calc-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px var(--accent-glow);
        }}

        .calc-result {{
            background: rgba(15, 23, 42, 0.7);
            border: 1px solid var(--border-color);
            border-radius: 14px;
            padding: 1.25rem;
            font-size: 1.1rem;
            margin-top: 1rem;
        }}

        footer {{
            text-align: center;
            color: var(--text-muted);
            font-size: 0.9rem;
            padding: 2rem 0;
            border-top: 1px solid var(--border-color);
            margin-top: 2rem;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

{ULTIMATE_RESPONSIVE_CSS}
    </style>
</head>
<body>
    <div class="container">
        <!-- Navigation -->
{nav_code}

        <!-- Header -->
        <header>
            <span class="badge">Matura z Matematyki • Zadanie {task_num}</span>
            <h1>{title}</h1>
            <p>{subtitle}</p>
        </header>

        <!-- Task Card -->
        <div class="card">
            <div class="card-header">
                <div class="card-icon">{task_num}</div>
                <div class="card-title">Treść Zadania</div>
            </div>

            <div class="task-box">
                {task_text}
            </div>

            <div class="task-image-preview">
                <img src="{image_filename}" alt="Zadanie {task_num} - treść i rysunek">
            </div>

{interactive_area}
        </div>

        <!-- Solution Card -->
        <div class="card">
            <div class="card-header">
                <div class="card-icon">💡</div>
                <div class="card-title">Rozwiązanie Krok po Kroku</div>
            </div>

{solution_html}
        </div>

        <!-- Traps Card -->
        <div class="card">
            <div class="card-header">
                <div class="card-icon">⚠️</div>
                <div class="card-title">Częste Pułapki i Błędy na Maturze</div>
            </div>

{traps_html}
        </div>

        <!-- Formulas Card -->
        <div class="card">
            <div class="card-header">
                <div class="card-icon">📖</div>
                <div class="card-title">Przydatne Wzory z Tablic Maturalnych</div>
            </div>

{formulas_html}
        </div>

        <!-- Interactive Tool Card -->
        <div class="card">
            <div class="card-header">
                <div class="card-icon">🧮</div>
                <div class="card-title">Interaktywne Narzędzie Pomocnicze</div>
            </div>

{calc_html}
        </div>

        <!-- Footer -->
        <footer>
            Wygenerowano dla przygotowania do Matura z Matematyki • Wszelkie prawa zastrzeżone
        </footer>
    </div>

    <script>
        function switchTab(tabId) {{
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(content => content.classList.remove('active'));
            
            const activeBtn = Array.from(document.querySelectorAll('.tab-btn')).find(b => b.getAttribute('onclick').includes(tabId));
            if (activeBtn) activeBtn.classList.add('active');
            
            const activeContent = document.getElementById(tabId);
            if (activeContent) activeContent.classList.add('active');
        }}

{js_code}
    </script>
</body>
</html>'''
    return html_content
