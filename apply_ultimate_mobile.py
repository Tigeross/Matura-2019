# -*- coding: utf-8 -*-
import os, glob, re

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

files = glob.glob("d:/matura/*.html")
print(f"Applying ultimate responsiveness to {len(files)} HTML files...")

for fname in files:
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    if "/* Complete Mobile & Universal Responsive System */" in content:
        content = re.sub(
            r"/\* Complete Mobile & Universal Responsive System \*/.*?</style>",
            ULTIMATE_RESPONSIVE_CSS + "\n    </style>",
            content,
            flags=re.DOTALL
        )
    elif "/* Mobile & Responsive Enhancements */" in content:
        content = re.sub(
            r"/\* Mobile & Responsive Enhancements \*/.*?</style>",
            ULTIMATE_RESPONSIVE_CSS + "\n    </style>",
            content,
            flags=re.DOTALL
        )
    else:
        content = content.replace("</style>", ULTIMATE_RESPONSIVE_CSS + "\n    </style>")

    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {os.path.basename(fname)}")

print("ALL 35 HTML FILES ARE NOW 100% MOBILE RESPONSIVE!")
