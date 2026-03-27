import gifos
import os
from datetime import datetime

def main():
    # width, height, xpad, ypad, font_file, font_size, line_spacing
    # We'll use 10 FPS for a slower animation (set via env or just assume default is 15 and we can't easily change it without config file, 
    # but x0rzavi's main.py didn't specify FPS in constructor. Wait, I'll check if I can set it via env in the workflow).
    
    t = gifos.Terminal(600, 500, 20, 20)
    
    # --- BIOS BOOT SECTION ---
    t.gen_text("", 1, count=10) # Initial wait
    t.toggle_show_cursor(False)
    year_now = datetime.now().strftime("%Y")
    t.gen_text("GIF_OS Modular BIOS v1.0.11", 1)
    t.gen_text(f"Copyright (C) {year_now}, DarkDolphin Softwares Inc.", 2)
    t.gen_text("GitHub Profile ReadMe Terminal, Rev 2026", 4)
    t.gen_text("Krypton(tm) GIFCPU - 250Hz", 6)
    
    for i in range(0, 65536, 8192):
        t.delete_row(7)
        t.gen_text(f"Memory Test: {i}KB", 7, contin=True)
    t.delete_row(7)
    t.gen_text("Memory Test: 64MB OK", 7, count=5, contin=True)
    
    t.gen_text("Detecting Storage Devices...", 9, count=5)
    t.gen_text("SATA Port 0: SSD 512GB", 10, count=2)
    t.gen_text("SATA Port 1: HDD 1TB", 11, count=2)
    
    t.gen_text("Booting from SSD...", 13, count=10)
    t.clear_frame()
    
    # --- LOGIN SECTION ---
    t.toggle_show_cursor(False)
    t.gen_text("DarkDolphin OS v1.0.11 (tty1)", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("stella", 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("*********", 4, contin=True)
    t.toggle_show_cursor(False)
    t.gen_text("Last login: Fri Mar 27 2026 on tty1", 6, count=5)
    
    # --- FETCH SECTION ---
    t.gen_text("> neofetch", 8, count=5)
    t.gen_text("darkDolphin1@github", 10)
    t.gen_text("-------------------------", 11)
    t.gen_text("OS       : Arch Linux", 12)
    t.gen_text("Shell    : fish 4.5.0", 13)
    t.gen_text("RAM      : 16GB", 14)
    t.gen_text("WM       : Hyprland", 15)
    t.gen_text("Terminal : alacritty 0.16.1", 16)
    t.gen_text("Editor   : VS Code / Neovim", 17, count=10)
    
    # --- STATS SECTION ---
    if os.getenv("GITHUB_TOKEN"):
        try:
            # Note: fetch_github_stats might need the username
            stats = gifos.utils.fetch_github_stats("DarkDolphin1")
            t.gen_text("", 19)
            t.gen_text(f"GitHub Stats for {stats.account_name}:", 20)
            t.gen_text(f"  Stars: {stats.total_stargazers} | Commits: {stats.total_commits_last_year}", 21)
            t.gen_text(f"  PRs: {stats.total_pull_requests_made} | Contribs: {stats.total_repo_contributions}", 22, count=10)
        except Exception as e:
            # Fallback if stats fail
            t.gen_text(f"Error fetching stats: {e}", 19, count=5)
    else:
        t.gen_text("Stats: GITHUB_TOKEN not found", 19, count=5)

    # --- COWSAY SECTION ---
    t.gen_text("", 24)
    t.gen_text("> ./sayHello.sh | cowsay", 25, count=5)
    cowsay_text = """ _________________________________________
/ \"Can you program?\" \"Well, I'm literate, \\
\\ if that's what you mean!\"               /
 -----------------------------------------
        \\   ^__^
         \\  (oo)\_______
            (__)\\       )\\/\\
                ||----w |
                ||     ||"""
    # We can use gen_text for multi-line
    t.gen_text(cowsay_text, 26, count=20)

    # --- END PAUSE ---
    # Hold the last frame for ~120 frames (approx 8-12 seconds depending on FPS)
    t.gen_text("", t.num_rows, count=120, contin=True)

    t.gen_gif()

if __name__ == "__main__":
    main()
