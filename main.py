import gifos
import os

def main():
    # Initialize terminal
    t = gifos.Terminal(width=500, height=300, xpad=15, ypad=15)
    
    # Set color scheme if desired (default is 'yoru')
    # t.set_color_scheme('dracula')

    t.gen_text(text="darkDolphin1@github", row_num=1)
    t.gen_text(text="-------------------------", row_num=2)
    t.gen_text(text="OS       : Arch Linux", row_num=3)
    t.gen_text(text="Shell    : fish 4.5.0", row_num=4)
    t.gen_text(text="RAM      : 16GB", row_num=5)
    t.gen_text(text="WM       : Hyprland", row_num=6)
    t.gen_text(text="Terminal : alacritty 0.16.1", row_num=7)
    t.gen_text(text="Editor   : VS Code / Neovim", row_num=8)
    
    t.gen_text(text="", row_num=9)
    t.gen_text(text="stella@starlet ~", row_num=10)
    t.gen_text(text="> whoami", row_num=11)
    t.gen_text(text="Shravan", row_num=12)
    
    # Optional: Fetch GitHub stats if token is available
    if os.getenv("GITHUB_TOKEN"):
        try:
            stats = gifos.utils.fetch_github_stats(user_name="darkDolphin1")
            t.gen_text(text="", row_num=13)
            t.gen_text(text=f"> GitHub Stats:", row_num=14)
            t.gen_text(text=f"  Total Stars: {stats.total_stars}", row_num=15)
            t.gen_text(text=f"  Total Commits: {stats.total_commits}", row_num=16)
        except Exception as e:
            print(f"Error fetching stats: {e}")

    t.gen_gif()

if __name__ == "__main__":
    main()
