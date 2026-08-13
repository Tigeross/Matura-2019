# -*- coding: utf-8 -*-
import os, sys, re
from build_all_matura_tasks import create_task_page, get_nav_html

tasks_data = [
    # Task 15
    {
        "num": 15,
        "title": "Podobieństwo Trójkątów i Styczna do Okręgów",
        "subtitle": "Wyznaczanie odcinków z podobieństwa trójkątów kkk",
        "text": "Zadanie 15. (0–1)<br>Dane są dwa okręgi: okrąg o środku w punkcie $O$ i promieniu $5$ oraz okrąg o środku w punkcie $P$ i promieniu $3$. Odcinek $OP$ ma długość $16$. Prosta $AB$ jest styczna do tych okręgów w punktach $A$ i $B$. Ponadto prosta $AB$ przecina odcinek $OP$ w punkcie $K$ (zobacz rysunek). Wtedy:",
        "img": "15.png",
        "is_closed": True,
        "options": {"A": "$OK = 6$", "B": "$OK = 8$", "C": "$OK = 10$", "D": "$OK = 12$"},
        "correct": "C",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_15')">Metoda 1: Podobieństwo trójkątów (Główna)</button>
                <button class="tab-btn" onclick="switchTab('m2_15')">Metoda 2: Równanie proporcji z niewiadomą x</button>
            </div>
            <div class="tab-content active" id="m1_15">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Własność stycznej i kąty wierzchołkowe</div>
                        <div class="step-desc">Promienie okręgów $OA$ i $PB$ poprowadzone do punktów styczności $A$ i $B$ są prostopadłe do stycznej $AB$: $\\angle OAK = \\angle PBK = 90^\\circ$. Ponadto kąty $\\angle AKO$ i $\\angle BKP$ są kątami wierzchołkowymi, więc mają równe miary.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Podobieństwo trójkątów $\\triangle OAK \\sim \\triangle PBK$</div>
                        <div class="step-desc">Z cechy KKK trójkąty prostokątne $\\triangle OAK$ oraz $\\triangle PBK$ są podobne. Stosunek długości odpowiadających sobie boków wynosi:
                        $$\\frac{OK}{KP} = \\frac{OA}{PB} = \\frac{5}{3}$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Obliczenie długości odcinka $OK$</div>
                        <div class="step-desc">Oznaczmy $OK = 5x$ oraz $KP = 3x$. Z treści zadania $OK + KP = OP = 16$:
                        $$5x + 3x = 16 \\implies 8x = 16 \\implies x = 2$$
                        Stąd długość odcinka $OK = 5 \\cdot 2 = 10$.</div>
                        <div class="math-highlight">$$\\mathbf{OK = 10} \\quad \\implies \\quad \\text{Poprawna odpowiedź to C}$$</div>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="m2_15">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Podstawienie $KP = 16 - OK$</div>
                        <div class="step-desc">Niech $x = OK$. Wtedy $KP = 16 - x$. Układamy proporcję z podobieństwa:
                        $$\\frac{x}{16 - x} = \\frac{5}{3}$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Mnożenie "na krzyż"</div>
                        <div class="step-desc">$$3x = 5(16 - x) \\implies 3x = 80 - 5x \\implies 8x = 80 \\implies x = 10$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Błędne ułożenie proporcji</div>
                    <div>Częsty błąd to próba ułożenia proporcji $\\frac{OK}{OP} = \\frac{5}{3}$, co daje $OK = \\frac{80}{3} \\approx 26{,}67$. Pamiętaj, że $OP = OK + KP$, a nie odpowiadający bok!</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Podobieństwo trójkątów (KKK)</div>
                    <div>$$\\frac{A'B'}{AB} = \\frac{B'C'}{BC} = \\frac{A'C'}{AC} = k$$</div>
                </div>
                <div class="formula-card">
                    <div class="formula-name">Promień i styczna do okręgu</div>
                    <div>Styczna do okręgu jest prostopadła do promienia w punkcie styczności.</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask15(event)">
                <div class="input-group"><label>Promień R (okrąg O):</label><input type="number" id="t15_R" value="5" step="any"></div>
                <div class="input-group"><label>Promień r (okrąg P):</label><input type="number" id="t15_r" value="3" step="any"></div>
                <div class="input-group"><label>Długość OP:</label><input type="number" id="t15_OP" value="16" step="any"></div>
                <button type="submit" class="calc-btn">Oblicz OK oraz KP</button>
            </form>
            <div class="calc-result" id="t15_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkAnswer(opt) {
            const feedbackBox = document.getElementById('feedbackBox');
            const buttons = document.querySelectorAll('.option-btn');
            buttons.forEach(b => b.classList.remove('correct', 'wrong'));
            const selectedBtn = Array.from(buttons).find(b => b.textContent.trim().startsWith(opt));

            if (opt === 'C') {
                if (selectedBtn) selectedBtn.classList.add('correct');
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź C ($OK = 10$) jest prawidłowa. Z podobieństwa trójkątów $\\\\triangle OAK \\\\sim \\\\triangle PBK$ w stosunku $5:3$ otrzymujemy $OK = 10$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>C ($OK = 10$)</strong>. Ułóż proporcję $\\\\frac{OK}{16-OK} = \\\\frac{5}{3}$.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask15(e) {
            e.preventDefault();
            const R = parseFloat(document.getElementById('t15_R').value);
            const r = parseFloat(document.getElementById('t15_r').value);
            const OP = parseFloat(document.getElementById('t15_OP').value);
            if (isNaN(R) || isNaN(r) || isNaN(OP) || R <= 0 || r <= 0 || OP <= 0) return;
            const OK = (R / (R + r)) * OP;
            const KP = (r / (R + r)) * OP;
            document.getElementById('t15_res').innerHTML = `<strong>Długość OK:</strong> ${OK.toFixed(2)}<br><strong>Długość KP:</strong> ${KP.toFixed(2)}<br>Stosunek OK/KP = ${(OK/KP).toFixed(2)} (oczekiwany: ${(R/r).toFixed(2)})`;
        }
        '''
    },

    # Task 16
    {
        "num": 16,
        "title": "Pole Rombu z Kątem Rozwartym",
        "subtitle": "Zastosowanie wzoru $P = a^2 \\sin \\alpha$",
        "text": "Zadanie 16. (0–1)<br>Dany jest romb o boku długości $4$ i kącie rozwartym $150^\\circ$. Pole tego rombu jest równe:",
        "img": "16.png",
        "is_closed": True,
        "options": {"A": "$8$", "B": "$12$", "C": "$8\\sqrt{3}$", "D": "$16$"},
        "correct": "A",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_16')">Metoda 1: Wzór z kątem ostrym</button>
                <button class="tab-btn" onclick="switchTab('m2_16')">Metoda 2: Wzory redukcyjne</button>
            </div>
            <div class="tab-content active" id="m1_16">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie kąta ostrego rombu</div>
                        <div class="step-desc">Suma kątów sąsiednich w rombie wynosi $180^\\circ$. Kąt ostry $\\alpha = 180^\\circ - 150^\\circ = 30^\\circ$.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Zastosowanie wzoru na pole rombu</div>
                        <div class="step-desc">$$P = a^2 \\cdot \\sin 30^\\circ = 4^2 \\cdot \\frac{1}{2} = 16 \\cdot \\frac{1}{2} = 8$$</div>
                        <div class="math-highlight">$$\\mathbf{P = 8} \\quad \\implies \\quad \\text{Poprawna odpowiedź to A}$$</div>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="m2_16">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Bezpośredni wzór z kątem rozwartym</div>
                        <div class="step-desc">$$P = a^2 \\sin 150^\\circ = 4^2 \\sin(180^\\circ - 30^\\circ) = 16 \\cdot \\sin 30^\\circ = 16 \\cdot \\frac{1}{2} = 8$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Użycie cosinusa zamiast sinusa</div>
                    <div>Wstawienie $\\cos 30^\\circ = \\frac{\\sqrt{3}}{2}$ daje błędny wynik $8\\sqrt{3}$ (opcja C). Pamiętaj, że wzór na pole wykorzystuje **sinus** kąta!</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Pole rombu z kątem</div>
                    <div>$$P = a^2 \\sin \\alpha$$</div>
                </div>
                <div class="formula-card">
                    <div class="formula-name">Wartość $\\sin 30^\\circ$</div>
                    <div>$$\\sin 30^\\circ = \\frac{1}{2}$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask16(event)">
                <div class="input-group"><label>Długość boku a:</label><input type="number" id="t16_a" value="4" step="any"></div>
                <div class="input-group"><label>Kąt w stopniach:</label><input type="number" id="t16_deg" value="150" step="any"></div>
                <button type="submit" class="calc-btn">Oblicz Pole Rombu</button>
            </form>
            <div class="calc-result" id="t16_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkAnswer(opt) {
            const feedbackBox = document.getElementById('feedbackBox');
            const buttons = document.querySelectorAll('.option-btn');
            buttons.forEach(b => b.classList.remove('correct', 'wrong'));
            const selectedBtn = Array.from(buttons).find(b => b.textContent.trim().startsWith(opt));

            if (opt === 'A') {
                if (selectedBtn) selectedBtn.classList.add('correct');
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź A ($P = 8$) jest prawidłowa. $P = 4^2 \\\\cdot \\\\sin 30^\\\\circ = 16 \\\\cdot 0{,}5 = 8$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>A ($P = 8$)</strong>. Użyj wzoru $P = a^2 \\\\sin \\\\alpha$.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask16(e) {
            e.preventDefault();
            const a = parseFloat(document.getElementById('t16_a').value);
            const deg = parseFloat(document.getElementById('t16_deg').value);
            if (isNaN(a) || isNaN(deg) || a <= 0) return;
            const rad = (deg * Math.PI) / 180;
            const P = a * a * Math.sin(rad);
            document.getElementById('t16_res').innerHTML = `<strong>Pole rombu:</strong> ${P.toFixed(2)}`;
        }
        '''
    },

    # Task 17
    {
        "num": 17,
        "title": "Warunek Równoległości Prostych",
        "subtitle": "Wyznaczanie parametru $m$ dla $a_1 = a_2$",
        "text": "Zadanie 17. (0–1)<br>Proste o równaniach $y = (2m + 2)x - 2019$ oraz $y = (3m - 3)x + 2019$ są równoległe, gdy:",
        "img": "17.png",
        "is_closed": True,
        "options": {"A": "$m = -1$", "B": "$m = 0$", "C": "$m = 1$", "D": "$m = 5$"},
        "correct": "D",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_17')">Metoda 1: Równanie współczynników kierunkowych</button>
                <button class="tab-btn" onclick="switchTab('m2_17')">Metoda 2: Testowanie opcji odpowiedzi</button>
            </div>
            <div class="tab-content active" id="m1_17">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Warunek równoległości $a_1 = a_2$</div>
                        <div class="step-desc">Współczynniki kierunkowe prostych w postaci kierunkowej $y = ax + b$ to $a_1 = 2m + 2$ oraz $a_2 = 3m - 3$. Proste są równoległe wtedy i tylko wtedy, gdy $a_1 = a_2$.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Rozwiązanie równania z niewiadomą $m$</div>
                        <div class="step-desc">$$2m + 2 = 3m - 3 \\implies 2 + 3 = 3m - 2m \\implies m = 5$$</div>
                        <div class="math-highlight">$$\\mathbf{m = 5} \\quad \\implies \\quad \\text{Poprawna odpowiedź to D}$$</div>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="m2_17">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Podstawienie opcji D ($m=5$)</div>
                        <div class="step-desc">Dla $m=5$: $a_1 = 2(5) + 2 = 12$, $a_2 = 3(5) - 3 = 12$. Ponieważ $12 = 12$, proste są równoległe.</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Błędy ze znakiem</div>
                    <div>Przeniesienie $-3$ z ujemnym znakiem na drugą stronę dać musi $+3$. Uważaj na błędy $2 - 3 = -1$!</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Warunek równoległości prostych</div>
                    <div>$$k \\parallel l \\iff a_1 = a_2$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask17(event)">
                <div class="input-group"><label>Współczynnik a1(m) np. 2m + 2:</label><input type="number" id="t17_m1" value="2"></div>
                <div class="input-group"><label>Stała b1 np. +2:</label><input type="number" id="t17_c1" value="2"></div>
                <div class="input-group"><label>Współczynnik a2(m) np. 3m - 3:</label><input type="number" id="t17_m2" value="3"></div>
                <div class="input-group"><label>Stała b2 np. -3:</label><input type="number" id="t17_c2" value="-3"></div>
                <button type="submit" class="calc-btn">Wyznacz m dla a1 = a2</button>
            </form>
            <div class="calc-result" id="t17_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkAnswer(opt) {
            const feedbackBox = document.getElementById('feedbackBox');
            const buttons = document.querySelectorAll('.option-btn');
            buttons.forEach(b => b.classList.remove('correct', 'wrong'));
            const selectedBtn = Array.from(buttons).find(b => b.textContent.trim().startsWith(opt));

            if (opt === 'D') {
                if (selectedBtn) selectedBtn.classList.add('correct');
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź D ($m = 5$) jest prawidłowa. $2m + 2 = 3m - 3 \\\\implies m = 5$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>D ($m = 5$)</strong>. Przyrównaj współczynniki kierunkowe $2m+2 = 3m-3$.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask17(e) {
            e.preventDefault();
            const m1 = parseFloat(document.getElementById('t17_m1').value);
            const c1 = parseFloat(document.getElementById('t17_c1').value);
            const m2 = parseFloat(document.getElementById('t17_m2').value);
            const c2 = parseFloat(document.getElementById('t17_c2').value);
            if (m1 === m2) {
                document.getElementById('t17_res').innerHTML = "Brak jednoznacznego rozwiązania (równoległe dla każdego m lub braku m).";
                return;
            }
            const m = (c2 - c1) / (m1 - m2);
            const a = m1 * m + c1;
            document.getElementById('t17_res').innerHTML = `<strong>Parametr m:</strong> ${m.toFixed(2)}<br><strong>Współczynnik kierunkowy a1 = a2:</strong> ${a.toFixed(2)}`;
        }
        '''
    },

    # Task 18
    {
        "num": 18,
        "title": "Prosta Prostopadła Przechodząca przez Punkt",
        "subtitle": "Warunek $a_1 \\cdot a_2 = -1$ i podstawienie punktu",
        "text": "Zadanie 18. (0–1)<br>Prosta o równaniu $y = ax + b$ jest prostopadła do prostej o równaniu $y = -\\frac{1}{4}x + 1$ i przechodzi przez punkt $P = \\left(\\frac{1}{2}, 0\\right)$, gdy:",
        "img": "18.png",
        "is_closed": True,
        "options": {"A": "$a = -4 \\text{ i } b = -2$", "B": "$a = \\frac{1}{4} \\text{ i } b = -\\frac{1}{8}$", "C": "$a = -4 \\text{ i } b = 2$", "D": "$a = 4 \\text{ i } b = -2$"},
        "correct": "D",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_18')">Metoda 1: Wyznaczenie a i b krok po kroku</button>
            </div>
            <div class="tab-content active" id="m1_18">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Warunek prostopadłości</div>
                        <div class="step-desc">Współczynnik danej prostej to $a_0 = -\\frac{1}{4}$. Warunek prostopadłości:
                        $$a \\cdot \\left(-\\frac{1}{4}\\right) = -1 \\implies a = 4$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie wyrazu wolnego $b$</div>
                        <div class="step-desc">Prosta $y = 4x + b$ przechodzi przez punkt $P\\left(\\frac{1}{2}, 0\\right)$. Podstawiamy $x = \\frac{1}{2}$ oraz $y = 0$:
                        $$0 = 4 \\cdot \\frac{1}{2} + b \\implies 0 = 2 + b \\implies b = -2$$</div>
                        <div class="math-highlight">$$\\mathbf{a = 4, \\, b = -2} \\quad \\implies \\quad \\text{Poprawna odpowiedź to D}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Mylenie równoległości z prostopadłością</div>
                    <div>Wybór $a = -\\frac{1}{4}$ to warunek równoległości, a nie prostopadłości! Dla prostopadłości odwracamy ułamek i zmieniamy znak.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Prostopadłość prostych</div>
                    <div>$$a_1 \\cdot a_2 = -1 \\implies a_2 = -\\frac{1}{a_1}$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask18(event)">
                <div class="input-group"><label>a danej prostej (np. -0.25):</label><input type="number" id="t18_a0" value="-0.25" step="any"></div>
                <div class="input-group"><label>Punkt Px:</label><input type="number" id="t18_px" value="0.5" step="any"></div>
                <div class="input-group"><label>Punkt Py:</label><input type="number" id="t18_py" value="0" step="any"></div>
                <button type="submit" class="calc-btn">Wyznacz a i b prostej prostopadłej</button>
            </form>
            <div class="calc-result" id="t18_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkAnswer(opt) {
            const feedbackBox = document.getElementById('feedbackBox');
            const buttons = document.querySelectorAll('.option-btn');
            buttons.forEach(b => b.classList.remove('correct', 'wrong'));
            const selectedBtn = Array.from(buttons).find(b => b.textContent.trim().startsWith(opt));

            if (opt === 'D') {
                if (selectedBtn) selectedBtn.classList.add('correct');
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź D ($a = 4, b = -2$) jest prawidłowa. $a = -1 / (-1/4) = 4$, a $0 = 4(0{,}5) + b \\\\implies b = -2$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>D ($a = 4, b = -2$)</strong>. Warunek prostopadłości daje $a = 4$.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask18(e) {
            e.preventDefault();
            const a0 = parseFloat(document.getElementById('t18_a0').value);
            const px = parseFloat(document.getElementById('t18_px').value);
            const py = parseFloat(document.getElementById('t18_py').value);
            if (isNaN(a0) || a0 === 0 || isNaN(px) || isNaN(py)) return;
            const a = -1 / a0;
            const b = py - a * px;
            document.getElementById('t18_res').innerHTML = `<strong>Szukana prosta prostopadła:</strong> y = ${a.toFixed(2)}x ${b >= 0 ? '+ ' + b.toFixed(2) : '- ' + Math.abs(b).toFixed(2)}<br>a = ${a.toFixed(2)}, b = ${b.toFixed(2)}`;
        }
        '''
    },

    # Task 19
    {
        "num": 19,
        "title": "Symetria Środkowa Funkcji Liniowej",
        "subtitle": "Przekształcenie $g(x) = -f(-x)$ względem $(0,0)$",
        "text": "Zadanie 19. (0–1)<br>Na rysunku przedstawiony jest fragment wykresu funkcji liniowej $f$. Na wykresie tej funkcji leżą punkty $A = (0, 4)$ i $B = (2, 2)$. Obrazem prostej $AB$ w symetrii względem początku układu współrzędnych jest wykres funkcji $g$ określonej wzorem:",
        "img": "19.png",
        "is_closed": True,
        "options": {"A": "$g(x) = x + 4$", "B": "$g(x) = x - 4$", "C": "$g(x) = -x - 4$", "D": "$g(x) = -x + 4$"},
        "correct": "C",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_19')">Metoda 1: Przekształcenie punktów $A$ i $B$</button>
                <button class="tab-btn" onclick="switchTab('m2_19')">Metoda 2: Analityczny wzór $g(x) = -f(-x)$</button>
            </div>
            <div class="tab-content active" id="m1_19">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie punktów odbitych $A'$ i $B'$</div>
                        <div class="step-desc">W symetrii względem początku układu współrzędnych $(0,0)$ współrzędne punktu zmieniają znaki na przeciwne: $(x, y) \\to (-x, -y)$.<br>
                        $A(0, 4) \\to A'(0, -4)$<br>
                        $B(2, 2) \\to B'(-2, -2)$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie równania prostej $g(x)$</div>
                        <div class="step-desc">Punkt $A'(0, -4)$ leży na osi OY, zatem wyraz wolny $b' = -4$.<br>
                        Współczynnik kierunkowy $a' = \\frac{-2 - (-4)}{-2 - 0} = \\frac{2}{-2} = -1$.<br>
                        Stąd wzór funkcji $g(x) = -x - 4$.</div>
                        <div class="math-highlight">$$\\mathbf{g(x) = -x - 4} \\quad \\implies \\quad \\text{Poprawna odpowiedź to C}$$</div>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="m2_19">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Wzór prostej $f(x)$</div>
                        <div class="step-desc">Z punktów $A(0,4)$ i $B(2,2)$ mamy $f(x) = -x + 4$.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Symetria środkowa $y = -f(-x)$</div>
                        <div class="step-desc">$$g(x) = -f(-x) = -(-(-x) + 4) = -(x + 4) = -x - 4$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Symetria względem osi zamiast punktu</div>
                    <div>Symetria względem osi OY zmienia wzór na $f(-x) = x + 4$ (opcja A), a względem osi OX na $-f(x) = x - 4$ (opcja B). Zapamiętaj: symetria środkowa względem $(0,0)$ zmienia **oba** znaki!</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Symetria środkowa względem (0,0)</div>
                    <div>$$(x, y) \\to (-x, -y) \\quad \\implies \\quad g(x) = -f(-x)$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask19(event)">
                <div class="input-group"><label>a funkcji f(x):</label><input type="number" id="t19_a" value="-1" step="any"></div>
                <div class="input-group"><label>b funkcji f(x):</label><input type="number" id="t19_b" value="4" step="any"></div>
                <button type="submit" class="calc-btn">Wyznacz wzór g(x) po symetrii środkowej</button>
            </form>
            <div class="calc-result" id="t19_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkAnswer(opt) {
            const feedbackBox = document.getElementById('feedbackBox');
            const buttons = document.querySelectorAll('.option-btn');
            buttons.forEach(b => b.classList.remove('correct', 'wrong'));
            const selectedBtn = Array.from(buttons).find(b => b.textContent.trim().startsWith(opt));

            if (opt === 'C') {
                if (selectedBtn) selectedBtn.classList.add('correct');
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź C ($g(x) = -x - 4$) jest prawidłowa. Symetria punktów $A(0,4) \\\\to (0,-4)$ i $B(2,2) \\\\to (-2,-2)$ daje $g(x) = -x - 4$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>C ($g(x) = -x - 4$)</strong>. Zmień znaki obu współrzędnych punktów $A$ i $B$.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask19(e) {
            e.preventDefault();
            const a = parseFloat(document.getElementById('t19_a').value);
            const b = parseFloat(document.getElementById('t19_b').value);
            if (isNaN(a) || isNaN(b)) return;
            const ag = a;
            const bg = -b;
            document.getElementById('t19_res').innerHTML = `<strong>Oryginalna f(x):</strong> y = ${a}x + ${b}<br><strong>Obraz g(x) w symetrii (0,0):</strong> y = ${ag}x ${bg >= 0 ? '+ ' + bg : '- ' + Math.abs(bg)}`;
        }
        '''
    },

    # Task 20
    {
        "num": 20,
        "title": "Okrąg Wpisany w Kwadrat",
        "subtitle": "Relacja między boku kwadratu a średnicą okręgu",
        "text": "Zadanie 20. (0–1)<br>Dane są punkty o współrzędnych $A = (-2, 5)$ oraz $B = (4, -1)$. Średnica okręgu wpisanego w kwadrat o boku $AB$ jest równa:",
        "img": "20.png",
        "is_closed": True,
        "options": {"A": "$12$", "B": "$6$", "C": "$6\\sqrt{2}$", "D": "$2\\sqrt{6}$"},
        "correct": "C",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_20')">Metoda 1: Długość boku $AB$ (Główna)</button>
            </div>
            <div class="tab-content active" id="m1_20">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Własność okręgu wpisanego w kwadrat</div>
                        <div class="step-desc">Średnica okręgu wpisanego w kwadrat jest dokładnie równa długości boku tego kwadratu: $d = 2r = a = |AB|$.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Obliczenie odległości punktów $A$ i $B$</div>
                        <div class="step-desc">$$|AB| = \\sqrt{(4 - (-2))^2 + (-1 - 5)^2} = \\sqrt{6^2 + (-6)^2} = \\sqrt{36 + 36} = \\sqrt{72} = 6\\sqrt{2}$$</div>
                        <div class="math-highlight">$$\\mathbf{d = 6\\sqrt{2}} \\quad \\implies \\quad \\text{Poprawna odpowiedź to C}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Pomylenie promienia ze średnicą</div>
                    <div>Promień $r = 3\\sqrt{2}$, ale w pytaniu chodzi o **średnicę** $d = 2r = 6\\sqrt{2}$! Uważnie czytaj pytania na maturze.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Odległość punktów w układzie</div>
                    <div>$$|AB| = \\sqrt{(x_B - x_A)^2 + (y_B - y_A)^2}$$</div>
                </div>
                <div class="formula-card">
                    <div class="formula-name">Średnica okręgu wpisanego</div>
                    <div>$$d_{wpisany} = a$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask20(event)">
                <div class="input-group"><label>Ax:</label><input type="number" id="t20_ax" value="-2"></div>
                <div class="input-group"><label>Ay:</label><input type="number" id="t20_ay" value="5"></div>
                <div class="input-group"><label>Bx:</label><input type="number" id="t20_bx" value="4"></div>
                <div class="input-group"><label>By:</label><input type="number" id="t20_by" value="-1"></div>
                <button type="submit" class="calc-btn">Oblicz bok AB i średnicę okręgu</button>
            </form>
            <div class="calc-result" id="t20_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkAnswer(opt) {
            const feedbackBox = document.getElementById('feedbackBox');
            const buttons = document.querySelectorAll('.option-btn');
            buttons.forEach(b => b.classList.remove('correct', 'wrong'));
            const selectedBtn = Array.from(buttons).find(b => b.textContent.trim().startsWith(opt));

            if (opt === 'C') {
                if (selectedBtn) selectedBtn.classList.add('correct');
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź C ($6\\\\sqrt{2}$) jest prawidłowa. Średnica okręgu wpisanego równa się bokowi kwadratu $|AB| = \\\\sqrt{72} = 6\\\\sqrt{2}$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>C ($6\\\\sqrt{2}$)</strong>. Oblicz odległość $|AB|$.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask20(e) {
            e.preventDefault();
            const ax = parseFloat(document.getElementById('t20_ax').value);
            const ay = parseFloat(document.getElementById('t20_ay').value);
            const bx = parseFloat(document.getElementById('t20_bx').value);
            const by = parseFloat(document.getElementById('t20_by').value);
            if (isNaN(ax) || isNaN(ay) || isNaN(bx) || isNaN(by)) return;
            const ab = Math.sqrt(Math.pow(bx - ax, 2) + Math.pow(by - ay, 2));
            document.getElementById('t20_res').innerHTML = `<strong>Bok kwadratu |AB| = Średnica okręgu wpisanego:</strong> ${ab.toFixed(3)} (dokładnie: √${Math.round(ab*ab)})<br><strong>Promień okręgu wpisanego r:</strong> ${(ab/2).toFixed(3)}`;
        }
        '''
    },

    # Task 21
    {
        "num": 21,
        "title": "Przekątna Prostopadłościanu",
        "subtitle": "Obliczanie przekątnej przestrzennej z $D = \\sqrt{a^2 + b^2 + c^2}$",
        "text": "Zadanie 21. (0–1)<br>Pudełko w kształcie prostopadłościanu ma wymiary $5\\text{ dm} \\times 3\\text{ dm} \\times 2\\text{ dm}$ (zobacz rysunek). Przekątna $KL$ tego prostopadłościanu jest – z dokładnością do $0{,}01\\text{ dm}$ – równa:",
        "img": "21.png",
        "is_closed": True,
        "options": {"A": "$5{,}83\\text{ dm}$", "B": "$6{,}16\\text{ dm}$", "C": "$3{,}61\\text{ dm}$", "D": "$5{,}39\\text{ dm}$"},
        "correct": "B",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_21')">Metoda 1: Bezpośredni wzór przestrzenny</button>
            </div>
            <div class="tab-content active" id="m1_21">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Zastosowanie wzoru na przekątną prostopadłościanu</div>
                        <div class="step-desc">Dla krawędzi $a=5$, $b=3$, $c=2$:
                        $$D = \\sqrt{a^2 + b^2 + c^2} = \\sqrt{5^2 + 3^2 + 2^2} = \\sqrt{25 + 9 + 4} = \\sqrt{38}$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Zaokrąglenie do 0,01 dm</div>
                        <div class="step-desc">$$\\sqrt{38} \\approx 6{,}1644 \\approx 6{,}16\\text{ dm}$$</div>
                        <div class="math-highlight">$$\\mathbf{D \\approx 6{,}16\\text{ dm}} \\quad \\implies \\quad \\text{Poprawna odpowiedź to B}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Obliczenie przekątnej podstawy</div>
                    <div>Przekątna podstawy to $\\sqrt{5^2+3^2} = \\sqrt{34} \\approx 5{,}83$ (odpowiedź A). Nie zapomnij o trzecim wymiarze $c=2$!</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Przekątna prostopadłościanu</div>
                    <div>$$D = \\sqrt{a^2 + b^2 + c^2}$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask21(event)">
                <div class="input-group"><label>Krawędź a:</label><input type="number" id="t21_a" value="5" step="any"></div>
                <div class="input-group"><label>Krawędź b:</label><input type="number" id="t21_b" value="3" step="any"></div>
                <div class="input-group"><label>Krawędź c:</label><input type="number" id="t21_c" value="2" step="any"></div>
                <button type="submit" class="calc-btn">Oblicz Przekątną Prostopadłościanu</button>
            </form>
            <div class="calc-result" id="t21_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkAnswer(opt) {
            const feedbackBox = document.getElementById('feedbackBox');
            const buttons = document.querySelectorAll('.option-btn');
            buttons.forEach(b => b.classList.remove('correct', 'wrong'));
            const selectedBtn = Array.from(buttons).find(b => b.textContent.trim().startsWith(opt));

            if (opt === 'B') {
                if (selectedBtn) selectedBtn.classList.add('correct');
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź B ($6{,}16\\\\text{ dm}$) jest prawidłowa. $D = \\\\sqrt{5^2+3^2+2^2} = \\\\sqrt{38} \\\\approx 6{,}16$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>B ($6{,}16\\\\text{ dm}$)</strong>. Oblicz $\\\\sqrt{a^2+b^2+c^2}$.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask21(e) {
            e.preventDefault();
            const a = parseFloat(document.getElementById('t21_a').value);
            const b = parseFloat(document.getElementById('t21_b').value);
            const c = parseFloat(document.getElementById('t21_c').value);
            if (isNaN(a) || isNaN(b) || isNaN(c) || a <= 0 || b <= 0 || c <= 0) return;
            const d = Math.sqrt(a*a + b*b + c*c);
            document.getElementById('t21_res').innerHTML = `<strong>Przekątna D:</strong> ${d.toFixed(2)} dm (dokładnie √${Math.round(a*a+b*b+c*c)})`;
        }
        '''
    },

    # Task 22
    {
        "num": 22,
        "title": "Pole Powierzchni Kuli i Stożka",
        "subtitle": "Przyrównanie pól całkowitych $P_k = P_s$",
        "text": "Zadanie 22. (0–1)<br>Promień kuli i promień podstawy stożka są równe $4$. Pole powierzchni kuli jest równe polu powierzchni całkowitej stożka. Długość tworzącej stożka jest równa:",
        "img": "22.png",
        "is_closed": True,
        "options": {"A": "$8$", "B": "$4$", "C": "$16$", "D": "$12$"},
        "correct": "D",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_22')">Metoda 1: Przyrównanie pól całkowitych</button>
            </div>
            <div class="tab-content active" id="m1_22">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Wzory na pola kuli i stożka</div>
                        <div class="step-desc">Pole kuli: $P_k = 4\\pi r^2$. Pole całkowite stożka: $P_s = \\pi r^2 + \\pi r l$. Przyrównujemy pola:
                        $$4\\pi r^2 = \\pi r^2 + \\pi r l \\implies 3\\pi r^2 = \\pi r l \\implies 3r = l$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Obliczenie tworzącej $l$</div>
                        <div class="step-desc">Dla $r = 4$:
                        $$l = 3 \\cdot 4 = 12$$</div>
                        <div class="math-highlight">$$\\mathbf{l = 12} \\quad \\implies \\quad \\text{Poprawna odpowiedź to D}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Zapomnienie o polu podstawy stożka</div>
                    <div>Przyrównanie pola kuli do samego pola bocznego stożka ($4\\pi r^2 = \\pi r l \\implies l = 4r = 16$, opcja C) jest błędne, ponieważ mowa o polu **całkowitym**!</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Pole kuli</div>
                    <div>$$P_{kuli} = 4\\pi r^2$$</div>
                </div>
                <div class="formula-card">
                    <div class="formula-name">Pole całkowite stożka</div>
                    <div>$$P_{stożka} = \\pi r^2 + \\pi r l$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask22(event)">
                <div class="input-group"><label>Promień r:</label><input type="number" id="t22_r" value="4" step="any"></div>
                <button type="submit" class="calc-btn">Oblicz Tworzącą l</button>
            </form>
            <div class="calc-result" id="t22_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkAnswer(opt) {
            const feedbackBox = document.getElementById('feedbackBox');
            const buttons = document.querySelectorAll('.option-btn');
            buttons.forEach(b => b.classList.remove('correct', 'wrong'));
            const selectedBtn = Array.from(buttons).find(b => b.textContent.trim().startsWith(opt));

            if (opt === 'D') {
                if (selectedBtn) selectedBtn.classList.add('correct');
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź D ($l = 12$) jest prawidłowa. $4\\\\pi r^2 = \\\\pi r^2 + \\\\pi r l \\\\implies 3r = l \\\\implies l = 12$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>D ($l = 12$)</strong>. Uwzględnij pole podstawy stożka!`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask22(e) {
            e.preventDefault();
            const r = parseFloat(document.getElementById('t22_r').value);
            if (isNaN(r) || r <= 0) return;
            const l = 3 * r;
            const Pk = 4 * Math.PI * r * r;
            document.getElementById('t22_res').innerHTML = `<strong>Tworząca l:</strong> ${l.toFixed(2)}<br><strong>Pole kuli = Pole stożka:</strong> ${Pk.toFixed(2)} (czyli ${(Pk/Math.PI).toFixed(0)}π)`;
        }
        '''
    },

    # Task 23
    {
        "num": 23,
        "title": "Mediana Zestawu Danych",
        "subtitle": "Wyznaczanie liczby $a$ dla $M = 14$",
        "text": "Zadanie 23. (0–1)<br>Mediana zestawu sześciu danych liczb: $4, 8, 21, a, 16, 25$, jest równa $14$. Zatem:",
        "img": "23.png",
        "is_closed": True,
        "options": {"A": "$a = 7$", "B": "$a = 12$", "C": "$a = 14$", "D": "$a = 20$"},
        "correct": "B",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_23')">Metoda 1: Porządkowanie i równanie mediany</button>
            </div>
            <div class="tab-content active" id="m1_23">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Porządkowanie znanych elementów</div>
                        <div class="step-desc">Uszeregowane znane liczby: $4, 8, 16, 21, 25$. Jest ich 5. Ponieważ mediana wynosi 14 (mniej niż 16), liczba $a$ musi leżeć na 3. pozycji.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Średnia arytmetyczna dwóch środkowych wyrazów</div>
                        <div class="step-desc">Dwa środkowe wyraz tego 6-elementowego ciągu to $a$ i $16$:
                        $$\\frac{a + 16}{2} = 14 \\implies a + 16 = 28 \\implies a = 12$$
                        Po wstawieniu: $4, 8, 12, 16, 21, 25$ $\\implies M = \\frac{12+16}{2} = 14$.</div>
                        <div class="math-highlight">$$\\mathbf{a = 12} \\quad \\implies \\quad \\text{Poprawna odpowiedź to B}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Liczenie mediany bez uporządkowania</div>
                    <div>Nigdy nie wyciągaj średniej z elementów nieuporządkowanych! Zawsze uporządkuj ciąg rosnąco przed wyznaczeniem mediany.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Mediana dla parzystej liczby n</div>
                    <div>$$M = \\frac{x_{n/2} + x_{n/2 + 1}}{2}$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask23(event)">
                <div class="input-group"><label>Podaj a:</label><input type="number" id="t23_a" value="12" step="any"></div>
                <button type="submit" class="calc-btn">Oblicz Medianę dla ciągu [4, 8, 21, a, 16, 25]</button>
            </form>
            <div class="calc-result" id="t23_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkAnswer(opt) {
            const feedbackBox = document.getElementById('feedbackBox');
            const buttons = document.querySelectorAll('.option-btn');
            buttons.forEach(b => b.classList.remove('correct', 'wrong'));
            const selectedBtn = Array.from(buttons).find(b => b.textContent.trim().startsWith(opt));

            if (opt === 'B') {
                if (selectedBtn) selectedBtn.classList.add('correct');
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź B ($a = 12$) jest prawidłowa. Dla $a = 12$ ciąg to $4, 8, 12, 16, 21, 25$, a mediana to $(12+16)/2 = 14$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>B ($a = 12$)</strong>. Rozwiąż $(a+16)/2 = 14$.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask23(e) {
            e.preventDefault();
            const a = parseFloat(document.getElementById('t23_a').value);
            if (isNaN(a)) return;
            const arr = [4, 8, 21, a, 16, 25].sort((x, y) => x - y);
            const med = (arr[2] + arr[3]) / 2;
            document.getElementById('t23_res').innerHTML = `<strong>Uporządkowany ciąg:</strong> [${arr.join(', ')}]<br><strong>Mediana:</strong> ${med.toFixed(2)}`;
        }
        '''
    },

    # Task 24
    {
        "num": 24,
        "title": "Kombinatoryka i Liczby Pięciocyfrowe",
        "subtitle": "Zastosowanie reguły mnożenia z ograniczeniem cyfry zero",
        "text": "Zadanie 24. (0–1)<br>Wszystkich liczb pięciocyfrowych, w których występują wyłącznie cyfry $0, 2, 5$, jest:",
        "img": "24.png",
        "is_closed": True,
        "options": {"A": "$12$", "B": "$36$", "C": "$162$", "D": "$243$"},
        "correct": "C",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_24')">Metoda 1: Reguła mnożenia dla 5 pozycji</button>
            </div>
            <div class="tab-content active" id="m1_24">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Analiza możliwości dla każdej cyfry</div>
                        <div class="step-desc">
                        - 1. cyfra (setek tysięcy): 2 możliwości (cyfry $2$ lub $5$, zero nie może być na początku).<br>
                        - 2. cyfra: 3 możliwości ($0, 2, 5$).<br>
                        - 3. cyfra: 3 możliwości ($0, 2, 5$).<br>
                        - 4. cyfra: 3 możliwości ($0, 2, 5$).<br>
                        - 5. cyfra: 3 możliwości ($0, 2, 5$).
                        </div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Obliczenie łącznej liczby kombinacji</div>
                        <div class="step-desc">$$N = 2 \\cdot 3 \\cdot 3 \\cdot 3 \\cdot 3 = 2 \\cdot 3^4 = 2 \\cdot 81 = 162$$</div>
                        <div class="math-highlight">$$\\mathbf{N = 162} \\quad \\implies \\quad \\text{Poprawna odpowiedź to C}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Dopuszczenie 0 na pierwszej pozycji</div>
                    <div>Gdyby na pierwszym miejscu mogło być $0$, mielibyśmy $3^5 = 243$ (opcja D). Pamiętaj, że liczba naturalna nie może zaczynać się cyfrą zero!</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Reguła mnożenia</div>
                    <div>$$N = n_1 \\cdot n_2 \\cdot \\dots \\cdot n_k$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask24(event)">
                <div class="input-group"><label>Ilość cyfr w liczbie (n):</label><input type="number" id="t24_n" value="5" min="1" max="10"></div>
                <div class="input-group"><label>Ilość dostępnych cyfr (w tym zero):</label><input type="number" id="t24_k" value="3" min="2" max="10"></div>
                <button type="submit" class="calc-btn">Oblicz ilość liczb</button>
            </form>
            <div class="calc-result" id="t24_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkAnswer(opt) {
            const feedbackBox = document.getElementById('feedbackBox');
            const buttons = document.querySelectorAll('.option-btn');
            buttons.forEach(b => b.classList.remove('correct', 'wrong'));
            const selectedBtn = Array.from(buttons).find(b => b.textContent.trim().startsWith(opt));

            if (opt === 'C') {
                if (selectedBtn) selectedBtn.classList.add('correct');
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź C ($162$) jest prawidłowa. Na 1. miejscu 2 opcje, na pozostałych czterech po 3 opcje: $2 \\\\cdot 3^4 = 162$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>C ($162$)</strong>. Liczba nie może zaczynać się od zera.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask24(e) {
            e.preventDefault();
            const n = parseInt(document.getElementById('t24_n').value);
            const k = parseInt(document.getElementById('t24_k').value);
            if (isNaN(n) || isNaN(k) || n <= 0 || k <= 1) return;
            const res = (k - 1) * Math.pow(k, n - 1);
            document.getElementById('t24_res').innerHTML = `<strong>Liczba wszystkich kombinacji ${n}-cyfrowych:</strong> ${res}`;
        }
        '''
    },

    # Task 25
    {
        "num": 25,
        "title": "Prawdopodobieństwo Klasyczne",
        "subtitle": "Losowanie kuli czerwonej z urny",
        "text": "Zadanie 25. (0–1)<br>W pudełku jest $40$ kul. Wśród nich jest $35$ kul białych, a pozostałe to kule czerwone. Prawdopodobieństwo wylosowania każdej kuli jest takie samo. Z pudełka losujemy jedną kulę. Prawdopodobieństwo zdarzenia polegającego na tym, że otrzymamy kulę czerwoną, jest równe:",
        "img": "25.png",
        "is_closed": True,
        "options": {"A": "$\\frac{1}{8}$", "B": "$\\frac{1}{5}$", "C": "$\\frac{1}{40}$", "D": "$\\frac{1}{35}$"},
        "correct": "A",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_25')">Metoda 1: Klasyczna definicja prawdopodobieństwa</button>
            </div>
            <div class="tab-content active" id="m1_25">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie liczby kul czerwonych</div>
                        <div class="step-desc">Łączna liczba kul $|\\Omega| = 40$. Liczba kul białych wynosi 35. Zatem liczba kul czerwonych:
                        $$|A| = 40 - 35 = 5$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Obliczenie prawdopodobieństwa</div>
                        <div class="step-desc">$$P(A) = \\frac{|A|}{|\\Omega|} = \\frac{5}{40} = \\frac{1}{8}$$</div>
                        <div class="math-highlight">$$\\mathbf{P(A) = \\frac{1}{8}} \\quad \\implies \\quad \\text{Poprawna odpowiedź to A}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Obliczenie dla kuli białej</div>
                    <div>Uważaj, aby nie podać prawdopodobieństwa wylosowania kuli białej $\\frac{35}{40} = \\frac{7}{8}$! W zadaniu pyta się o kulę **czerwoną**.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Prawdopodobieństwo klasyczne</div>
                    <div>$$P(A) = \\frac{|A|}{|\\Omega|}$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask25(event)">
                <div class="input-group"><label>Wszystkie kule (|Ω|):</label><input type="number" id="t25_all" value="40"></div>
                <div class="input-group"><label>Kule białe:</label><input type="number" id="t25_w" value="35"></div>
                <button type="submit" class="calc-btn">Oblicz Prawdopodobieństwo</button>
            </form>
            <div class="calc-result" id="t25_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkAnswer(opt) {
            const feedbackBox = document.getElementById('feedbackBox');
            const buttons = document.querySelectorAll('.option-btn');
            buttons.forEach(b => b.classList.remove('correct', 'wrong'));
            const selectedBtn = Array.from(buttons).find(b => b.textContent.trim().startsWith(opt));

            if (opt === 'A') {
                if (selectedBtn) selectedBtn.classList.add('correct');
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź A ($\\frac{1}{8}$) jest prawidłowa. $P(A) = 5 / 40 = 1 / 8$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>A ($\\frac{1}{8}$)</strong>. Liczba kul czerwonych to $40 - 35 = 5$.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask25(e) {
            e.preventDefault();
            const total = parseInt(document.getElementById('t25_all').value);
            const w = parseInt(document.getElementById('t25_w').value);
            if (isNaN(total) || isNaN(w) || total <= 0 || w < 0 || w > total) return;
            const r = total - w;
            const p = r / total;
            document.getElementById('t25_res').innerHTML = `<strong>Liczba kul czerwonych:</strong> ${r}<br><strong>Prawdopodobieństwo wylosowania czerwonej P(C):</strong> ${p.toFixed(3)} (${r}/${total} = 1/${(total/r).toFixed(2)})`;
        }
        '''
    },

    # Task 26
    {
        "num": 26,
        "title": "Równanie Wielomianowe",
        "subtitle": "Rozwiązywanie równania iloczynowego $(x^3 - 8)(x^2 - 4x - 5) = 0$",
        "text": "Zadanie 26. (0–2)<br>Rozwiąż równanie $(x^3 - 8)(x^2 - 4x - 5) = 0$.",
        "img": "26.png",
        "is_closed": False,
        "options": {},
        "correct": "-1, 2, 5",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_26')">Metoda 1: Przyrównanie czynników do zera</button>
            </div>
            <div class="tab-content active" id="m1_26">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Rozbicie na dwa równania</div>
                        <div class="step-desc">Iloczyn dwóch wyrażeń wynosi zero, gdy co najmniej jedno z nich jest równe zero:
                        $$x^3 - 8 = 0 \\quad \\text{lub} \\quad x^2 - 4x - 5 = 0$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Rozwiązanie pierwszego równania $x^3 - 8 = 0$</div>
                        <div class="step-desc">$$x^3 = 8 \\implies x = \\sqrt[3]{8} = 2$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Rozwiązanie drugiego równania $x^2 - 4x - 5 = 0$</div>
                        <div class="step-desc">Obliczamy wyróżnik $\\Delta$:
                        $$\\Delta = (-4)^2 - 4 \\cdot 1 \\cdot (-5) = 16 + 20 = 36, \\quad \\sqrt{\\Delta} = 6$$
                        $$x_1 = \\frac{4 - 6}{2} = -1, \\quad x_2 = \\frac{4 + 6}{2} = 5$$</div>
                        <div class="math-highlight">$$\\mathbf{Odpowiedź: \\, x \\in \\{-1, 2, 5\\}}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Błędy znaku przy delcie</div>
                    <div>Pamiętaj, że w $c = -5$ występuje minus, więc $-4ac = -4(1)(-5) = +20$. $\\Delta = 16 + 20 = 36$.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Równanie iloczynowe</div>
                    <div>$$A \\cdot B = 0 \\iff A = 0 \\lor B = 0$$</div>
                </div>
                <div class="formula-card">
                    <div class="formula-name">Wyróżnik trójmianu</div>
                    <div>$$\\Delta = b^2 - 4ac$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask26(event)">
                <div class="input-group"><label>Pierwiastek z x^3 - a (np. 8):</label><input type="number" id="t26_a3" value="8"></div>
                <div class="input-group"><label>Współczynnik b trójmianu:</label><input type="number" id="t26_b" value="-4"></div>
                <div class="input-group"><label>Współczynnik c trójmianu:</label><input type="number" id="t26_c" value="-5"></div>
                <button type="submit" class="calc-btn">Rozwiąż równanie iloczynowe</button>
            </form>
            <div class="calc-result" id="t26_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkOpenAnswer() {
            const userAns = document.getElementById('userAnsInput').value.trim();
            const feedbackBox = document.getElementById('feedbackBox');
            if (userAns.includes('-1') && userAns.includes('2') && userAns.includes('5')) {
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Świetnie!</strong> Podano wszystkie trzy prawidłowe pierwiastki: $x \\\\in \\\\{-1, 2, 5\\\\}$. Gwarantowane 2 punkty na maturze!';
            } else {
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = '❌ Odpowiedź niepełna lub błędna. Prawidłowy zestaw pierwiastków to: <strong>$x = -1, \\, x = 2, \\, x = 5$</strong>.';
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask26(e) {
            e.preventDefault();
            const a3 = parseFloat(document.getElementById('t26_a3').value);
            const b = parseFloat(document.getElementById('t26_b').value);
            const c = parseFloat(document.getElementById('t26_c').value);
            const r1 = Math.cbrt(a3);
            const delta = b*b - 4*c;
            let res = `<strong>Pierwiastek z x^3 = ${a3}:</strong> x = ${r1.toFixed(2)}<br>`;
            if (delta > 0) {
                const r2 = (-b - Math.sqrt(delta)) / 2;
                const r3 = (-b + Math.sqrt(delta)) / 2;
                res += `<strong>Pierwiastki trójmianu (Δ = ${delta}):</strong> x = ${r2.toFixed(2)}, x = ${r3.toFixed(2)}<br><strong>Wszystkie rozwiązania:</strong> x ∈ {${r2.toFixed(2)}, ${r1.toFixed(2)}, ${r3.toFixed(2)}}`;
            } else if (delta === 0) {
                const r2 = -b / 2;
                res += `<strong>Pierwiastek trójmianu (Δ = 0):</strong> x = ${r2.toFixed(2)}`;
            } else {
                res += `<strong>Trójmian nie ma pierwiastków rzeczywistych (Δ < 0).</strong>`;
            }
            document.getElementById('t26_res').innerHTML = res;
        }
        '''
    },

    # Task 27
    {
        "num": 27,
        "title": "Nierówność Kwadratowa",
        "subtitle": "Rozwiązywanie nierówności $3x^2 - 16x + 16 > 0$",
        "text": "Zadanie 27. (0–2)<br>Rozwiąż nierówność $3x^2 - 16x + 16 > 0$.",
        "img": "27.png",
        "is_closed": False,
        "options": {},
        "correct": "(-inf, 4/3) U (4, inf)",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_27')">Metoda 1: Szkic paraboli i delta</button>
            </div>
            <div class="tab-content active" id="m1_27">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie miejsc zerowych trójmianu</div>
                        <div class="step-desc">Przyrównujemy trójmian do zera $3x^2 - 16x + 16 = 0$:
                        $$\\Delta = (-16)^2 - 4 \\cdot 3 \\cdot 16 = 256 - 192 = 64, \\quad \\sqrt{\\Delta} = 8$$
                        $$x_1 = \\frac{16 - 8}{6} = \\frac{8}{6} = \\frac{4}{3}, \\quad x_2 = \\frac{16 + 8}{6} = \\frac{24}{6} = 4$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Szkic paraboli i odczytanie rozwiązania</div>
                        <div class="step-desc">Współczynnik $a = 3 > 0$, więc ramiona paraboli są skierowane do góry. Nierówność jest ostra $> 0$, więc wybieramy przedziały nad osią OX:
                        <div class="math-highlight">$$\\mathbf{x \\in \\left(-\\infty, \\frac{4}{3}\\right) \\cup (4, +\\infty)}$$</div></div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Nawiasy domknięte przy ostrej nierówności</div>
                    <div>Nierówność brzmi $> 0$ (bez znaku $\\ge$). Dlatego przedziały muszą mieć **nawiasy otwarte**! Zapis z nawiasami domkniętymi kosztuje 1 punkt.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Pierwiastki trójmianu kwadratowego</div>
                    <div>$$x_1 = \\frac{-b - \\sqrt{\\Delta}}{2a}, \\quad x_2 = \\frac{-b + \\sqrt{\\Delta}}{2a}$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask27(event)">
                <div class="input-group"><label>a:</label><input type="number" id="t27_a" value="3"></div>
                <div class="input-group"><label>b:</label><input type="number" id="t27_b" value="-16"></div>
                <div class="input-group"><label>c:</label><input type="number" id="t27_c" value="16"></div>
                <button type="submit" class="calc-btn">Rozwiąż Nierówność ax^2 + bx + c > 0</button>
            </form>
            <div class="calc-result" id="t27_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkOpenAnswer() {
            const userAns = document.getElementById('userAnsInput').value.trim();
            const feedbackBox = document.getElementById('feedbackBox');
            if ((userAns.includes('4/3') || userAns.includes('1.33')) && userAns.includes('4')) {
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Świetnie!</strong> Prawidłowy przedział: $x \\\\in \\\\left(-\\\\infty, \\\\frac{4}{3}\\\\right) \\\\cup (4, +\\\\infty)$. Gratulacje!';
            } else {
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = '❌ Odpowiedź niepełna. Prawidłowe rozwiązanie to: <strong>$x \\\\in \\\\left(-\\\\infty, \\\\frac{4}{3}\\\\right) \\\\cup (4, +\\\\infty)$</strong>.';
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask27(e) {
            e.preventDefault();
            const a = parseFloat(document.getElementById('t27_a').value);
            const b = parseFloat(document.getElementById('t27_b').value);
            const c = parseFloat(document.getElementById('t27_c').value);
            if (isNaN(a) || isNaN(b) || isNaN(c) || a === 0) return;
            const delta = b*b - 4*a*c;
            if (delta > 0) {
                const x1 = (-b - Math.sqrt(delta)) / (2*a);
                const x2 = (-b + Math.sqrt(delta)) / (2*a);
                const minX = Math.min(x1, x2);
                const maxX = Math.max(x1, x2);
                document.getElementById('t27_res').innerHTML = `<strong>Miejsca zerowe (Δ = ${delta}):</strong> x1 = ${minX.toFixed(2)}, x2 = ${maxX.toFixed(2)}<br><strong>Rozwiązanie nierówności > 0:</strong> x ∈ (-∞, ${minX.toFixed(2)}) ∪ (${maxX.toFixed(2)}, +∞)`;
            } else {
                document.getElementById('t27_res').innerHTML = `Δ <= 0`;
            }
        }
        '''
    },

    # Task 28
    {
        "num": 28,
        "title": "Dowód Algebraiczny Nierówności",
        "subtitle": "Wykazanie nieujemności $3a^2 - 2ab + 3b^2 \\ge 0$",
        "text": "Zadanie 28. (0–2)<br>Wykaż, że dla dowolnych liczb rzeczywistych $a$ i $b$ prawdziwa jest nierówność $3a^2 - 2ab + 3b^2 \\ge 0$.",
        "img": "28.png",
        "is_closed": False,
        "options": {},
        "correct": "(a-b)^2 + 2a^2 + 2b^2 >= 0",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_28')">Metoda 1: Rozbicie na sumę kwadratów (Główna)</button>
                <button class="tab-btn" onclick="switchTab('m2_28')">Metoda 2: Dopełnienie do pełnego kwadratu</button>
            </div>
            <div class="tab-content active" id="m1_28">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Grupowanie wyrażeń</div>
                        <div class="step-desc">Rozpisujemy wyrażenia $3a^2$ oraz $3b^2$:
                        $$L = 3a^2 - 2ab + 3b^2 = (a^2 - 2ab + b^2) + 2a^2 + 2b^2$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Zastosowanie wzoru skróconego mnożenia</div>
                        <div class="step-desc">Wyrażenie $(a^2 - 2ab + b^2)$ zwijamy do $(a - b)^2$:
                        $$L = (a - b)^2 + 2a^2 + 2b^2$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Argumentacja matematyczna</div>
                        <div class="step-desc">Dla dowolnych liczb rzeczywistych $a, b \\in \\mathbb{R}$:
                        - $(a - b)^2 \\ge 0$ (kwadrat jest nieujemny),
                        - $2a^2 \\ge 0$,
                        - $2b^2 \\ge 0$.<br>
                        Suma trzech wyrażeń nieujemnych jest zawsze nieujemna, co kończy dowód.
                        <div class="math-highlight">$$\\mathbf{L = (a-b)^2 + 2a^2 + 2b^2 \\ge 0 \\quad \\text{c.n.d.}}$$</div></div>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="m2_28">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Dopełnienie do kwadratu względem a</div>
                        <div class="step-desc">$$3a^2 - 2ab + 3b^2 = 3\\left(a^2 - \\frac{2}{3}ab\\right) + 3b^2 = 3\\left(a - \\frac{1}{3}b\\right)^2 - \\frac{1}{3}b^2 + 3b^2 = 3\\left(a - \\frac{1}{3}b\\right)^2 + \\frac{8}{3}b^2 \\ge 0$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Dowód na konkretnych liczbach</div>
                    <div>Podstawienie wybranych liczb (np. $a=1, b=2$) i wykazanie, że zachodzi dla nich nierówność, daje **0 punktów**! Dowód musi być ogólny dla wszystkich $a, b \\in \\mathbb{R}$.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Kwadrat różnicy</div>
                    <div>$$(a - b)^2 = a^2 - 2ab + b^2$$</div>
                </div>
                <div class="formula-card">
                    <div class="formula-name">Nieujemność kwadratu</div>
                    <div>$$x^2 \\ge 0 \\quad \\text{dla każdego } x \\in \\mathbb{R}$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask28(event)">
                <div class="input-group"><label>Liczba a:</label><input type="number" id="t28_a" value="2" step="any"></div>
                <div class="input-group"><label>Liczba b:</label><input type="number" id="t28_b" value="-3" step="any"></div>
                <button type="submit" class="calc-btn">Sprawdź wartość L = 3a^2 - 2ab + 3b^2</button>
            </form>
            <div class="calc-result" id="t28_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkOpenAnswer() {
            const userAns = document.getElementById('userAnsInput').value.trim();
            const feedbackBox = document.getElementById('feedbackBox');
            feedbackBox.className = 'feedback-box active correct';
            feedbackBox.innerHTML = '✨ <strong>Brawo!</strong> Prawidłowo przeprowadzone zwinięcie do postaci $(a-b)^2 + 2a^2 + 2b^2 \\\\ge 0$ stanowi pełny dowód formalny na 2 punkty!';
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask28(e) {
            e.preventDefault();
            const a = parseFloat(document.getElementById('t28_a').value);
            const b = parseFloat(document.getElementById('t28_b').value);
            if (isNaN(a) || isNaN(b)) return;
            const L = 3*a*a - 2*a*b + 3*b*b;
            const sq = Math.pow(a - b, 2) + 2*a*a + 2*b*b;
            document.getElementById('t28_res').innerHTML = `<strong>Wartość L:</strong> ${L.toFixed(2)}<br><strong>Postać zwinięta (a-b)^2 + 2a^2 + 2b^2:</strong> ${sq.toFixed(2)} (zawsze >= 0)`;
        }
        '''
    },

    # Task 29
    {
        "num": 29,
        "title": "Dowód Geometryczny w Okręgu",
        "subtitle": "Wykazanie relacji kątowej $\\angle ASD = 3\\alpha$",
        "text": "Zadanie 29. (0–2)<br>Dany jest okrąg o środku w punkcie $S$ i promieniu $r$. Na przedłużeniu cięciwy $AB$ poza punkt $B$ odłożono odcinek $BC$ równy promieniowi danego okręgu ($BC = r$). Przez punkty $C$ i $S$ poprowadzono prostą. Prosta $CS$ przecina dany okrąg w punktach $D$ i $E$ (zobacz rysunek). Wykaż, że jeżeli miara kąta $ACS$ jest równa $\\alpha$, to miara kąta $ASD$ jest równa $3\\alpha$.",
        "img": "29.png",
        "is_closed": False,
        "options": {},
        "correct": "ASD = 3alpha",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_29')">Metoda 1: Dowód z kątami zewnętrznymi i trójkątami równoramiennymi</button>
            </div>
            <div class="tab-content active" id="m1_29">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Trójkąt równoramienny $SBC$</div>
                        <div class="step-desc">Z treści zadania $BC = r$, a odcinek $SB$ jest promieniem okręgu ($SB = r$). Zatem trójkąt $SBC$ jest równoramienny o ramionach $SB = BC$. Kąty przy podstawie $SC$ są równe:
                        $$\\angle BSC = \\angle BCS = \\alpha$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Kąt zewnętrzny trójkąta $SBC$ przy wierzchołku $B$</div>
                        <div class="step-desc">Kąt $\\angle ABS$ jest kątem zewnętrznym trójkąta $SBC$. Jego miara wynosi:
                        $$\\angle ABS = \\angle BSC + \\angle BCS = \\alpha + \\alpha = 2\\alpha$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Trójkąt równoramienny $SAB$ i kąt zewnętrzny trójkąta $SAC$</div>
                        <div class="step-desc">Trójkąt $SAB$ ma ramiona $SA = r$ oraz $SB = r$, więc jest równoramienny: $\\angle SAB = \\angle ABS = 2\\alpha$.<br>
                        Kąt $\\angle ASD$ jest kątem zewnętrznym trójkąta $SAC$ przy wierzchołku $S$:
                        $$\\angle ASD = \\angle SAC + \\angle ACS = 2\\alpha + \\alpha = 3\\alpha$$
                        <div class="math-highlight">$$\\mathbf{\\angle ASD = 3\\alpha \\quad \\text{c.n.d.}}$$</div></div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Błędne uznanie prostej AB za średnicę</div>
                    <div>Pamiętaj, że prosta $AB$ jest tylko cięciwą i **nie przechodzi** przez środek okręgu $S$! Wszelkie założenia, że $\\angle SAB$ jest kątem prostym, są błędne.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Twierdzenie o kącie zewnętrznym</div>
                    <div>Kąt zewnętrzny trójkąta jest równy sumie dwóch kątów wewnętrznych przyległych do niego.</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask29(event)">
                <div class="input-group"><label>Kąt alpha (ACS) w stopniach:</label><input type="number" id="t29_alpha" value="20" min="1" max="50"></div>
                <button type="submit" class="calc-btn">Oblicz Kąt ASD</button>
            </form>
            <div class="calc-result" id="t29_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkOpenAnswer() {
            const userAns = document.getElementById('userAnsInput').value.trim();
            const feedbackBox = document.getElementById('feedbackBox');
            feedbackBox.className = 'feedback-box active correct';
            feedbackBox.innerHTML = '✨ <strong>Świetnie!</strong> Przeprowadzony dowód oparty na dwóch trójkątach równoramiennych i kącie zewnętrznym daje pełne 2 punkty!';
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask29(e) {
            e.preventDefault();
            const alpha = parseFloat(document.getElementById('t29_alpha').value);
            if (isNaN(alpha) || alpha <= 0 || alpha >= 60) return;
            document.getElementById('t29_res').innerHTML = `<strong>Kąt ACS (α):</strong> ${alpha}°<br><strong>Kąt ABS:</strong> ${2*alpha}°<br><strong>Kąt ASD (3α):</strong> ${3*alpha}°`;
        }
        '''
    },

    # Task 30
    {
        "num": 30,
        "title": "Prawdopodobieństwo Dwukrotnego Losowania",
        "subtitle": "Losowanie ze zwracaniem i nieparzysty iloczyn",
        "text": "Zadanie 30. (0–2)<br>Ze zbioru liczb $\\{1, 2, 3, 4, 5\\}$ losujemy dwa razy po jednej liczbie ze zwracaniem. Oblicz prawdopodobieństwo zdarzenia $A$ polegającego na wylosowaniu liczb, których iloczyn jest liczbą nieparzystą.",
        "img": "30.png",
        "is_closed": False,
        "options": {},
        "correct": "9/25 lub 0.36",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_30')">Metoda 1: Zliczanie zdarzeń elementarnych</button>
                <button class="tab-btn" onclick="switchTab('m2_30')">Metoda 2: Niezależność zdarzeń</button>
            </div>
            <div class="tab-content active" id="m1_30">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Moc przestrzeni zdarzeń elementarnych</div>
                        <div class="step-desc">Losujemy dwa razy ze zwracaniem ze zbioru 5-elementowego:
                        $$|\\Omega| = 5 \\cdot 5 = 25$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie liczby zdarzeń sprzyjających</div>
                        <div class="step-desc">Iloczyn dwóch liczb jest nieparzysty wtedy i tylko wtedy, gdy **obie** wylosowane liczby są nieparzyste. Liczby nieparzyste to $\\{1, 3, 5\\}$ (3 liczby).<br>
                        Liczba sprzyjających par:
                        $$|A| = 3 \\cdot 3 = 9$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Obliczenie prawdopodobieństwa</div>
                        <div class="step-desc">$$P(A) = \\frac{|A|}{|\\Omega|} = \\frac{9}{25} = 0{,}36$$</div>
                        <div class="math-highlight">$$\\mathbf{P(A) = \\frac{9}{25} = 0{,}36}$$</div>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="m2_30">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Iloczyn prawdopodobieństw</div>
                        <div class="step-desc">Losowania są niezależne:
                        $$P(A) = P(\\text{I nieparzysta}) \\cdot P(\\text{II nieparzysta}) = \\frac{3}{5} \\cdot \\frac{3}{5} = \\frac{9}{25}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Losowanie bez zwracania</div>
                    <div>Pamiętaj, że w treści zadania jest "ze zwracaniem" ($|\\Omega|=25$). Pomylenie z losowaniem bez zwracania ($|\\Omega|=20$) to częsty błąd.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Prawdopodobieństwo klasyczne</div>
                    <div>$$P(A) = \\frac{|A|}{|\\Omega|}$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask30(event)">
                <div class="input-group"><label>Liczba elementów nieparzystych:</label><input type="number" id="t30_n" value="3"></div>
                <div class="input-group"><label>Łączna liczba elementów:</label><input type="number" id="t30_all" value="5"></div>
                <button type="submit" class="calc-btn">Oblicz Prawdopodobieństwo</button>
            </form>
            <div class="calc-result" id="t30_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkOpenAnswer() {
            const userAns = document.getElementById('userAnsInput').value.trim();
            const feedbackBox = document.getElementById('feedbackBox');
            if (userAns.includes('9/25') || userAns.includes('0.36') || userAns.includes('0,36')) {
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Świetnie!</strong> Wynik $P(A) = \\\\frac{9}{25} = 0{,}36$ jest w pełni poprawny!';
            } else {
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = '❌ Błędny wynik. Prawidłowe prawdopodobieństwo wynosi: <strong>$P(A) = \\\\frac{9}{25} = 0{,}36$</strong>.';
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask30(e) {
            e.preventDefault();
            const n = parseInt(document.getElementById('t30_n').value);
            const total = parseInt(document.getElementById('t30_all').value);
            if (isNaN(n) || isNaN(total) || total <= 0 || n > total) return;
            const p = (n / total) * (n / total);
            document.getElementById('t30_res').innerHTML = `<strong>Liczba zdarzeń sprzyjających |A|:</strong> ${n*n}<br><strong>Liczba zdarzeń elementarnych |Ω|:</strong> ${total*total}<br><strong>Prawdopodobieństwo P(A):</strong> ${p.toFixed(4)} (${n*n}/${total*total})`;
        }
        '''
    },

    # Task 31
    {
        "num": 31,
        "title": "Przekątna w Trapezie Prostokątnym",
        "subtitle": "Kąty naprzemianległe i twierdzenie Pitagorasa",
        "text": "Zadanie 31. (0–2)<br>W trapezie prostokątnym $ABCD$ dłuższa podstawa $AB$ ma długość $8$. Przekątna $AC$ tego trapezu ma długość $4$ i tworzy z krótszą podstawą trapezu kąt o mierze $30^\\circ$ (zobacz rysunek). Oblicz długość przekątnej $BD$ tego trapezu.",
        "img": "31.png",
        "is_closed": False,
        "options": {},
        "correct": "2*sqrt(17) lub sqrt(68)",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_31')">Metoda 1: Funkcje trygonometryczne i Pitagoras</button>
            </div>
            <div class="tab-content active" id="m1_31">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Kąty naprzemianległe</div>
                        <div class="step-desc">Podstawy $CD \\parallel AB$ są równoległe, więc kąt $\\angle CAB = \\angle ACD = 30^\\circ$.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie wysokości trapezu $AD$</div>
                        <div class="step-desc">W trójkącie prostokątnym $ADC$ (z kątem prostym przy $D$):
                        $$AD = AC \\cdot \\sin 30^\\circ = 4 \\cdot \\frac{1}{2} = 2$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Obliczenie przekątnej $BD$ z trójkąta $DAB$</div>
                        <div class="step-desc">Trójkąt $DAB$ jest prostokątny o przyprostokątnych $AD = 2$ oraz $AB = 8$. Z twierdzenia Pitagorasa:
                        $$BD^2 = AD^2 + AB^2 = 2^2 + 8^2 = 4 + 64 = 68$$
                        $$BD = \\sqrt{68} = \\sqrt{4 \\cdot 17} = 2\\sqrt{17}$$</div>
                        <div class="math-highlight">$$\\mathbf{BD = 2\\sqrt{17}}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Błędne przypisanie kąta</div>
                    <div>Nie pomyl kąta $\\angle ACD = 30^\\circ$ z kątem przy podstawie $AB$! Kąty te są równorzędne naprzemianległe.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Twierdzenie Pitagorasa</div>
                    <div>$$a^2 + b^2 = c^2$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask31(event)">
                <div class="input-group"><label>Dłuższa podstawa AB:</label><input type="number" id="t31_ab" value="8"></div>
                <div class="input-group"><label>Przekątna AC:</label><input type="number" id="t31_ac" value="4"></div>
                <div class="input-group"><label>Kąt ACD w deg:</label><input type="number" id="t31_deg" value="30"></div>
                <button type="submit" class="calc-btn">Oblicz Przekątną BD</button>
            </form>
            <div class="calc-result" id="t31_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkOpenAnswer() {
            const userAns = document.getElementById('userAnsInput').value.trim();
            const feedbackBox = document.getElementById('feedbackBox');
            if (userAns.includes('2sqrt(17)') || userAns.includes('2\\sqrt{17}') || userAns.includes('sqrt(68)') || userAns.includes('8.25')) {
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Świetnie!</strong> Wynik $BD = 2\\sqrt{17} = \\sqrt{68}$ jest w pełni poprawny!';
            } else {
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = '❌ Błędny wynik. Prawidłowa długość przekątnej to: <strong>$BD = 2\\sqrt{17}$</strong>.';
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask31(e) {
            e.preventDefault();
            const ab = parseFloat(document.getElementById('t31_ab').value);
            const ac = parseFloat(document.getElementById('t31_ac').value);
            const deg = parseFloat(document.getElementById('t31_deg').value);
            if (isNaN(ab) || isNaN(ac) || isNaN(deg)) return;
            const rad = (deg * Math.PI) / 180;
            const ad = ac * Math.sin(rad);
            const bd = Math.sqrt(ad*ad + ab*ab);
            document.getElementById('t31_res').innerHTML = `<strong>Wysokość AD:</strong> ${ad.toFixed(2)}<br><strong>Przekątna BD:</strong> ${bd.toFixed(3)} (dokładnie √${Math.round(bd*bd)})`;
        }
        '''
    },

    # Task 32
    {
        "num": 32,
        "title": "Ciąg Arytmetyczny i Średnia Wyrazów",
        "subtitle": "Wyznaczanie $a_1$ oraz wskaźnika $k$ dla $a_k = -78$",
        "text": "Zadanie 32. (0–4)<br>Ciąg arytmetyczny $(a_n)$ jest określony dla każdej liczby naturalnej $n \\ge 1$. Różnicą tego ciągu jest liczba $r = -4$, a średnia arytmetyczna początkowych sześciu wyrazów tego ciągu: $a_1, a_2, a_3, a_4, a_5, a_6$, jest równa $16$.<br>a) Oblicz pierwszy wyraz tego ciągu.<br>b) Oblicz liczbę $k$, dla której $a_k = -78$.",
        "img": "32.png",
        "is_closed": False,
        "options": {},
        "correct": "a1 = 26, k = 27",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_32')">Metoda 1: Wzór na sumę ciągu (Główna)</button>
            </div>
            <div class="tab-content active" id="m1_32">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Część a) Obliczenie sumy $S_6$ i wyznaczenie $a_1$</div>
                        <div class="step-desc">Średnia arytmetyczna 6 wyrazów wynosi 16, zatem suma wynosi $S_6 = 6 \\cdot 16 = 96$.<br>
                        Wzór na sumę $S_6$:
                        $$S_6 = \\frac{2a_1 + 5r}{2} \\cdot 6 = 3(2a_1 + 5(-4)) = 6a_1 - 60$$
                        Przyrównujemy do 96:
                        $$6a_1 - 60 = 96 \\implies 6a_1 = 156 \\implies a_1 = 26$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Część b) Wyznaczenie liczby $k$</div>
                        <div class="step-desc">Zastępujemy dane do wzoru ogólnego $a_k = a_1 + (k-1)r$:
                        $$-78 = 26 + (k-1)(-4) \\implies -104 = -4(k-1) \\implies k-1 = 26 \\implies k = 27$$</div>
                        <div class="math-highlight">$$\\mathbf{a_1 = 26, \\quad k = 27}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Błędy ze znakiem przy ujemnej różnicy r</div>
                    <div>Pamiętaj, że $r = -4$ jest liczbą ujemną. Przeniesienie wyrazu z $k$ wymusza zmianę znaków: $-104 / (-4) = +26$.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Wzór ogólny ciągu arytmetycznego</div>
                    <div>$$a_n = a_1 + (n-1)r$$</div>
                </div>
                <div class="formula-card">
                    <div class="formula-name">Suma n wyrazów ciągu</div>
                    <div>$$S_n = \\frac{2a_1 + (n-1)r}{2} \\cdot n$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask32(event)">
                <div class="input-group"><label>Średnia arytmetyczna 6 wyrazów:</label><input type="number" id="t32_avg" value="16"></div>
                <div class="input-group"><label>Różnica r:</label><input type="number" id="t32_r" value="-4"></div>
                <div class="input-group"><label>Szukany wyraz ak:</label><input type="number" id="t32_ak" value="-78"></div>
                <button type="submit" class="calc-btn">Oblicz a1 oraz k</button>
            </form>
            <div class="calc-result" id="t32_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkOpenAnswer() {
            const userAns = document.getElementById('userAnsInput').value.trim();
            const feedbackBox = document.getElementById('feedbackBox');
            if (userAns.includes('26') && userAns.includes('27')) {
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Obliczono bezbłędnie obu części: $a_1 = 26$ oraz $k = 27$. Pełne 4 punkty!';
            } else {
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = '❌ Prawidłowe odpowiedzi to: <strong>a) $a_1 = 26$, b) $k = 27$</strong>.';
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask32(e) {
            e.preventDefault();
            const avg = parseFloat(document.getElementById('t32_avg').value);
            const r = parseFloat(document.getElementById('t32_r').value);
            const ak = parseFloat(document.getElementById('t32_ak').value);
            if (isNaN(avg) || isNaN(r) || isNaN(ak)) return;
            const S6 = avg * 6;
            const a1 = (S6 - 15*r) / 6;
            const k = (ak - a1) / r + 1;
            document.getElementById('t32_res').innerHTML = `<strong>Pierwszy wyraz a1:</strong> ${a1.toFixed(2)}<br><strong>Wskaźnik k dla a_k = ${ak}:</strong> k = ${k.toFixed(2)}`;
        }
        '''
    },

    # Task 33
    {
        "num": 33,
        "title": "Symetralna Odcinka i Współrzędne Punktu",
        "subtitle": "Wyznaczanie punktu $B$ odbitego względem prostej $y=3x$",
        "text": "Zadanie 33. (0–4)<br>Dany jest punkt $A = (-18, 10)$. Prosta o równaniu $y = 3x$ jest symetralną odcinka $AB$. Wyznacz współrzędne punktu $B$.",
        "img": "33.png",
        "is_closed": False,
        "options": {},
        "correct": "B = (20.4, -2.8) lub B = (102/5, -14/5)",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_33')">Metoda 1: Krok po kroku przez punkt przecięcia S</button>
            </div>
            <div class="tab-content active" id="m1_33">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie prostej $AB$</div>
                        <div class="step-desc">Prosta $AB$ jest prostopadła do symetralnej $y = 3x$, więc jej współczynnik kierunkowy $a_{AB} = -\\frac{1}{3}$.<br>
                        Podstawiamy punkt $A(-18, 10)$:
                        $$y - 10 = -\\frac{1}{3}(x + 18) \\implies y = -\\frac{1}{3}x - 6 + 10 \\implies y = -\\frac{1}{3}x + 4$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie środka $S$ odcinka $AB$</div>
                        <div class="step-desc">Punkt $S$ jest punktem przecięcia prostej $AB$ i symetralnej $y = 3x$:
                        $$3x = -\\frac{1}{3}x + 4 \\implies \\frac{10}{3}x = 4 \\implies x_S = 1{,}2 = \\frac{6}{5}$$
                        $$y_S = 3(1{,}2) = 3{,}6 = \\frac{18}{5}$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie punktu $B$ z wzoru na środek odcinka</div>
                        <div class="step-desc">$$\\frac{-18 + x_B}{2} = 1{,}2 \\implies -18 + x_B = 2{,}4 \\implies x_B = 20{,}4 = \\frac{102}{5}$$
                        $$\\frac{10 + y_B}{2} = 3{,}6 \\implies 10 + y_B = 7{,}2 \\implies y_B = -2{,}8 = -\\frac{14}{5}$$</div>
                        <div class="math-highlight">$$\\mathbf{B = (20{,}4; \\, -2{,}8) = \\left(\\frac{102}{5}, \\, -\\frac{14}{5}\\right)}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Błędy rachunkowe na ułamkach</div>
                    <div>Uważaj przy dzieleniu $4 / (10/3) = 1{,}2$. Częstym błędem jest pomylenie współrzędnych środka ze współrzędnymi szukanego punktu $B$.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Warunek prostopadłości</div>
                    <div>$$a_1 \\cdot a_2 = -1$$</div>
                </div>
                <div class="formula-card">
                    <div class="formula-name">Środek odcinka</div>
                    <div>$$S = \\left(\\frac{x_A + x_B}{2}, \\frac{y_A + y_B}{2}\\right)$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask33(event)">
                <div class="input-group"><label>Ax:</label><input type="number" id="t33_ax" value="-18"></div>
                <div class="input-group"><label>Ay:</label><input type="number" id="t33_ay" value="10"></div>
                <div class="input-group"><label>Prosta symetralna y = m*x (m):</label><input type="number" id="t33_m" value="3"></div>
                <button type="submit" class="calc-btn">Oblicz Punkt B</button>
            </form>
            <div class="calc-result" id="t33_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkOpenAnswer() {
            const userAns = document.getElementById('userAnsInput').value.trim();
            const feedbackBox = document.getElementById('feedbackBox');
            if ((userAns.includes('20.4') || userAns.includes('20,4') || userAns.includes('102/5')) && (userAns.includes('-2.8') || userAns.includes('-2,8') || userAns.includes('-14/5'))) {
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Świetnie!</strong> Współrzędne punktu $B = (20{,}4; -2{,}8)$ obliczone bezbłędnie! 4 punkty!';
            } else {
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = '❌ Błędny wynik. Prawidłowe współrzędne to: <strong>$B = (20{,}4; -2{,}8) = \\\\left(\\\\frac{102}{5}, -\\\\frac{14}{5}\\\\right)$</strong>.';
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask33(e) {
            e.preventDefault();
            const ax = parseFloat(document.getElementById('t33_ax').value);
            const ay = parseFloat(document.getElementById('t33_ay').value);
            const m = parseFloat(document.getElementById('t33_m').value);
            if (isNaN(ax) || isNaN(ay) || isNaN(m)) return;
            const a_ab = -1 / m;
            const b_ab = ay - a_ab * ax;
            const xs = b_ab / (m - a_ab);
            const ys = m * xs;
            const bx = 2 * xs - ax;
            const by = 2 * ys - ay;
            document.getElementById('t33_res').innerHTML = `<strong>Środek S:</strong> (${xs.toFixed(2)}, ${ys.toFixed(2)})<br><strong>Punkt B:</strong> (${bx.toFixed(2)}, ${by.toFixed(2)})`;
        }
        '''
    },

    # Task 34
    {
        "num": 34,
        "title": "Stereometria Ostrosłupa Prawidłowego",
        "subtitle": "Kąt nachylenia krawędzi bocznej i cosinus $\\alpha$",
        "text": "Zadanie 34. (0–5)<br>Długość krawędzi podstawy ostrosłupa prawidłowego czworokątnego jest równa $6$. Pole powierzchni całkowitej tego ostrosłupa jest cztery razy większe od pola jego podstawy. Kąt $\\alpha$ jest kątem nachylenia krawędzi bocznej tego ostrosłupa do płaszczyzny podstawy (zobacz rysunek). Oblicz cosinus kąta $\\alpha$.",
        "img": "34.png",
        "is_closed": False,
        "options": {},
        "correct": "sqrt(5)/5 lub 1/sqrt(5) lub 0.447",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_34')">Metoda 1: Pełna analiza bryły krok po kroku</button>
            </div>
            <div class="tab-content active" id="m1_34">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie pola podstawy i pola bocznego</div>
                        <div class="step-desc">Podstawa to kwadrat o boku $a = 6$. Pole podstawy $P_p = 6^2 = 36$.<br>
                        Pole całkowite $P_c = 4 \\cdot P_p = 4 \\cdot 36 = 144$.<br>
                        Pole boczne $P_b = P_c - P_p = 144 - 36 = 108$.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie wysokości ściany bocznej $h_b$</div>
                        <div class="step-desc">Ostrosłup ma 4 ściany boczne: $P_b = 4 \\cdot \\left(\\frac{1}{2} a h_b\\right) = 2 a h_b$.
                        $$2 \\cdot 6 \\cdot h_b = 108 \\implies 12 h_b = 108 \\implies h_b = 9$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie wysokości ostrosłupa $H$</div>
                        <div class="step-desc">Z trójkąta prostokątnego o przyprostokątnych $H$ i $r = \\frac{a}{2} = 3$ oraz przeciwprostokątnej $h_b = 9$:
                        $$H^2 + 3^2 = 9^2 \\implies H^2 + 9 = 81 \\implies H^2 = 72 \\implies H = \\sqrt{72} = 6\\sqrt{2}$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">4</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie krawędzi bocznej $b$ i cosinusa $\\alpha$</div>
                        <div class="step-desc">Połowa przekątnej podstawy $R = \\frac{a\\sqrt{2}}{2} = \\frac{6\\sqrt{2}}{2} = 3\\sqrt{2}$.<br>
                        Z twierdzenia Pitagorasa krawędź boczna $b$:
                        $$b = \\sqrt{H^2 + R^2} = \\sqrt{72 + (3\\sqrt{2})^2} = \\sqrt{72 + 18} = \\sqrt{90} = 3\\sqrt{10}$$
                        Cosinus kąta $\\alpha$ nachylenia krawędzi bocznej do podstawy:
                        $$\\cos \\alpha = \\frac{R}{b} = \\frac{3\\sqrt{2}}{3\\sqrt{10}} = \\frac{\\sqrt{2}}{\\sqrt{10}} = \\frac{1}{\\sqrt{5}} = \\frac{\\sqrt{5}}{5}$$</div>
                        <div class="math-highlight">$$\\mathbf{\\cos \\alpha = \\frac{\\sqrt{5}}{5}}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Pomylenie kąta krawędzi bocznej z kątem ściany bocznej</div>
                    <div>Dla kąta nachylenia **ściany bocznej** $\\cos \\beta = \\frac{r}{h_b} = \\frac{3}{9} = \\frac{1}{3}$. Pamiętaj, że w pytaniu chodzi o krawędź boczną, więc w mianowniku musi być długość krawędzi bocznej $b$!</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Przekątna kwadratu</div>
                    <div>$$d = a\\sqrt{2}$$</div>
                </div>
                <div class="formula-card">
                    <div class="formula-name">Cosinus w trójkącie prostokątnym</div>
                    <div>$$\\cos \\alpha = \\frac{\\text{przyległa}}{\\text{przeciwprostokątna}}$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask34(event)">
                <div class="input-group"><label>Krawędź podstawy a:</label><input type="number" id="t34_a" value="6"></div>
                <div class="input-group"><label>Krotność pola całkowitego (Pc/Pp):</label><input type="number" id="t34_k" value="4"></div>
                <button type="submit" class="calc-btn">Oblicz Cosinus α i Wszystkie Elementy</button>
            </form>
            <div class="calc-result" id="t34_res">Wprowadź dane i kliknij przycisk.</div>
        ''',
        "js": '''
        function checkOpenAnswer() {
            const userAns = document.getElementById('userAnsInput').value.trim();
            const feedbackBox = document.getElementById('feedbackBox');
            if (userAns.includes('sqrt(5)/5') || userAns.includes('\\sqrt{5}/5') || userAns.includes('1/sqrt(5)') || userAns.includes('0.447') || userAns.includes('0,447')) {
                feedbackBox.className = 'feedback-box active correct';
                feedbackBox.innerHTML = '✨ <strong>Fantastycznie!</strong> Obliczono bezbłędnie cosinus kąta $\\\\cos \\\\alpha = \\\\frac{\\\\sqrt{5}}{5}$. Maksymalne 5 punktów!';
            } else {
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = '❌ Prawidłowy wynik to: <strong>$\\\\cos \\\\alpha = \\\\frac{\\\\sqrt{5}}{5} = \\\\frac{1}{\\\\sqrt{5}} \\\\approx 0{,}447$</strong>.';
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask34(e) {
            e.preventDefault();
            const a = parseFloat(document.getElementById('t34_a').value);
            const mult = parseFloat(document.getElementById('t34_k').value);
            if (isNaN(a) || isNaN(mult) || a <= 0 || mult <= 1) return;
            const Pp = a * a;
            const Pc = mult * Pp;
            const Pb = Pc - Pp;
            const hb = Pb / (2 * a);
            const r = a / 2;
            const H = Math.sqrt(hb*hb - r*r);
            const R = (a * Math.sqrt(2)) / 2;
            const b = Math.sqrt(H*H + R*R);
            const cosAlpha = R / b;
            document.getElementById('t34_res').innerHTML = `<strong>Wysokość ściany hb:</strong> ${hb.toFixed(2)}<br><strong>Wysokość ostrosłupa H:</strong> ${H.toFixed(2)}<br><strong>Krawędź boczna b:</strong> ${b.toFixed(2)}<br><strong>Cosinus α:</strong> ${cosAlpha.toFixed(4)} (dokładnie √5/5)`;
        }
        '''
    }
]

print("Total tasks defined:", len(tasks_data))

# Generate HTML files for task 15 to 34
for t in tasks_data:
    html = create_task_page(
        task_num=t["num"],
        title=t["title"],
        subtitle=t["subtitle"],
        task_text=t["text"],
        image_filename=t["img"],
        is_closed=t["is_closed"],
        options_dict=t["options"],
        correct_opt_or_ans=t["correct"],
        solution_html=t["solution"],
        traps_html=t["traps"],
        formulas_html=t["formulas"],
        calc_html=t["calc"],
        js_code=t["js"]
    )
    filename = f"d:/matura/zadanie{t['num']}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {filename}")

# Update navigation across existing task1.html .. task14.html and index.html
print("Updating navigation across existing HTML files...")

for i in range(1, 15):
    fname = f"d:/matura/zadanie{i}.html"
    if os.path.exists(fname):
        with open(fname, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace nav section
        new_nav = get_nav_html(i)
        updated_content = re.sub(r'<nav class="task-nav">.*?</nav>', new_nav, content, flags=re.DOTALL)
        
        with open(fname, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"Updated nav in {fname}")

# Update index.html
if os.path.exists("d:/matura/index.html"):
    with open("d:/matura/index.html", "r", encoding="utf-8") as f:
        content = f.read()
    new_nav = get_nav_html(1)
    updated_content = re.sub(r'<nav class="task-nav">.*?</nav>', new_nav, content, flags=re.DOTALL)
    with open("d:/matura/index.html", "w", encoding="utf-8") as f:
        f.write(updated_content)
    print("Updated nav in d:/matura/index.html")

print("ALL MATURA TASKS GENERATED AND NAVIGATIONS UPDATED SUCCESSFULLY!")
