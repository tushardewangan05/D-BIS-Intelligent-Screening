import pathlik

html_code = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>D-BIS — Dynamic Burn-In Intelligence System | SIH 2026 (SIH26170)</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Plotly.js CDN -->
  <script src="https://cdn.plot.ly/plotly-2.32.0.min.js"></script>
  
  <style>
    :root {
      /* Dark Theme (Default Industrial AI Palette) */
      --bg-primary: #050c17;
      --bg-secondary: #91629;
      --bg-card: rgba(9, 22, 41, 0.75);
      --bg-card-hover: rgba(15, 32, 59, 0.85);
      --bg-card-border: rgba(0, 212, 255, 0.18);
      --text-primary: #ffffff;
      --text-secondary: #8ba8cc;
      --text-muted: #536b88;
      --accent-primary: #00d4ff;
      --accent-glow: rgba(0, 212, 255, 0.25);
      --accent-blue: #0f62fe;
      
      --status-pass: #00d4ff;
      --status-pass-bg: rgba(0, 212, 255, 0.12);
      --status-review: #ffcc00;
      --status-review-bg: rgba(255, 204, 0, 0.12);
      --status-hold: #ff4d4d;
      --status-hold-bg: rgba(255, 77, 77, 0.12);
      
      --table-header-bg: rgba(5, 12, 23, 0.9);
      --table-row-hover: rgba(0, 212, 255, 0.05);
      
      --plotly-bg: rgba(9, 22, 41, 0.4);
      --plotly-grid: rgba(255, 255, 255, 0.07);
      --font-main: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }

    [data-theme="light"] {
      --bg-primary: #f1f5f9;
      --bg-secondary: #ffffff;
      --bg-card: #ffffff;
      --bg-card-hover: #f8fafc;
      --bg-card-border: rgba(15, 98, 254, 0.18);
      --text-primary: #0f172a;
      --text-secondary: #475569;
      --text-muted: #94a3b8;
      --accent-primary: #0f62fe;
      --accent-glow: rgba(15, 98, 254, 0.15);
      --accent-blue: #2563eb;
      
      --status-pass: #0284c7;
      --status-pass-bg: rgba(2, 132, 199, 0.12);
      --status-review: #d97706;
      --status-review-bg: rgba(217, 119, 6, 0.12);
      --status-hold: #dc2626;
      --status-hold-bg: rgba(220, 38, 38, 0.12);
      
      --table-header-bg: #f8fafc;
      --table-row-hover: rgba(15, 98, 254, 0.04);
      
      --plotly-bg: #ffffff;
      --plotly-grid: rgba(0, 0, 0, 0.06);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      transition: background-color 0.2s ease, border-color 0.2s ease, color 0.2s ease;
    }

    body {
      font-family: var(--font-main);
      background-color: var(--bg-primary);
      color: var(--text-primary);
      display: flex;
      min-height: 100vh;
      overflow-x: hidden;
    }

    #sidebar {
      width: 260px;
      background: var(--bg-secondary);
      border-right: 1px solid var(--bg-card-border);
      display: flex;
      flex-direction: column;
      position: fixed;
      top: 0;
      bottom: 0;
      left: 0;
      z-index: 100;
    }

    .brand-container {
      padding: 20px 18px;
      border-bottom: 1px solid var(--bg-card-border);
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-icon {
      width: 36px;
      height: 36px;
      background: linear-gradient(135deg, var(--accent-primary), var(--accent-blue));
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      color: #fff;
      font-family: var(--font-mono);
      font-size: 16px;
      box-shadow: 0 0 15px var(--accent-glow);
    }

    .brand-title {
      font-family: var(--font-mono);
      font-size: 14px;
      font-weight: 700;
      color: var(--accent-primary);
      letter-spacing: 1px;
    }

    .brand-subtitle {
      font-size: 10px;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .nav-menu {
      list-style: none;
      padding: 15px 10px;
      flex-grow: 1;
      overflow-y: auto;
    }

    .nav-item {
      margin-bottom: 4px;
    }

    .nav-link {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 10px 14px;
      border-radius: 6px;
      color: var(--text-secondary);
      text-decoration: none;
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
    }

    .nav-link:hover {
      background: var(--bg-card-hover);
      border-color: var(--accent-primary);
    }

    .nav-link.active {
      background: var(--status-pass-bg);
      border-left: 3px solid var(--accent-primary);
      color: var(--accent-primary);
      font-weight: 600;
    }

    .nav-icon {
      font-family: var(--font-mono);
      font-size: 14px;
      width: 18px;
      text-align: center;
    }

    .team-badge {
      padding: 15px 18px;
      border-top: 1px solid var(--bg-card-border);
      font-size: 11px;
      color: var(--text-muted);
      font-family: var(--font-mono);
      line-height: 1.5;
    }

    #main-content {
      margin-left: 260px;
      flex-grow: 1;
      display: flex;
      flex-direction: column;
      min-width: 0;
    }

    #top-header {
      height: 64px;
      background: var(--bg-secondary);
      border-bottom: 1px solid var(--bg-card-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      position: sticky;
      top: 0;
      z-index: 90;
    }

    .header-main-title {
      font-size: 20px;
      font-weight: 700;
      color: var(--text-primary);
      text-shadow: 0 0 20px rgba(0, 212, 255, 0.25);
    }

    .header-sub-title {
      font-size: 11px;
      color: var(--text-muted);
      font-family: var(--font-mono);
    }

    .header-controls {
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .statuspill {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 4px 10px;
      background: var(--status-pass-bg);
      border: 1px solid var(--status-pass);
      border-radius: 20px;
      font-size: 11px;
      font-family: var(--font-mono);
      color: var(--status-pass);
    }

    .status-dot {
      width: 7px;
      height: 7px;
      background: var(--status-pass);
      border-radius: 50%;
      box-shadow: 0 0 8px var(--status-pass);
    }

    .theme-switcher {
      display: flex;
      background: var(--bg-primary);
      border: 1px solid var(--bg-card-border);
      border-radius: 6px;
      padding: 2px;
    }

    .theme-btn {
      padding: 4px 10px;
      font-size: 11px;
      border: none;
      background: transparent;
      color: var(--text-secondary);
      cursor: pointer;
      border-radius: 4px;
      font-family: var(--font-mono);
    }

    .theme-btn.active {
      background: var(--accent-primary);
      color: #000;
      font-weight: 700;
    }

    .page-panel {
      display: none;
      padding: 24px;
    }

    .page-panel.active {
      display: block;
    }

    .section-title {
      font-family: var(--font-mono);
      font-size: 13.5px;
      font-weight: 700;
      color: var(--accent-primary);
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }

    .kpi-card {
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 8px;
      padding: 16px;
      backdrop-filter: blur(12px);
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .kpi-card:hover {
      background: var(--bg-card-hover);
      border-color: var(--accent-primary);
    }

    .kpi-title {
      font-size: 11.5px;
      text-transform: uppercase;
      color: var(--text-secondary);
      font-family: var(--font-mono);
      letter-spacing: 0.5px;
    }

    .kpi-value {
      font-size: 24px;
      font-weight: 700;
      color: var(--text-primary);
      font-family: var(--font-mono);
    }

    .kpi-subtext {
      font-size: 10.5px;
      color: var(--text-muted);
    }

    .charts-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
      gap: 20px;
      margin-bottom: 24px;
    }

    .chart-container {
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 8px;
      padding: 16px;
      min-height: 320px;
      display: flex;
      flex-direction: column;
    }

    .chart-header {
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--accent-primary);
      text-transform: uppercase;
      margin-bottom: 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .plotly-box {
      flex-grow: 1;
      width: 100%;
      height: 290px;
    }

    .table-container {
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-radius: 8px;
      overflow-x: auto;
      margin-bottom: 24px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 13px;
    }

    th {
      background: var(--table-header-bg);
      color: var(--text-secondary);
      font-family: var(--font-mono);
      font-size: 11px;
      text-transform: uppercase;
      padding: 12px 16px;
      border-bottom: 1px solid var(--bg-card-border);
    }

    td {
      padding: 12px 16px;
      border-bottom: 1px solid rgba(255, 204, 0, 0.04);
      color: var(--text-primary);
    }

    tr:hover {
      background: var(--table-row-hover);
      cursor: pointer;
    }

    .badge {
      display: inline-block;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 10.5px;
      font-weight: 700;
      font-family: var(--font-mono);
      text-transform: uppercase;
    }

    .badge-pass {
      background: var(--status-pass-bg);
      color: var(--status-pass);
      border: 1px solid var(--status-pass);
    }

    .badge-review {
      background: var(--status-review-bg);
      color: var(--status-review);
      border: 1px solid var(--status-review);
    }

    .badge-hold {
      background: var(--status-hold-bg);
      color: var(--status-hold);
      border: 1px solid var(--status-hold);
    }

    .modal-overlay {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(5, 12, 23, 0.85);
      backdrop-filter: blur(12px);
      z-index: 1000;
      align-items: center;
      ustify-content: center;
      padding: 20px;
    }

    .modal-content {
      background: var(--bg-secondary);
      border: 1px solid var(--accent-primary);
      border-radius: 12px;
      max-width: 850px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 24px;
      box-shadow: 0 0 30px var(--accent-glow);
      position: relative;
    }

    .modal-close {
      position: absolute;
      top: 16px;
      right: 16px;
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 20px;
      cursor: pointer;
    }

    .modal-close:hover {
      color: var(--accent-primary);
    }

    .xai-box {
      background: var(--bg-card);
      border: 1px solid var(--bg-card-border);
      border-left: 4px solid var(--accent-primary);
      padding: 16px;
      border-radius: 6px;
      margin: 16px 0;
      font-size: 13px;
      line-height: 1.5;
    }

    .xai-title {
      font-family: var(--font-mono);
      font-size: 11.5px;
      color: var(--accent-primary);
      text-transform: uppercase;
      margin-bottom: 6px;
      font-weight: 700;
    }

    .input-control {
      background: var(--bg-primary);
      border: 1px solid var(--bg-card-border);
      color: var(--text-primary);
      padding: 8px 12px;
      border-radius: 6px;
      font-family: var(--font-main);
      font-size: 13px;
      outline: none;
    }

    .input-control:focus {
      border-color: var(--accent-primary);
    }

    .btn-action {
      background: linear-gradient(135deg, var(--accent-primary), var(--accent-blue));
      color: #fff;
      border: none;
      padding: 9px 18px;
      border-radius: 6px;
      font-weight: 600;
      font-size: 12.5px;
      cursor: pointer;
      font-family: var(--font-mono);
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    .btn-action:hover {
      opacity: 0.9;
      box-shadow: 0 0 15px var(--accent-glow);
    }

    .dropzone {
      border: 2px dashed var(--bg-card-border);
      border-radius: 8px;
      padding: 40px;
      text-align: center;
      background: var(--bg-card);
      cursor: pointer;
      margin-bottom: 20px;
    }

    .dropzone:hover {
      border-color: var(--accent-primary);
      background: var(--bg-card-hover);
    }

    @media print {
      #sidebar, #top-header, .btn-action, .theme-switcher {
        display: none !important;
      }
      #main-content {
        margin-left: 0 !important;
      }
      .page-panel {
        display: none !important;
      }
      #page-reports {
        display: block !important;
      }
      .cert-container {
        border: 2px solid #000 !important;
        color: #000 !important;
        background: #fff !important;
      }
    }
  </style>
</head>
<body>
