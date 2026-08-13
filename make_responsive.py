# -*- coding: utf-8 -*-
import os, glob, re

RESPONSIVE_CSS = """
        /* Mobile & Responsive Enhancements */
        @media (max-width: 768px) {
            body {
                padding: 1rem 0.5rem;
            }

            .container {
                gap: 1.25rem;
            }

            header {
                padding: 1.5rem 0.75rem;
                border-radius: 16px;
            }

            h1 {
                font-size: 1.6rem;
                line-height: 1.3;
            }

            header p {
                font-size: 0.95rem;
            }

            .card {
                padding: 1.25rem 1rem;
                border-radius: 16px;
            }

            .card-header {
                margin-bottom: 1rem;
                padding-bottom: 0.75rem;
            }

            .card-title {
                font-size: 1.15rem;
            }

            .task-box {
                font-size: 1.05rem;
                padding: 1rem;
            }

            .options-grid {
                grid-template-columns: 1fr;
                gap: 0.75rem;
            }

            .option-btn {
                padding: 0.9rem;
                font-size: 1rem;
            }

            .task-nav {
                padding: 0.75rem 0.5rem;
                gap: 0.3rem;
                max-height: 160px;
                overflow-y: auto;
                -webkit-overflow-scrolling: touch;
            }

            .task-nav-link {
                padding: 0.35rem 0.65rem;
                font-size: 0.75rem;
            }

            .tabs-nav {
                gap: 0.35rem;
            }

            .tab-btn {
                padding: 0.5rem 0.85rem;
                font-size: 0.85rem;
            }

            .step-item {
                gap: 0.85rem;
            }

            .step-number {
                width: 30px;
                height: 30px;
                font-size: 0.9rem;
            }

            .step-title {
                font-size: 1.05rem;
            }

            .step-desc {
                font-size: 0.95rem;
            }

            .calc-form {
                grid-template-columns: 1fr;
            }

            .calc-form input, .calc-form select, .open-task-input input {
                font-size: 16px; /* Prevents auto-zoom on iOS */
            }

            .math-highlight, .formula-card {
                padding: 0.75rem;
                font-size: 0.95rem;
            }
        }

        /* MathJax Overflow Handling for Small Screens */
        mjx-container[jax="SVG"][display="true"], mjx-container[jax="CHTML"][display="true"], .MathJax_Display {
            overflow-x: auto !important;
            overflow-y: hidden !important;
            max-width: 100% !important;
            padding: 0.25rem 0;
            -webkit-overflow-scrolling: touch;
        }
"""

files = glob.glob("d:/matura/*.html")
print(f"Found {len(files)} HTML files to process.")

for fname in files:
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if responsive CSS already injected
    if "/* Mobile & Responsive Enhancements */" in content:
        # Update existing block
        content = re.sub(
            r"/\* Mobile & Responsive Enhancements \*/.*?</style>",
            RESPONSIVE_CSS + "\n    </style>",
            content,
            flags=re.DOTALL
        )
    else:
        # Inject before </style>
        content = content.replace("</style>", RESPONSIVE_CSS + "\n    </style>")

    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated responsive CSS in {os.path.basename(fname)}")

print("All HTML files are now mobile responsive!")
