import gifos
import os

def main():
    # Initialize terminal
    t = gifos.Terminal(width=600, height=500, xpad=20, ypad=20)
    
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
    
    t.gen_text(text="", row_num=13)
    t.gen_text(text="stella@starlet ~", row_num=14)
    t.gen_text(text="❯ ./sayHello.sh | cowsay", row_num=15)
    t.gen_text(text=" _________________________________________", row_num=16)
    t.gen_text(text="/ \"Can you program?\" \"Well, I'm literate, \\", row_num=17)
    t.gen_text(text="\\ if that's what you mean!\"               /", row_num=18)
    t.gen_text(text=" -----------------------------------------", row_num=19)
    t.gen_text(text="        \\   ^__^", row_num=20)
    t.gen_text(text="         \\  (oo)\\_______", row_num=21)
    t.gen_text(text="            (__)\\       )\\/\\", row_num=22)
    t.gen_text(text="                ||----w |", row_num=23)
    t.gen_text(text="                ||     ||", row_num=24)

    # Optional: Fetch GitHub stats if token is available
    if os.getenv("GITHUB_TOKEN"):
        try:
            stats = gifos.utils.fetch_github_stats(user_name="darkDolphin1")
            t.gen_text(text="", row_num=25)
            t.gen_text(text=f"GitHub Stats for {stats.account_name}:", row_num=26)
            t.gen_text(text=f"  Stars: {stats.total_stars} | Commits: {stats.total_commits}", row_num=27)
            t.gen_text(text=f"  Followers: {stats.followers} | Following: {stats.following}", row_num=28)
        except Exception as e:
            print(f"Error fetching stats: {e}")

    t.gen_gif()

if __name__ == "__main__":
    main()
