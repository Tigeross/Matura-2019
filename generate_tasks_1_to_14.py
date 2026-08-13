# -*- coding: utf-8 -*-
import os, sys, re
from build_all_matura_tasks import create_task_page, get_nav_html, ULTIMATE_RESPONSIVE_CSS

tasks_1_14 = [
    # Task 1
    {
        "num": 1,
        "title": "Działania na Potęgach",
        "subtitle": "Sprowadzanie do wspólnej podstawy $2^k$",
        "text": "Zadanie 1. (0–1)<br>Liczba $\\left(\\frac{1}{2}\\right)^{-3} \\cdot 8^{-2}$ jest równa:",
        "img": "1.png",
        "is_closed": True,
        "options": {"A": "$2^{-3}$", "B": "$2^{-9}$", "C": "$2^3$", "D": "$2^9$"},
        "correct": "A",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_1')">Metoda 1: Zamiana na potęgi dwójki (Główna)</button>
                <button class="tab-btn" onclick="switchTab('m2_1')">Metoda 2: Obliczenia na ułamkach</button>
            </div>
            <div class="tab-content active" id="m1_1">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Przekształcenie pierwszego czynnika $\\left(\\frac{1}{2}\\right)^{-3}$</div>
                        <div class="step-desc">Korzystamy ze wzoru na ujemny wykładnik $\\left(\\frac{a}{b}\\right)^{-n} = \\left(\\frac{b}{a}\\right)^n$:
                        $$\\left(\\frac{1}{2}\\right)^{-3} = 2^3 = 8$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Przekształcenie drugiego czynnika $8^{-2}$</div>
                        <div class="step-desc">Zapisujemy $8$ jako $2^3$:
                        $$8^{-2} = (2^3)^{-2} = 2^{3 \\cdot (-2)} = 2^{-6}$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Mnożenie potęg o jednakowych podstawach</div>
                        <div class="step-desc">Dodajemy wykładniki potęg:
                        $$2^3 \\cdot 2^{-6} = 2^{3 + (-6)} = 2^{-3}$$</div>
                        <div class="math-highlight">$$\\mathbf{2^{-3}} \\quad \\implies \\quad \\text{Poprawna odpowiedź to A}$$</div>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="m2_1">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Wartości liczbowe obu czynników</div>
                        <div class="step-desc">$$\\left(\\frac{1}{2}\\right)^{-3} = 8, \\quad 8^{-2} = \\frac{1}{64}$$
                        $$8 \\cdot \\frac{1}{64} = \\frac{8}{64} = \\frac{1}{8} = \\frac{1}{2^3} = 2^{-3}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Mnożenie wykładników przy mnożeniu potęg</div>
                    <div>Częsty błąd to mnożenie wykładników $3 \\cdot (-6) = -18$ lub dodawanie ujemnych podstaw. Pamiętaj: przy mnożeniu tych samych podstaw **dodajemy** wykładniki ($m + n$)!</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Ujemny wykładnik</div>
                    <div>$$a^{-n} = \\frac{1}{a^n}, \\quad \\left(\\frac{a}{b}\\right)^{-n} = \\left(\\frac{b}{a}\\right)^n$$</div>
                </div>
                <div class="formula-card">
                    <div class="formula-name">Potęgowanie potęgi</div>
                    <div>$$(a^m)^n = a^{m \\cdot n}$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask1(event)">
                <div class="input-group"><label>Wykładnik n przy (1/2)^(-n):</label><input type="number" id="t1_n" value="3"></div>
                <div class="input-group"><label>Wykładnik m przy 8^(m):</label><input type="number" id="t1_m" value="-2"></div>
                <button type="submit" class="calc-btn">Oblicz potęgę 2^k</button>
            </form>
            <div class="calc-result" id="t1_res">Wprowadź dane i kliknij przycisk.</div>
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
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź A ($2^{-3}$) jest prawidłowa. $(1/2)^{-3} \\\\cdot 8^{-2} = 2^3 \\\\cdot 2^{-6} = 2^{-3}$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>A ($2^{-3}$)</strong>. Sprowadź oba czynniki do podstawy 2.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask1(e) {
            e.preventDefault();
            const n = parseFloat(document.getElementById('t1_n').value);
            const m = parseFloat(document.getElementById('t1_m').value);
            if (isNaN(n) || isNaN(m)) return;
            const exp = n + 3 * m;
            const val = Math.pow(2, exp);
            document.getElementById('t1_res').innerHTML = `<strong>Wykładnik k przy 2^k:</strong> ${exp}<br><strong>Wynik 2^(${exp}):</strong> ${val} (czyli 1/${Math.pow(2, -exp)})`;
        }
        '''
    },

    # Task 2
    {
        "num": 2,
        "title": "Potęgi i Zapis Dziesiętny",
        "subtitle": "Wyznaczanie liczby cyfr z $n = 2^{14} \\cdot 5^{15}$",
        "text": "Zadanie 2.<br>Liczba naturalna $n = 2^{14} \\cdot 5^{15}$ w zapisie dziesiętnym ma:",
        "img": "2.png",
        "is_closed": True,
        "options": {"A": "14 cyfr", "B": "15 cyfr", "C": "16 cyfr", "D": "30 cyfr"},
        "correct": "B",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_2')">Metoda 1: Wyłączanie potęgi 10 (Główna)</button>
                <button class="tab-btn" onclick="switchTab('m2_2')">Metoda 2: Logarytm dziesiętny</button>
            </div>
            <div class="tab-content active" id="m1_2">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Rozbicie wykładnika $5^{15}$</div>
                        <div class="step-desc">Rozpisujemy $5^{15} = 5^1 \\cdot 5^{14}$.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Grupowanie w iloczyn $10^{14}$</div>
                        <div class="step-desc">$$n = 2^{14} \\cdot 5^1 \\cdot 5^{14} = 5 \\cdot (2 \\cdot 5)^{14} = 5 \\cdot 10^{14}$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Zliczenie cyfr</div>
                        <div class="step-desc">Liczba $5 \\cdot 10^{14}$ składa się z cyfry $5$ oraz $14$ zer:
                        $$1 \\text{ (cyfra 5)} + 14 \\text{ (zer)} = 15 \\text{ cyfr}$$</div>
                        <div class="math-highlight">$$\\mathbf{15 \\text{ cyfr}} \\quad \\implies \\quad \\text{Poprawna odpowiedź to B}$$</div>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="m2_2">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Logarytm ze wskaźnikiem podłogi</div>
                        <div class="step-desc">$$\\log_{10}(5 \\cdot 10^{14}) = \\log_{10} 5 + 14 \\approx 0{,}699 + 14 = 14{,}699$$
                        Liczba cyfr: $\\lfloor 14{,}699 \\rfloor + 1 = 14 + 1 = 15$.</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Sumowanie wykładników</div>
                    <div>Dodawanie $14 + 15 = 29 \\implies 30$ cyfr (odpowiedź D) to błędne zastosowanie wzoru dla potęg o różnych podstawach!</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Iloczyn potęg o tym samym wykładniku</div>
                    <div>$$a^k \\cdot b^k = (a \\cdot b)^k$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask2(event)">
                <div class="input-group"><label>Wykładnik przy 2 (m):</label><input type="number" id="t2_m" value="14"></div>
                <div class="input-group"><label>Wykładnik przy 5 (n):</label><input type="number" id="t2_n" value="15"></div>
                <button type="submit" class="calc-btn">Oblicz ilość cyfr 2^m * 5^n</button>
            </form>
            <div class="calc-result" id="t2_res">Wprowadź dane i kliknij przycisk.</div>
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
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź B (15 cyfr) jest prawidłowa. $n = 5 \\\\cdot 10^{14}$ składa się z cyfry 5 oraz 14 zer.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>B (15 cyfr)</strong>. Zapisz $n = 5 \\\\cdot 10^{14}$.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask2(e) {
            e.preventDefault();
            const m = parseInt(document.getElementById('t2_m').value);
            const n = parseInt(document.getElementById('t2_n').value);
            if (isNaN(m) || isNaN(n) || m < 0 || n < 0) return;
            const minExp = Math.min(m, n);
            const coef = Math.pow(2, m - minExp) * Math.pow(5, n - minExp);
            const digits = coef.toString().length + minExp;
            document.getElementById('t2_res').innerHTML = `<strong>Postać:</strong> ${coef} · 10^${minExp}<br><strong>Łączna liczba cyfr:</strong> ${digits}`;
        }
        '''
    },

    # Task 3
    {
        "num": 3,
        "title": "Działania na Logarytmach",
        "subtitle": "Różnica logarytmów $\\log_5 225 - 2\\log_5 3$",
        "text": "Zadanie 3. (0–1)<br>Liczba $\\log_5 225 - 2\\log_5 3$ jest równa:",
        "img": "3.png",
        "is_closed": True,
        "options": {"A": "$\\log_5 216$", "B": "$2$", "C": "$\\log_5 219$", "D": "$1$"},
        "correct": "B",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_3')">Metoda 1: Wzory na logarytmy (Główna)</button>
            </div>
            <div class="tab-content active" id="m1_3">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Wniesienie liczby 2 do wnętrza logarytmu</div>
                        <div class="step-desc">$$2\\log_5 3 = \\log_5(3^2) = \\log_5 9$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Zastosowanie wzoru na różnicę logarytmów</div>
                        <div class="step-desc">$$\\log_5 225 - \\log_5 9 = \\log_5\\left(\\frac{225}{9}\\right) = \\log_5 25$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Obliczenie wartości $\\log_5 25$</div>
                        <div class="step-desc">$$\\log_5 25 = 2 \\quad \\text{ponieważ } 5^2 = 25$$</div>
                        <div class="math-highlight">$$\\mathbf{\\log_5 25 = 2} \\quad \\implies \\quad \\text{Poprawna odpowiedź to B}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Odejmowanie liczb zamiast dzielenia</div>
                    <div>Błędne podjęcie różnicy $225 - 9 = 216 \\implies \\log_5 216$ (opcja A) lub $225 - 6 = 219$ (opcja C). Pamiętaj: różnica logarytmów to **logarytm ilorazu**!</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Różnica logarytmów</div>
                    <div>$$\\log_a x - \\log_a y = \\log_a\\left(\\frac{x}{y}\\right)$$</div>
                </div>
                <div class="formula-card">
                    <div class="formula-name">Logarytm potęgi</div>
                    <div>$$k \\log_a x = \\log_a(x^k)$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask3(event)">
                <div class="input-group"><label>Podstawa logarytmu a:</label><input type="number" id="t3_a" value="5"></div>
                <div class="input-group"><label>Liczba x:</label><input type="number" id="t3_x" value="225"></div>
                <div class="input-group"><label>Mnożnik k przy log(y):</label><input type="number" id="t3_k" value="2"></div>
                <div class="input-group"><label>Liczba y:</label><input type="number" id="t3_y" value="3"></div>
                <button type="submit" class="calc-btn">Oblicz log_a(x) - k*log_a(y)</button>
            </form>
            <div class="calc-result" id="t3_res">Wprowadź dane i kliknij przycisk.</div>
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
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź B ($2$) jest prawidłowa. $\\\\log_5 225 - \\\\log_5 9 = \\\\log_5 25 = 2$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>B ($2$)</strong>. Podziel 225 przez 9.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask3(e) {
            e.preventDefault();
            const a = parseFloat(document.getElementById('t3_a').value);
            const x = parseFloat(document.getElementById('t3_x').value);
            const k = parseFloat(document.getElementById('t3_k').value);
            const y = parseFloat(document.getElementById('t3_y').value);
            if (isNaN(a) || isNaN(x) || isNaN(k) || isNaN(y) || a <= 0 || a === 1 || x <= 0 || y <= 0) return;
            const yk = Math.pow(y, k);
            const div = x / yk;
            const res = Math.log(div) / Math.log(a);
            document.getElementById('t3_res').innerHTML = `<strong>Iloraz wewnątrz logarytmu:</strong> ${x} / ${yk} = ${div}<br><strong>Wynik log_${a}(${div}):</strong> ${res.toFixed(2)}`;
        }
        '''
    },

    # Task 4
    {
        "num": 4,
        "title": "Obniżki Procentowe",
        "subtitle": "Dwukrotna zmiana ceny towaru",
        "text": "Zadanie 4. (0–1)<br>Cena towaru została obniżona o $15\\%$, a następnie nową cenę obniżono o $20\\%$. W wyniku obu obniżek cena towaru zmniejszyła się o:",
        "img": "4.png",
        "is_closed": True,
        "options": {"A": "$32\\%$", "B": "$35\\%$", "C": "$68\\%$", "D": "$70\\%$"},
        "correct": "A",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_4')">Metoda 1: Mnożenie współczynników zmian (Główna)</button>
                <button class="tab-btn" onclick="switchTab('m2_4')">Metoda 2: Podstawienie ceny początkowej 100 zł</button>
            </div>
            <div class="tab-content active" id="m1_4">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Pierwsza obniżka o 15%</div>
                        <div class="step-desc">Cena po I obniżce wynosi $100\\% - 15\\% = 85\\%$ ceny początkowej $x$, czyli $0{,}85x$.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Druga obniżka o 20%</div>
                        <div class="step-desc">Cena po II obniżce wynosi $80\\%$ z nowej ceny:
                        $$0{,}80 \\cdot 0{,}85x = 0{,}68x = 68\\%x$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Obliczenie łącznego procentu obniżki</div>
                        <div class="step-desc">$$\\text{Obniżka} = 100\\% - 68\\% = 32\\%$$</div>
                        <div class="math-highlight">$$\\mathbf{32\\%} \\quad \\implies \\quad \\text{Poprawna odpowiedź to A}$$</div>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="m2_4">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Przyjmijmy cenę początkową 100 zł</div>
                        <div class="step-desc">1. Po obniżce o 15%: $100 - 15 = 85$ zł.<br>
                        2. Obniżka o 20% z 85 zł: $0{,}20 \\cdot 85 = 17$ zł.<br>
                        3. Nowa cena: $85 - 17 = 68$ zł.<br>
                        4. Łączny spadek ceny: $100 - 68 = 32$ zł $\\implies 32\\%$.</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Zwykłe dodawanie procentów</div>
                    <div>Dodanie $15\\% + 20\\% = 35\\%$ (opcja B) to podstawowy błąd! Druga obniżka naliczana jest od **nowej, niższej ceny**, a nie od ceny początkowej.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Kolejne zmiany procentowe</div>
                    <div>$$x_{końcowe} = x_{pocz} \\cdot (1 - p_1) \\cdot (1 - p_2)$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask4(event)">
                <div class="input-group"><label>Pierwsza obniżka p1 (%):</label><input type="number" id="t4_p1" value="15"></div>
                <div class="input-group"><label>Druga obniżka p2 (%):</label><input type="number" id="t4_p2" value="20"></div>
                <button type="submit" class="calc-btn">Oblicz łączną obniżkę</button>
            </form>
            <div class="calc-result" id="t4_res">Wprowadź dane i kliknij przycisk.</div>
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
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź A ($32\\%$) jest prawidłowa. $1 - (0{,}85 \\\\cdot 0{,}80) = 1 - 0{,}68 = 0{,}32 = 32\\%$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>A ($32\\%$)</strong>. Pamiętaj, że $0{,}85 \\\\cdot 0{,}80 = 0{,}68$.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask4(e) {
            e.preventDefault();
            const p1 = parseFloat(document.getElementById('t4_p1').value);
            const p2 = parseFloat(document.getElementById('t4_p2').value);
            if (isNaN(p1) || isNaN(p2)) return;
            const finalRatio = (1 - p1/100) * (1 - p2/100);
            const totalDiscount = (1 - finalRatio) * 100;
            document.getElementById('t4_res').innerHTML = `<strong>Cena końcowa stanowić będzie:</strong> ${(finalRatio*100).toFixed(2)}% ceny początkowej<br><strong>Łączny procent obniżki:</strong> ${totalDiscount.toFixed(2)}%`;
        }
        '''
    },

    # Task 5
    {
        "num": 5,
        "title": "Pierwiastki Równania Kwadratowego",
        "subtitle": "Wyznaczanie całkowitych współczynników $b$ i $c$",
        "text": "Zadanie 5. (0–1)<br>Liczba $a = \\sqrt{2} + 1$ jest jednym z pierwiastków równania $x^2 + bx + c = 0$ o współczynnikach całkowitych $b$ i $c$. Wtedy:",
        "img": "5.png",
        "is_closed": True,
        "options": {"A": "$b = -2, \\, c = -1$", "B": "$b = 2, \\, c = -1$", "C": "$b = -2, \\, c = 1$", "D": "$b = 2, \\, c = 1$"},
        "correct": "A",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_5')">Metoda 1: Pierwiastek sprzężony i wzory Viète'a (Główna)</button>
                <button class="tab-btn" onclick="switchTab('m2_5')">Metoda 2: Podstawienie $x = \\sqrt{2}+1$</button>
            </div>
            <div class="tab-content active" id="m1_5">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Drugi pierwiastek równania o całkowitych współczynnikach</div>
                        <div class="step-desc">Dla równania o współczynnikach całkowitych, jeśli jednym pierwiastkiem jest $x_1 = 1 + \\sqrt{2}$, to drugim musi być pierwiastek sprzężony $x_2 = 1 - \\sqrt{2}$.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Zastosowanie wzorów Viète'a</div>
                        <div class="step-desc">$$b = -(x_1 + x_2) = -((1 + \\sqrt{2}) + (1 - \\sqrt{2})) = -2$$
                        $$c = x_1 \\cdot x_2 = (1 + \\sqrt{2})(1 - \\sqrt{2}) = 1^2 - (\\sqrt{2})^2 = 1 - 2 = -1$$</div>
                        <div class="math-highlight">$$\\mathbf{b = -2, \\, c = -1} \\quad \\implies \\quad \\text{Poprawna odpowiedź to A}$$</div>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="m2_5">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Podstawienie pod $x^2 + bx + c = 0$</div>
                        <div class="step-desc">$$(\\sqrt{2}+1)^2 + b(\\sqrt{2}+1) + c = 0 \\implies (3 + 2\\sqrt{2}) + b\\sqrt{2} + b + c = 0$$
                        $$(3 + b + c) + (2 + b)\\sqrt{2} = 0$$
                        Ponieważ $b, c \\in \\mathbb{Z}$, część niewymierna musi zerować się osobiście: $2 + b = 0 \\implies b = -2$, a wtedy $3 - 2 + c = 0 \\implies c = -1$.</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Błędy znaku przy sumie pierwiastków</div>
                    <div>Pamiętaj, że ze wzorów Viète'a $x_1 + x_2 = -b$, a nie $+b$. Zatem $b = -2$.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Wzory Viète'a dla $x^2 + bx + c = 0$</div>
                    <div>$$x_1 + x_2 = -b, \\quad x_1 \\cdot x_2 = c$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask5(event)">
                <div class="input-group"><label>Podaj współczynnik b:</label><input type="number" id="t5_b" value="-2"></div>
                <div class="input-group"><label>Podaj współczynnik c:</label><input type="number" id="t5_c" value="-1"></div>
                <button type="submit" class="calc-btn">Oblicz pierwiastki równania x^2 + bx + c = 0</button>
            </form>
            <div class="calc-result" id="t5_res">Wprowadź dane i kliknij przycisk.</div>
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
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź A ($b = -2, c = -1$) jest prawidłowa. $x_1+x_2 = 2 \\\\implies b = -2$, a $x_1 x_2 = 1-2 = -1 \\\\implies c = -1$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>A ($b = -2, c = -1$)</strong>. Skorzystaj ze wzorów Viète'a.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask5(e) {
            e.preventDefault();
            const b = parseFloat(document.getElementById('t5_b').value);
            const c = parseFloat(document.getElementById('t5_c').value);
            if (isNaN(b) || isNaN(c)) return;
            const delta = b*b - 4*c;
            if (delta >= 0) {
                const x1 = (-b + Math.sqrt(delta)) / 2;
                const x2 = (-b - Math.sqrt(delta)) / 2;
                document.getElementById('t5_res').innerHTML = `<strong>Wyróżnik Δ:</strong> ${delta}<br><strong>Pierwiastki:</strong> x1 = ${x1.toFixed(3)}, x2 = ${x2.toFixed(3)}`;
            } else {
                document.getElementById('t5_res').innerHTML = `Wyróżnik Δ < 0 (brak pierwiastków rzeczywistych).`;
            }
        }
        '''
    },

    # Task 6
    {
        "num": 6,
        "title": "Liczba Rozwiązań Równania Wymiernego",
        "subtitle": "Badanie dziedziny i zerowania licznika",
        "text": "Zadanie 6. (0–1)<br>Liczba rozwiązań równania $\\frac{(x^2 - 1)(x - 2)}{(x-1)(x+2)} = 0$ jest równa:",
        "img": "6.png",
        "is_closed": True,
        "options": {"A": "0", "B": "1", "C": "2", "D": "3"},
        "correct": "C",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_6')">Metoda 1: Dziedzina i rozkład na czynniki (Główna)</button>
            </div>
            <div class="tab-content active" id="m1_6">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie dziedziny równania</div>
                        <div class="step-desc">Mianownik musi być różny od zera:
                        $$(x-1)(x+2) \\neq 0 \\implies x \\neq 1 \\quad \\text{oraz} \\quad x \\neq -2$$
                        $$\\mathcal{D} = \\mathbb{R} \\setminus \\{-2, 1\\}$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Przyrównanie licznika do zera</div>
                        <div class="step-desc">$$(x^2 - 1)(x - 2) = 0 \\implies (x-1)(x+1)(x-2) = 0$$
                        Miejsca zerowe licznika to: $x = 1$, $x = -1$, $x = 2$.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Weryfikacja z dziedziną</div>
                        <div class="step-desc">Liczba $x = 1$ nie należy do dziedziny $\\mathcal{D}$.<br>
                        Rozwiązaniami są tylko $x = -1$ oraz $x = 2$ (2 rozwiązania).</div>
                        <div class="math-highlight">$$\\mathbf{2 \\text{ rozwiązania}} \\quad \\implies \\quad \\text{Poprawna odpowiedź to C}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Zapomnienie o dziedzinie</div>
                    <div>Wskazanie 3 rozwiązań (opcja D) bez odrzucenia $x = 1$ z mianownika to klasyczna pułapka maturalna! Pamiętaj: dzielenie przez zero jest niedozwolone.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Równanie wymierne</div>
                    <div>$$\\frac{L(x)}{M(x)} = 0 \\iff L(x) = 0 \\quad \\text{i} \\quad M(x) \\neq 0$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask6(event)">
                <div class="input-group"><label>Zastąp wartość x do sprawdzenia:</label><input type="number" id="t6_x" value="1"></div>
                <button type="submit" class="calc-btn">Sprawdź czy x należy do rozwiązania</button>
            </form>
            <div class="calc-result" id="t6_res">Wprowadź dane i kliknij przycisk.</div>
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
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź C (2 rozwiązania) jest prawidłowa. Liczba $x=1$ odpada z dziedziny, zostają $x = -1$ i $x = 2$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>C (2 rozwiązania)</strong>. Pamiętaj o wykluczeniu $x=1$ z mianownika!`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask6(e) {
            e.preventDefault();
            const x = parseFloat(document.getElementById('t6_x').value);
            if (isNaN(x)) return;
            if (x === 1 || x === -2) {
                document.getElementById('t6_res').innerHTML = `<span style="color:#ef4444;">x = ${x} NIE należy do dziedziny (mianownik jest równy 0)!</span>`;
            } else if (x === -1 || x === 2) {
                document.getElementById('t6_res').innerHTML = `<span style="color:#10b981;">x = ${x} JEST poprawnym rozwiązaniem równania!</span>`;
            } else {
                document.getElementById('t6_res').innerHTML = `x = ${x} należy do dziedziny, ale nie zeruje licznika.`;
            }
        }
        '''
    },

    # Task 7
    {
        "num": 7,
        "title": "Miejsca Zerowe z Wykresu Funkcji",
        "subtitle": "Odczytywanie punktów przecięcia z osią OX",
        "text": "Zadanie 7. (0–1)<br>Na rysunku przedstawiono wykres funkcji $f$. Miejscami zerowymi tej funkcji są liczby:",
        "img": "7.png",
        "is_closed": True,
        "options": {"A": "$-2$ oraz $2$", "B": "$-4$ oraz $4$", "C": "$-4, -2, 2, 4$", "D": "$-2, 0, 2$"},
        "correct": "A",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_7')">Metoda 1: Odczyt z wykresu</button>
            </div>
            <div class="tab-content active" id="m1_7">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Definicja miejsca zerowego</div>
                        <div class="step-desc">Miejsce zerowe funkcji to argument $x$, dla którego wartość funkcji wynosi zero ($f(x) = 0$). Na wykresie są to współrzędne $x$ punktów przecięcia wykresu z osią OX.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Odczyt punktów przeciecia z osią OX</div>
                        <div class="step-desc">Wykres przecina oś OX dokładnie w dwóch punktach: $x = -2$ oraz $x = 2$.</div>
                        <div class="math-highlight">$$\\mathbf{x = -2 \\quad \\text{oraz} \\quad x = 2} \\quad \\implies \\quad \\text{Poprawna odpowiedź to A}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Pomylenie końców dziedziny z miejscami zerowymi</div>
                    <div>Liczby $-4$ i $4$ to krańce dziedziny funkcji na wykresie, a nie miejsca zerowe! Miejsca zerowe to tylko te punkty, gdzie linia wykresu dotyka osi OX.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Miejsce zerowe</div>
                    <div>$$f(x_0) = 0$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask7(event)">
                <div class="input-group"><label>Wpisz x do sprawdzenia:</label><input type="number" id="t7_x" value="-2"></div>
                <button type="submit" class="calc-btn">Sprawdź czy x jest miejscem zerowym</button>
            </form>
            <div class="calc-result" id="t7_res">Wprowadź dane i kliknij przycisk.</div>
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
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź A ($-2$ oraz $2$) jest prawidłowa. Wykres przecina oś OX w punktach $x = -2$ i $x = 2$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>A ($-2$ oraz $2$)</strong>. Odczytaj punkty przecięcia z osią OX.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask7(e) {
            e.preventDefault();
            const x = parseFloat(document.getElementById('t7_x').value);
            if (isNaN(x)) return;
            if (x === -2 || x === 2) {
                document.getElementById('t7_res').innerHTML = `<span style="color:#10b981;">x = ${x} JEST miejscem zerowym funkcji f!</span>`;
            } else {
                document.getElementById('t7_res').innerHTML = `x = ${x} NIE jest miejscem zerowym tej funkcji.`;
            }
        }
        '''
    },

    # Task 8
    {
        "num": 8,
        "title": "Wierzchołek Paraboli w Postaci Kanonicznej",
        "subtitle": "Odczytanie współrzędnych $W=(p,q)$ z $f(x) = a(x-p)^2 + q$",
        "text": "Zadanie 8. (0–1)<br>Wierzchołek paraboli będącej wykresem funkcji kwadratowej $f(x) = -2(x - 1)^2 + 3$ ma współrzędne:",
        "img": "8.png",
        "is_closed": True,
        "options": {"A": "$(1, -3)$", "B": "$(1, 3)$", "C": "$(-1, 3)$", "D": "$(-1, -3)$"},
        "correct": "B",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_8')">Metoda 1: Bezpośredni odczyt z postaci kanonicznej</button>
            </div>
            <div class="tab-content active" id="m1_8">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Wzór postaci kanonicznej</div>
                        <div class="step-desc">Postać kanoniczna funkcji kwadratowej to $f(x) = a(x - p)^2 + q$, gdzie $W = (p, q)$ są współrzędnymi wierzchołka paraboli.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Odczytanie parametrów $p$ i $q$</div>
                        <div class="step-desc">Porównujemy $f(x) = -2(x - 1)^2 + 3$ ze wzorem ogólnym:<br>
                        - $p = 1$ (zwróć uwagę na minus we wzorze $x - 1$),<br>
                        - $q = 3$.<br>
                        Zatem $W = (1, 3)$.</div>
                        <div class="math-highlight">$$\\mathbf{W = (1, 3)} \\quad \\implies \\quad \\text{Poprawna odpowiedź to B}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Zmiana znaku przy p</div>
                    <div>Wzór brzmi $(x - p)^2$. Przy zapisie $(x - 1)^2$ wartość $p = +1$. Błędne odczytanie $p = -1$ prowadzi do zlej opcji C.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Postać kanoniczna</div>
                    <div>$$f(x) = a(x - p)^2 + q \\quad \\implies \\quad W = (p, q)$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask8(event)">
                <div class="input-group"><label>a:</label><input type="number" id="t8_a" value="-2"></div>
                <div class="input-group"><label>p:</label><input type="number" id="t8_p" value="1"></div>
                <div class="input-group"><label>q:</label><input type="number" id="t8_q" value="3"></div>
                <button type="submit" class="calc-btn">Wyznacz Wierzchołek W=(p,q)</button>
            </form>
            <div class="calc-result" id="t8_res">Wprowadź dane i kliknij przycisk.</div>
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
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź B ($(1, 3)$) jest prawidłowa. Z postaci kanonicznej $p = 1, q = 3$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>B ($(1, 3)$)</strong>. Pamiętaj o znaku we wzorze $a(x-p)^2+q$.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask8(e) {
            e.preventDefault();
            const a = parseFloat(document.getElementById('t8_a').value);
            const p = parseFloat(document.getElementById('t8_p').value);
            const q = parseFloat(document.getElementById('t8_q').value);
            if (isNaN(a) || isNaN(p) || isNaN(q)) return;
            document.getElementById('t8_res').innerHTML = `<strong>Wierzchołek paraboli W:</strong> (${p}, ${q})<br><strong>Kierunek ramion:</strong> ${a < 0 ? 'w dół (a < 0)' : 'w górę (a > 0)'}`;
        }
        '''
    },

    # Task 9
    {
        "num": 9,
        "title": "Zbiór Wartości Funkcji Kwadratowej",
        "subtitle": "Wyznaczanie $Y_f$ z wierzchołka $q$ i kierunku ramion $a < 0$",
        "text": "Zadanie 9. (0–1)<br>Zbiorem wartości funkcji kwadratowej $f(x) = -(x - 1)^2 + 3$ jest przedział:",
        "img": "9.png",
        "is_closed": True,
        "options": {"A": "$(-\\infty, 1]$", "B": "$[1, +\\infty)$", "C": "$[3, +\\infty)$", "D": "$(-\\infty, 3]$"},
        "correct": "D",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_9')">Metoda 1: Analiza wierzchołka i współczynnika a</button>
            </div>
            <div class="tab-content active" id="m1_9">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Kierunek ramion paraboli</div>
                        <div class="step-desc">Współczynnik przy kwadracie $a = -1 < 0$. Oznacza to, że ramiona paraboli skierowane są **w dół**, a funkcja osiąga wartość maksymalną w wierzchołku.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Wartość rzędnej wierzchołka $q$</div>
                        <div class="step-desc">Z postaci kanonicznej $f(x) = -(x - 1)^2 + 3$ odczytujemy $q = 3$.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie zbioru wartości</div>
                        <div class="step-desc">Dla $a < 0$ zbiór wartości wynosi $Y_f = (-\\infty, q] = (-\\infty, 3]$.</div>
                        <div class="math-highlight">$$\\mathbf{Y_f = (-\\infty, 3]} \\quad \\implies \\quad \\text{Poprawna odpowiedź to D}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Pomylenie p z q</div>
                    <div>Użycie współrzędnej $p = 1$ zamiast $q = 3$ daje przedział $(-\\infty, 1]$ (opcja A). Zbiór wartości dotyczy osi OY, a więc współrzędnej **q**!</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Zbiór wartości funkcji kwadratowej</div>
                    <div>Gdy $a > 0 \\implies Y_f = [q, +\\infty)$, gdy $a < 0 \\implies Y_f = (-\\infty, q]$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask9(event)">
                <div class="input-group"><label>a:</label><input type="number" id="t9_a" value="-1"></div>
                <div class="input-group"><label>q:</label><input type="number" id="t9_q" value="3"></div>
                <button type="submit" class="calc-btn">Wyznacz Zbiór Wartości Yf</button>
            </form>
            <div class="calc-result" id="t9_res">Wprowadź dane i kliknij przycisk.</div>
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
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź D ($(-\\\\infty, 3]$) jest prawidłowa. Ramiona w dół ($a < 0$), wartość max $q = 3$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>D ($(-\\\\infty, 3]$)</strong>. Zbiór wartości zależy od $q = 3$.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask9(e) {
            e.preventDefault();
            const a = parseFloat(document.getElementById('t9_a').value);
            const q = parseFloat(document.getElementById('t9_q').value);
            if (isNaN(a) || isNaN(q)) return;
            const res = a > 0 ? `[${q}, +∞)` : `(-∞, ${q}]`;
            document.getElementById('t9_res').innerHTML = `<strong>Zbiór wartości Yf:</strong> ${res}`;
        }
        '''
    },

    # Task 10
    {
        "num": 10,
        "title": "Wartość Najmniejsza w Przedziale Domykańczym",
        "subtitle": "Badanie funkcji kwadratowej w przedziale $[0, 4]$",
        "text": "Zadanie 10. (0–1)<br>Najmniejsza wartość funkcji kwadratowej $f(x) = x^2 - 4x + 3$ w przedziale $[0, 4]$ jest równa:",
        "img": "10.png",
        "is_closed": True,
        "options": {"A": "$3$", "B": "$0$", "C": "$-1$", "D": "$4$"},
        "correct": "C",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_10')">Metoda 1: Badanie wierzchołka i krańców przedziału</button>
            </div>
            <div class="tab-content active" id="m1_10">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie współrzędnej $p$ wierzchołka</div>
                        <div class="step-desc">$$p = -\\frac{b}{2a} = -\\frac{-4}{2(1)} = 2$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Sprawdzenie przynależności $p$ do przedziału $[0, 4]$</div>
                        <div class="step-desc">Punkt $p = 2$ leży wewnątrz przedziału $[0, 4]$. Ponieważ $a = 1 > 0$, parabola ma ramiona do góry, więc w wierzchołku osiągana jest najmniejsza wartość w całej dziedzinie.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Obliczenie wartości $q = f(p)$</div>
                        <div class="step-desc">$$q = f(2) = 2^2 - 4(2) + 3 = 4 - 8 + 3 = -1$$</div>
                        <div class="math-highlight">$$\\mathbf{f_{min} = -1} \\quad \\implies \\quad \\text{Poprawna odpowiedź to C}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Liczenie wartości tylko na krańcach przedziału</div>
                    <div>$f(0) = 3$, $f(4) = 3$. Gdyby sprawdzić tylko krańce, błędnie wybrano by 3 (opcja A). Zawsze sprawdzaj, czy wierzchołek $p$ wpada do przedziału!</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Współrzędna p wierzchołka</div>
                    <div>$$p = -\\frac{b}{2a}$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask10(event)">
                <div class="input-group"><label>a:</label><input type="number" id="t10_a" value="1"></div>
                <div class="input-group"><label>b:</label><input type="number" id="t10_b" value="-4"></div>
                <div class="input-group"><label>c:</label><input type="number" id="t10_c" value="3"></div>
                <div class="input-group"><label>Początek x1:</label><input type="number" id="t10_x1" value="0"></div>
                <div class="input-group"><label>Koniec x2:</label><input type="number" id="t10_x2" value="4"></div>
                <button type="submit" class="calc-btn">Znajdź wartość min i max w przedziale</button>
            </form>
            <div class="calc-result" id="t10_res">Wprowadź dane i kliknij przycisk.</div>
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
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź C ($-1$) jest prawidłowa. Wierzchołek $p = 2$ leży w przedziale $[0,4]$, a $f(2) = -1$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>C ($-1$)</strong>. Oblicz wartość w wierzchołku $f(2)$.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask10(e) {
            e.preventDefault();
            const a = parseFloat(document.getElementById('t10_a').value);
            const b = parseFloat(document.getElementById('t10_b').value);
            const c = parseFloat(document.getElementById('t10_c').value);
            const x1 = parseFloat(document.getElementById('t10_x1').value);
            const x2 = parseFloat(document.getElementById('t10_x2').value);
            if (isNaN(a) || isNaN(b) || isNaN(c) || isNaN(x1) || isNaN(x2)) return;
            const p = -b / (2*a);
            const f1 = a*x1*x1 + b*x1 + c;
            const f2 = a*x2*x2 + b*x2 + c;
            let minVal = Math.min(f1, f2);
            let maxVal = Math.max(f1, f2);
            if (p >= x1 && p <= x2) {
                const fp = a*p*p + b*p + c;
                minVal = Math.min(minVal, fp);
                maxVal = Math.max(maxVal, fp);
            }
            document.getElementById('t10_res').innerHTML = `<strong>Wierzchołek p:</strong> ${p.toFixed(2)}<br><strong>Wartość najmniejsza w [${x1}, ${x2}]:</strong> ${minVal.toFixed(2)}<br><strong>Wartość największa:</strong> ${maxVal.toFixed(2)}`;
        }
        '''
    },

    # Task 11
    {
        "num": 11,
        "title": "Ciąg Geometryczny i Suma S4",
        "subtitle": "Wyznaczanie ilorazu $q$ oraz sumy pierwszych wyrazów",
        "text": "Zadanie 11. (0–1)<br>W ciągu geometrycznym $(a_n)$, określonym dla $n \\ge 1$, dane są $a_1 = 3$ i $a_2 = 12$. Wtedy suma $S_4$ czterech pierwszych wyrazów tego ciągu jest równa:",
        "img": "11.png",
        "is_closed": True,
        "options": {"A": "$255$", "B": "$\\frac{255}{4}$", "C": "$\\frac{255}{12}$", "D": "$765$"},
        "correct": "A",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_11')">Metoda 1: Obliczenie wyrazów i zsumowanie (Główna)</button>
                <button class="tab-btn" onclick="switchTab('m2_11')">Metoda 2: Wzór na sumę Sn</button>
            </div>
            <div class="tab-content active" id="m1_11">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie ilorazu ciągu $q$</div>
                        <div class="step-desc">$$q = \\frac{a_2}{a_1} = \\frac{12}{3} = 4$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Obliczenie kolejnych wyrazów</div>
                        <div class="step-desc">$$a_1 = 3$$
                        $$a_2 = 12$$
                        $$a_3 = 12 \\cdot 4 = 48$$
                        $$a_4 = 48 \\cdot 4 = 192$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Zsumowanie czterech wyrazów</div>
                        <div class="step-desc">$$S_4 = 3 + 12 + 48 + 192 = 255$$</div>
                        <div class="math-highlight">$$\\mathbf{S_4 = 255} \\quad \\implies \\quad \\text{Poprawna odpowiedź to A}$$</div>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="m2_11">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Zastosowanie wzoru na $S_4$</div>
                        <div class="step-desc">$$S_4 = a_1 \\cdot \\frac{1 - q^4}{1 - q} = 3 \\cdot \\frac{1 - 4^4}{1 - 4} = 3 \\cdot \\frac{1 - 256}{-3} = 255$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Błędy znaku przy dzieleniu przez 1-q</div>
                    <div>W mianowniku wzoru jest $1 - q = 1 - 4 = -3$. Minus w liczniku i mianowniku skracają się dając dodatni wynik $255$.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Iloraz ciągu geometrycznego</div>
                    <div>$$q = \\frac{a_{n+1}}{a_n}$$</div>
                </div>
                <div class="formula-card">
                    <div class="formula-name">Suma n wyrazów ciągu geometrycznego</div>
                    <div>$$S_n = a_1 \\cdot \\frac{1 - q^n}{1 - q}$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask11(event)">
                <div class="input-group"><label>Wyraz a1:</label><input type="number" id="t11_a1" value="3"></div>
                <div class="input-group"><label>Wyraz a2:</label><input type="number" id="t11_a2" value="12"></div>
                <div class="input-group"><label>Ilość wyrazów n:</label><input type="number" id="t11_n" value="4"></div>
                <button type="submit" class="calc-btn">Oblicz Sumę Sn Ciągu Geometrycznego</button>
            </form>
            <div class="calc-result" id="t11_res">Wprowadź dane i kliknij przycisk.</div>
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
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź A ($255$) jest prawidłowa. $q = 4$, wyrazy to $3, 12, 48, 192$, ich suma to $255$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>A ($255$)</strong>. Dodaj cztery pierwsze wyrazy.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask11(e) {
            e.preventDefault();
            const a1 = parseFloat(document.getElementById('t11_a1').value);
            const a2 = parseFloat(document.getElementById('t11_a2').value);
            const n = parseInt(document.getElementById('t11_n').value);
            if (isNaN(a1) || isNaN(a2) || isNaN(n) || a1 === 0 || n <= 0) return;
            const q = a2 / a1;
            const Sn = a1 * (1 - Math.pow(q, n)) / (1 - q);
            document.getElementById('t11_res').innerHTML = `<strong>Iloraz q:</strong> ${q}<br><strong>Suma ${n} wyrazów Sn:</strong> ${Sn}`;
        }
        '''
    },

    # Task 12
    {
        "num": 12,
        "title": "Ciąg Arytmetyczny i Suma S10",
        "subtitle": "Zastosowanie wzoru na sumę $S_n$",
        "text": "Zadanie 12. (0–1)<br>W ciągu arytmetycznym $(a_n)$, określonym dla $n \\ge 1$, dane są $a_1 = -4$ i $r = 3$. Wtedy suma $S_{10}$ dziesięciu pierwszych wyrazów tego ciągu jest równa:",
        "img": "12.png",
        "is_closed": True,
        "options": {"A": "$95$", "B": "$190$", "C": "$85$", "D": "$100$"},
        "correct": "A",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_12')">Metoda 1: Wzór na sumę z a1 i r (Główna)</button>
                <button class="tab-btn" onclick="switchTab('m2_12')">Metoda 2: Wyznaczenie a10 i wzór podstawowy</button>
            </div>
            <div class="tab-content active" id="m1_12">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Bezpośredni wzór na sumę $S_n$</div>
                        <div class="step-desc">$$S_n = \\frac{2a_1 + (n-1)r}{2} \\cdot n$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Podstawienie danych $a_1 = -4, r = 3, n = 10$</div>
                        <div class="step-desc">$$S_{10} = \\frac{2(-4) + 9(3)}{2} \\cdot 10 = \\frac{-8 + 27}{2} \\cdot 10 = \\frac{19}{2} \\cdot 10 = 19 \\cdot 5 = 95$$</div>
                        <div class="math-highlight">$$\\mathbf{S_{10} = 95} \\quad \\implies \\quad \\text{Poprawna odpowiedź to A}$$</div>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="m2_12">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Wyznaczenie dziesiątego wyrazu $a_{10}$</div>
                        <div class="step-desc">$$a_{10} = a_1 + 9r = -4 + 9(3) = -4 + 27 = 23$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Obliczenie sumy $S_{10}$</div>
                        <div class="step-desc">$$S_{10} = \\frac{a_1 + a_{10}}{2} \\cdot 10 = \\frac{-4 + 23}{2} \\cdot 10 = 19 \\cdot 5 = 95$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Zapomnienie o dzieleniu przez 2</div>
                    <div>Wynik $190$ (opcja B) powstaje przy pominięciu dzielenia przez 2 we wzorze na sumę. Pamiętaj: $S_n = \\frac{a_1+a_n}{2} \\cdot n$!</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Suma wyrazów ciągu arytmetycznego</div>
                    <div>$$S_n = \\frac{2a_1 + (n-1)r}{2} \\cdot n$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask12(event)">
                <div class="input-group"><label>a1:</label><input type="number" id="t12_a1" value="-4"></div>
                <div class="input-group"><label>r:</label><input type="number" id="t12_r" value="3"></div>
                <div class="input-group"><label>n:</label><input type="number" id="t12_n" value="10"></div>
                <button type="submit" class="calc-btn">Oblicz Sumę Sn Ciągu Arytmetycznego</button>
            </form>
            <div class="calc-result" id="t12_res">Wprowadź dane i kliknij przycisk.</div>
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
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź A ($95$) jest prawidłowa. $a_{10} = 23$, a $S_{10} = ((-4+23)/2) \\\\cdot 10 = 95$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>A ($95$)</strong>. Użyj wzoru na sumę $S_n$.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask12(e) {
            e.preventDefault();
            const a1 = parseFloat(document.getElementById('t12_a1').value);
            const r = parseFloat(document.getElementById('t12_r').value);
            const n = parseInt(document.getElementById('t12_n').value);
            if (isNaN(a1) || isNaN(r) || isNaN(n) || n <= 0) return;
            const an = a1 + (n - 1) * r;
            const Sn = ((a1 + an) / 2) * n;
            document.getElementById('t12_res').innerHTML = `<strong>Wyraz a_${n}:</strong> ${an}<br><strong>Suma S_${n}:</strong> ${Sn}`;
        }
        '''
    },

    # Task 13
    {
        "num": 13,
        "title": "Jedynka Trygonometryczna",
        "subtitle": "Wyznaczanie $\\cos \\alpha$ dla danego $\\sin \\alpha = \\frac{3}{5}$",
        "text": "Zadanie 13. (0–1)<br>Kąt $\\alpha$ jest ostry i $\\sin \\alpha = \\frac{3}{5}$. Wtedy $\\cos \\alpha$ jest równy:",
        "img": "13.png",
        "is_closed": True,
        "options": {"A": "$\\frac{4}{5}$", "B": "$\\frac{2}{5}$", "C": "$\\frac{1}{5}$", "D": "$\\frac{3}{4}$"},
        "correct": "A",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_13')">Metoda 1: Jedynka trygonometryczna (Główna)</button>
                <button class="tab-btn" onclick="switchTab('m2_13')">Metoda 2: Trójkąt pitagorejski (3, 4, 5)</button>
            </div>
            <div class="tab-content active" id="m1_13">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Zastosowanie wzoru na jedynkę trygonometryczną</div>
                        <div class="step-desc">$$\\sin^2 \\alpha + \\cos^2 \\alpha = 1$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Podstawienie wartości $\\sin \\alpha = \\frac{3}{5}$</div>
                        <div class="step-desc">$$\\left(\\frac{3}{5}\\right)^2 + \\cos^2 \\alpha = 1 \\implies \\frac{9}{25} + \\cos^2 \\alpha = 1 \\implies \\cos^2 \\alpha = 1 - \\frac{9}{25} = \\frac{16}{25}$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Pierwiastkowanie (dla kąta ostrego $\\cos \\alpha > 0$)</div>
                        <div class="step-desc">$$\\cos \\alpha = \\sqrt{\\frac{16}{25}} = \\frac{4}{5}$$</div>
                        <div class="math-highlight">$$\\mathbf{\\cos \\alpha = \\frac{4}{5}} \\quad \\implies \\quad \\text{Poprawna odpowiedź to A}$$</div>
                    </div>
                </div>
            </div>
            <div class="tab-content" id="m2_13">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Trójkąt prostokątny o bokach 3, 4, 5</div>
                        <div class="step-desc">$\\sin \\alpha = \\frac{a}{c} = \\frac{3}{5}$. Z twierdzenia Pitagorasa $b = \\sqrt{5^2 - 3^2} = 4$.<br>
                        Stąd $\\cos \\alpha = \\frac{b}{c} = \\frac{4}{5}$.</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Pomylenie cosinusa z tangensem</div>
                    <div>Wartość $\\frac{3}{4}$ (opcja D) to $\\operatorname{tg} \\alpha = \\frac{\\sin \\alpha}{\\cos \\alpha}$. Pamiętaj, że $\\cos \\alpha$ ma w mianowniku przeciwprostokątną $5$!</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Jedynka trygonometryczna</div>
                    <div>$$\\sin^2 \\alpha + \\cos^2 \\alpha = 1$$</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask13(event)">
                <div class="input-group"><label>Licznik sin(α):</label><input type="number" id="t13_num" value="3"></div>
                <div class="input-group"><label>Mianownik sin(α):</label><input type="number" id="t13_den" value="5"></div>
                <button type="submit" class="calc-btn">Oblicz cos(α) oraz tg(α)</button>
            </form>
            <div class="calc-result" id="t13_res">Wprowadź dane i kliknij przycisk.</div>
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
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź A ($\\frac{4}{5}$) jest prawidłowa. $\\cos^2 \\\\alpha = 1 - 9/25 = 16/25 \\\\implies \\cos \\\\alpha = 4/5$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>A ($\\frac{4}{5}$)</strong>. Użyj wzoru $\\sin^2 \\\\alpha + \\cos^2 \\\\alpha = 1$.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask13(e) {
            e.preventDefault();
            const num = parseFloat(document.getElementById('t13_num').value);
            const den = parseFloat(document.getElementById('t13_den').value);
            if (isNaN(num) || isNaN(den) || den <= 0 || num > den) return;
            const sinVal = num / den;
            const cosVal = Math.sqrt(1 - sinVal * sinVal);
            const tgVal = sinVal / cosVal;
            document.getElementById('t13_res').innerHTML = `<strong>sin(α):</strong> ${sinVal.toFixed(3)}<br><strong>cos(α):</strong> ${cosVal.toFixed(3)}<br><strong>tg(α):</strong> ${tgVal.toFixed(3)}`;
        }
        '''
    },

    # Task 14
    {
        "num": 14,
        "title": "Kąt Wpisany i Dwusieczna w Okręgu",
        "subtitle": "Kąty oparte na tym samym łuku w trójkącie równobocznym",
        "text": "Zadanie 14. (0–1)<br>W okręgu o środku $O$ dany jest trójkąt równoboczny $ABC$, którego wierzchołki leżą na tym okręgu. Średnica $CD$ tego okręgu przecina bok $AB$. Kąt $\\alpha = \\angle DEB$ zaznaczony na rysunku jest równy:",
        "img": "14.png",
        "is_closed": True,
        "options": {"A": "$\\alpha = 30^\\circ$", "B": "$\\alpha < 30^\\circ$", "C": "$\\alpha > 45^\\circ$", "D": "$\\alpha = 45^\\circ$"},
        "correct": "A",
        "solution": '''
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="switchTab('m1_14')">Metoda 1: Dwusieczna i kąty wpisane oparte na tym samym łuku</button>
            </div>
            <div class="tab-content active" id="m1_14">
                <div class="step-item">
                    <div class="step-number">1</div>
                    <div class="step-body">
                        <div class="step-title">Kąty w trójkącie równobocznym</div>
                        <div class="step-desc">Trójkąt $ABC$ jest równoboczny, więc każdy jego kąt wewnętrzny ma $60^\\circ$: $\\angle ACB = 60^\\circ$.</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">2</div>
                    <div class="step-body">
                        <div class="step-title">Średnica jako dwusieczna kąta</div>
                        <div class="step-desc">Średnica $CD$ passing przechodząca przez wierzchołek $C$ trójkąta równobocznego dzieli kąt $\\angle ACB$ dokładnie na dwie równe połowy:
                        $$\\angle DCB = \\frac{1}{2} \\cdot 60^\\circ = 30^\\circ$$</div>
                    </div>
                </div>
                <div class="step-item">
                    <div class="step-number">3</div>
                    <div class="step-body">
                        <div class="step-title">Kąty wpisane oparte na tym samym łuku $DB$</div>
                        <div class="step-desc">Zarówno kąt wpisany $\\angle DCB$, jak i szukany kąt $\\alpha = \\angle DEB$ opierają się na tym samym łuku $DB$:
                        $$\\alpha = \\angle DEB = \\angle DCB = 30^\\circ$$</div>
                        <div class="math-highlight">$$\\mathbf{\\alpha = 30^\\circ} \\quad \\implies \\quad \\text{Poprawna odpowiedź to A}$$</div>
                    </div>
                </div>
            </div>
        ''',
        "traps": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name" style="color:#ef4444;">Pułapka: Złe zidentyfikowanie łuku</div>
                    <div>Zawsze szukaj innych kątów wpisanych opartych na tym samym łuku! Tutaj kąt $\\alpha = \\angle DEB$ opiera się na łuku $DB$, dokładnie tak samo jak kąt $\\angle DCB = 30^\\circ$.</div>
                </div>
            </div>
        ''',
        "formulas": '''
            <div class="formulas-grid">
                <div class="formula-card">
                    <div class="formula-name">Twierdzenie o kącie wpisanym</div>
                    <div>Kąty wpisane oparte na tym samym łuku mają równe miary.</div>
                </div>
            </div>
        ''',
        "calc": '''
            <form class="calc-form" onsubmit="calcTask14(event)">
                <div class="input-group"><label>Kąt trójkąta równobocznego:</label><input type="number" id="t14_deg" value="60" readonly></div>
                <button type="submit" class="calc-btn">Wyznacz Kąt α</button>
            </form>
            <div class="calc-result" id="t14_res">Kliknij przycisk, aby przeliczyć kąt.</div>
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
                feedbackBox.innerHTML = '✨ <strong>Doskonale!</strong> Odpowiedź A ($\\alpha = 30^\\circ$) jest prawidłowa. Kąty wpisane $\\angle DEB$ i $\\angle DCB$ są oparte na tym samym łuku $DB$, a $\\angle DCB = 30^\\circ$.';
            } else {
                if (selectedBtn) selectedBtn.classList.add('wrong');
                feedbackBox.className = 'feedback-box active wrong';
                feedbackBox.innerHTML = `❌ Odpowiedź ${opt} jest niepoprawna. Prawidłowa odpowiedź to <strong>A ($\\alpha = 30^\\circ$)</strong>.`;
            }
            if (window.MathJax) MathJax.typesetPromise([feedbackBox]);
        }

        function calcTask14(e) {
            e.preventDefault();
            document.getElementById('t14_res').innerHTML = `<strong>Kąt DCB:</strong> 30°<br><strong>Szukany kąt α = ∠DEB:</strong> 30° (oparty na tym samym łuku DB)`;
        }
        '''
    }
]

print("Generating Tasks 1 to 14 HTML files...")

for t in tasks_1_14:
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
    
    # Ensure Ultimate Responsive CSS is in place
    if "/* Complete Mobile & Universal Responsive System */" not in html:
        html = html.replace("</style>", ULTIMATE_RESPONSIVE_CSS + "\n    </style>")
        
    filename = f"d:/matura/zadanie{t['num']}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Re-generated premium {filename}")

print("TASKS 1 TO 14 SUCCESSFULLY REGENERATED IN PREMIUM QUALITY!")
